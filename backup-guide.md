# Backup & Versioning Guide (GitHub)

> **Repo (NEW):** `https://github.com/cybersecurityocean/practical-ai-healthcare`
> **Old repo:** `cyber-news-bot` → retired/demolished. Your book content lives ONLY in the new repo.
> **Email policy:** account signups use your **publishing email**. `imthiyazzilaan@gmail.com` = public contact only.

---

## Plan — 3-2-1 backup for your book files

| Copy | Location | Purpose |
|---|---|---|
| 1 | **GitHub private repo** (this repo) | Version history, access from any device |
| 2 | **Google Drive / OneDrive** folder | Second storage, access offline |
| 3 | **Your laptop** (local folder) | Working copy |

Rule: never have only one copy. When you finish any edit, push to GitHub + upload to Drive.

---

## Option A — You keep everything local first, then connect to GitHub

Run these in your terminal **inside the folder where your book files live** (e.g., `book-01-ai-in-healthcare-dos-and-donts`):

```bash
git init
git add .
git commit -m "Manuscript + all assets"
git branch -M main
git remote add origin https://github.com/cybersecurityocean/practical-ai-healthcare.git
git push -u origin main
```

GitHub will ask for a username + **Personal Access Token** (not your password):
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → scope: `repo` (full) → Generate
3. Copy the token and paste it as the password on push. Save the token in a password manager.

---

## Option B — Only the `ebooks` folder is published to this repo

If your laptop folder contains other projects you don't want in the new repo:

1. Create the new repo as **Private** on GitHub: `cybersecurityocean/practical-ai-healthcare`
2. Copy ONLY your `ebooks` folder into a clean folder, then run Option A's commands there.

> ⚠️ Do NOT push your portfolio's `.env.local`, `node_modules`, or any secrets. Keep repo private.

---

## Everyday workflow (after first push)

```bash
git add .
git commit -m "Describe change"
git push
```

---

## Retiring the old cyber-news-bot repo

To remove old content:
1. GitHub → repo `cyber-news-bot` → Settings → Danger Zone → **Delete this repository**
2. Confirm with the repo name.
3. (If you want the old code kept offline, download it to a ZIP/Drive first. Then delete.)

---

## Recovery (if you ever lose your laptop)

1. Go to `github.com/cybersecurityocean/practical-ai-healthcare`
2. Code → Download ZIP, or clone: `git clone https://github.com/cybersecurityocean/practical-ai-healthcare.git`
3. Done — you have your latest manuscript + assets back.

---

## Checklist when editing

- [ ] Edit files locally
- [ ] `git add .` && `git commit` && `git push`
- [ ] Upload finished PDF/EPUB/cover to Google Drive
- [ ] Keep original videos (YouTube backups) in Drive too