#!/usr/bin/env python3
"""Generate Aayvu marketing sub-pages: usecases/*.html and features/*.html."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = """<nav class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="../index.html">aayvu<span class="star">✳</span></a>
    <div class="nav-links">
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-use-cases">Use cases ▾</button>
        <div class="drop-menu" id="nav-use-cases" hidden>
          <a href="../usecases/brand-tracking.html">📈 Brand tracking</a>
          <a href="../usecases/nps-csat.html">💜 NPS &amp; CSAT</a>
          <a href="../usecases/concept-testing.html">💡 Concept testing</a>
          <a href="../usecases/pricing-research.html">💰 Pricing research</a>
          <a href="../usecases/ad-testing.html">🎬 Ad &amp; creative testing</a>
          <a href="../usecases/ua-studies.html">🧭 Usage &amp; attitude</a>
          <a href="../usecases/customer-feedback.html">🛍️ Customer feedback</a>
          <a href="../usecases/employee-engagement.html">🏢 Employee engagement</a>
        </div>
      </div>
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-features">Features ▾</button>
        <div class="drop-menu" id="nav-features" hidden>
          <a href="../features/ai-editor.html">🤖 AI agent editor</a>
          <a href="../features/question-types.html">🧩 Question types</a>
          <a href="../features/testing.html">🧪 Testing &amp; QA</a>
          <a href="../features/themes.html">🎨 Themes &amp; branding</a>
          <a href="../features/quotas.html">🎯 Quota management</a>
          <a href="../features/admin.html">🔐 Admin controls</a>
        </div>
      </div>
      <a href="../index.html#contact">Contact</a>
    </div>
    <div class="nav-cta">
      <button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Switch to dark mode">
        <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 13A8.5 8.5 0 0 1 11 3.5 8.5 8.5 0 1 0 20.5 13Z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg>
      </button>
      <a class="text-link" href="https://app.aayvu.io/login">Sign in →</a>
      <a class="btn btn-primary" href="../index.html#contact">Get early access</a>
    </div>
  </div>
</nav>"""

FOOT = """<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="../index.html">aayvu<span class="star">✳</span></a>
        <p class="foot-tag">Better questions. Closer answers.</p>
      </div>
      <div><h5>Product</h5><ul><li><a href="../index.html#features">Features</a></li><li><a href="../index.html#use-cases">Use cases</a></li><li><a href="../index.html#savings">Time savings</a></li><li><a href="https://app.aayvu.io/login">Sign in</a></li></ul></div>
      <div><h5>Company</h5><ul><li><a href="../index.html#contact">Contact</a></li><li><a href="../index.html#contact">Early access</a></li></ul></div>
      <div><h5>Resources</h5><ul><li><a href="../index.html#how">How it works</a></li><li><a href="../index.html#contact">Support</a></li></ul></div>
    </div>
    <div class="foot-base"><span>© 2026 Aayvu. All rights reserved.</span><span>Built for modern research teams.</span></div>
  </div>
</footer>"""

def page(kind_label, icon, title, tagline, sections_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aayvu — {title}</title>
<script src="../theme.js?v=1"></script>
<link rel="stylesheet" href="../styles.css?v=nav-4">
<link rel="stylesheet" href="../theme.css?v=1">
<script src="../navigation.js?v=nav-5" defer></script>
</head>
<body>
<div class="bg-fx"></div>
{NAV}
<header class="page-hero">
  <div class="wrap">
    <span class="eyebrow rv in">{kind_label}</span>
    <div class="ph-title rv in"><span class="ph-icon">{icon}</span><h1>{title}</h1></div>
    <p class="sub rv in">{tagline}</p>
    <div class="hero-actions rv in" style="justify-content:flex-start">
      <a class="btn btn-primary btn-lg" href="../index.html#contact">Get early access →</a>
      <a class="text-link" href="../index.html#how">How the agent works ↓</a>
    </div>
  </div>
</header>
{sections_html}
<section class="ctaband"><div class="wrap">
  <h2 class="rv in">Curious what the agent <span class="grad">would build for you?</span></h2>
  <p class="rv in">Send over a questionnaire — we'll show you the agent's version.</p>
  <a class="btn btn-primary btn-lg rv in" href="../index.html#contact">Get early access →</a>
</div></section>
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
    return '<div class="trio">' + ''.join(
        f'<div class="tcard"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'

def usecase_page(u):
    secs = f"""
<section class="block" style="padding-top:20px"><div class="wrap">
  <div class="sec-head rv"><span class="eyebrow">Why AI helps here</span>
  <h2 style="font-size:clamp(26px,3vw,38px)">The fiddly parts, handled.</h2></div>
  {''.join(f'<p class="bodycopy rv">{p}</p>' for p in u['why_ai'])}
</div></section>
<section class="block" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv"><span class="eyebrow">Question types that fit</span>
  <h2 style="font-size:clamp(26px,3vw,38px)">The right tools for this study.</h2></div>
  {cards(u['qtypes'])}
</div></section>
<section class="block" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv"><span class="eyebrow">Why Aayvu</span>
  <h2 style="font-size:clamp(26px,3vw,38px)">Why teams run {u['short']} on Aayvu.</h2></div>
  {cards([(t, d) for t, d in u['why']])}
</div></section>"""
    return page("Use cases", u['icon'], u['title'], u['tagline'], secs)

def feature_page(f):
    secs = f"""
<section class="block" style="padding-top:20px"><div class="wrap">
  <div class="sec-head rv"><span class="eyebrow">In depth</span>
  <h2 style="font-size:clamp(26px,3vw,38px)">{f['depth_head']}</h2></div>
  {''.join(f'<p class="bodycopy rv">{p}</p>' for p in f['depth'])}
  <ul class="checklist rv">{''.join(f'<li><span class="tick">✓</span><span><b>{t}</b> — {d}</span></li>' for t, d in f['includes'])}</ul>
</div></section>"""
    return page("Features", f['icon'], f['title'], f['tagline'], secs)

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
        with open(p, "w") as f: f.write(usecase_page(u))
    for feat in FEATURES:
        p = os.path.join(BASE, "features", feat["slug"] + ".html")
        with open(p, "w") as f: f.write(feature_page(feat))
    css = open(os.path.join(BASE, "styles.css")).read()
    if "/* nav dropdowns */" not in css:
        with open(os.path.join(BASE, "styles.css"), "a") as f: f.write(CSS)
    print(f"wrote {len(USE_CASES)} usecase + {len(FEATURES)} feature pages")

if __name__ == "__main__":
    main()
