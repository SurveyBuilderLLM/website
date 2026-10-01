# Aayvu website

The static marketing site served at https://aayvu.io.

## Local development

The supported setup starts from the workspace repository:

```bash
python scripts/aayvu.py bootstrap
python scripts/aayvu.py dev
```

To preview only this repository:

```bash
python -m http.server 3001
```

Open `http://localhost:3001`. Shared navigation and generated feature and use
case pages are maintained by `build.py`; run it after changing their source
content.

Production deploys through Zoho Catalyst Slate. Architecture, domains, and
deployment procedures are maintained at https://docs.aayvu.io.
