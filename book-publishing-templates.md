# Book Publishing Templates & Book 3 Details

## Gemini Image Prompt (Book Cover Generation)

**PROTECTED — Use for ALL future books (Book 4+)**

```
Create a premium ebook cover, portrait 1600x2400 pixels, photorealism with a
subtle cinematic-digital finish (NOT cartoon, NOT illustration — a realistic,
high-quality rendered look).

COMPOSITION:
- Background: deep navy #0B2447 with a soft glowing gradient, plus a delicate
  grid-dot technology pattern and faint bokeh light particles for depth.
- A graceful, glowing ECG/heartbeat line in teal #4FD1C5 and sky blue #38BDF8
  sweeps across the lower half in a smooth pulse.
- A small, elegant medical-cross merged with a circuit node sits in the
  top-right corner as a subtle brand mark.

PERSON (realistic photo):
- Use the person from the uploaded reference photo — realistic, professional,
  approachable, wearing a smart blazer/shirt, confident warm smile, natural
  skin texture, soft studio lighting. Place them on the RIGHT side of the
  lower third, slightly overlapping into the cover, so they look like a real
  author portrait.

TEXT (single-line, spelled EXACTLY — do NOT wrap onto two lines):
- Top-center, one line only, small, letterspaced, teal:
  PRACTICAL AI IN HEALTHCARE
- Center, ONE single bold white line only, clearly readable:
  [BOOK TITLE - update per book]
- Below it, one line, medium, teal:
  [SUBTITLE - update per book]
- Bottom, one line, medium, white:
  MOHAMMED IMTHIYAZ A

DESIGN RULES:
- Leave clean, uncluttered dark space behind all text so it is fully readable.
- Balanced, symmetrical, attractive, high-end professional book cover.
- No other words, watermarks, or logos. Cold, trustworthy, "no hype" mood.
```

**To use for Book 4+:** Copy prompt above, replace `[BOOK TITLE]` and `[SUBTITLE]`, paste into Gemini. Download 1600x2400 image, then use `generate_covers.py` to resize into all required formats (KDP, Gumroad, thumbnail, Google Play).

---

## GUMROAD LISTING TEMPLATE

**Title:** [Book Title]
**URL:** [custom-slug]
**PDF File:** [upload PDF]
**Thumbnail:** Square image, at least 600x600px
**Cover Image:** Horizontal, at least 1280x720px, 72 DPI
**Summary:** [Book Title] — [Subtitle]. [1-2 sentence description]
**Add Details:** No. of pages: [X]
**Price:** $[X.XX]
**Button text:** Download Your eBook Now
**Custom message:**
```
Thank you for purchasing [Book Title]!

You now have the practical frameworks, checklists, and roadmaps to implement AI responsibly in your organization.

If you found this valuable, please leave a review! Connect with me for the rest of the 8-part book series:
🔗 YouTube: @HealthAI_Insights
🔗 LinkedIn: linkedin.com/in/mohammed-imthiyaz-a-63266446

Click below to download your PDF!
```
**Category:** Education & Science
**Tags:** AI, Healthcare, Hospital, Implementation, Leadership

---

## AMAZON KDP TEMPLATE

**Cover:** JPG format only
**Manuscript:** EPUB format
**ISBN:** [assigned ISBN]
**DRM:** No (do not apply Digital Rights Management — allow PDF/EPUB download)
**Author Biography:**
```
Mohammed Imthiyaz A is a healthcare AI specialist and author of the "Practical AI in Healthcare" series. With deep expertise in hospital data systems, AI implementation, and patient data privacy, he helps hospital leaders and analysts navigate the complex journey from AI pilot projects to full-scale production. His work bridges the gap between cutting-edge AI technology and real-world hospital operations.
```

---

## BOOK 3 — READY TO UPLOAD

### Gumroad Listing
- **Title:** Healthy AI Implementation Roadmap for Hospitals
- **URL:** Healthy_AI_Implementation_Roadmap_for_Hospitals
- **PDF File:** `book-03-healthy-ai-implementation-roadmap/book.pdf`
- **Summary:** Healthy AI Implementation Roadmap for Hospitals - From Pilot to Production -- A Step-by-Step Playbook for Hospital Leaders and Analysts
- **Pages:** 30
- **Price:** $4.99
- **Button text:** Download Your eBook Now
- **Custom message:** Thank you for purchasing AI in Healthcare: The Do's and Don'ts! You now have the practical frameworks, 50-point checklist, and 90-day roadmap to implement AI responsibly in your organization. If you found this valuable, please leave a review! Connect with me for the rest of the 8-part book series: 🔗 YouTube: @HealthAI_Insights 🔗 LinkedIn: linkedin.com/in/mohammed-imthiyaz-a-63266446 Click below to download your PDF!
- **Category:** Education & Science
- **Tags:** AI, Healthcare, Hospital, Implementation, Leadership

### Amazon KDP Listing
- **Cover:** `book-03-healthy-ai-implementation-roadmap/cover_kdp_full.jpg`
- **Manuscript:** `book-03-healthy-ai-implementation-roadmap/book.epub`
- **ISBN:** 9798193703846
- **DRM:** No
- **Author Biography:** Mohammed Imthiyaz A is a healthcare AI specialist and author of the "Practical AI in Healthcare" series. With deep expertise in hospital data systems, AI implementation, and patient data privacy, he helps hospital leaders and analysts navigate the complex journey from AI pilot projects to full-scale production. His work bridges the gap between cutting-edge AI technology and real-world hospital operations.

---

## NOTES FOR FUTURE BOOKS

When generating Book 4+, provide:
1. Book number and title
2. Subtitle
3. Number of pages
4. Gumroad price
5. ISBN (if assigned)
6. Generated files: book.epub, book.pdf, cover_kdp_full.jpg, cover_gumroad.jpg
7. Use the Gemini prompt template above with updated title/subtitle
