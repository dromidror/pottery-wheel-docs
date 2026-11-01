# Pottery Wheel — User Guide (docs)

The end-user guide for the **Pottery Wheel** apps (Android and macOS), built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages.

One guide covers **both platforms**; where the apps differ, the page shows an
Android/macOS note or tabbed steps.

## Contents
Task-oriented chapters plus a **Cookbook** of start-to-finish recipes, illustrated with
screenshots and short animations.

## Build locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # live preview at http://127.0.0.1:8000
mkdocs build --strict
```

## Publish
Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site and
deploys it to GitHub Pages. (Enable Pages → "GitHub Actions" in the repo settings once.)

## Authoring conventions
- **Platform differences**: use tabbed content
  ```
  === "Android"
      Tap **Add**.
  === "macOS"
      Click **Add**.
  ```
  or an inline badge: `<span class="badge android">Android</span>`.
- **Callouts**: `!!! tip`, `!!! note`, `!!! warning`.
- **Figures** (screenshots / GIFs): put files in `docs/assets/` and use
  ```
  <figure markdown>
    ![Alt text](../assets/example.png){ width="600" }
    <figcaption>What the reader is looking at.</figcaption>
  </figure>
  ```
- **Diagrams**: fenced ` ```mermaid ` blocks (flowcharts, sequences).
- Keep UI labels **exactly** as they appear in the app.

## Assets
- `docs/assets/screenshots/` — still images (PNG).
- `docs/assets/animations/` — short GIF/MP4 clips (keep clips < ~5 MB).
- `docs/assets/diagrams/` — exported diagrams (or inline mermaid).

### Placeholder assets
Every referenced screenshot/animation currently ships as a labeled **placeholder** so the
site builds with `--strict`. Regenerate any missing ones with:

```bash
python3 tools/gen_placeholders.py
```

The script never overwrites an existing file, so dropping a real screenshot in place is
all it takes to replace a placeholder.
