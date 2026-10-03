(function () {
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var loops = Array.from(document.querySelectorAll('.type-feature-loop, .fv-translations .feature-loop, .admin-loop'));

  loops.forEach(function (loop) {
    var scenes = Array.from(loop.querySelectorAll(':scope > .loop-scene'));
    if (scenes.length < 2) return;

    var activeIndex = 0;
    loop.classList.add('product-loop');

    function show(index) {
      activeIndex = index;
      scenes.forEach(function (scene, sceneIndex) {
        scene.hidden = sceneIndex !== activeIndex;
        scene.setAttribute('aria-hidden', sceneIndex === activeIndex ? 'false' : 'true');
      });
      loop.style.setProperty('--product-step', activeIndex);
    }

    show(0);
    if (!reducedMotion) {
      window.setInterval(function () {
        show((activeIndex + 1) % scenes.length);
      }, 1650);
    }
  });
})();
