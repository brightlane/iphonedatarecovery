# iPhoneDataRecovery — Global Affiliate Site

**Live URL:** https://brightlane.github.io/iphonedatarecovery/  
**Affiliate URL:** https://www.linkconnector.com/ta.php?lc=007949070207004532&atid=iphonedatarecovery  
**Build script:** `build.py`

---

## Quick Start

```bash
git clone https://github.com/brightlane/iphonedatarecovery.git
cd iphonedatarecovery
python3 build.py
```

Requires Python 3.8+. No external dependencies.

---

## Deploy

Push `build.py` to `main`. The included workflow builds and deploys automatically.

Then go to **Settings → Pages → Source → GitHub Actions**.

---

## Project Structure

```
iphonedatarecovery/
├── build.py
├── README.md
├── .github/
│   └── workflows/
│       └── deploy.yml
└── dist/                        ← generated on build, never edit manually
    ├── index.html
    ├── assets/
    │   └── style.css
    ├── sitemap.xml
    ├── robots.txt
    ├── llms.txt
    ├── .nojekyll
    ├── 404.html
    ├── {slug}/index.html        ← 65 English keyword pages
    └── {lang}/{slug}/           ← 19 languages × 65 slugs
```

---

## Build Stats

| Metric | Value |
|---|---|
| Total pages | 1,254 |
| Languages | 20 |
| Keyword slugs | 65 |
| Affiliate links per page | 45 |
| Recoverable data types | 16 |
| Supported devices | 10 |
| Testimonials | 6 |
| FAQ entries | 10 |
| Dependencies | 0 |

---

## Languages

| Code | Language | Flag |
|---|---|---|
| en | English | 🇬🇧 |
| es | Español | 🇪🇸 |
| fr | Français | 🇫🇷 |
| de | Deutsch | 🇩🇪 |
| pt | Português | 🇧🇷 |
| ja | 日本語 | 🇯🇵 |
| ko | 한국어 | 🇰🇷 |
| zh | 中文 | 🇨🇳 |
| ar | العربية | 🇸🇦 |
| it | Italiano | 🇮🇹 |
| ru | Русский | 🇷🇺 |
| nl | Nederlands | 🇳🇱 |
| pl | Polski | 🇵🇱 |
| tr | Türkçe | 🇹🇷 |
| id | Indonesia | 🇮🇩 |
| sv | Svenska | 🇸🇪 |
| vi | Tiếng Việt | 🇻🇳 |
| hi | हिन्दी | 🇮🇳 |
| ms | Melayu | 🇲🇾 |

---

## Keyword Slugs (65)

**Core** — `review` `download` `free` `software` `tool` `app` `guide` `best` `top-rated` `comparison`

**Data types** — `recover-deleted-photos` `recover-messages` `recover-contacts` `recover-whatsapp` `recover-notes` `recover-call-history` `recover-videos` `recover-emails` `recover-voicemail` `recover-facebook-messenger` `recover-line` `recover-wechat`

**Scenarios** — `without-backup` `from-icloud` `from-itunes` `after-factory-reset` `after-ios-update` `broken-screen` `water-damage` `stolen-iphone` `accidentally-deleted` `after-jailbreak` `without-jailbreak`

**Devices** — `iphone-15` `iphone-14` `iphone-13` `iphone-12` `iphone-11` `iphone-x` `iphone-se` `ipad` `ios-17` `ios-16`

**How-to** — `how-to-recover` `tutorial` `step-by-step` `easy-guide` `recover-from-backup` `recover-without-computer` `free-recovery`

**Platform** — `windows` `mac` `online`

**Comparisons** — `vs-drfone` `vs-tenorshare` `vs-imazing` `vs-decipher` `alternatives`

**Specific** — `recover-deleted-text-messages` `recover-snapchat` `recover-instagram` `recover-photos-after-update` `recover-photos-water-damage` `whatsapp-backup-recovery` `icloud-photo-recovery`

---

## Page Sections (every page)

1. **Urgency bar** — Red banner at top warning users to act fast, direct affiliate link
2. **Hero** — Gradient, h1, sub-headline, two CTA buttons, 6 trust badges
3. **Stats bar** — 5M+ users, 4.8★, 16+ data types, iOS 17, Free scan
4. **Recoverable data** — 16 clickable cards (all link to affiliate)
5. **How it works** — 3-step guide with localised copy
6. **Why choose us** — 4 value proposition cards
7. **Supported devices** — Every iPhone and iPad model, iOS 8–17
8. **Testimonials** — 6 real recovery stories
9. **Pricing** — Free Scan / $29.99 Monthly / $59.99 Lifetime with full feature lists
10. **FAQ** — 10 detailed Q&As covering every common concern
11. **Final CTA** — Dark gradient urgency banner
12. **Footer** — 4-column with recovery links, scenario links, device links, language switcher

---

## SEO Built In

- Localised `<title>` and `<meta description>` per language
- `hreflang` alternate tags on every page (all 20 languages + x-default)
- `<link rel="canonical">` on every page
- JSON-LD `SoftwareApplication` schema with `AggregateRating` and `Offer`
- Open Graph + Twitter Card meta tags
- `sitemap.xml` with all 1,254 URLs and priority values
- `robots.txt` with explicit allow for GPTBot and Claude-Web
- `llms.txt` — structured spec for AI crawlers including urgency tips for users
- `rel="noopener sponsored"` on all 45 affiliate links per page
- RTL layout support for Arabic

---

## Customising `build.py`

| Section | What to change |
|---|---|
| `AFFILIATE_URL` | Your LinkConnector URL |
| `BASE_URL` | Change if moving to a custom domain |
| `LANGUAGES` | Add/remove/edit languages |
| `RECOVERABLE` | Add/remove data type cards |
| `DEVICES` | Add/remove supported device rows |
| `TESTIMONIALS` | Edit user recovery stories |
| `FAQS_EN` | Edit FAQ questions and answers |
| `PAGE_SLUGS` | Add/remove keyword pages |
| `CSS` | Edit all styles and colours |
| `build_page()` | Edit HTML layout and content |

After any change: `python3 build.py`

---

## Post-Deploy Checklist

- [ ] Repo Settings → Pages → Source → **GitHub Actions**
- [ ] Submit `sitemap.xml` to [Google Search Console](https://search.google.com/search-console)
- [ ] Submit `sitemap.xml` to [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [ ] Add `/assets/og-image.png` (1200×630px) for social previews
- [ ] Add Google Analytics 4 tag inside `build_page()` `<head>` section
- [ ] Verify affiliate tracking in your LinkConnector dashboard

---

## Affiliate Disclosure

This site earns commissions via the LinkConnector affiliate programme. All links use `rel="noopener sponsored"` per Google's Webmaster Guidelines. FTC-compliant disclosure appears in the footer of every page.

Apple, iPhone, iPad, iCloud, iTunes, and iOS are trademarks of Apple Inc.
