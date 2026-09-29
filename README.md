# InkSpire — Modern Editorial Magazine & High-Speed SEO Blog

An enterprise-grade, high-performance blogging platform built with **Python (FastAPI + Jinja2 SSR + Modern Tailwind UI + SQLite)**. Engineered for pure search engine indexation, editorial beauty, and stealth background security.

---

## ✨ Features

- **⚡ 100% Server-Side Rendered (SSR)**: Sub-30ms load times with zero client hydration lag for instant Googlebot indexation.
- **🗺️ Complete SEO Suite**:
  - Dynamic Google-compliant `sitemap.xml` & `robots.txt`
  - Automated Schema.org (`BlogPosting`, `BreadcrumbList`, `WebSite`) JSON-LD structured data
  - OpenGraph & Twitter Card social meta tags with automatic image fallbacks
  - Standard RSS 2.0 Syndication Feed (`/feed.xml`)
- **📖 Full Suite of Blogger Features**:
  - Hero featured article + Trending stories list
  - Interactive reader "Clap / Like" heart counter
  - Dynamic Table of Contents (TOC) with scroll spy
  - Reading progress indicator bar
  - One-click social sharing (WhatsApp, X, LinkedIn, Facebook, Copy Link)
  - Topic categories & search filter
  - Author bio & newsletter lead-magnet widget
  - Anti-spam reader discussion & comments
- **✍️ Writer Studio (CMS)**:
  - Live split Markdown editor
  - **Live Google SERP Simulator**: Pixel-accurate preview of search snippets
  - **Real-Time SEO Scorecard (0–100)**: Keyword density, title/description length analyzer
  - Media library with drag-and-drop image upload
- **🛡️ Silent Stealth Security**:
  - Rate limiting with SlowAPI (anti-brute-force login defense)
  - Active XSS sanitization & input boundary validation
  - Bcrypt salted password hashing (work factor 12)
  - Tamper-proof HttpOnly signed session cookies
  - Image sanitization (Pillow magic-byte inspection, EXIF stripping, UUID rename)
  - Defense headers: CSP, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/your-username/inkspire-blog.git
cd inkspire-blog
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment
```bash
# Copy example environment configuration
cp .env.example .env
```

### 4. Run the Application
```bash
python run.py
```

- **Public Blog**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Writer Studio (CMS)**: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
  - **Default User:** `admin`
  - **Default Password:** `InkSpire@2025Secure!` *(Can be changed in .env)*

---

## 🧪 Running Tests

To verify all security layers, database seeding, and SEO endpoints:

```bash
python tests/test_platform.py
```

---

## 📄 License
MIT License. Built for creators and digital publishers.
