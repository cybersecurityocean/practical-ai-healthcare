# Platform Upload Guide

## Files Generated

| File | Purpose |
|------|---------|
| `book.epub` | EPUB manuscript for KDP and Google Play |
| `book_preview.html` | HTML version - open in browser and print to PDF for Gumroad |
| `cover_kdp_full.jpg` | KDP cover (1600x2560) |
| `cover_kdp_thumbnail.jpg` | KDP thumbnail (600x600) |
| `cover_gumroad.jpg` | Gumroad cover (1280x720) |
| `cover_google_play.jpg` | Google Play cover (1024x1600) |
| `metadata.json` | All metadata for all platforms |

---

## 1. Amazon KDP

**Go to:** kdp.amazon.com -> Create -> Kindle eBook

| Field | Value |
|-------|-------|
| Language | English |
| Book Title | Healthy AI Implementation Roadmap for Hospitals |
| Subtitle | From Pilot to Production -- A Step-by-Step Playbook for Hospital Leaders and Analysts |
| Author | Mohammed Imthiyaz A |
| Description | See metadata.json -> amazon.description |
| Keywords | Use the 7 keywords from metadata.json |
| Categories | Health Administration & Policy, Medical Technology |
| Manuscript | Upload book.epub |
| Cover | Upload cover_kdp_full.jpg |
| Pricing | $7.99 (70% royalty) |

**Paperback:**
- Click "Create Paperback"
- Print: Black & White, 6x9 inches
- Cover: Upload cover_kdp_full.jpg as Front, cover_back.jpg as Back
- Manuscript: Print book_preview.html to PDF, upload that

**DO NOT check:** DRM, Enable X-Ray, Kindle Matchbook

---

## 2. Gumroad

**Go to:** gumroad.com -> Products -> New Product

| Field | Value |
|-------|-------|
| Type | Ebook (Digital) |
| Name | Healthy AI Implementation Roadmap for Hospitals |
| Subtitle | From Pilot to Production -- A Step-by-Step Playbook |
| Description | See metadata.json -> gumroad.description |
| Cover Image | Upload cover_gumroad.jpg |
| Content | Upload book_preview.html (print to PDF first) |
| Price | $7.99 |
| Tags | See metadata.json -> gumroad.tags |

**DO NOT check:** Require shipping address, Generate license keys

---

## 3. Google Play Books

**Go to:** play.google.com/books/publish -> Create Book -> EPUB

| Field | Value |
|-------|-------|
| Manuscript | Upload book.epub |
| Title | Healthy AI Implementation Roadmap for Hospitals |
| Description | See metadata.json -> google_play.description |
| Author | Mohammed Imthiyaz A |
| Cover | Upload cover_google_play.jpg |
| Content Rating | No mature content |
| Pricing | $7.99 |
| Territory | Worldwide |

**DO NOT check:** Requires DRM, Disable PDF download

---

## Pricing Strategy

| Platform | Price | Notes |
|----------|-------|-------|
| KDP (Kindle) | $7.99 | 70% royalty = $5.59 per sale |
| KDP (Paperback) | $14.99 | Print cost ~$4, profit ~$6 |
| Gumroad | $7.99 | 95% royalty = $7.59 per sale |
| Google Play | $7.99 | 70% royalty = $5.59 per sale |

## Series Links

- Book 1: AI in Healthcare -- The Do's and Don'ts (free on Gumroad)
- Book 2: Stop AI From Leaking Patient Data ($4.99)
- Book 3: Healthy AI Implementation Roadmap for Hospitals ($7.99) -- THIS BOOK
