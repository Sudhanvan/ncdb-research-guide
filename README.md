# NCDB Research Guide

Public educational guide for students and researchers. No patient-level data are included.

Published with GitHub Pages at https://sudhanvan.github.io/ncdb-research-guide/.

## Edit and publish

The editable Quarto content is in `website/`. The published static files are in `docs/`.
Install Quarto 1.9.38 or a compatible version, then run:

```bash
python3 build_site.py
```

Review the rendered site, commit the updated source and `docs/`, and push to `main`.
GitHub Pages publishes `docs/` from the `main` branch. No local server is needed.
The PDF download is an explicitly generated educational artifact; regenerate it
when lessons change, and place it at `website/downloads/NCDB_Research_Guide.pdf`.

## Scope

Official definitions must be checked against the relevant PUF release and linked
source documentation. The guide provides original explanations, not reproduced
NCDB manuals. Advanced chapters still require development and methodological review.
Keep real datasets, derived patient records, credentials and local analysis outputs
outside this public repository. This repository contains the website only; analysis
project workspaces should be maintained separately in approved storage.
