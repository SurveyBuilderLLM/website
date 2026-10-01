#!/usr/bin/env python3
"""Generate Aayvu marketing sub-pages: usecases/*.html and features/*.html."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = """<a class="skip-link" href="#main-content">Skip to content</a>
<nav class="nav detail-nav" aria-label="Primary navigation">
  <div class="wrap nav-inner">
    <a class="brand" href="../index.html">aayvu<span class="star">✳</span></a>
    <div class="nav-links">
      <a href="../index.html#how">How it works</a>
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-use-cases">Use cases <span>⌄</span></button>
        <div class="drop-menu" id="nav-use-cases" hidden>
          <a href="../usecases/brand-tracking.html"><span>01</span>Brand tracking</a>
          <a href="../usecases/nps-csat.html"><span>02</span>NPS &amp; CSAT</a>
          <a href="../usecases/concept-testing.html"><span>03</span>Concept testing</a>
          <a href="../usecases/pricing-research.html"><span>04</span>Pricing research</a>
          <a href="../usecases/ad-testing.html"><span>05</span>Ad &amp; creative testing</a>
          <a href="../usecases/ua-studies.html"><span>06</span>Usage &amp; attitude</a>
          <a href="../usecases/customer-feedback.html"><span>07</span>Customer feedback</a>
          <a href="../usecases/employee-engagement.html"><span>08</span>Employee engagement</a>
        </div>
      </div>
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-features">Features <span>⌄</span></button>
        <div class="drop-menu" id="nav-features" hidden>
          <a href="../features/ai-editor.html"><span>01</span>AI agent editor</a>
          <a href="../features/question-types.html"><span>02</span>Question types</a>
          <a href="../features/testing.html"><span>03</span>Testing &amp; QA</a>
          <a href="../features/themes.html"><span>04</span>Themes &amp; branding</a>
          <a href="../features/translations.html"><span>05</span>Translations</a>
          <a href="../features/quotas.html"><span>06</span>Quota management</a>
          <a href="../features/admin.html"><span>07</span>Admin controls</a>
        </div>
      </div>
      <a href="../index.html#contact">Contact</a>
    </div>
    <div class="nav-cta">
      <button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Switch to dark mode">
        <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 13A8.5 8.5 0 0 1 11 3.5 8.5 8.5 0 1 0 20.5 13Z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg>
      </button>
      <a class="detail-signin" href="#">Sign in</a>
      <a class="detail-cta" href="../index.html#contact">Request access <span>↗</span></a>
    </div>
  </div>
</nav>"""

FOOT = """<footer class="detail-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="../index.html">aayvu<span class="star">✳</span></a>
        <p class="foot-tag">Better questions. Closer answers.</p>
      </div>
      <div><h5>Product</h5><ul><li><a href="../index.html#features">Features</a></li><li><a href="../index.html#use-cases">Use cases</a></li><li><a href="../index.html#savings">Time savings</a></li><li><a href="#">Sign in</a></li></ul></div>
      <div><h5>Company</h5><ul><li><a href="../index.html#contact">Contact</a></li><li><a href="../index.html#contact">Early access</a></li></ul></div>
      <div><h5>Explore</h5><ul><li><a href="../index.html#how">How it works</a></li><li><a href="../features/translations.html">Translations</a></li></ul></div>
    </div>
    <div class="foot-base"><span>© 2026 Aayvu. All rights reserved.</span><span>Marketing mockup — copy in draft.</span></div>
  </div>
</footer>"""

USECASE_QUESTION_DEMOS = {
 "brand-tracking": [
  ("Multi-select", "Which brands have you heard of?", "<span class='demo-chip on'>Northstar</span><span class='demo-chip'>Hush</span><span class='demo-chip on'>Vale</span>"),
  ("Rating grid", "How innovative is Northstar?", "<span class='demo-scale'>1</span><span class='demo-scale'>2</span><span class='demo-scale on'>3</span><span class='demo-scale'>4</span><span class='demo-scale'>5</span>"),
  ("Brand grid", "Which words describe each brand?", "<span class='demo-grid'>Bold <i>●</i><i>○</i></span><span class='demo-grid'>Trusted <i>○</i><i>●</i></span>"),
 ],
 "nps-csat": [
  ("0–10 NPS", "How likely are you to recommend Acme?", "<span class='demo-scale'>0</span><span class='demo-scale'>2</span><span class='demo-scale'>4</span><span class='demo-scale'>6</span><span class='demo-scale on'>9</span>"),
  ("Follow-up", "What is the main reason for your score?", "<span class='demo-input'>Fast support and a simple workflow…</span>"),
  ("Driver", "What should we improve first?", "<span class='demo-option on'>Reporting</span><span class='demo-option'>Onboarding</span>"),
 ],
 "concept-testing": [
  ("Media choice", "Which concept feels most distinctive?", "<span class='concept-tile'>A</span><span class='concept-tile on'>B</span><span class='concept-tile'>C</span>"),
  ("Appeal rating", "How appealing is Concept B?", "<span class='demo-scale'>1</span><span class='demo-scale'>2</span><span class='demo-scale'>3</span><span class='demo-scale on'>4</span><span class='demo-scale'>5</span>"),
  ("MaxDiff", "Pick the strongest and weakest idea.", "<span class='demo-option on'>Most · Simple</span><span class='demo-option'>Least · Familiar</span>"),
 ],
 "pricing-research": [
  ("Price entry", "At what price is this too expensive?", "<span class='demo-price'>$2,499</span>"),
  ("Gabor–Granger", "Would you buy this at $1,499?", "<span class='demo-option on'>Yes</span><span class='demo-option'>No</span>"),
  ("Conjoint", "Which offer would you choose?", "<span class='offer-tile'>Basic<small>$999</small></span><span class='offer-tile on'>Plus<small>$1,499</small></span>"),
 ],
 "ad-testing": [
  ("Video exposure", "Watch Creative B before continuing.", "<span class='media-tile'><i>▶</i><small>00:15</small></span>"),
  ("Memorability", "How memorable was the main message?", "<span class='demo-scale'>1</span><span class='demo-scale'>2</span><span class='demo-scale'>3</span><span class='demo-scale on'>4</span><span class='demo-scale'>5</span>"),
  ("Open reaction", "What was the ad trying to say?", "<span class='demo-input'>The product makes planning feel easier…</span>"),
 ],
 "ua-studies": [
  ("Usage grid", "How often do you use each brand?", "<span class='demo-grid'>Northstar <i>○</i><i>●</i></span><span class='demo-grid'>Vale <i>●</i><i>○</i></span>"),
  ("Multi-select", "Which occasions apply to you?", "<span class='demo-chip on'>Work</span><span class='demo-chip on'>Travel</span><span class='demo-chip'>Home</span>"),
  ("Constant sum", "Allocate 100 points by usage.", "<span class='sum-row'>Northstar <i style='--fill:65%'></i><b>65</b></span><span class='sum-row'>Vale <i style='--fill:35%'></i><b>35</b></span>"),
 ],
 "customer-feedback": [
  ("CSAT", "How satisfied were you with delivery?", "<span class='demo-scale'>1</span><span class='demo-scale'>2</span><span class='demo-scale'>3</span><span class='demo-scale on'>4</span><span class='demo-scale'>5</span>"),
  ("Journey", "What were you trying to do today?", "<span class='demo-option on'>Track an order</span><span class='demo-option'>Make a return</span>"),
  ("Verbatim", "What could have made this easier?", "<span class='demo-input'>A clearer delivery window…</span>"),
 ],
 "employee-engagement": [
  ("Agreement", "I have what I need to do my best work.", "<span class='demo-scale'>SD</span><span class='demo-scale'>D</span><span class='demo-scale'>N</span><span class='demo-scale on'>A</span><span class='demo-scale'>SA</span>"),
  ("eNPS", "Would you recommend this as a workplace?", "<span class='demo-scale'>0</span><span class='demo-scale'>2</span><span class='demo-scale'>4</span><span class='demo-scale'>6</span><span class='demo-scale on'>9</span>"),
  ("Anonymous text", "What is one thing we should change?", "<span class='demo-input'>More protected time for deep work…</span>"),
 ],
}

FEATURE_VISUALS = {
 "ai-editor": """<div class="feature-visual fv-agent"><div class="visual-bar"><span>Agent editor</span><b>Working through requests</b></div><div class="feature-loop"><article class="loop-scene agent-scene"><div class="agent-prompt">Only show Q8 to detractors.</div><div class="agent-patch"><p><i>IF</i> Q7 is 0–6</p><p><i>SHOW</i> Q8 · Long text</p><p><i>ELSE</i> Continue to Q9</p></div><div class="visual-ok">✓ Logic updated · 0 conflicts</div></article><article class="loop-scene agent-scene" style="--delay:5s"><div class="agent-prompt">Add a screener for weekly shoppers.</div><div class="agent-patch"><p><i>ADD</i> Q2 · Shopping frequency</p><p><i>IF</i> Less than weekly</p><p><i>GO TO</i> Screen-out page</p></div><div class="visual-ok">✓ Screener inserted · paths tested</div></article><article class="loop-scene agent-scene" style="--delay:10s"><div class="agent-prompt">Randomize concepts A, B, and C.</div><div class="agent-patch"><p><i>GROUP</i> Concepts A–C</p><p><i>ORDER</i> Balanced rotation</p><p><i>LOCK</i> Follow-ups to exposure</p></div><div class="visual-ok">✓ Rotation applied · 6 paths</div></article></div></div>""",
 "question-types": """<div class="feature-visual fv-types"><div class="visual-bar"><span>Question library</span><b>Types rotating live</b></div><div class="feature-loop"><article class="loop-scene type-loop-scene"><small>01 · SINGLE SELECT</small><h3>Which plan fits your team?</h3><p><i></i> Starter</p><p class="chosen"><i></i> Scale</p><p><i></i> Enterprise</p></article><article class="loop-scene type-loop-scene" style="--delay:5s"><small>02 · RATING</small><h3>How easy was setup?</h3><div class="loop-rating"><i>1</i><i>2</i><i>3</i><i class="chosen">4</i><i>5</i></div><footer>Very difficult <span>Very easy</span></footer></article><article class="loop-scene type-loop-scene" style="--delay:10s"><small>03 · MULTI-SELECT</small><h3>Which tools do you use?</h3><p class="chosen square"><i></i> Surveys</p><p><i></i> Interviews</p><p class="chosen square"><i></i> Analytics</p></article></div></div>""",
 "testing": """<div class="feature-visual fv-testing"><div class="visual-bar"><span>Automated QA</span><b>Scanning build</b></div><div class="feature-loop"><article class="loop-scene qa-scene file-scan"><div class="file-sheet"><b>DOCX</b><span></span><span></span><span></span><em></em></div><h3>Reading brand_tracker_Q3.docx</h3><p>40 questions · 11 logic rules · 6 validations</p></article><article class="loop-scene qa-scene" style="--delay:5s"><div class="test-path"><span>Q1</span><i></i><span>Q4</span><i></i><span>Q8</span><i></i><span>END</span><em></em></div><h3>Walking every respondent path</h3><p>Promoter, passive, and detractor routes</p></article><article class="loop-scene qa-scene" style="--delay:10s"><div class="logic-scan"><p><i>IF</i> Q7 ≤ 6 <b>Valid</b></p><p><i>SHOW</i> Q8 <b>Reachable</b></p><p><i>REQUIRE</i> Q8 <b>Passed</b></p><em></em></div><h3>Checking logic and validation</h3><p>0 conflicts found · ready for review</p></article></div></div>""",
 "themes": """<div class="feature-visual fv-themes"><div class="visual-bar"><span>Brand studio</span><b>Theme preview</b></div><div class="feature-loop"><article class="loop-scene theme-scene" style="--scene-accent:#345dc1"><div class="scene-swatches"><i></i><i></i><i></i><span>Acme blue</span></div><div class="theme-survey"><b>A</b><small>Question 4 of 8</small><h3>How satisfied are you?</h3><p><i>1</i><i>2</i><i class="on">3</i><i>4</i><i>5</i></p><button>Next</button></div></article><article class="loop-scene theme-scene" style="--delay:5s;--scene-accent:#28704f"><div class="scene-swatches"><i></i><i></i><i></i><span>Verdant green</span></div><div class="theme-survey"><b>V</b><small>Question 5 of 8</small><h3>Which benefit matters most?</h3><p class="theme-choice"><i class="on">Speed</i><i>Control</i><i>Price</i></p><button>Continue</button></div></article><article class="loop-scene theme-scene" style="--delay:10s;--scene-accent:#8f3f76"><div class="scene-swatches"><i></i><i></i><i></i><span>Studio plum</span></div><div class="theme-survey"><b>S</b><small>Question 6 of 8</small><h3>How likely are you to return?</h3><p><i>0</i><i>2</i><i>4</i><i class="on">8</i><i>10</i></p><button>Next</button></div></article></div></div>""",
 "translations": """<div class="feature-visual fv-translations"><div class="visual-bar"><span>Translation review</span><b>Language focus</b></div><div class="feature-loop loop-four"><article class="loop-scene language-focus"><small>EN · SOURCE</small><h3>How likely are you to recommend Northstar?</h3><p>English · approved source</p></article><article class="loop-scene language-focus" style="--delay:4s"><small>ES · APPROVED</small><h3>¿Qué probabilidad hay de que recomiende Northstar?</h3><p>Spanish · reviewed by Lucía</p></article><article class="loop-scene language-focus" style="--delay:8s"><small>FR · IN REVIEW</small><h3>Quelle est la probabilité que vous recommandiez Northstar?</h3><p>French · one source change pending</p></article><article class="loop-scene language-focus" style="--delay:12s"><small>HI · APPROVED</small><h3>आप नॉर्थस्टार की सिफारिश करने की कितनी संभावना रखते हैं?</h3><p>Hindi · reviewed by Aditi</p></article><div class="language-tabs"><span>EN</span><span>ES</span><span>FR</span><span>HI</span></div></div></div>""",
 "quotas": """<div class="feature-visual fv-quotas"><div class="visual-bar"><span>Live sample</span><b>Balancing continuously</b></div><div class="quota-visual quota-moving"><p><span>18–34 · New York</span><b>Target 300</b><i><em></em></i></p><p><span>35+ · California</span><b>Target 300</b><i><em></em></i></p><p><span>Women · South</span><b>Target 240</b><i><em></em></i></p></div><div class="quota-alert"><i></i><span>Sample updates as completes arrive</span></div></div>""",
 "admin": """<div class="feature-visual fv-admin"><div class="visual-bar"><span>Acme workspace</span><b>Editing member access</b></div><div class="feature-loop"><article class="loop-scene admin-scene"><div class="member-card"><span>SR</span><h3>Sam Rivera<small>Researcher · 2 projects</small></h3></div><div class="permission-editor"><p>Create surveys <i class="on"></i></p><p>Publish surveys <i class="on"></i></p><p>Manage members <i></i></p></div></article><article class="loop-scene admin-scene" style="--delay:5s"><div class="member-card"><span>MK</span><h3>Mina Kapoor<small>Admin · all projects</small></h3></div><div class="permission-editor"><p>Create surveys <i class="on"></i></p><p>Publish surveys <i class="on"></i></p><p>Manage members <i class="on"></i></p></div></article><article class="loop-scene admin-scene" style="--delay:10s"><div class="member-card"><span>JL</span><h3>Jon Lee<small>Viewer · client workspace</small></h3></div><div class="permission-editor"><p>View results <i class="on"></i></p><p>Export data <i></i></p><p>Edit surveys <i></i></p></div></article></div></div>""",
}

def usecase_visual(u):
    cards_html = ''.join(
        f'<article class="uc-question-card"><div><span>Q{i}</span><b>{kind}</b></div><h3>{prompt}</h3><div class="question-control">{control}</div><p>Programmed for {u["title"].lower()}</p></article>'
        for i, (kind, prompt, control) in enumerate(USECASE_QUESTION_DEMOS[u['slug']], 1)
    )
    return f'<div class="context-visual usecase-visual"><div class="visual-bar"><span>{u["title"]} · sample questions</span><b>Live rotation</b></div><div class="question-carousel">{cards_html}<div class="carousel-count"><span>01</span><i></i><span>03</span></div></div></div>'

def feature_visual(f):
    return FEATURE_VISUALS[f['slug']]

def page(kind_label, icon, title, tagline, visual_html, sections_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aayvu — {title}</title>
<script src="../theme.js?v=1"></script>
<link rel="stylesheet" href="../styles.css?v=nav-4">
<link rel="stylesheet" href="../theme.css?v=1">
<link rel="stylesheet" href="../subpage-v2.css?v=1">
<script src="../navigation.js?v=nav-5" defer></script>
</head>
<body class="sub-page">
{NAV}
<main id="main-content">
<header class="detail-hero">
  <div class="wrap detail-hero-grid">
    <div class="detail-hero-copy rv in">
      <p class="detail-kicker">{kind_label} / Research workbench</p>
      <h1>{title}</h1>
      <p class="detail-sub">{tagline}</p>
      <div class="detail-actions">
        <a class="detail-button" href="../index.html#contact">Bring us a questionnaire <span>↗</span></a>
        <a href="../index.html#how">See the four-step process ↓</a>
      </div>
    </div>
    <div class="detail-context rv in" aria-hidden="true">{visual_html}</div>
  </div>
</header>
{sections_html}
<section class="detail-cta-band"><div class="wrap rv">
  <p>Start with the document you already have.</p>
  <h2>See what the agent<br>would build for you.</h2>
  <a class="detail-button detail-button-light" href="../index.html#contact">Request early access <span>↗</span></a>
</div></section>
</main>
{FOOT}
<script>
if (location.search.indexOf('static=1') > -1) {{ document.write('<style>.rv{{opacity:1!important;transform:none!important}}</style>'); }}
(function(){{var els=document.querySelectorAll('.rv');
if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return;}}
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{threshold:.12}});
els.forEach(function(e){{io.observe(e);}});}})();
</script>
</body>
</html>"""

def cards(items):
    return '<div class="detail-cards rv">' + ''.join(
        f'<article><span>{i:02d}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(items, 1)) + '</div>'

def usecase_page(u):
    secs = f"""
<section class="detail-story"><div class="wrap detail-story-grid">
  <div class="detail-section-heading rv"><p>01 / Why AI helps here</p><h2>The fiddly parts,<br>handled.</h2></div>
  <div class="story-copy rv">{''.join(f'<p>{p}</p>' for p in u['why_ai'])}<div class="story-note"><span>What changes</span><b>Hours of setup become minutes of review.</b></div></div>
</div></section>
<section class="detail-tools"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p>02 / Study toolkit</p><h2>The right tools<br>for this study.</h2></div>
  {cards(u['qtypes'])}
</div></section>
<section class="detail-outcomes"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p>03 / Why Aayvu</p><h2>Why teams run<br>{u['short']} on Aayvu.</h2></div>
  {cards([(t, d) for t, d in u['why']])}
</div></section>"""
    return page("Use cases", u['icon'], u['title'], u['tagline'], usecase_visual(u), secs)

def feature_page(f):
    secs = f"""
<section class="detail-story feature-story"><div class="wrap detail-story-grid">
  <div class="detail-section-heading rv"><p>01 / In depth</p><h2>{f['depth_head']}</h2></div>
  <div class="story-copy rv">{''.join(f'<p>{p}</p>' for p in f['depth'])}<div class="story-note"><span>Built for control</span><b>The agent drafts. The researcher approves.</b></div></div>
</div></section>
<section class="detail-tools"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p>02 / Included</p><h2>Useful by default.<br>Flexible when needed.</h2></div>
  <div class="feature-ledger rv">{''.join(f'<article><span>{i:02d}</span><h3>{t}</h3><p>{d}</p><i>Included</i></article>' for i, (t, d) in enumerate(f['includes'], 1))}</div>
</div></section>"""
    return page("Features", f['icon'], f['title'], f['tagline'], feature_visual(f), secs)

USE_CASES = [
 dict(slug="brand-tracking", icon="📈", title="Brand tracking", short="brand trackers",
  tagline="Wave after wave of consistent, comparable data — without the wave of programming.",
  why_ai=[
   "Trackers live or die on consistency. One changed scale label and your trend line is fiction. The agent rebuilds the exact structure every wave — same question types, same scales, same routing — so each wave stays perfectly comparable to the last.",
   "And when the business asks for a new brand added mid-year, you don't re-brief a programmer. You ask the agent, review the change, and field."],
  qtypes=[("Multi-select", "Awareness batteries across long brand lists."), ("Rating scales", "Imagery, consideration, and preference."), ("Grids", "Brand × attribute matrices in one screen.")],
  why=[("Consistency, enforced", "The agent keeps every wave structurally identical."), ("Changes in minutes", "Add brands, tweak attributes, re-field — same day."), ("Multi-market ready", "Translations keep every market on the same questionnaire.")]),
 dict(slug="nps-csat", icon="💜", title="NPS & CSAT", short="NPS programs",
  tagline="Loyalty scores in, follow-ups out — automatically.",
  why_ai=[
   "NPS looks simple until you program it: the 0–10 scale, the detractor / passive / promoter split, different follow-ups for each group, piping the score into later questions. The agent wires all of it from a one-line description.",
   "Change the follow-up wording next quarter? One prompt, reviewed in seconds — no rebuild."],
  qtypes=[("0–10 rating", "The classic likelihood-to-recommend scale."), ("Long text", "Open-ended 'why' follow-ups per segment."), ("Single select", "Reason codes and driver questions.")],
  why=[("Branching included", "Detractor and promoter paths wired automatically."), ("Iterate freely", "Reword follow-ups without reprogramming."), ("Trend-safe", "The scale stays identical quarter to quarter.")]),
 dict(slug="concept-testing", icon="💡", title="Concept testing", short="concept tests",
  tagline="Screen ideas in hours, not weeks.",
  why_ai=[
   "Concept tests are fiddly: randomized concept order, monadic or sequential exposure, diagnostics after each concept. It's exactly the kind of setup work researchers dread and programmers bill for.",
   "The agent sets up the rotation and randomization, keeps each respondent's path clean, and lets you add another concept the morning of fieldwork."],
  qtypes=[("Image & media", "Show the concept, pack, or stimulus."), ("Rating", "Appeal, uniqueness, and relevance diagnostics."), ("Ranking & MaxDiff", "Force choices between competing ideas.")],
  why=[("Randomization built in", "Concept order rotated without scripting."), ("Same-day iterations", "Add a concept, re-field, no re-quote."), ("Clean respondent paths", "Monadic or sequential — handled correctly.")]),
 dict(slug="pricing-research", icon="💰", title="Pricing research", short="pricing studies",
  tagline="Price with evidence, not gut feel.",
  why_ai=[
   "Pricing methods are precise instruments: Van Westendorp's four questions must be asked exactly right, Gabor-Granger needs its price ladder sequenced, conjoint needs its experimental design respected. The agent knows these methods and sets them up correctly.",
   "You bring the price points; the agent builds the instrument."],
  qtypes=[("Number & text", "Van Westendorp's four price questions."), ("Single select", "Gabor-Granger buy / no-buy ladders."), ("Conjoint & MaxDiff", "Trade-off and feature-value exercises.")],
  why=[("Method-correct setups", "The agent follows the method, not a guess."), ("Validation included", "Sensible ranges and required answers."), ("Analysis-ready output", "Clean CSVs structured for pricing analysis.")]),
 dict(slug="ad-testing", icon="🎬", title="Ad & creative testing", short="creative tests",
  tagline="Know before it airs.",
  why_ai=[
   "Creative testing means exposing respondents to media, then asking the right diagnostics while it's fresh — with creative order randomized across respondents. Doing that by hand is slow; the agent assembles it in one pass.",
   "Swap in a new cut the night before field? The agent re-wires the exposure in minutes."],
  qtypes=[("Image & video", "Native media exposure questions."), ("Rating scales", "Breakthrough, branding, and persuasion diagnostics."), ("Long text", "Open-ended reactions in their own words.")],
  why=[("Media built in", "Show images and video natively."), ("Randomized exposure", "Creative order rotated automatically."), ("Fast swaps", "New creative, same survey, minutes.")]),
 dict(slug="ua-studies", icon="🧭", title="Usage & attitude", short="U&A studies",
  tagline="The deep studies, without the deep programming pain.",
  why_ai=[
   "U&A studies are the heavyweights: long questionnaires, category usage, brand funnels, and routing that branches on everything. They're the studies most likely to stall in a programming queue.",
   "The agent takes the whole document — all forty, sixty, eighty questions — and programs it in one go, logic included. You spend your time on the analysis, not the setup."],
  qtypes=[("Grids", "Category × brand usage matrices."), ("Multi-select", "Long repertoire and behavior lists."), ("Constant sum", "Share-of-wallet allocation.")],
  why=[("Handles the long ones", "60+ question documents programmed in one pass."), ("Complex routing, done", "Funnels and branches wired correctly."), ("Test before field", "Walk every path as a respondent first.")]),
 dict(slug="customer-feedback", icon="🛍️", title="Customer feedback", short="feedback programs",
  tagline="Every journey, every touchpoint, heard.",
  why_ai=[
   "Feedback surveys need to adapt: a delivery question for the delivery customer, a returns path for the returns customer. The agent builds those adaptive paths from your journey map.",
   "Launch in the morning, tweak by the afternoon — feedback programs stay alive instead of going stale."],
  qtypes=[("CSAT rating", "Satisfaction at each touchpoint."), ("Single select", "Journey stage and reason codes."), ("Long text", "Verbatims that explain the score.")],
  why=[("Adaptive paths", "Questions follow the customer's journey."), ("Piping everywhere", "Names, orders, and context carried through."), ("Always editable", "Live surveys updated without rebuilds.")]),
 dict(slug="employee-engagement", icon="🏢", title="Employee engagement", short="engagement surveys",
  tagline="Hear the whole company, in every language.",
  why_ai=[
   "Engagement surveys span regions, languages, and departments — with anonymity to protect and cuts to deliver. The agent handles the translations workflow and the department routing in one build.",
   "Pulse monthly without the monthly programming invoice."],
  qtypes=[("Agreement scales", "Classic engagement statements."), ("Rating", "eNPS and satisfaction."), ("Long text", "Anonymous comments, handled carefully.")],
  why=[("Translations workflow", "Every region on the same questionnaire."), ("Department routing", "Cuts and filters structured correctly."), ("On brand", "Your logo, your colors, your voice.")]),
]

FEATURES = [
 dict(slug="ai-editor", icon="🤖", title="AI agent editor",
  tagline="Describe the change in plain language. The agent makes it.",
  depth_head="An editor that edits itself.",
  depth=[
   "Most survey tools make you do the clicking. Aayvu's agent does the work: it generates the survey from your document, and then it keeps working — rewriting questions, rebuilding sections, re-wiring logic — on your instruction.",
   "Every change lands as a reviewable draft. Nothing goes live without your approval, and every edit is one you could have made by hand — the agent just makes it in seconds."],
  includes=[("Prompt-driven edits", "Rewrite, add, remove, or re-wire anything by describing it."), ("Bring your own AI key", "Works with OpenAI-compatible models, AWS Bedrock, and more."), ("Review before launch", "Every agent change is inspectable and reversible.")] ),
 dict(slug="question-types", icon="🧩", title="Question types",
  tagline="Every question you'll ever need — all working with logic, validation, and translations.",
  depth_head="Eighteen types. Zero compromises.",
  depth=[
   "From quick polls to advanced research methods, every question type is a first-class citizen: each one works with skip logic, validation, piping, randomization, and translations.",
   "The agent picks the right type for each question in your document — and you can change any of them with a click."],
  includes=[("Choice", "Single select, multi-select, dropdown."), ("Scales", "Rating (stars, numbers, custom), ranking, slider."), ("Text & numbers", "Short text, long text, number with validation."), ("Grids", "Matrix, grid, constant sum — plus Hybrid, our signature rows × columns type."), ("Advanced methods", "MaxDiff, conjoint analysis, hotspot."), ("Media", "Image & video questions, info blocks.")] ),
 dict(slug="testing", icon="🧪", title="Testing & QA",
  tagline="Catch breaks before respondents do.",
  depth_head="Field with confidence.",
  depth=[
   "The most expensive bug in research is the one found after fieldwork starts. Aayvu's test mode lets you walk the survey exactly as a respondent would — taking every branch, triggering every validation.",
   "Meanwhile the logic checker scans your rules for conflicts automatically, so broken routing never reaches the field."],
  includes=[("Respondent test mode", "Walk every path with full logic simulation."), ("Conflict detection", "Contradictory rules flagged automatically."), ("Validation preview", "Every required field checked before launch.")] ),
 dict(slug="themes", icon="🎨", title="Themes & branding",
  tagline="Surveys that look like you sent them.",
  depth_head="On brand, automatically.",
  depth=[
   "A survey is a touchpoint with your brand — or your client's. Set your colors, typography, and logo once, and every survey inherits the theme.",
   "Respondent-facing pages are clean and mobile-friendly by default, so your research looks professional on any device."],
 includes=[("Custom themes", "Colors, fonts, and styling in one place."), ("Your logo", "On every respondent-facing page."), ("Mobile-friendly", "Clean layouts on any screen size.")] ),
 dict(slug="translations", icon="文", title="Translations",
  tagline="One source survey, every market — with human review where it matters.",
  depth_head="One survey. Every language.",
  depth=[
   "Aayvu extracts every respondent-facing string into one translation workspace, so questions, options, errors, and buttons never get lost between files.",
   "Reviewers approve market by market. When the source changes, only affected strings reopen — the rest of the approved survey stays untouched."],
  includes=[("Automatic extraction", "Every visible string is collected without copy-and-paste."), ("Human review", "Market experts approve language before launch."), ("Change tracking", "Only edited source strings return for translation.")] ),
 dict(slug="quotas", icon="🎯", title="Quota management",
  tagline="Full control of your sample.",
  depth_head="The right respondents, in the right numbers.",
  depth=[
   "Cap completes by any segment — age, region, behavior, anything you ask. When a quota fills, new respondents are screened gracefully instead of hitting a dead end.",
   "Watch quotas fill live while fieldwork runs, and adjust on the fly."],
  includes=[("Segment quotas", "Caps on any combination of answers."), ("Graceful screening", "Over-quota and screened-out respondents routed politely."), ("Live monitoring", "Quota fills tracked while fieldwork runs.")] ),
 dict(slug="admin", icon="🔐", title="Admin controls",
  tagline="Run research like a team.",
  depth_head="One place for the whole operation.",
  depth=[
   "Research is a team sport. Aayvu's admin controls let you manage users and roles, organize work into projects and workspaces, and keep an eye on usage — all from one dashboard.",
   "Whether you're a two-person team or an agency running client workspaces, everyone sees what they should and nothing they shouldn't."],
  includes=[("Users & roles", "Admins and researchers, managed simply."), ("Projects & workspaces", "Organize by team, client, or study."), ("Usage dashboard", "Activity and volume in one view.")] ),
]

CSS = """
/* nav dropdowns */
.drop { position: relative; display: flex; align-items: center; }
.drop-trigger { display: flex; align-items: center; height: 68px; cursor: pointer;
  border: 0; padding: 0; background: transparent; color: inherit; font: inherit; }
.drop-trigger:hover, .drop-trigger[aria-expanded="true"] { color: var(--ink); }
.drop-trigger:focus-visible, .drop-menu a:focus-visible { outline: 2px solid var(--brand); outline-offset: 3px; }
.drop-menu { display: block; position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  min-width: 260px; background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 8px;
  box-shadow: 0 18px 44px rgba(120,84,30,.16); z-index: 60;
  animation: none; transition: none; }
.drop-menu[hidden] { display: none; }
.drop-menu a { display: block; padding: 10px 14px; border-radius: 10px; font-size: 14px; color: var(--ink-70); white-space: nowrap; }
.drop-menu a:hover { background: var(--brand-wash); color: var(--ink); }
/* sub-pages */
.page-hero { padding: 90px 0 30px; }
.page-hero .sub { text-align: left; margin: 0 0 30px; font-size: 19px; }
.ph-title { display: flex; align-items: center; gap: 18px; margin: 22px 0 18px; }
.ph-title h1 { font-size: clamp(38px, 5vw, 60px); font-weight: 800; }
.ph-icon { font-size: 52px; }
.bodycopy { font-size: 17px; color: var(--ink-70); max-width: 760px; margin-bottom: 16px; }
.checklist { list-style: none; display: grid; gap: 14px; margin-top: 26px; max-width: 760px; }
.checklist li { display: flex; gap: 12px; font-size: 16px; color: var(--ink-70); background: var(--card);
  border: 1px solid var(--line); border-radius: 14px; padding: 18px 20px; }
.checklist .tick { color: var(--brand); font-weight: 700; flex: none; }
.checklist b { color: var(--ink); }
.ctaband { text-align: center; padding: 90px 0 100px; }
.ctaband h2 { font-size: clamp(30px, 4vw, 48px); font-weight: 800; margin-bottom: 14px; }
.ctaband p { color: var(--ink-70); font-size: 17px; margin-bottom: 28px; }
.uc-more { display: inline-block; margin-top: 16px; font-size: 14px; font-weight: 600; color: var(--brand-deep); }
.uc-more:hover { color: var(--brand); }
.fp-more { display: inline-block; margin-top: 20px; }
"""

def main():
    for d in ("usecases", "features"):
        os.makedirs(os.path.join(BASE, d), exist_ok=True)
    for u in USE_CASES:
        p = os.path.join(BASE, "usecases", u["slug"] + ".html")
        with open(p, "w", encoding="utf-8") as f: f.write(usecase_page(u))
    for feat in FEATURES:
        p = os.path.join(BASE, "features", feat["slug"] + ".html")
        with open(p, "w", encoding="utf-8") as f: f.write(feature_page(feat))
    with open(os.path.join(BASE, "styles.css"), encoding="utf-8") as f:
        css = f.read()
    if "/* nav dropdowns */" not in css:
        with open(os.path.join(BASE, "styles.css"), "a", encoding="utf-8") as f: f.write(CSS)
    print(f"wrote {len(USE_CASES)} usecase + {len(FEATURES)} feature pages")

if __name__ == "__main__":
    main()
