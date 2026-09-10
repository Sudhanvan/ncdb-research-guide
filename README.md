# NCDB Research Guide

Public educational guide for students and researchers. No patient-level data are included.

Published with GitHub Pages at https://sudhanvan.github.io/ncdb-research-guide/.

## Edit and publish

Edit the `.qmd` files in `website/` on GitHub using the pencil button, then
choose **Commit changes** to save to `main`. GitHub Actions automatically renders
and publishes the guide, usually within a few minutes. The public URL stays the same.
Check the repository's **Actions** tab for the **Publish guide** result. If rendering
fails, the previous successful website remains available; fix the reported error
and save again. Changes on another branch publish only after merging into `main`.

For optional local preview, install Quarto 1.9.38 or a compatible version and run:

```bash
python3 build_site.py
```

Review the rendered site and push the source changes to `main`. No local server is needed.
The `docs/` directory is a legacy local snapshot, no longer the publishing source.
Automatic publishing builds directly from `website/`; do not edit generated HTML in `docs/`.
The PDF download is an explicitly generated educational artifact; regenerate it
when lessons change, and place it at `website/downloads/NCDB_Research_Guide.pdf`.

## Scope

Official definitions must be checked against the relevant PUF release and linked
source documentation. The guide provides original explanations, not reproduced
NCDB manuals. Advanced chapters still require development and methodological review.
Keep real datasets, derived patient records, credentials and local analysis outputs
outside this public repository. This repository contains the website only; analysis
project workspaces should be maintained separately in approved storage.
