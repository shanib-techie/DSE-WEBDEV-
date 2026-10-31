import math, os
from lib import *

REPO = '/home/claude/ResaleIQ'
def loc(p):
    return sum(1 for _ in open(os.path.join(REPO, p), encoding='utf-8'))
LOC_MAIN = loc('main.py'); LOC_PJS = loc('resaleiq-website/js/predict.js')
LOC_TJS = loc('resaleiq-website/js/theme.js'); LOC_AJS = loc('resaleiq-website/js/about.js')
LOC_CSS = loc('resaleiq-website/css/style.css')
LOC_HTML = sum(loc(f'resaleiq-website/{f}') for f in ['index.html', 'dataset.html', 'predict.html', 'about.html'])

reg = Registry(
    ['overview', 'layers', 'framework', 'waterfall', 'incremental', 'prototyping', 'spiral', 'agile'],
    ['stack', 'features', 'layermap', 'quality', 'frameworkmap', 'umbrella', 'metrics', 'risks', 'compare', 'increments'])
F, Tb = reg.F, reg.Tb
S = []

# ------------------------------------------------------------------ figures
def fig_overview(c):
    box(c, 20, 60, 190, 125, '', fill=LIGHT2)
    label(c, 115, 175, 'Browser: resaleiq-website/ (static)', fs=8, font='Sans-B', color=NAVY)
    for i, t in enumerate(['index.html - The Model', 'dataset.html - The Dataset', 'predict.html + predict.js', 'about.html + about.js']):
        box(c, 30, 140 - i * 27, 170, 22, t, fs=7.6, fill=colors.white)
    box(c, 20, 193, 190, 22, 'GitHub public API (api.github.com)', fs=7.6, fill=AMBER)
    arrow(c, [(115, 185), (115, 193)], 'about.js: GET', lpos=(158, 189), dash=True, fs=6.5)
    box(c, 280, 60, 180, 125, '', fill=LIGHT2)
    label(c, 370, 175, 'FastAPI application (main.py)', fs=8, font='Sans-B', color=NAVY)
    box(c, 290, 106, 160, 54, 'POST /prediction handler\nresale_price(): validate, encode,\nalign columns, predict', fs=7.6, fill=colors.white)
    box(c, 290, 68, 160, 30, "StaticFiles mount at '/'\nserves resaleiq-website/", fs=7.4, fill=colors.white)
    box(c, 280, 4, 85, 34, 'model.pkl\n(LightGBM model)', fs=7.4, fill=GREEN)
    box(c, 375, 4, 85, 34, 'model_columns.pkl\n(22 column names)', fs=7.4, fill=GREEN)
    box(c, 20, 4, 190, 34, 'analysis.ipynb (offline training)', fs=7.8, fill=AMBER)
    arrow(c, [(210, 140), (290, 140)], 'POST /prediction\nJSON, 13 fields', lpos=(250, 140), fs=6.5)
    arrow(c, [(290, 118), (210, 118)], 'JSON:\npredicted_resale_price', lpos=(250, 112), fs=6.5)
    arrow(c, [(322, 38), (322, 60)], 'load at\nstart-up', lpos=(300, 49), fs=6.3, color=GREY)
    arrow(c, [(417, 38), (417, 60)], None, color=GREY)
    arrow(c, [(210, 21), (280, 21)], 'joblib.dump', lpos=(245, 28), dash=True, fs=6.5)

def fig_layers(c):
    rows = [('Tools', 'Python, FastAPI, Uvicorn, pandas, LightGBM, joblib,\nJupyter notebook, Git and GitHub, browser fetch API', LIGHT),
            ('Methods', 'Supervised regression, one-hot encoding of brand and\ncondition, 80/20 hold-out split, JSON API contract', LIGHT),
            ('Process', 'Iterative experiment, refine and deploy cycle:\nRandom Forest, XGBoost, then LightGBM (per README)', LIGHT),
            ('A Quality Focus', 'Accuracy (R2 0.9836, MAE 1,698.63 INR), reproducibility\n(random_state=42), correct column alignment, usability', GREEN)]
    y = 160
    for i, (n, t, f) in enumerate(rows):
        h = 38
        ind = (3 - i) * 0
        box(c, 0, y, 150, h, n, fill=NAVY if i < 3 else TEAL, stroke=NAVY, fs=10.5, tc=colors.white, bold=True)
        box(c, 158, y, 312, h, t, fill=f, fs=8.2)
        if i < 3:
            arrow(c, [(75, y - 2), (75, y - 7)], head=True, lw=0.8, color=GREY)
        y -= 46
    label(c, 75, 188 + 2, 'Layer', fs=7.5, color=GREY)
    label(c, 314, 202, 'ResaleIQ example (from repository evidence)', fs=7.8, color=GREY, font='Sans-I')

def fig_framework(c):
    names = ['Communication', 'Planning', 'Modeling', 'Construction', 'Deployment']
    outs = ['README goals,\ninput list\n(13 fields)', 'Feature trim,\nmodel choice,\nendpoint plan', 'Data schema,\nJSON contract,\nlayout of pages',
            'main.py, notebook,\npredict.js, HTML/CSS', 'Hosted API URL,\nrequirements.txt,\nCORS']
    w = 82
    for i, (n, o) in enumerate(zip(names, outs)):
        x = i * 97
        box(c, x, 112, w, 34, n, fill=NAVY, tc=colors.white, fs=8.6, bold=True)
        box(c, x, 54, w, 46, o, fill=LIGHT, fs=7.2)
        arrow(c, [(x + w / 2, 112), (x + w / 2, 100)], head=True, lw=0.8)
        if i < 4:
            arrow(c, [(x + w, 129), (x + 97, 129)])
    label(c, 235, 156, 'Framework activities and representative ResaleIQ work products', fs=8, font='Sans-B', color=NAVY)
    box(c, 0, 4, 470, 38, '', fill=AMBER)
    label(c, 235, 33, 'UMBRELLA ACTIVITIES (applied throughout the whole project)', fs=7.8, font='Sans-B', color=NAVY)
    label(c, 235, 18, 'Tracking and control | Risk management | Quality assurance | Technical reviews | Measurement |\nConfiguration management | Reuse management | Work-product preparation', fs=7.2)

def fig_waterfall(c):
    names = ['Requirements', 'Design', 'Implementation', 'Testing', 'Deployment', 'Maintenance']
    for i, n in enumerate(names):
        x = i * 74
        y = 130 - i * 24
        box(c, x, y, 94, 26, n, fill=LIGHT if i % 2 == 0 else colors.white, fs=8.2, bold=True)
        if i < 5:
            arrow(c, [(x + 80, y), (x + 80, y - 6), (x + 74 + 20, y - 6), (x + 74 + 20, y - 0.5)], lw=0.9, head=True)
    arrow(c, [(10, 143), (-0, 143)], head=False)
    arrow(c, [(440, 6), (470, 6), (470, 160), (30, 160), (30, 158)], 'limited feedback (change is costly)', lpos=(250, 160), dash=True, fs=6.8, color=GREY)
    label(c, 100, 30, 'Each phase is completed and signed off before\nthe next begins; output of one phase is input\nto the next.', fs=7.6, align='l', color=GREY)

def fig_incremental(c):
    label(c, 235, 168, 'Time \u2192', fs=8, font='Sans-B', color=NAVY)
    arrow(c, [(110, 160), (468, 160)], head=True, color=NAVY)
    phases = ['Communicate\nand plan', 'Model', 'Construct', 'Deploy']
    incs = [('Increment 1', 'Trained model\n+ notebook'), ('Increment 2', 'FastAPI\n/prediction'), ('Increment 3', 'Predict page\n(UI form)'),
            ('Increment 4', 'Info pages,\nhardening')]
    for r, (n, d) in enumerate(incs):
        y = 118 - r * 38
        box(c, 0, y, 100, 30, n + ': ' + d.replace('\n', ' '), fill=NAVY, tc=colors.white, fs=7.2)
        for p, t in enumerate(phases):
            x = 112 + r * 52 + p * 70
            box(c, x, y, 66, 30, t, fill=LIGHT if p < 3 else GREEN, fs=7.2)
        arrow(c, [(112 + r * 52 + 3 * 70 + 33, y + 30), (112 + r * 52 + 3 * 70 + 33, y + 36)], head=False, lw=0.6)
    label(c, 235, 2, 'Each increment delivers a working, usable subset; later increments add functionality.', fs=7.6, color=GREY, font='Sans-I')

def fig_proto(c):
    cx, cy = 235, 98
    items = [('1. Communication', 235, 170), ('2. Quick plan', 380, 120), ('3. Modeling:\nquick design', 340, 40),
             ('4. Construction of\nprototype', 130, 40), ('5. Deployment, delivery\nand feedback', 90, 120)]
    ws = 116
    for t, x, y in items:
        box(c, x - ws / 2, y - 16, ws, 32, t, fill=LIGHT, fs=7.8, bold=True)
    pos = [(x, y) for _, x, y in items]
    arrow(c, [(235 + 58, 170), (380 - 20, 136)], lw=1.2)
    arrow(c, [(380, 104), (340 + 30, 56)], lw=1.2)
    arrow(c, [(340 - 58, 40), (130 + 58, 40)], lw=1.2)
    arrow(c, [(130 - 20, 56), (90 + 6, 104)], lw=1.2)
    arrow(c, [(90 + 20, 136), (235 - 58, 170)], lw=1.2)
    label(c, 235, 98, 'Iterate until the stakeholder\naccepts the prototype', fs=8, font='Sans-I', color=GREY)
    box(c, 395, 150, 75, 34, 'Final system\nengineered', fill=GREEN, fs=7.4)
    arrow(c, [(235 + 58, 176), (395, 170)], dash=True, color=GREY)

def fig_spiral(c):
    cx, cy = 150, 100
    line(c, cx - 140, cy, cx + 140, cy, color=GREY, lw=0.8)
    line(c, cx, cy - 98, cx, cy + 98, color=GREY, lw=0.8)
    label(c, cx - 70, cy + 88, 'Planning', fs=8, font='Sans-B', color=NAVY)
    label(c, cx + 70, cy + 88, 'Risk analysis', fs=8, font='Sans-B', color=NAVY)
    label(c, cx + 70, cy - 88, 'Engineering', fs=8, font='Sans-B', color=NAVY)
    label(c, cx - 70, cy - 88, 'Customer evaluation', fs=8, font='Sans-B', color=NAVY)
    pts = []
    for k in range(0, 4 * 36 + 1):
        th = k * (2 * math.pi / 36)
        r = 12 + 6.0 * th
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.8)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.drawPath(p, stroke=1, fill=0)
    arrow(c, [pts[-3], pts[-1]], color=TEAL, lw=1.8)
    notes = [(12, 'Loop 1: concept and feasibility\n(can features predict price?)'),
             (12 + 6 * 2 * math.pi, 'Loop 2: prototype models\n(Random Forest, XGBoost)'),
             (12 + 6 * 4 * math.pi, 'Loop 3: LightGBM + API\n(/prediction endpoint)'),
             (12 + 6 * 6 * math.pi, 'Loop 4: web UI, deployment\nand hardening')]
    for i, (r, t) in enumerate(notes):
        x = cx + r
        c.setFillColor(NAVY)
        c.circle(x, cy, 3, stroke=0, fill=1)
        ty = cy + 78 - i * 40
        arrow(c, [(x, cy + 2), (x, ty - 6), (312, ty - 6)] if False else [(x, cy + 3), (x + 0.01, cy + 3)], head=False, lw=0.1)
        box(c, 312, ty - 15, 158, 30, t, fill=LIGHT, fs=7.2, r=3)
        line(c, x, cy, 312, ty, color=GREY, lw=0.5, dash=(2, 2))
    label(c, 150, 2, 'Radius = cumulative cost and effort; angle = progress through the four activities', fs=6.8, color=GREY, font='Sans-I')

def fig_agile(c):
    box(c, 0, 90, 80, 44, 'Product\nBacklog\n(user stories)', fill=AMBER, fs=7.6)
    box(c, 100, 90, 70, 44, 'Sprint\nPlanning', fill=LIGHT, fs=8, bold=True)
    box(c, 190, 50, 190, 128, '', fill=LIGHT2, dash=(4, 2))
    label(c, 285, 168, 'Sprint (time-boxed, e.g. 1 to 2 weeks)', fs=7.8, font='Sans-B', color=NAVY)
    for i, t in enumerate(['Design', 'Code', 'Test']):
        box(c, 200 + i * 60, 108, 52, 30, t, fill=colors.white, fs=8)
        if i < 2:
            arrow(c, [(252 + i * 60, 123), (260 + i * 60, 123)])
    box(c, 220, 62, 130, 28, 'Daily stand-up\n(inspect and adapt)', fill=GREEN, fs=7.4)
    arrow(c, [(170, 112), (190, 112)])
    arrow(c, [(80, 112), (100, 112)])
    box(c, 400, 90, 70, 44, 'Working\nincrement', fill=GREEN, fs=8, bold=True)
    arrow(c, [(380, 112), (400, 112)])
    box(c, 190, 0, 190, 30, 'Sprint Review and Retrospective', fill=LIGHT, fs=8, bold=True)
    arrow(c, [(435, 90), (435, 15), (380, 15)], 'feedback', lpos=(435, 50), fs=6.8)
    arrow(c, [(190, 15), (40, 15), (40, 90)], 'refine backlog', lpos=(110, 15), fs=6.8)

# ------------------------------------------------------------------ story
S.append(H1('Introduction'))
S += [P('This document is the Unit 1 submission of the Software Engineering project of Group CSC/24 (Aryabhatta College, Computer Science, Semester 5). It applies the Unit 1 syllabus topics (the layered approach to software engineering, the software process framework and umbrella activities, and the principal process models including Agile) to a real project: <b>ResaleIQ</b>, a used-smartphone resale price prediction system. The source of truth for every project-specific statement is the public repository <font name="Mono" size="9">github.com/shanib-techie/ResaleIQ</font>, which the team inspected in full (README, <font name="Mono" size="9">main.py</font>, the notebook <font name="Mono" size="9">analysis.ipynb</font>, the two model artifacts, <font name="Mono" size="9">requirements.txt</font>, the four-page static website and the git history). The FastAPI endpoint was also executed locally to check its behaviour.'),
      P('Because a repository records <i>what</i> was built but rarely <i>how</i> the team worked, this report keeps evidence and interpretation separate. Four tags are used consistently in the tables:')]
S += [T([['Tag', 'Meaning'],
         [V, 'Verified: observed directly in repository files, or confirmed by running the code.'],
         [R, 'Reported: stated in the README or in notebook output but not independently reproducible here (for example, the training data file is not in the repository).'],
         [A, 'Assumption: a reasonable reconstruction or generic statement, not recorded in the repository.'],
         [PR, 'Proposed: a recommended improvement that does not exist in the current implementation.']], [1, 9], zebra=False), Spacer(1, 6)]

# ---- Chapter 1
S.append(H1('Chapter 1: ResaleIQ Project Introduction'))
S.append(H2('1.1 Project overview and abstract'))
S.append(P('ResaleIQ estimates the resale value, in Indian rupees, of a second-hand smartphone. A user supplies thirteen inputs: brand, overall condition, original price, age in months, battery health, three damage indicators (screen cracked, body damage, water damage), the number of past repairs, remaining warranty months, availability of the original box and charger, and a market demand score. The values are sent as JSON to a FastAPI endpoint, <font name="Mono" size="9">POST /prediction</font>, which converts them into the feature layout expected by a pre-trained LightGBM regression model and returns <font name="Mono" size="9">predicted_resale_price</font>. The same FastAPI process also serves the project website, a static site written in plain HTML, CSS and JavaScript.'))
S.append(P(f'According to the README, the model was trained on a dataset of one million listings with 800,000 rows used for training; the notebook output confirms a 1,000,000 &times; 28 table, a training set of 800,000 rows and 22 final features. On the 200,000-row hold-out set the notebook reports R&sup2; = 0.9836, MAE = \u20b91,698.63 and RMSE = \u20b92,141.41 {V}. The dataset file itself is not stored in the repository, so these figures cannot be reproduced from the repository alone {R}. We also executed the README example (a Google phone in Good condition) against the stored model and obtained exactly the documented \u20b919,361.48 {V}.'))
S.append(H2('1.2 Problem statement and motivation'))
S.append(P(f'The resale price of a used phone depends on many interacting factors: how expensive it was when new, how old it is, how healthy the battery is, whether the screen is cracked, and how strong the market demand is. Sellers and buyers usually rely on guesswork, informal quotes or fixed price lists, which cannot reflect the particular combination of condition factors of one handset. This leads to under-pricing by sellers, over-pricing that stalls sales, and unequal bargaining power. ResaleIQ addresses this by learning the relationship between these factors and the final price from a large number of examples, and by exposing the result as an instant, interactive estimate. The README summarises the intent as a <i>live estimate, not a lookup table</i>. {A}'))
S.append(H2('1.3 Objectives'))
S += BL(['To predict the resale price of a used smartphone from thirteen user-supplied attributes with low average error.',
         'To compare several regression algorithms and adopt the one with the best accuracy and training scalability (Random Forest, XGBoost and LightGBM are compared in the README).',
         'To expose the trained model through a documented REST endpoint (<font name="Mono" size="9">POST /prediction</font>) with a simple JSON request and response.',
         'To provide an easy-to-use web interface in which a non-technical person can enter details and see the estimate immediately.',
         'To document the model, the dataset and the retraining procedure so that the system can be maintained and improved.'])
S.append(H2('1.4 Scope and intended users'))
S.append(P('<b>In scope</b> (verified): price estimation for seven brands (Apple, Samsung, Google, OnePlus, Xiaomi, Vivo, Realme) and four condition grades (Excellent, Good, Fair, Poor); a prediction web form; informational pages on the model and dataset; a developer profile page; and an offline retraining notebook. <b>Out of scope</b> (not present in the repository): user accounts or login, a database, a marketplace or listing facility, image-based damage detection, prediction by specific handset model (the <font name="Mono" size="9">model</font> column was deliberately dropped), and automatic collection of market data (the demand score is typed in by the user).'))
S.append(P(f'<b>Intended users.</b> Individual sellers and buyers who want a fair reference price; small resellers {A}; students and evaluators examining the project; and the developer or maintainer who retrains and redeploys the model.'))
S.append(H2('1.5 Main functionalities verified from the repository'))
S.append(reg.tabcap('features', 'Functionalities of ResaleIQ confirmed in the repository'))
S.append(T([['Functionality', 'Where implemented', 'Description'],
            ['Predict a price', 'predict.html, js/predict.js, main.py', 'Form with 13 inputs; button sends JSON to /prediction; result shown in rupees with a brand and condition badge.'],
            ['Model explanation', 'index.html', 'Accuracy comparison of three algorithms and feature importance charts.'],
            ['Dataset overview', 'dataset.html', 'Brand distribution, schema and feature groups of the training data.'],
            ['Developer profile', 'about.html, js/about.js', 'Fetches profile and repository data from the public GitHub API; keeps static fallback values on failure.'],
            ['Theme and navigation', 'js/theme.js, css/style.css', 'Dark/light toggle remembered in localStorage, mobile sidebar, active-link highlighting.'],
            ['Static hosting', 'main.py', "StaticFiles mount serves the website from the same Uvicorn process."],
            ['Model retraining', 'analysis.ipynb', 'Loads data, drops 14 columns, one-hot encodes, trains LightGBM, evaluates and exports two joblib files.']],
           [2.2, 3, 7]))
S.append(Spacer(1, 6))
S.append(H2('1.6 Existing approach and proposed system'))
S.append(reg.tabcap('stack', 'Comparison of common manual practice and ResaleIQ (the left column is a general description ' + A + ')'))
S.append(T([['Aspect', 'Typical existing approach', 'ResaleIQ'],
            ['Price source', 'Personal judgement, shop quotation, fixed lists, comparison with advertisements', 'Gradient-boosted model learned from one million records'],
            ['Condition factors', 'Considered informally; hard to weigh consistently', 'Eleven numeric and binary condition inputs plus brand and grade, weighted by the model'],
            ['Speed and access', 'Needs time, travel or negotiation', 'Instant estimate through a web form'],
            ['Consistency', 'Varies by person', 'Same inputs always give the same output'],
            ['Transparency', 'Rarely explained', 'Feature importance and accuracy are published on the website']],
           [1.6, 4, 4.4]))
S.append(H2('1.7 Benefits and limitations'))
S.append(P('<b>Benefits.</b> The system is fast and consistent, the web interface needs no installation, the whole stack is small (one Python file for the backend), and the retraining procedure is documented. <b>Limitations</b> found during inspection are listed below; they also feed the risk table in Chapter 4.'))
S += BL([f'Server-side validation is limited to data types. When we sent an unknown brand ("Nokia"), an unknown condition ("Mint"), a battery health of 500 or a negative price, the endpoint still returned HTTP 200 with a price {V}.',
         f'The frontend calls a hard-coded hosted address, <font name="Mono" size="9">http://resaleiq-checkyourownphone.onrender.com//prediction</font>, rather than the local server described in the README; the plain-http scheme and the double slash are also noteworthy {V}.',
         f'No automated tests, continuous integration or configuration files other than <font name="Mono" size="9">requirements.txt</font> exist, and package versions are not pinned {V}.',
         f'The training data file is absent and the README describes it both as "real-world" and as "synthetic-but-realistic", so the provenance of the data is unclear {R}.',
         f'The README feature-importance table lists <font name="Mono" size="9">os_type_Android</font>, which is not among the 22 columns of the production model, and gives a different <font name="Mono" size="9">brand_Apple</font> value (288) from the notebook output (304) {V}.',
         'The output is a single point estimate without a confidence range, and the market demand score must be supplied manually.'])
S.append(H2('1.8 Technology stack and system overview'))
S.append(reg.tabcap('stack', 'Verified technology stack'))
S.append(T([['Layer', 'Technology', 'Evidence'],
            ['Machine learning', 'Python, pandas, scikit-learn (metrics, split), LightGBM; XGBoost and Random Forest for comparison', 'analysis.ipynb, requirements.txt, README'],
            ['Model persistence', 'joblib (model.pkl, model_columns.pkl)', 'main.py, notebook cell 5'],
            ['Backend', 'FastAPI, Pydantic (class Detail), Uvicorn, CORS middleware, StaticFiles', 'main.py, README'],
            ['Frontend', 'HTML5, CSS3, vanilla JavaScript (fetch API, localStorage)', 'resaleiq-website/'],
            ['Version control', 'Git and GitHub (14 commits on 2026-08-08 and 2026-10-17)', 'git log']],
           [1.8, 5, 3]))
S.append(Spacer(1, 4))
S.append(KeepTogether([Diagram(470, 220, fig_overview),
                       reg.figcap('overview', 'High-level overview of ResaleIQ components as found in the repository')]))
S.append(P(f'{F("overview")} shows the physical components. The browser loads static pages from the FastAPI server and posts prediction requests to it; the server loads the two model artifacts once at start-up; the notebook, run offline by the developer, produces those artifacts. The About page contacts the GitHub API directly from the browser and does not involve the ResaleIQ server.'))

# ---- Chapter 2
S.append(H1('Chapter 2: Software Engineering \u2014 A Layered Approach'))
S.append(P('Software engineering is the application of a systematic, disciplined and quantifiable approach to the development, operation and maintenance of software. In the layered view popularised by Pressman, the discipline is a stack of four layers, each resting on the one below. The foundation is a <b>quality focus</b>: every layer exists to produce software that meets its requirements and is dependable. Above it sits the <b>process</b> layer, the glue that holds the technology layers together and defines the framework of activities for delivering software on time. The <b>methods</b> layer supplies the technical "how-to" for each task (communication, requirements analysis, design modelling, construction and testing). The topmost <b>tools</b> layer gives automated or semi-automated support for the process and the methods.'))
S.append(KeepTogether([Diagram(470, 205, fig_layers),
                       reg.figcap('layers', 'The layered approach of software engineering mapped to ResaleIQ')]))
S.append(P(f'{F("layers")} maps each layer to concrete elements of ResaleIQ, and {Tb("layermap")} explains the mapping.'))
S.append(reg.tabcap('layermap', 'Layer-by-layer application to ResaleIQ'))
S.append(T([['Layer', 'Role', 'Concrete example in ResaleIQ', 'Evidence'],
            ['Quality focus', 'Defines what "good" means and drives all other layers', 'Hold-out accuracy (R&sup2;, MAE, RMSE) used to choose LightGBM; fixed random_state=42 for repeatable results; column alignment so training and serving features agree', V],
            ['Process', 'Organises work into activities and tasks', 'Experiment in a notebook, trim features, export artifacts, build API, build UI, redeploy (commit history shows a build phase in August and a deployment phase in October)', f'{V} {A}'],
            ['Methods', 'Technical techniques for each task', 'Supervised regression, one-hot encoding, train/test split, feature-importance analysis, REST/JSON contract, Pydantic schema validation', V],
            ['Tools', 'Automation and support', 'Python, FastAPI, Uvicorn, pandas, LightGBM, joblib, Jupyter, Git/GitHub, requirements.txt', V]],
           [1.5, 2.3, 6, 0.8]))
S.append(H2('2.1 Addressing quality across the lifecycle'))
S.append(reg.tabcap('quality', 'Quality concerns at each stage of the ResaleIQ lifecycle'))
S.append(T([['Stage', 'Quality question', 'ResaleIQ practice or gap'],
            ['Requirements', 'Are inputs, outputs and ranges clearly defined?', 'README API table defines types and ranges; ranges are declared but not enforced by the server (Unit 2 treats this in detail)'],
            ['Design', 'Is responsibility separated?', 'Static frontend, a single prediction endpoint and externalised model artifacts; the handler combines several steps in one function (Unit 3)'],
            ['Implementation', 'Is the code consistent and reproducible?', 'Same encoding steps in notebook and API; model_columns.pkl guards column order; unpinned dependencies are a weakness'],
            ['Validation', 'Does the system meet accuracy goals?', 'Hold-out metrics in the notebook; README example reproduced; no automated test suite'],
            ['Maintenance', 'Can the model be updated safely?', 'README gives a retraining recipe: dump model and columns, restart the server']],
           [1.4, 3, 6]))

# ---- Chapter 3
S.append(H1('Chapter 3: Software Process Framework'))
S.append(P('A <b>process framework</b> identifies a small number of <i>framework activities</i> that apply to every software project regardless of size or complexity. Each activity is populated by a set of actions, tasks and work products that vary with the project. Five generic activities are used: <b>Communication</b> (understanding stakeholder needs and gathering requirements), <b>Planning</b> (describing tasks, risks, resources and schedule), <b>Modeling</b> (creating models that show requirements and design), <b>Construction</b> (code generation and testing) and <b>Deployment</b> (delivery to the customer, who evaluates it and gives feedback).'))
S.append(KeepTogether([Diagram(470, 165, fig_framework),
                       reg.figcap('framework', 'Process framework activities and umbrella activities applied to ResaleIQ')]))
S.append(reg.tabcap('frameworkmap', 'Framework activities mapped to ResaleIQ, separating documented evidence from reconstruction'))
S.append(T([['Activity', 'Documented evidence in repository', 'Reconstructed or recommended practice'],
            ['Communication', 'README states goals and defines the 13-field API contract', f'{A} Informal discussion among the three team members and a faculty member about scope; recommended: a one-page stakeholder note'],
            ['Planning', 'README records why Random Forest and XGBoost were dropped; the final feature set was trimmed by importance', f'{A} Schedule and task allocation are not recorded; recommended: an issue list with milestones'],
            ['Modeling', 'Data schema and feature groups on dataset.html; JSON request/response specification; architecture sketch in README', f'{PR} Formal use case, DFD and design models, which this report set (Units 2 and 3) supplies'],
            ['Construction', 'main.py, analysis.ipynb, model.pkl, model_columns.pkl, four HTML pages, three JS files, style.css', f'{PR} Automated tests (none exist); input validation in the API'],
            ['Deployment', 'requirements.txt, CORS middleware and an external API URL added on 2026-10-17; run instructions in README', f'{A} Hosting platform is inferred from the onrender.com address only; feedback loop from real users is not documented']],
           [1.4, 4.2, 4.4]))
S.append(Spacer(1, 4))
S.append(P(f'The commit history (nine commits on 8 August 2026 and five on 17 October 2026) shows that the work happened in two bursts: first the model, website and README, then a deployment-oriented phase that added dependencies, CORS and the production API address. This is consistent with a Construction-then-Deployment pattern, but the history alone cannot show how requirements or plans were obtained {A}.'))

# ---- Chapter 4
S.append(H1('Chapter 4: Umbrella Activities'))
S.append(P('Umbrella activities are applied across the entire project and support the framework activities. Table '+ str(reg.tabs.index('umbrella')+1) +' summarises how each is applied to ResaleIQ and what evidence exists.'))
S.append(reg.tabcap('umbrella', 'Umbrella activities applied to ResaleIQ'))
S.append(T([['Umbrella activity', 'Purpose', 'Application to ResaleIQ', 'Status'],
            ['Project tracking and control', 'Compare progress with plan and take corrective action', 'Git commit log provides a time-stamped record; recommended: issue board with milestones for increments', f'{V} partial'],
            ['Risk management', 'Identify, assess and mitigate risks', 'Risk table below covering data, model, API and deployment risks', PR],
            ['Software quality assurance', 'Ensure conformance to standards and requirements', 'Hold-out evaluation (R&sup2;, MAE, RMSE); manual run of README example; recommended: automated API tests', f'{V} partial'],
            ['Technical reviews', 'Find defects before they propagate', 'Team code walkthrough of main.py and predict.js; this inspection found README/notebook inconsistencies (Section 1.7)', f'{A}'],
            ['Measurement and metrics', 'Quantify process and product', 'Product metrics in Table ' + str(reg.tabs.index('metrics')+1), V],
            ['Configuration management', 'Control changes to work products', 'Git and GitHub hold all source and model artifacts; .gitignore excludes venv/ and caches; dependencies unpinned', f'{V} partial'],
            ['Reuse management', 'Reuse proven components', 'Reuses FastAPI, Pydantic, pandas, LightGBM, joblib; reuse of trained model.pkl across restarts', V],
            ['Work-product preparation', 'Produce documents and models', 'README, notebook, website pages and this three-unit report set', V]],
           [1.7, 2.4, 5, 1]))
S.append(H2('4.1 Measurement and metrics'))
S.append(reg.tabcap('metrics', 'Product and model metrics collected from the repository'))
S.append(T([['Metric', 'Value', 'Source / note'],
            ['Backend source size', f'{LOC_MAIN} lines (main.py)', 'Counted from the cloned repository'],
            ['Frontend JavaScript', f'{LOC_PJS + LOC_TJS + LOC_AJS} lines in 3 files (predict.js {LOC_PJS}, theme.js {LOC_TJS}, about.js {LOC_AJS})', 'Counted'],
            ['Frontend HTML / CSS', f'{LOC_HTML} lines in 4 pages; {LOC_CSS} lines CSS', 'Counted'],
            ['API surface', '1 endpoint (POST /prediction) plus static mount', 'main.py'],
            ['Input fields / model columns', '13 request fields; 22 model columns after one-hot encoding', 'Pydantic class Detail; model_columns.pkl'],
            ['Training / test rows', '800,000 / 200,000 (80/20 split, random_state=42)', 'Notebook output ' + R],
            ['Model accuracy', 'R&sup2; 0.9836; MAE \u20b91,698.63; RMSE \u20b92,141.41', 'Notebook output ' + R],
            ['Automated tests', '0', 'None found in the repository']],
           [2.3, 4.2, 3.5]))
S.append(H2('4.2 Project-specific risk table'))
S.append(reg.tabcap('risks', 'Risk register for ResaleIQ (L = likelihood, I = impact)'))
S.append(T([['ID', 'Risk', 'L', 'I', 'Mitigation'],
            ['R1', 'Out-of-range or unknown categorical input produces a plausible but meaningless price (confirmed by test)', 'High', 'High', 'Add Pydantic constraints and enumerations; return HTTP 422 for invalid values'],
            ['R2', 'Training data not representative or provenance unclear, causing biased estimates', 'Med', 'High', 'Document data source; evaluate by brand and condition; refresh data'],
            ['R3', 'Market drift: prices change but model is static', 'Med', 'High', 'Schedule periodic retraining using the documented procedure'],
            ['R4', 'Hosting or address dependency: hard-coded external URL, plain http, double slash', 'Med', 'High', 'Move URL to configuration; use relative path or https; add health check'],
            ['R5', 'Training-serving skew if model.pkl and model_columns.pkl are updated inconsistently', 'Low', 'High', 'Version both files together; add start-up assertion on column count'],
            ['R6', 'Unpinned dependencies make pickled model fail to load after library upgrade', 'Med', 'High', 'Pin versions in requirements.txt; record training environment'],
            ['R7', 'No automated tests, so regressions go unnoticed', 'High', 'Med', 'Add pytest tests for the endpoint and encoding step'],
            ['R8', 'Open CORS and no rate limit allow abuse of the public endpoint', 'Med', 'Med', 'Restrict allowed origins; add rate limiting if public use grows']],
           [0.6, 5.2, 0.7, 0.7, 4.4]))

# ---- Chapter 5
S.append(H1('Chapter 5: Software Process Models'))
S.append(P('A <b>process model</b> prescribes the order and relationship of the framework activities. No model is universally best; the choice depends on how stable the requirements are, how risky the technology is, how quickly working software is needed and how large the team is. The sections below describe each model in the syllabus and apply it to ResaleIQ. The applications are <i>illustrative</i>: the repository does not state which model the team followed.'))
S.append(H2('5.1 Waterfall model'))
S.append(P('The Waterfall (classic life-cycle) model is a linear, sequential model in which communication, planning, modelling, construction and deployment follow one another, and each phase ends with a review before the next begins. It works best when requirements are well understood and unlikely to change.'))
S.append(KeepTogether([Diagram(470, 168, fig_waterfall),
                       reg.figcap('waterfall', 'Waterfall model phases')]))
S += BL(['<b>Advantages:</b> simple and easy to manage; clear milestones and documentation; suits stable, well-defined problems.',
         '<b>Disadvantages:</b> real projects rarely proceed linearly; working software appears late; changes found in testing are costly; clients must state all requirements early.',
         '<b>ResaleIQ application:</b> the 13-field input list and the JSON contract are stable and could be specified up front: define the contract, design the pipeline, implement, test, deploy. The weakness is the model itself, whose best algorithm and feature set could not be known in advance, so a purely linear plan would be risky.'])
S.append(H2('5.2 Incremental model'))
S.append(P('The Incremental model combines the linear flow of Waterfall with the iterative flow of prototyping. Software is built in a sequence of increments, each passing through communication, planning, modelling, construction and deployment and each delivering a usable subset of the final functionality. The first increment is often the core product.'))
S.append(KeepTogether([Diagram(470, 175, fig_incremental),
                       reg.figcap('incremental', 'Incremental model applied to ResaleIQ increments')]))
S += BL(['<b>Advantages:</b> early working software; easier to test and debug in small steps; flexible and adaptable to staffing limits; risk is spread.',
         '<b>Disadvantages:</b> needs a good up-front architecture so that increments integrate; total cost may be higher; poor planning leads to design erosion.',
         '<b>ResaleIQ application:</b> the system decomposes naturally into increments: (1) trained model and notebook, (2) FastAPI prediction endpoint, (3) prediction page, (4) informational pages and deployment hardening. These match the files in the repository, although the order is a reconstruction ' + A + '.'])
S.append(H2('5.3 Evolutionary process models'))
S.append(P('Evolutionary models are iterative: they produce increasingly complete versions of the software and are designed for situations where requirements or the product concept evolve. Two representative models are Prototyping and the Spiral model, described next.'))
S.append(H2('5.4 Prototyping model'))
S.append(P('Prototyping begins with communication to establish objectives, then proceeds through a quick plan and a quick design that concentrates on what the user will see. A prototype is constructed, deployed and evaluated by stakeholders, whose feedback refines the requirements; the cycle repeats until stakeholders are satisfied, after which the real system is engineered. The prototype is usually thrown away or evolved.'))
S.append(KeepTogether([Diagram(470, 195, fig_proto),
                       reg.figcap('prototyping', 'Prototyping model: iterative cycle between developers and stakeholders')]))
S += BL(['<b>Advantages:</b> clarifies unclear requirements early; users see something tangible; reduces the risk of building the wrong product.',
         '<b>Disadvantages:</b> stakeholders may mistake a prototype for the finished product; quick design compromises can persist; effort may be wasted.',
         '<b>ResaleIQ application:</b> the notebook is a model prototype (the README records Random Forest and XGBoost attempts before LightGBM), and the prediction form began as a way to try the model with real inputs. Pressman&rsquo;s advice that the prototype be a "first system" to throw away is relevant: the notebook&rsquo;s interactive <font name="Mono" size="9">input()</font> loop is the throw-away prototype, whereas <font name="Mono" size="9">main.py</font> is the engineered version.'])
S.append(H2('5.5 Spiral model'))
S.append(P('Proposed by Barry Boehm, the Spiral model is a risk-driven evolutionary model. Each loop around the spiral passes through four broad activities: planning, risk analysis, engineering and customer evaluation. Early loops produce concept documents or prototypes; later loops yield progressively complete versions. Cost and effort accumulate with distance from the centre.'))
S.append(KeepTogether([Diagram(470, 205, fig_spiral),
                       reg.figcap('spiral', 'Spiral model with four illustrative ResaleIQ loops')]))
S += BL(['<b>Advantages:</b> explicit risk handling; suits large, innovative or uncertain projects; supports reuse and change.',
         '<b>Disadvantages:</b> demands risk-assessment expertise; heavy management overhead; unsuitable for small, low-risk projects.',
         '<b>ResaleIQ application:</b> the riskiest question was technical: can the thirteen inputs predict price accurately? Loop 1 answers feasibility, Loop 2 compares candidate algorithms, Loop 3 builds the production model and API, and Loop 4 handles interface, deployment and hardening. The mapping is illustrative; the project is small enough that full Spiral management would be excessive.'])
S.append(H2('5.6 Agile development and the Agile model'))
S.append(P('Agile software development responds to changing requirements through short iterations, close collaboration with stakeholders and continuous delivery of working software. It is based on the Agile Manifesto (2001), which values individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. Common agile methods include Scrum (product backlog, time-boxed sprints, daily stand-ups, review and retrospective) and Extreme Programming (pair programming, test-driven development, continuous integration).'))
S.append(KeepTogether([Diagram(470, 182, fig_agile),
                       reg.figcap('agile', 'Agile (Scrum-style) iteration cycle')]))
S += BL(['<b>Advantages:</b> rapid delivery; high adaptability; continuous feedback; good fit for small, co-located teams.',
         '<b>Disadvantages:</b> less formal documentation; needs active stakeholder involvement; scope can drift without a disciplined backlog.',
         '<b>ResaleIQ application:</b> a product backlog could contain user stories such as "As a seller, I want to enter my phone&rsquo;s condition and see an estimated price" or "As a maintainer, I want to retrain the model without changing the API". A one- or two-week sprint could deliver one story, e.g. adding server-side validation, with a review against acceptance criteria (Unit 2).'])
S.append(H2('5.7 Comparison and recommendation'))
S.append(reg.tabcap('compare', 'Comparison of process models'))
S.append(T([['Criterion', 'Waterfall', 'Incremental', 'Prototyping', 'Spiral', 'Agile'],
            ['Requirement stability needed', 'High', 'Medium', 'Low', 'Low', 'Low'],
            ['Working software delivered', 'Late', 'Early, repeated', 'Prototype early', 'Each loop', 'Every sprint'],
            ['Risk handling', 'Weak', 'Moderate', 'Moderate (UI/needs)', 'Strong, explicit', 'Moderate, via feedback'],
            ['Documentation', 'Heavy', 'Moderate', 'Light', 'Moderate to heavy', 'Light'],
            ['Management overhead', 'Low', 'Medium', 'Low', 'High', 'Medium'],
            ['Suitability for small teams', 'Fair', 'Good', 'Good', 'Poor', 'Very good'],
            ['Fit for ResaleIQ', 'Low', 'High', 'Medium (for model and UI)', 'Low (too heavy)', 'High']],
           [2.3, 1.5, 1.8, 1.8, 1.6, 1.7], hl_first_col=True))
S.append(Spacer(1, 5))
S.append(P('<b>Recommendation.</b> For ResaleIQ the team recommends the <b>Incremental model with evolutionary prototyping inside each increment, run in an agile, sprint-like cadence</b>. This recommendation rests on the actual characteristics of the project: (i) the product has a small, separable structure (model, API, UI, information pages) that suits incremental delivery; (ii) the model selection was exploratory, which demands prototyping and re-evaluation; (iii) the team is small, so light-weight agile ceremonies suffice and the Spiral model\u2019s overhead is unjustified; and (iv) the input contract is stable enough that heavy up-front documentation, as in Waterfall, is unnecessary. The repository history is <i>consistent with</i> this pattern (a working base followed by deployment refinements) but does not prove it.'))
S.append(reg.tabcap('increments', 'Recommended increment plan (Increments 1\u20134 correspond to existing files; Increment 5 is proposed)'))
S.append(T([['Increment', 'Deliverable', 'Status'],
            ['1', 'Cleaned feature set, LightGBM model, evaluation, exported artifacts (analysis.ipynb, model.pkl, model_columns.pkl)', f'{V} exists'],
            ['2', 'FastAPI endpoint with Pydantic schema, encoding and alignment (main.py)', f'{V} exists'],
            ['3', 'Prediction form and result display (predict.html, predict.js)', f'{V} exists'],
            ['4', 'Model, dataset and about pages; theme; CORS and deployment URL', f'{V} exists'],
            ['5', 'Server-side range and category validation, automated tests, configurable API URL, pinned dependencies', f'{PR} proposed']],
           [1.2, 7.5, 1.6]))

# ---- Chapter 6
S.append(H1('Chapter 6: Unit Conclusion'))
S.append(P('This unit has shown that the abstract ideas of software engineering are directly visible in a small machine-learning project. The layered approach explains why accuracy metrics (quality focus), a repeatable experiment-to-deployment flow (process), regression and API techniques (methods) and the Python ecosystem (tools) must be considered together. The five framework activities and the umbrella activities show where ResaleIQ is well supported (version control, measurement of model accuracy, reuse of libraries) and where it is weak (no automated tests, no recorded plan, limited validation, unpinned dependencies). The review of the Waterfall, Incremental, Evolutionary (Prototyping and Spiral) and Agile models led to the recommendation of incremental delivery with prototyping and an agile cadence, a choice justified by the project\u2019s separable structure, exploratory modelling and small team. The risk register and the increment plan give a concrete path for maintaining and improving ResaleIQ, and the following units build on this foundation by specifying its requirements (Unit 2) and design (Unit 3).'))

S.append(H1('References'))
for r in ['Pressman, R. S. and Maxim, B. R. <i>Software Engineering: A Practitioner&rsquo;s Approach</i>, McGraw-Hill (layered approach, process framework, umbrella activities, process models).',
          'Sommerville, I. <i>Software Engineering</i>, Pearson (process models and agile methods).',
          'Royce, W. W. (1970). Managing the Development of Large Software Systems. <i>Proceedings of IEEE WESCON</i>.',
          'Boehm, B. W. (1988). A Spiral Model of Software Development and Enhancement. <i>IEEE Computer</i>, 21(5), 61\u201372.',
          'Beck, K. et al. (2001). <i>Manifesto for Agile Software Development</i>. agilemanifesto.org.',
          'Ke, G. et al. (2017). LightGBM: A Highly Efficient Gradient Boosting Decision Tree. <i>Advances in Neural Information Processing Systems 30</i>.',
          'ResaleIQ source repository: https://github.com/shanib-techie/ResaleIQ (README, main.py, analysis.ipynb, resaleiq-website/, requirements.txt, git history), inspected October 2026.',
          'FastAPI and Pydantic project documentation (framework behaviour confirmed by running the application locally).']:
    S.append(Paragraph(rup(r), STY['ref'], bulletText='\u2022'))

reg.check()
build('/mnt/user-data/outputs/ResaleIQ_Unit_1_Software_Processes.pdf', 1, 'Software Engineering and Software Processes',
      'Syllabus: Software Engineering \u2014 A Layered Approach; Software Process Framework and Umbrella Activities; Waterfall, Incremental and Evolutionary Process Models (Prototyping, Spiral); Introduction to Agile and the Agile Model.', S)
print('built')