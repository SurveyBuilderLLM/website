#!/usr/bin/env python3
"""Generate Aayvu marketing sub-pages: usecases/*.html and features/*.html."""
import os
from html import escape

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = """<a class="skip-link" href="#main-content">Skip to content</a>
<nav class="nav" aria-label="Primary navigation">
  <div class="wrap nav-inner">
    <a class="brand" href="../index.html" translate="no">aayvu<span class="brand-mark" aria-hidden="true">✳</span></a>

    <button class="nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="primary-links">
      <span></span><span></span>
    </button>

    <div class="nav-links" id="primary-links">
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-use-cases">Use cases <span aria-hidden="true">⌄</span></button>
        <div class="drop-menu" id="nav-use-cases" hidden>
          <a href="../usecases/brand-tracking.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 18V9m7 9V5m7 13v-7M3 21h18"/></svg><span>Brand tracking</span></a>
          <a href="../usecases/nps-csat.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 15a8 8 0 1 1 16 0m-8 0 4-5M7 19h10"/></svg><span>NPS &amp; CSAT</span></a>
          <a href="../usecases/concept-testing.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6m-5 3h4M8 14c-1.2-1-2-2.8-2-4.7a6 6 0 1 1 12 0c0 1.9-.8 3.7-2 4.7-.8.7-1 1.2-1 2H9c0-.8-.2-1.3-1-2Z"/></svg><span>Concept testing</span></a>
          <a href="../usecases/pricing-research.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M15.5 8.5C14.8 7.5 13.7 7 12.2 7 10.4 7 9 7.9 9 9.3c0 3.7 6.5 1.4 6.5 5 0 1.6-1.5 2.7-3.5 2.7-1.6 0-2.9-.6-3.7-1.7M12 5v14"/></svg><span>Pricing research</span></a>
          <a href="../usecases/ad-testing.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m10 9 5 3-5 3V9Z"/></svg><span>Ad &amp; creative testing</span></a>
          <a href="../usecases/ua-studies.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/></svg><span>Usage &amp; attitude</span></a>
          <a href="../usecases/customer-feedback.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-8l-5 4v-4H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Zm2 5h10m-10 3h6"/></svg><span>Customer feedback</span></a>
          <a href="../usecases/employee-engagement.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm13 9v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg><span>Employee engagement</span></a>
        </div>
      </div>
      <div class="drop"><button class="drop-trigger" type="button" aria-expanded="false" aria-controls="nav-features">Features <span aria-hidden="true">⌄</span></button>
        <div class="drop-menu" id="nav-features" hidden>
          <a href="../features/ai-editor.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19.5V8a3 3 0 0 1 3-3h7a3 3 0 0 1 3 3v5a3 3 0 0 1-3 3H8l-4 3.5ZM18 3l.7 1.8 2.3.7-2.3.7L18 8l-.7-1.8-2.3-.7 2.3-.7L18 3Z"/></svg><span>AI agent editor</span></a>
          <a href="../features/question-types.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h5m4 0h7M9 3v6M4 12h10m4 0h2m-6-3v6M4 18h2m4 0h10m-14-3v6"/></svg><span>Question types</span></a>
          <a href="../features/testing.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 5 6v5c0 4.6 2.8 8 7 10 4.2-2 7-5.4 7-10V6l-7-3Zm-3 8 2 2 4-4"/></svg><span>Testing &amp; QA</span></a>
          <a href="../features/themes.html"><svg class="drop-icon palette-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0 0 20 2 2 0 0 0 2-2c0-.55-.22-1.05-.57-1.42A2 2 0 0 1 15 15.25h1.75A5.25 5.25 0 0 0 22 10C22 5.58 17.52 2 12 2Z"/><circle cx="6.7" cy="10.4" r="1"/><circle cx="9.2" cy="6.7" r="1"/><circle cx="13.7" cy="5.8" r="1"/><circle cx="17.3" cy="8.8" r="1"/></svg><span>Themes &amp; branding</span></a>
          <a href="../features/translations.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h8m-4-2v2m-3 4c1.2 2.5 3.2 4.5 6 6m0-6c-1.2 2.5-3.2 4.5-6 6m9 4 3.5-9 3.5 9m-5.8-3h4.6"/></svg><span>Translations</span></a>
          <a href="../features/quotas.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/><circle cx="9" cy="7" r="2"/><circle cx="15" cy="12" r="2"/><circle cx="11" cy="17" r="2"/></svg><span>Quota management</span></a>
          <a href="../features/admin.html"><svg class="drop-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 19v-1.5a3.5 3.5 0 0 0-3.5-3.5h-5A3.5 3.5 0 0 0 3 17.5V19M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm8-1v6m-3-3h6"/></svg><span>Admin controls</span></a>
        </div>
      </div>
      <a href="../index.html#team">Team</a>
      <a href="../contact.html">Contact</a>
    </div>

    <div class="nav-cta">
      <button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Switch to dark mode">
        <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 13A8.5 8.5 0 0 1 11 3.5 8.5 8.5 0 1 0 20.5 13Z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg>
      </button>
      <a class="signin-link" href="https://app.aayvu.io/login">Sign in</a>
      <a class="button button-solid nav-access" href="../contact.html">Get early access</a>
    </div>
  </div>
</nav>"""

FOOT = """<footer>
  <div class="wrap footer-main">
    <div><a class="brand footer-brand" href="../index.html" translate="no">aayvu<span class="brand-mark" aria-hidden="true">✳</span></a><p>Research, reimagined.</p><a class="footer-social" href="https://www.linkedin.com/company/autosurveybuilder/" target="_blank" rel="noopener" aria-label="Aayvu on LinkedIn" title="Aayvu on LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg></a></div>
    <div><h2>Product</h2><a href="../index.html#features">Features</a><a href="../index.html#use-cases">Use cases</a><a href="../index.html#savings">Time savings</a><a href="https://app.aayvu.io/login">Sign in</a></div>
    <div><h2>Company</h2><a href="../index.html#team">Team</a><a href="../contact.html">Contact</a><a href="../contact.html">Early access</a><a href="../index.html#how">How it works</a></div>
    <div><h2>Explore</h2><a href="../features/ai-editor.html">AI editor</a><a href="../features/question-types.html">Question types</a><a href="../features/testing.html">Testing &amp; QA</a></div>
  </div>
  <div class="wrap footer-base"><span>© 2026 Aayvu. All rights reserved.</span><span>AI-powered research suite for research teams.</span></div>
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
 "ai-editor": """<div class="feature-visual fv-agent"><div class="visual-bar agent-status"><span><i></i>Aayvu agent</span><b>Working in brand_tracker_Q3</b></div><div class="feature-loop agent-loop"><article class="loop-scene agent-scene"><div class="agent-user"><small>You</small><p>Only show Q8 to detractors.</p></div><div class="agent-assistant"><i>✳</i><div><small>Aayvu</small><p>I’ll add display logic to Q8 and test both paths.</p><div class="agent-tool"><b><span>✓</span> Updated display logic</b><em>Q7 is 0–6 → show Q8</em></div></div></div><div class="agent-compose">Message Aayvu <b>↗</b></div></article><article class="loop-scene agent-scene" style="--delay:3s"><div class="agent-user"><small>You</small><p>Add a screener for weekly shoppers.</p></div><div class="agent-assistant"><i>✳</i><div><small>Aayvu</small><p>Added. People who shop less often now exit through a polite screen-out.</p><div class="agent-tool"><b><span>✓</span> Added question and route</b><em>Q2 · frequency → screen-out</em></div></div></div><div class="agent-compose">Message Aayvu <b>↗</b></div></article><article class="loop-scene agent-scene" style="--delay:6s"><div class="agent-user"><small>You</small><p>Randomize concepts A, B, and C.</p></div><div class="agent-assistant"><i>✳</i><div><small>Aayvu</small><p>Done. I balanced the exposure order and kept each follow-up with its concept.</p><div class="agent-tool"><b><span>✓</span> Rotation tested</b><em>3 concepts · 6 valid paths</em></div></div></div><div class="agent-compose">Message Aayvu <b>↗</b></div></article></div></div>""",
 "question-types": """<div class="feature-visual fv-types"><div class="visual-bar"><span>Question library</span><b>Previewing live</b></div><div class="feature-loop type-feature-loop"><article class="loop-scene type-canvas"><nav><span class="active">Single select</span><span>Rating</span><span>Multi-select</span></nav><div><small>Question 4</small><h3>Which plan fits your team?</h3><p><i></i> Starter</p><p class="chosen"><i></i> Scale</p><p><i></i> Enterprise</p></div></article><article class="loop-scene type-canvas" style="--delay:3s"><nav><span>Single select</span><span class="active">Rating</span><span>Multi-select</span></nav><div><small>Question 5</small><h3>How easy was setup?</h3><div class="loop-rating"><i>1</i><i>2</i><i>3</i><i class="chosen">4</i><i>5</i></div><footer>Very difficult <span>Very easy</span></footer></div></article><article class="loop-scene type-canvas" style="--delay:6s"><nav><span>Single select</span><span>Rating</span><span class="active">Multi-select</span></nav><div><small>Question 6</small><h3>Which tools do you use?</h3><p class="chosen square"><i></i> Surveys</p><p><i></i> Interviews</p><p class="chosen square"><i></i> Analytics</p></div></article></div></div>""",
 "testing": """<div class="feature-visual fv-testing"><div class="visual-bar"><span>Automated QA</span><b>Scanning build</b></div><div class="feature-loop"><article class="loop-scene qa-scene file-scan"><div class="file-sheet"><b>DOCX</b><span></span><span></span><span></span><em></em></div><h3>Reading brand_tracker_Q3.docx</h3><p>40 questions · 11 logic rules · 6 validations</p></article><article class="loop-scene qa-scene" style="--delay:3s"><div class="test-path"><span>Q1</span><i></i><span>Q4</span><i></i><span>Q8</span><i></i><span>END</span><em></em></div><h3>Walking every respondent path</h3><p>Promoter, passive, and detractor routes</p></article><article class="loop-scene qa-scene" style="--delay:6s"><div class="logic-scan"><p><i>IF</i> Q7 ≤ 6 <b>Valid</b></p><p><i>SHOW</i> Q8 <b>Reachable</b></p><p><i>REQUIRE</i> Q8 <b>Passed</b></p><em></em></div><h3>Checking logic and validation</h3><p>0 conflicts found · ready for review</p></article></div></div>""",
 "themes": """<div class="feature-visual fv-themes"><div class="visual-bar"><span>Brand studio</span><b>Theme preview</b></div><div class="feature-loop"><article class="loop-scene theme-scene" style="--scene-accent:#345dc1"><div class="scene-swatches"><i></i><i></i><i></i><span>Acme blue</span></div><div class="theme-survey"><b>A</b><small>Question 4 of 8</small><h3>How satisfied are you?</h3><p><i>1</i><i>2</i><i class="on">3</i><i>4</i><i>5</i></p><button>Next</button></div></article><article class="loop-scene theme-scene" style="--delay:3s;--scene-accent:#28704f"><div class="scene-swatches"><i></i><i></i><i></i><span>Verdant green</span></div><div class="theme-survey"><b>V</b><small>Question 5 of 8</small><h3>Which benefit matters most?</h3><p class="theme-choice"><i class="on">Speed</i><i>Control</i><i>Price</i></p><button>Continue</button></div></article><article class="loop-scene theme-scene" style="--delay:6s;--scene-accent:#8f3f76"><div class="scene-swatches"><i></i><i></i><i></i><span>Studio plum</span></div><div class="theme-survey"><b>S</b><small>Question 6 of 8</small><h3>How likely are you to return?</h3><p><i>0</i><i>2</i><i>4</i><i class="on">8</i><i>10</i></p><button>Next</button></div></article></div></div>""",
 "translations": """<div class="feature-visual fv-translations"><div class="visual-bar"><span>Translation review</span><b>4 languages</b></div><div class="feature-loop loop-four"><article class="loop-scene language-focus"><small>English · Source</small><h3>How likely are you to recommend Northstar?</h3><div class="language-tabs"><span class="active"><b>🇺🇸</b>EN</span><span><b>🇪🇸</b>ES</span><span><b>🇫🇷</b>FR</span><span><b>🇮🇳</b>HI</span></div></article><article class="loop-scene language-focus" style="--delay:3s"><small>Spanish · Approved</small><h3>¿Qué probabilidad hay de que recomiende Northstar?</h3><div class="language-tabs"><span><b>🇺🇸</b>EN</span><span class="active"><b>🇪🇸</b>ES</span><span><b>🇫🇷</b>FR</span><span><b>🇮🇳</b>HI</span></div></article><article class="loop-scene language-focus" style="--delay:6s"><small>French · In review</small><h3>Quelle est la probabilité que vous recommandiez Northstar?</h3><div class="language-tabs"><span><b>🇺🇸</b>EN</span><span><b>🇪🇸</b>ES</span><span class="active"><b>🇫🇷</b>FR</span><span><b>🇮🇳</b>HI</span></div></article><article class="loop-scene language-focus" style="--delay:9s"><small>Hindi · Approved</small><h3>आप नॉर्थस्टार की सिफारिश करने की कितनी संभावना रखते हैं?</h3><div class="language-tabs"><span><b>🇺🇸</b>EN</span><span><b>🇪🇸</b>ES</span><span><b>🇫🇷</b>FR</span><span class="active"><b>🇮🇳</b>HI</span></div></article></div></div>""",
 "quotas": """<div class="feature-visual fv-quotas"><div class="visual-bar"><span>Brand tracker · Wave 3</span><b><i class="live-dot"></i>664 completes</b></div><div class="quota-board quota-moving"><header><span>Audience</span><span>Complete</span><span>Target</span></header><p><span>18–34 · New York</span><b>216</b><em>300</em><i><u></u></i></p><p><span>35+ · California</span><b>300</b><em>300</em><i><u></u></i></p><p><span>Women · South</span><b>148</b><em>240</em><i><u></u></i></p></div></div>""",
 "admin": """<div class="feature-visual fv-admin"><div class="visual-bar"><span>Acme Insights</span><b>Members</b></div><div class="feature-loop admin-loop loop-four"><article class="loop-scene admin-scene member-list-scene"><p class="selected"><span>SR</span><b>Sam Rivera<small>Researcher</small></b><i>›</i></p><p><span>MK</span><b>Mina Kapoor<small>Admin</small></b><i>›</i></p><p><span>JL</span><b>Jon Lee<small>Viewer</small></b><i>›</i></p></article><article class="loop-scene admin-scene" style="--delay:3s"><a class="member-back">← All members</a><div class="member-card"><span>SR</span><h3>Sam Rivera<small>Researcher · 2 projects</small></h3></div><div class="permission-editor"><p>Create surveys <i class="on"></i></p><p>Publish surveys <i class="on"></i></p><p>Manage members <i></i></p></div></article><article class="loop-scene admin-scene member-list-scene" style="--delay:6s"><p><span>SR</span><b>Sam Rivera<small>Researcher</small></b><i>›</i></p><p class="selected"><span>MK</span><b>Mina Kapoor<small>Admin</small></b><i>›</i></p><p><span>JL</span><b>Jon Lee<small>Viewer</small></b><i>›</i></p></article><article class="loop-scene admin-scene" style="--delay:9s"><a class="member-back">← All members</a><div class="member-card"><span>MK</span><h3>Mina Kapoor<small>Admin · all projects</small></h3></div><div class="permission-editor"><p>Create surveys <i class="on"></i></p><p>Publish surveys <i class="on"></i></p><p>Manage members <i class="on"></i></p></div></article></div></div>""",
}

ICON_PATHS = {
 "brand-tracking": '<path d="M5 18V9m7 9V5m7 13v-7"/><path d="M3 21h18"/>',
 "nps-csat": '<path d="M4 15a8 8 0 1 1 16 0"/><path d="m12 15 4-5"/><path d="M7 19h10"/>',
 "concept-testing": '<path d="M9 18h6m-5 3h4"/><path d="M8 14c-1.2-1-2-2.8-2-4.7a6 6 0 1 1 12 0c0 1.9-.8 3.7-2 4.7-.8.7-1 1.2-1 2H9c0-.8-.2-1.3-1-2Z"/>',
 "pricing-research": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5c-.7-1-1.8-1.5-3.3-1.5-1.8 0-3.2.9-3.2 2.3 0 3.7 6.5 1.4 6.5 5 0 1.6-1.5 2.7-3.5 2.7-1.6 0-2.9-.6-3.7-1.7M12 5v14"/>',
 "ad-testing": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m10 9 5 3-5 3V9Z"/>',
 "ua-studies": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
 "customer-feedback": '<path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-8l-5 4v-4H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Z"/><path d="M7 10h10m-10 3h6"/>',
 "employee-engagement": '<path d="M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 20v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "ai-editor": '<path d="M4 19.5V8a3 3 0 0 1 3-3h7a3 3 0 0 1 3 3v5a3 3 0 0 1-3 3H8l-4 3.5Z"/><path d="m18 3 .7 1.8L21 5.5l-2.3.7L18 8l-.7-1.8-2.3-.7 2.3-.7L18 3Z"/>',
 "question-types": '<path d="M4 6h3m4 0h9M4 12h3m4 0h9M4 18h3m4 0h9"/><circle cx="7" cy="6" r="1"/><rect x="5.8" y="10.8" width="2.4" height="2.4"/><path d="m5.8 18 1 1 2-2"/>',
 "testing": '<path d="M12 3 4 6v6c0 5 3.4 8 8 9 4.6-1 8-4 8-9V6l-8-3Z"/><path d="m8.5 12 2.2 2.2 4.8-5"/>',
 "themes": '<path d="M12 2a10 10 0 0 0 0 20 2 2 0 0 0 2-2c0-.55-.22-1.05-.57-1.42A2 2 0 0 1 15 15.25h1.75A5.25 5.25 0 0 0 22 10C22 5.58 17.52 2 12 2Z"/><circle cx="6.7" cy="10.4" r="1"/><circle cx="9.2" cy="6.7" r="1"/><circle cx="13.7" cy="5.8" r="1"/><circle cx="17.3" cy="8.8" r="1"/>',
 "translations": '<path d="M4 5h8m-4-2v2m-3 4c1.2 2.5 3.2 4.5 6 6m0-6c-1.2 2.5-3.2 4.5-6 6"/><path d="m14 19 3.5-9 3.5 9m-5.8-3h4.6"/>',
 "quotas": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "admin": '<path d="M15 19v-1.5a3.5 3.5 0 0 0-3.5-3.5h-5A3.5 3.5 0 0 0 3 17.5V19"/><circle cx="9" cy="8" r="3"/><path d="M17 11v6m-3-3h6"/>',
}

def detail_icon(slug):
    return f'<div class="detail-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICON_PATHS[slug]}</svg></div>'

def usecase_visual(u):
    cards = [
        f'<article class="uc-question-card"><div><span>{i:02d}</span><b>{kind}</b></div><h3>{prompt}</h3><div class="question-control">{control}</div></article>'
        for i, (kind, prompt, control) in enumerate(USECASE_QUESTION_DEMOS[u['slug']], 1)
    ]
    cards_html = ''.join(cards + [cards[0].replace('class="uc-question-card"', 'class="uc-question-card" aria-hidden="true"')])
    return f'<div class="context-visual usecase-visual"><div class="question-carousel"><div class="question-card-track">{cards_html}</div></div></div>'

def feature_visual(f):
    return FEATURE_VISUALS[f['slug']]

def page(kind_label, slug, title, tagline, visual_html, sections_html):
    page_class = "feature-page" if kind_label == "Features" else "usecase-page"
    if kind_label == "Use cases":
        seo_title = f"{title} Survey Software | Aayvu"
        seo_description = f"Aayvu helps research teams {tagline[0].lower() + tagline[1:]}"
    else:
        seo_title = f"{title} for AI Survey Programming | Aayvu"
        seo_description = f"Aayvu helps research teams {tagline[0].lower() + tagline[1:]}"
    seo_title_html = escape(seo_title, quote=True)
    seo_description_html = escape(seo_description, quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{seo_description_html}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{seo_title_html}">
<meta property="og:description" content="{seo_description_html}">
<title>{seo_title_html}</title>
<script src="../theme.js?v=1"></script>
<link rel="stylesheet" href="../styles.css?v=nav-5">
<link rel="stylesheet" href="../theme.css?v=1">
<link rel="stylesheet" href="../home-v3.css?v=11">
<link rel="stylesheet" href="../subpage-v2.css?v=16">
<script src="../navigation.js?v=nav-5" defer></script>
<script src="../ambient.js?v=5" defer></script>
<script src="../feature-demos.js?v=1" defer></script>
</head>
<body class="home-page sub-page {page_class} {page_class}-{slug}">
{NAV}
<main id="main-content">
<header class="detail-hero">
  <canvas class="distortion-grid" data-distortion-grid aria-hidden="true"></canvas>
  <div class="wrap detail-hero-grid">
    <div class="detail-hero-copy rv in">
      {detail_icon(slug)}
      <h1>{title}</h1>
      <p class="detail-sub">{tagline}</p>
      <div class="detail-actions">
        <a class="detail-button" href="../contact.html">Bring us a questionnaire <span>↗</span></a>
        <a href="../index.html#how">See the four-step process ↓</a>
      </div>
    </div>
    <div class="detail-context rv in" aria-hidden="true">{visual_html}</div>
  </div>
</header>
{sections_html}
<section class="detail-cta-band"><div class="wrap rv">
  <p>Start with the questionnaire you already have.</p>
  <h2>Turn it into a survey<br>that is ready to review.</h2>
  <a class="detail-button detail-button-light" href="../contact.html">Request early access <span>↗</span></a>
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
  <div class="detail-section-heading rv"><p><span>01</span> Survey programming</p><h2>{u['title']} setup,<br>handled.</h2></div>
  <div class="story-copy rv">{''.join(f'<p>{p}</p>' for p in u['why_ai'])}<div class="story-note"><span>Why it matters</span><b>Spend less time on setup and more time reviewing the research.</b></div></div>
</div></section>
<section class="detail-tools"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p><span>02</span> Study design</p><h2>What your {u['short']}<br>need.</h2></div>
  {cards(u['qtypes'])}
</div></section>
<section class="detail-outcomes"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p><span>03</span> Research outcomes</p><h2>Build {u['short']}<br>faster with Aayvu.</h2></div>
  {cards([(t, d) for t, d in u['why']])}
</div></section>"""
    return page("Use cases", u['slug'], u['title'], u['tagline'], usecase_visual(u), secs)

def feature_page(f):
    secs = f"""
<section class="detail-story feature-story"><div class="wrap detail-story-grid">
  <div class="detail-section-heading rv"><p><span>01</span> How {f['title'].lower()} works</p><h2>{f['depth_head']}</h2></div>
  <div class="story-copy rv">{''.join(f'<p>{p}</p>' for p in f['depth'])}<div class="story-note"><span>{f['note_label']}</span><b>{f['note']}</b></div></div>
</div></section>
<section class="feature-benefits" id="why-it-matters"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p><span>02</span> Benefits for research teams</p><h2>{f['benefit_head']}</h2></div>
  <div class="feature-benefit-grid rv">{''.join(f'<article><span>{i:02d}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(f['benefits'], 1))}</div>
</div></section>
<section class="feature-workflow" id="in-practice"><div class="wrap feature-workflow-layout">
  <div class="detail-section-heading rv"><p><span>03</span> Workflow</p><h2>{f['workflow_head']}</h2><p class="workflow-intro">{f['workflow_intro']}</p></div>
  <ol class="feature-step-list rv">{''.join(f'<li><span>{i:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(f['workflow'], 1))}</ol>
</div></section>
<section class="detail-tools" id="capabilities"><div class="wrap">
  <div class="detail-section-heading detail-heading-row rv"><p><span>04</span> Capabilities</p><h2>{f['included_head']}</h2></div>
  <div class="feature-ledger rv">{''.join(f'<article><span>{i:02d}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(f['includes'], 1))}</div>
</div></section>"""
    return page("Features", f['slug'], f['title'], f['tagline'], feature_visual(f), secs)

USE_CASES = [
 dict(slug="brand-tracking", icon="📈", title="Brand tracking", short="brand trackers",
  tagline="Build consistent, review-ready brand tracking surveys for every wave and market.",
  why_ai=[
   "Trackers live or die on consistency. One changed scale label and your trend line is fiction. The agent rebuilds the exact structure every wave — same question types, same scales, same routing — so each wave stays perfectly comparable to the last.",
   "And when the business asks for a new brand added mid-year, you don't re-brief a programmer. You ask the agent, review the change, and field."],
  qtypes=[("Multi-select", "Awareness batteries across long brand lists."), ("Rating scales", "Imagery, consideration, and preference."), ("Grids", "Brand × attribute matrices in one screen.")],
  why=[("Consistency, enforced", "The agent keeps every wave structurally identical."), ("Changes in minutes", "Add brands, tweak attributes, re-field — same day."), ("Multi-market ready", "Translations keep every market on the same questionnaire.")]),
 dict(slug="nps-csat", icon="💜", title="NPS & CSAT", short="NPS programs",
  tagline="Build NPS and CSAT surveys with automatic score routing, follow-ups, and trend-safe scales.",
  why_ai=[
   "NPS looks simple until you program it: the 0–10 scale, the detractor / passive / promoter split, different follow-ups for each group, piping the score into later questions. The agent wires all of it from a one-line description.",
   "Change the follow-up wording next quarter? One prompt, reviewed in seconds — no rebuild."],
  qtypes=[("0–10 rating", "The classic likelihood-to-recommend scale."), ("Long text", "Open-ended 'why' follow-ups per segment."), ("Single select", "Reason codes and driver questions.")],
  why=[("Branching included", "Detractor and promoter paths wired automatically."), ("Iterate freely", "Reword follow-ups without reprogramming."), ("Trend-safe", "The scale stays identical quarter to quarter.")]),
 dict(slug="concept-testing", icon="💡", title="Concept testing", short="concept tests",
  tagline="Build concept testing surveys with randomized exposure, diagnostics, and respondent-ready logic.",
  why_ai=[
   "Concept tests are fiddly: randomized concept order, monadic or sequential exposure, diagnostics after each concept. It's exactly the kind of setup work researchers dread and programmers bill for.",
   "The agent sets up the rotation and randomization, keeps each respondent's path clean, and lets you add another concept the morning of fieldwork."],
  qtypes=[("Image & media", "Show the concept, pack, or stimulus."), ("Rating", "Appeal, uniqueness, and relevance diagnostics."), ("Ranking & MaxDiff", "Force choices between competing ideas.")],
  why=[("Randomization built in", "Concept order rotated without scripting."), ("Same-day iterations", "Add a concept, re-field, no re-quote."), ("Clean respondent paths", "Monadic or sequential — handled correctly.")]),
 dict(slug="pricing-research", icon="💰", title="Pricing research", short="pricing studies",
  tagline="Build pricing surveys for Van Westendorp, Gabor-Granger, conjoint, and other evidence-led methods.",
  why_ai=[
   "Pricing methods are precise instruments: Van Westendorp's four questions must be asked exactly right, Gabor-Granger needs its price ladder sequenced, conjoint needs its experimental design respected. The agent knows these methods and sets them up correctly.",
   "You bring the price points; the agent builds the instrument."],
  qtypes=[("Number & text", "Van Westendorp's four price questions."), ("Single select", "Gabor-Granger buy / no-buy ladders."), ("Conjoint & MaxDiff", "Trade-off and feature-value exercises.")],
  why=[("Method-correct setups", "The agent follows the method, not a guess."), ("Validation included", "Sensible ranges and required answers."), ("Analysis-ready output", "Clean CSVs structured for pricing analysis.")]),
 dict(slug="ad-testing", icon="🎬", title="Ad & creative testing", short="creative tests",
  tagline="Build ad testing surveys with randomized creative exposure, media questions, and clear diagnostics.",
  why_ai=[
   "Creative testing means exposing respondents to media, then asking the right diagnostics while it's fresh — with creative order randomized across respondents. Doing that by hand is slow; the agent assembles it in one pass.",
   "Swap in a new cut the night before field? The agent re-wires the exposure in minutes."],
  qtypes=[("Image & video", "Native media exposure questions."), ("Rating scales", "Breakthrough, branding, and persuasion diagnostics."), ("Long text", "Open-ended reactions in their own words.")],
  why=[("Media built in", "Show images and video natively."), ("Randomized exposure", "Creative order rotated automatically."), ("Fast swaps", "New creative, same survey, minutes.")]),
 dict(slug="ua-studies", icon="🧭", title="Usage & attitude", short="U&A studies",
  tagline="Program complex usage and attitude surveys with brand funnels, grids, and branching logic intact.",
  why_ai=[
   "U&A studies are the heavyweights: long questionnaires, category usage, brand funnels, and routing that branches on everything. They're the studies most likely to stall in a programming queue.",
   "The agent takes the whole document — all forty, sixty, eighty questions — and programs it in one go, logic included. You spend your time on the analysis, not the setup."],
  qtypes=[("Grids", "Category × brand usage matrices."), ("Multi-select", "Long repertoire and behavior lists."), ("Constant sum", "Share-of-wallet allocation.")],
  why=[("Handles the long ones", "60+ question documents programmed in one pass."), ("Complex routing, done", "Funnels and branches wired correctly."), ("Test before field", "Walk every path as a respondent first.")]),
 dict(slug="customer-feedback", icon="🛍️", title="Customer feedback", short="feedback programs",
  tagline="Build adaptive customer feedback surveys for every journey, touchpoint, and follow-up.",
  why_ai=[
   "Feedback surveys need to adapt: a delivery question for the delivery customer, a returns path for the returns customer. The agent builds those adaptive paths from your journey map.",
   "Launch in the morning, tweak by the afternoon — feedback programs stay alive instead of going stale."],
  qtypes=[("CSAT rating", "Satisfaction at each touchpoint."), ("Single select", "Journey stage and reason codes."), ("Long text", "Verbatims that explain the score.")],
  why=[("Adaptive paths", "Questions follow the customer's journey."), ("Piping everywhere", "Names, orders, and context carried through."), ("Always editable", "Live surveys updated without rebuilds.")]),
 dict(slug="employee-engagement", icon="🏢", title="Employee engagement", short="engagement surveys",
  tagline="Build employee engagement surveys across teams, departments, regions, and languages.",
  why_ai=[
   "Engagement surveys span regions, languages, and departments — with anonymity to protect and cuts to deliver. The agent handles the translations workflow and the department routing in one build.",
   "Pulse monthly without the monthly programming invoice."],
  qtypes=[("Agreement scales", "Classic engagement statements."), ("Rating", "eNPS and satisfaction."), ("Long text", "Anonymous comments, handled carefully.")],
  why=[("Translations workflow", "Every region on the same questionnaire."), ("Department routing", "Cuts and filters structured correctly."), ("On brand", "Your logo, your colors, your voice.")]),
]

FEATURES = [
 dict(slug="ai-editor", icon="🤖", title="AI agent editor",
  tagline="Edit survey questions, logic, validation, and flow by describing the change in plain language.",
  depth_head="An editor that edits itself.",
  depth=[
   "Most survey tools make you do the clicking. Aayvu's agent does the work: it generates the survey from your document, and then it keeps working — rewriting questions, rebuilding sections, re-wiring logic — on your instruction.",
   "Every change lands as a reviewable draft. Nothing goes live without your approval, and every edit is one you could have made by hand — the agent just makes it in seconds."],
  note_label="The difference", note="The agent changes the survey, not just the sentence.",
  benefit_head="From request to reviewed change.",
  benefits=[
   ("Keeps the whole survey in view", "A change to one question carries its connected logic, validation, and answer piping with it."),
   ("Works at survey speed", "Add a screener, restructure a section, or update answer options without chasing every dependency."),
   ("Leaves control with the researcher", "Every change stays editable, and publishing remains a separate decision.")],
  workflow_head="A conversation with your survey.",
  workflow_intro="Start with the outcome you want. Aayvu handles the connected setup and gives you a draft to inspect.",
  workflow=[
   ("Ask", "Describe the result in plain language—from a neutral rewrite to a new routed follow-up."),
   ("Build", "Aayvu updates the question and the dependent parts of the questionnaire together."),
   ("Review", "Preview the path, adjust anything by hand, and publish only when it is ready.")],
  included_head="Everything the agent can change.",
  includes=[("Rewrite in context", "Adjust tone, clarity, or neutrality without losing the question's role."), ("Add and reorganize", "Create questions, insert sections, and change the order of the flow."), ("Change question structure", "Switch types, options, scales, rows, or columns."), ("Re-wire logic", "Update visibility, skips, terminations, and answer actions."), ("Connect earlier answers", "Pipe answers and numeric targets into later questions."), ("Review before launch", "Inspect the draft in the visual editor and respondent preview.")] ),
 dict(slug="question-types", icon="🧩", title="Question types",
  tagline="Build simple questions, advanced grids, MaxDiff, conjoint, media, and more without custom setup.",
  depth_head="A format for every answer.",
  depth=[
   "From quick choice questions to hybrid grids and advanced research methods, each format is built into the same editor rather than bolted on as a special case.",
   "Logic, validation, answer piping, and respondent preview travel with the question, so changing its type does not mean rebuilding the rest of the survey."],
  note_label="Built in", note="Twenty-seven formats, one consistent editing model.",
  benefit_head="Use the shape the question deserves.",
  benefits=[
   ("Simple when it should be", "Choice, text, number, date, time, rating, and slider questions stay quick to configure."),
   ("Serious when it needs to be", "Matrices, hybrid grids, allocations, MaxDiff, conjoint, hotspot, and matching are first-class formats."),
   ("Consistent for respondents", "Required states, limits, option behavior, and mobile layouts follow the same rules across the survey.")],
  workflow_head="Choose. Configure. Test.",
  workflow_intro="Question design stays visual from the first option to the last validation rule.",
  workflow=[
   ("Choose the format", "Let the agent infer it from the source or switch types directly in the editor."),
   ("Shape the behavior", "Add options, scales, rows, columns, limits, conditional wording, and option visibility."),
   ("Try the answer", "Use respondent preview to confirm the control behaves properly before fieldwork.")],
  included_head="From a radio button to conjoint.",
  includes=[("Choice", "Single select, multiple select, dropdowns, and image selection."), ("Text, number, date & time", "Open answers with length, range, integer, pattern, and uniqueness rules."), ("Scales", "Ratings and sliders with custom bounds and labels."), ("Matrices & hybrid grids", "Single, multiple, rating, numeric, and mixed-type columns with row-level behavior."), ("Allocation", "Ranking, constant sum, and percentage allocation with total checks."), ("Advanced research", "MaxDiff, conjoint, hotspot, and drag-and-drop matching."), ("Media & content", "File upload, voice input, and information screens.")] ),
 dict(slug="testing", icon="🧪", title="Testing & QA",
  tagline="Test every respondent path and catch broken logic, invalid references, and validation issues before launch.",
  depth_head="Field with confidence.",
  depth=[
   "The most expensive bug in research is the one found after fieldwork starts. Aayvu's test mode lets you walk the survey exactly as a respondent would — taking every branch, triggering every validation.",
   "Meanwhile the logic checker scans your rules for conflicts automatically, so broken routing never reaches the field."],
  note_label="Before fieldwork", note="Find the broken path while it is still free to fix.",
  benefit_head="Test the experience, not a checklist.",
  benefits=[
   ("See what respondents see", "Run the published experience with real controls, validations, messages, and branching."),
   ("Inspect connected rules", "Catch missing references, unreachable targets, invalid quotas, and logic cycles before launch."),
   ("Fix without leaving the editor", "Move from an issue to the exact question, rule, or validation that caused it.")],
  workflow_head="Walk every important path.",
  workflow_intro="A good QA pass combines automatic checks with a human run-through of the respondent experience.",
  workflow=[
   ("Scan", "Analyze the questionnaire for broken references, conflicting actions, and invalid configuration."),
   ("Run", "Answer as a respondent and deliberately trigger screeners, branches, quotas, and validations."),
   ("Resolve", "Return to the flagged rule, make the change, and repeat the path before publishing.")],
  included_head="Checks that follow the logic.",
  includes=[("Respondent preview", "Fill the survey with the same question controls used in the live form."), ("Logic analysis", "Check question, row, column, and answer-action dependencies."), ("Reference checks", "Flag missing questions, variables, options, pipes, and quotas."), ("Cycle detection", "Surface circular visibility and hybrid column gating."), ("Validation preview", "Exercise required fields, ranges, selection limits, patterns, and sum rules."), ("Publish separation", "Keep editing without changing the live snapshot until you republish.")] ),
 dict(slug="themes", icon="🎨", title="Themes & branding",
  tagline="Apply your colors, typography, and logo across every respondent-facing survey.",
  depth_head="On brand, automatically.",
  depth=[
   "A survey is a touchpoint with your brand — or your client's. Set your colors, typography, and logo once, and every survey inherits the theme.",
   "Respondent-facing pages are clean and mobile-friendly by default, so your research looks professional on any device."],
  note_label="One system", note="Make the survey recognizable without redesigning every question.",
  benefit_head="Brand presence without visual noise.",
  benefits=[
   ("Consistent by default", "The same palette, typography, spacing, and controls carry across every respondent screen."),
   ("Easy to approve", "Preview the experience as a complete survey instead of judging disconnected settings."),
   ("Made for real devices", "Layouts adapt from desktop research panels to respondents answering on a phone.")],
  workflow_head="Set the system once.",
  workflow_intro="Brand decisions live above individual questions, so the experience stays coherent as the study changes.",
  workflow=[
   ("Choose the foundation", "Set the accent palette, typography, logo, and surface treatment."),
   ("Preview real questions", "Check choices, scales, grids, messages, and buttons in the respondent layout."),
   ("Apply consistently", "Carry the approved theme across the entire survey and future edits.")],
  included_head="The details respondents notice.",
  includes=[("Color system", "Accent, surface, text, border, and interaction states."), ("Typography", "Readable type choices with a consistent hierarchy."), ("Logo placement", "A clear brand presence across respondent-facing pages."), ("Survey controls", "Buttons, fields, choices, scales, and progress states that belong together."), ("Responsive layouts", "Comfortable spacing and controls across desktop and mobile."), ("Live preview", "Review the complete look before the survey is published.")] ),
 dict(slug="translations", icon="文", title="Translations",
  tagline="Translate one source survey for every market, with human review and source changes kept in sync.",
  depth_head="One survey. Every language.",
  depth=[
   "Aayvu extracts every respondent-facing string into one translation workspace, so questions, options, errors, and buttons never get lost between files.",
   "Reviewers approve market by market. When the source changes, only affected strings reopen — the rest of the approved survey stays untouched."],
  note_label="No spreadsheets", note="The source, translation, and reviewer feedback stay connected.",
  benefit_head="Give every market a real review path.",
  benefits=[
   ("Nothing important gets missed", "Questions, options, helper text, validation messages, and respondent pages stay in one bundle."),
   ("Local experts can focus", "A shareable review link lets reviewers approve, correct, or transliterate without entering the editor."),
   ("Status stays visible", "See which language is generating, ready for review, approved, or waiting on corrections.")],
  workflow_head="From source to approved locale.",
  workflow_intro="Each language moves through a visible workflow instead of disappearing into an email attachment.",
  workflow=[
   ("Add a locale", "Choose the language and create its translation bundle from the current source survey."),
   ("Generate and edit", "Review each string in context and adjust the wording directly."),
   ("Share for approval", "Send a time-bound review link, collect corrections, and approve the language for use.")],
  included_head="Translation with a paper trail.",
  includes=[("Automatic extraction", "Collect respondent-facing strings without copy-and-paste."), ("Language workspace", "Review source and translated wording together."), ("External review links", "Invite market experts without giving them editor access."), ("Approve, correct, transliterate", "Capture the exact kind of change a reviewer is requesting."), ("Reviewer feedback", "See approvals and suggested wording inside the survey workspace."), ("Change tracking", "Return affected strings to review when the source changes.")] ),
 dict(slug="quotas", icon="🎯", title="Quota management",
  tagline="Set sample targets, monitor completes, and control what happens when a respondent segment fills.",
  depth_head="The right respondents, in the right numbers.",
  depth=[
   "Cap completes by any segment — age, region, behavior, anything you ask. When a quota fills, new respondents are screened gracefully instead of hitting a dead end.",
   "Watch quotas fill live while fieldwork runs, and adjust on the fly."],
  note_label="Two modes", note="Hard quotas stop at the target. Soft quotas keep counting.",
  benefit_head="Control composition while fieldwork moves.",
  benefits=[
   ("Define the audience precisely", "Map a quota to a specific question and answer rather than maintaining a separate sample sheet."),
   ("Choose what happens at the limit", "Stop respondents with a hard quota or continue collecting with a soft one."),
   ("Keep the exit understandable", "Use a dedicated quota-full message instead of leaving respondents at a dead end.")],
  workflow_head="Map the answer to the target.",
  workflow_intro="Quota setup stays close to the survey logic that decides who counts.",
  workflow=[
   ("Define", "Name the segment, set the completion limit, and choose hard or soft behavior."),
   ("Map", "Connect the quota to the qualifying answer or apply it through an answer action."),
   ("Monitor", "Watch completes against the target and adjust the setup as fieldwork changes.")],
  included_head="Everything behind the target bar.",
  includes=[("Question-and-answer mapping", "Count respondents from the exact answer that defines the segment."), ("Hard quotas", "Stop additional respondents when the target is reached."), ("Soft quotas", "Track the segment without interrupting the respondent."), ("Answer actions", "Apply a quota as part of a question's routed outcome."), ("Quota-full messaging", "Control the page shown when a hard quota closes."), ("Configuration checks", "Flag missing mappings, invalid limits, and deleted quota references.")] ),
 dict(slug="admin", icon="🔐", title="Admin controls",
  tagline="Manage roles, workspaces, projects, and survey collaborators from one clear admin view.",
  depth_head="One place for the whole operation.",
  depth=[
   "Research is a team sport. Aayvu's admin controls let you manage users and roles, organize work into projects and workspaces, and keep an eye on usage — all from one dashboard.",
   "Whether you're a two-person team or an agency running client workspaces, everyone sees what they should and nothing they shouldn't."],
  note_label="Clear ownership", note="Workspace access and survey collaboration are managed separately.",
  benefit_head="Give people the access their work needs.",
  benefits=[
   ("Keep responsibilities clear", "Separate organization admins, feature access, and survey-level editing."),
   ("Organize the research", "Group surveys, language versions, responses, and shared context inside projects."),
   ("Share without handing over everything", "Invite a colleague to edit one survey without opening the full workspace.")],
  workflow_head="From member to working access.",
  workflow_intro="The interface makes access visible, adjustable, and specific to the job a teammate is doing.",
  workflow=[
   ("Choose a member", "Open the person whose role or feature access needs to change."),
   ("Set access", "Assign admin status or grant the specific product areas they need."),
   ("Share the work", "Add editors to individual surveys and organize the studies inside projects.")],
  included_head="Control at the right level.",
  includes=[("Members & roles", "Manage organization members and administrator access."), ("Feature permissions", "Control access to translation and operational run views."), ("Survey collaborators", "Invite or remove editors on an individual questionnaire."), ("Projects", "Group surveys, translations, response totals, and shared work."), ("Workspace views", "Move between personal work and organization-wide administration."), ("Usage visibility", "Review activity and processing volume from one place.")] ),
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
