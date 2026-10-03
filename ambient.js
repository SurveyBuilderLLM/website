(function () {
  var gridCanvases = Array.from(document.querySelectorAll('[data-distortion-grid]'));
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cellSize = 28;
  var pointer = { x: -1000, y: -1000, active: false };
  var gridFrame = 0;

  function setCanvasSize(canvas, context, width, height) {
    var ratio = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
  }

  var grids = gridCanvases.map(function (canvas) {
    return {
      canvas: canvas,
      context: canvas.getContext('2d'),
      width: 0,
      height: 0,
      x: 0,
      y: 0,
      targetX: 0,
      targetY: 0,
      intensity: 0,
      targetIntensity: 0
    };
  });

  function sizeGrid(state) {
    var rect = state.canvas.getBoundingClientRect();
    state.width = Math.max(1, rect.width);
    state.height = Math.max(1, rect.height);
    setCanvasSize(state.canvas, state.context, state.width, state.height);
    drawGrid(state, true);
  }

  function warpedPoint(state, x, y) {
    if (state.intensity < .001) return [x, y];
    var dx = x - state.x;
    var dy = y - state.y;
    var distance = Math.sqrt(dx * dx + dy * dy);
    var radius = 150;
    if (!distance || distance >= radius) return [x, y];
    var influence = 1 - distance / radius;
    var displacement = influence * influence * 17 * state.intensity;
    return [x + dx / distance * displacement, y + dy / distance * displacement];
  }

  function drawGrid(state, immediate) {
    var rect = state.canvas.getBoundingClientRect();
    state.targetX = pointer.x - rect.left;
    state.targetY = pointer.y - rect.top;
    state.targetIntensity = pointer.active &&
      pointer.x >= rect.left && pointer.x <= rect.right &&
      pointer.y >= rect.top && pointer.y <= rect.bottom ? 1 : 0;

    if (immediate) {
      state.x = state.targetX;
      state.y = state.targetY;
      state.intensity = reducedMotion ? 0 : state.targetIntensity;
    } else {
      // The grid itself stays locked to the cursor; only its strength eases.
      // Positional interpolation made fast movements look like random bends.
      state.x = state.targetX;
      state.y = state.targetY;
      state.intensity += (state.targetIntensity - state.intensity) * .24;
    }

    var context = state.context;
    var lineColor = getComputedStyle(state.canvas).getPropertyValue('--interactive-grid-color').trim() || 'rgba(55,50,43,.09)';
    context.clearRect(0, 0, state.width, state.height);
    context.strokeStyle = lineColor;
    context.lineWidth = 1;

    var x;
    var y;
    var point;
    for (x = 0; x <= state.width + cellSize; x += cellSize) {
      context.beginPath();
      for (y = -cellSize; y <= state.height + cellSize; y += 14) {
        point = warpedPoint(state, x, y);
        if (y === -cellSize) context.moveTo(point[0], point[1]);
        else context.lineTo(point[0], point[1]);
      }
      context.stroke();
    }
    for (y = 0; y <= state.height + cellSize; y += cellSize) {
      context.beginPath();
      for (x = -cellSize; x <= state.width + cellSize; x += 14) {
        point = warpedPoint(state, x, y);
        if (x === -cellSize) context.moveTo(point[0], point[1]);
        else context.lineTo(point[0], point[1]);
      }
      context.stroke();
    }

    return Math.abs(state.targetX - state.x) > .15 ||
      Math.abs(state.targetY - state.y) > .15 ||
      Math.abs(state.targetIntensity - state.intensity) > .002;
  }

  function animateGrids() {
    var keepGoing = false;
    grids.forEach(function (state) {
      if (drawGrid(state, false)) keepGoing = true;
    });
    gridFrame = keepGoing ? window.requestAnimationFrame(animateGrids) : 0;
  }

  function queueGridDraw() {
    if (!gridFrame && !reducedMotion) gridFrame = window.requestAnimationFrame(animateGrids);
  }

  grids.forEach(function (state) { sizeGrid(state); });
  if ('ResizeObserver' in window) {
    var gridResizeObserver = new ResizeObserver(function (entries) {
      entries.forEach(function (entry) {
        var state = grids.find(function (item) { return item.canvas === entry.target; });
        if (state) sizeGrid(state);
      });
    });
    grids.forEach(function (state) { gridResizeObserver.observe(state.canvas); });
  }

  if (!finePointer || reducedMotion) return;

  window.addEventListener('pointermove', function (event) {
    pointer.x = event.clientX;
    pointer.y = event.clientY;
    pointer.active = true;
    document.body.style.setProperty('--cursor-x', event.clientX + 'px');
    document.body.style.setProperty('--cursor-y', event.clientY + 'px');
    document.body.classList.add('cursor-active');

    queueGridDraw();
  }, { passive: true });

  document.documentElement.addEventListener('mouseleave', function () {
    pointer.active = false;
    document.body.classList.remove('cursor-active');
    queueGridDraw();
  });
  window.addEventListener('scroll', queueGridDraw, { passive: true });
  window.addEventListener('resize', function () {
    grids.forEach(function (state) { sizeGrid(state); });
  }, { passive: true });
  new MutationObserver(function () {
    grids.forEach(function (state) { drawGrid(state, true); });
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
})();
