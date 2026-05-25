#!/usr/bin/env python3

"""
Tellent Affiliate SEO Site Builder
GitHub Pages Ready Static Site Generator

Domain:
https://brightlane.github.io/tellent/

Affiliate:
https://join.tellent.com/sjxu9svfbqoi
"""

import json
import random
import shutil
from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

SITE_NAME = "Tellent Hiring Hub"

DOMAIN = "https://brightlane.github.io/tellent"

AFFILIATE_URL = "https://join.tellent.com/sjxu9svfbqoi"

YEAR = datetime.now().year

TODAY = datetime.now().strftime("%Y-%m-%d")

# =========================================================
# CTA VARIATIONS
# =========================================================

CTAS = [
    "Start Using Tellent",
    "Automate Hiring Today",
    "Improve Recruitment Workflows",
    "Launch Tellent ATS",
    "Hire Smarter With Tellent",
    "Streamline Your Recruiting",
    "Get Started With Tellent",
]

# =========================================================
# CORE SEO PAGES
# =========================================================

PAGES = [
    {
        "slug": "index",
        "title": "Tellent ATS & Recruiting Software",
        "description": "Modern recruiting software and applicant tracking tools for growing teams.",
        "keyword": "tellent ats"
    },

    {
        "slug": "ai-recruiting",
        "title": "AI Recruiting Software",
        "description": "Automate hiring and recruitment workflows using AI recruiting tools.",
        "keyword": "ai recruiting software"
    },

    {
        "slug": "applicant-tracking-system",
        "title": "Best Applicant Tracking System",
        "description": "Discover how ATS platforms streamline hiring pipelines.",
        "keyword": "applicant tracking system"
    },

    {
        "slug": "recruitment-automation",
        "title": "Recruitment Automation Tools",
        "description": "Reduce manual hiring work using recruitment automation.",
        "keyword": "recruitment automation"
    },

    {
        "slug": "candidate-management",
        "title": "Candidate Management Software",
        "description": "Organize candidates and improve hiring collaboration.",
        "keyword": "candidate management software"
    },

    {
        "slug": "hiring-software",
        "title": "Best Hiring Software For Businesses",
        "description": "Top hiring platforms for startups, HR teams, and recruiters.",
        "keyword": "hiring software"
    },

    {
        "slug": "ats-for-startups",
        "title": "Best ATS For Startups",
        "description": "Affordable applicant tracking systems for startup hiring.",
        "keyword": "ats for startups"
    },

    {
        "slug": "recruiting-crm",
        "title": "Recruiting CRM Software",
        "description": "Manage recruiting pipelines and candidate relationships.",
        "keyword": "recruiting crm"
    }
]

# =========================================================
# INDUSTRY PAGES
# =========================================================

INDUSTRIES = [
    "tech-companies",
    "staffing-agencies",
    "healthcare",
    "restaurants",
    "retail",
    "startups",
    "law-firms",
    "real-estate",
    "construction",
    "saas"
]

# =========================================================
# BLOG TOPICS
# =========================================================

BLOG_TOPICS = [
    "How AI Is Changing Recruitment",
    "Best ATS Platforms For Small Businesses",
    "How To Improve Candidate Experience",
    "Recruitment Automation Strategies",
    "Best Hiring Software For Startups",
    "How To Hire Faster Using AI",
    "Modern Recruiting Best Practices",
    "How To Reduce Hiring Costs",
    "Benefits Of Applicant Tracking Systems",
    "How Recruiters Use AI Tools"
]

# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).parent

DIST_DIR = BASE_DIR / "dist"

ASSETS_DIR = DIST_DIR / "assets"

BLOG_DIR = DIST_DIR / "blog"

TAG_DIR = DIST_DIR / "tag"

# =========================================================
# CLEAN DIST
# =========================================================

if DIST_DIR.exists():
    shutil.rmtree(DIST_DIR)

DIST_DIR.mkdir()
ASSETS_DIR.mkdir()
BLOG_DIR.mkdir()
TAG_DIR.mkdir()

# =========================================================
# CSS
# =========================================================

STYLE = """
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#0f172a;
    color:#e2e8f0;
    font-family:Arial,sans-serif;
    line-height:1.7;
}

header{
    background:#111827;
    padding:20px 0;
    border-bottom:2px solid #22c55e;
    position:sticky;
    top:0;
    z-index:999;
}

.container{
    width:92%;
    max-width:1200px;
    margin:auto;
}

.logo{
    font-size:2rem;
    color:#22c55e;
    font-weight:bold;
}

nav{
    margin-top:15px;
}

nav a{
    color:#cbd5e1;
    text-decoration:none;
    margin-right:18px;
    font-weight:bold;
}

nav a:hover{
    color:#22c55e;
}

.hero{
    text-align:center;
    padding:120px 20px;
    background:linear-gradient(to right,#111827,#1e293b);
}

.hero h1{
    font-size:3.5rem;
    color:#22c55e;
    margin-bottom:20px;
}

.hero p{
    max-width:850px;
    margin:auto;
    margin-bottom:35px;
    font-size:1.2rem;
}

.button{
    display:inline-block;
    background:#22c55e;
    color:white;
    padding:15px 30px;
    border-radius:6px;
    text-decoration:none;
    font-weight:bold;
}

.button:hover{
    background:#16a34a;
}

.section{
    padding:80px 0;
}

.card{
    background:#1e293b;
    padding:30px;
    border-radius:10px;
    border:1px solid #334155;
    margin-bottom:30px;
}

.card h2,
.card h3{
    color:#22c55e;
    margin-bottom:15px;
}

.related a{
    display:block;
    color:#22c55e;
    margin-bottom:10px;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th, td{
    border:1px solid #334155;
    padding:12px;
}

th{
    background:#111827;
}

footer{
    background:#020617;
    padding:40px 20px;
    text-align:center;
    border-top:2px solid #22c55e;
}
"""

(ASSETS_DIR / "style.css").write_text(
    STYLE,
    encoding="utf-8"
)

# =========================================================
# NAVIGATION
# =========================================================

def build_nav():

    links = []

    for page in PAGES:

        file = (
            "index.html"
            if page["slug"] == "index"
            else f"{page['slug']}.html"
        )

        links.append(
            f'<a href="{file}">{page["title"]}</a>'
        )

    links.append('<a href="blog/index.html">Blog</a>')

    return "\n".join(links)

NAV = build_nav()

# =========================================================
# CTA
# =========================================================

def random_cta():
    return random.choice(CTAS)

# =========================================================
# RELATED LINKS
# =========================================================

def related_links(current_slug):

    pages = []

    for page in PAGES:

        if page["slug"] == current_slug:
            continue

        file = (
            "index.html"
            if page["slug"] == "index"
            else f"{page['slug']}.html"
        )

        pages.append(
            f'<a href="{file}">{page["title"]}</a>'
        )

    random.shuffle(pages)

    return "\n".join(pages[:5])

# =========================================================
# LONG SEO CONTENT
# =========================================================

def generate_content(keyword):

    sections = []

    for i in range(1, 9):

        sections.append(f"""
        <div class="card">

        <h2>{keyword.title()} Guide {i}</h2>

        <p>
        Modern recruiting teams increasingly use applicant tracking systems,
        AI hiring automation, and recruitment CRM software to streamline hiring.
        </p>

        <p>
        Tellent helps HR teams automate candidate communication,
        organize hiring pipelines, and improve collaboration across recruiting workflows.
        </p>

        <p>
        Businesses using recruitment automation software can reduce hiring costs,
        improve candidate experience, and accelerate hiring decisions.
        </p>

        <a class="button" href="{AFFILIATE_URL}">
        {random_cta()}
        </a>

        </div>
        """)

    return "\n".join(sections)

# =========================================================
# FAQ SCHEMA
# =========================================================

FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What is Tellent?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Tellent is a recruiting and applicant tracking platform for modern businesses."
            }
        },
        {
            "@type": "Question",
            "name": "Does Tellent support recruitment automation?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Tellent includes automation features for recruiting and hiring workflows."
            }
        },
        {
            "@type": "Question",
            "name": "Who uses Tellent?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Recruiters, HR teams, startups, staffing agencies, and enterprises use Tellent."
            }
        }
    ]
}

# =========================================================
# TEMPLATE
# =========================================================

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">

<meta name="keywords" content="{keyword}">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">

<link rel="stylesheet" href="assets/style.css">

<script type="application/ld+json">
{schema}
</script>

<script type="application/ld+json">
{faq_schema}
</script>

</head>

<body>

<header>

<div class="container">

<div class="logo">
{site_name}
</div>

<nav>
{navigation}
</nav>

</div>

</header>

<section class="hero">

<div class="container">

<h1>{title}</h1>

<p>{description}</p>

<a class="button" href="{affiliate}">
{cta}
</a>

</div>

</section>

<section class="section">

<div class="container">

<div class="card">

<h2>
Why Businesses Use Tellent
</h2>

<p>
Tellent combines applicant tracking systems, recruitment automation,
candidate management, and AI hiring workflows into one scalable hiring platform.
</p>

<a class="button" href="{affiliate}">
{cta}
</a>

</div>

<div class="card">

<h2>
Hiring Software Comparison
</h2>

<table>

<tr>
<th>Feature</th>
<th>Tellent</th>
<th>Traditional Hiring</th>
</tr>

<tr>
<td>AI Automation</td>
<td>Yes</td>
<td>No</td>
</tr>

<tr>
<td>ATS Platform</td>
<td>Yes</td>
<td>Manual</td>
</tr>

<tr>
<td>Recruitment CRM</td>
<td>Included</td>
<td>No</td>
</tr>

<tr>
<td>Analytics</td>
<td>Advanced</td>
<td>Basic</td>
</tr>

</table>

</div>

{content}

<div class="card related">

<h2>
Related Guides
</h2>

{related_links}

</div>

<div class="card">

<h2>
Recruiting Newsletter
</h2>

<form>

<input
type="email"
placeholder="Enter your email"
style="padding:12px;width:100%;margin-bottom:15px;"
>

<button
style="padding:12px 24px;background:#22c55e;color:white;border:none;"
>
Subscribe
</button>

</form>

</div>

</div>

</section>

<footer>

<p>
© {year} {site_name}
</p>

<p style="margin-top:20px;">
<a class="button" href="{affiliate}">
{cta}
</a>
</p>

</footer>

</body>

</html>
"""

# =========================================================
# GENERATE CORE PAGES
# =========================================================

all_urls = []

for page in PAGES:

    filename = (
        "index.html"
        if page["slug"] == "index"
        else f"{page['slug']}.html"
    )

    canonical = (
        DOMAIN + "/"
        if page["slug"] == "index"
        else f"{DOMAIN}/{page['slug']}.html"
    )

    all_urls.append(canonical)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": page["title"],
        "description": page["description"]
    }, indent=2)

    html = PAGE_TEMPLATE.format(
        title=page["title"],
        description=page["description"],
        keyword=page["keyword"],
        canonical=canonical,
        schema=schema,
        faq_schema=json.dumps(FAQ_SCHEMA, indent=2),
        site_name=SITE_NAME,
        navigation=NAV,
        affiliate=AFFILIATE_URL,
        cta=random_cta(),
        content=generate_content(page["keyword"]),
        related_links=related_links(page["slug"]),
        year=YEAR
    )

    (DIST_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# INDUSTRY PAGES
# =========================================================

for industry in INDUSTRIES:

    slug = f"ats-for-{industry}"

    title = f"Best ATS For {industry.replace('-', ' ').title()}"

    keyword = f"ats for {industry.replace('-', ' ')}"

    filename = f"{slug}.html"

    canonical = f"{DOMAIN}/{filename}"

    all_urls.append(canonical)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": keyword
    }, indent=2)

    html = PAGE_TEMPLATE.format(
        title=title,
        description=f"Discover how recruiting software helps {industry.replace('-', ' ')} businesses hire faster.",
        keyword=keyword,
        canonical=canonical,
        schema=schema,
        faq_schema=json.dumps(FAQ_SCHEMA, indent=2),
        site_name=SITE_NAME,
        navigation=NAV,
        affiliate=AFFILIATE_URL,
        cta=random_cta(),
        content=generate_content(keyword),
        related_links=related_links("index"),
        year=YEAR
    )

    (DIST_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# DAILY BLOG POSTS
# =========================================================

blog_links = []

for i in range(5):

    topic = random.choice(BLOG_TOPICS)

    slug = f"{TODAY}-{i}"

    filename = f"{slug}.html"

    canonical = f"{DOMAIN}/blog/{filename}"

    all_urls.append(canonical)

    blog_links.append(
        f'<li><a href="{filename}">{topic}</a></li>'
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <title>{topic}</title>

    <link rel="stylesheet" href="../assets/style.css">

    </head>

    <body>

    <section class="hero">

    <div class="container">

    <h1>{topic}</h1>

    <p>
    Learn how modern recruiting software improves hiring efficiency.
    </p>

    <a class="button" href="{AFFILIATE_URL}">
    {random_cta()}
    </a>

    </div>

    </section>

    <section class="section">

    <div class="container">

    {generate_content(topic)}

    </div>

    </section>

    </body>

    </html>
    """

    (BLOG_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# BLOG INDEX
# =========================================================

BLOG_INDEX = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>Tellent Recruiting Blog</title>

<link rel="stylesheet" href="../assets/style.css">

</head>

<body>

<section class="section">

<div class="container">

<div class="card">

<h1>
Tellent Recruiting Blog
</h1>

<ul>

{"".join(blog_links)}

</ul>

<p style="margin-top:20px;">

<a class="button" href="{AFFILIATE_URL}">
{random_cta()}
</a>

</p>

</div>

</div>

</section>

</body>

</html>
"""

(BLOG_DIR / "index.html").write_text(
    BLOG_INDEX,
    encoding="utf-8"
)

# =========================================================
# TAG PAGES
# =========================================================

tags = [
    "ats",
    "recruiting",
    "hr-software",
    "hiring",
    "candidate-management"
]

for tag in tags:

    filename = f"{tag}.html"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <title>{tag}</title>

    <link rel="stylesheet" href="../assets/style.css">

    </head>

    <body>

    <section class="section">

    <div class="container">

    <div class="card">

    <h1>{tag.replace('-', ' ').title()}</h1>

    <p>
    Explore resources related to {tag.replace('-', ' ')}.
    </p>

    <a class="button" href="{AFFILIATE_URL}">
    {random_cta()}
    </a>

    </div>

    </div>

    </section>

    </body>

    </html>
    """

    (TAG_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# SITEMAP
# =========================================================

sitemap_urls = []

for url in all_urls:

    sitemap_urls.append(f"""
    <url>
    <loc>{url}</loc>
    </url>
    """)

SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

{''.join(sitemap_urls)}

</urlset>
"""

(DIST_DIR / "sitemap.xml").write_text(
    SITEMAP,
    encoding="utf-8"
)

# =========================================================
# ROBOTS
# =========================================================

ROBOTS = f"""
User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

(DIST_DIR / "robots.txt").write_text(
    ROBOTS,
    encoding="utf-8"
)

# =========================================================
# EXPORT CONFIG
# =========================================================

with open(DIST_DIR / "site.json", "w") as f:

    json.dump(
        {
            "site_name": SITE_NAME,
            "domain": DOMAIN,
            "affiliate_url": AFFILIATE_URL,
            "pages": PAGES,
            "industries": INDUSTRIES
        },
        f,
        indent=2
    )

# =========================================================
# DONE
# =========================================================

print("=" * 60)
print("TELLENT AFFILIATE SEO SITE GENERATED")
print("=" * 60)
print(f"Core Pages: {len(PAGES)}")
print(f"Industry Pages: {len(INDUSTRIES)}")
print("Daily Blog Posts: 5")
print(f"Output Folder: {DIST_DIR}")
print("Ready For GitHub Pages Deployment")
print("=" * 60)
