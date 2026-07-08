# IJC LaTeX Package

This folder contains the International Journal of Computing template version of
the Hybrid PQ-OPAQUE manuscript.

## Main Files

- `main_ijc.tex` - manuscript source in the IJC template.
- `main_ijc.pdf` - compiled submission PDF.
- `ieeeijc.cls`, `IEEEtran.cls`, `IEEEtran.bst` - local template files.
- `img/` - manuscript figures.

## Build

Run three LaTeX passes from this folder:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main_ijc.tex
pdflatex -interaction=nonstopmode -halt-on-error main_ijc.tex
pdflatex -interaction=nonstopmode -halt-on-error main_ijc.tex
```

No BibTeX step is required because the bibliography is embedded in
`main_ijc.tex`.

The template uses Times-compatible, Helvetica-compatible, and Courier-compatible
PSNFSS fonts. A full TeX Live installation already includes them. On a minimal
TeX Live Basic setup, install the recommended font packages first:

```sh
tlmgr --usermode install helvetic courier
```

## Editorial Placeholders

The issue, DOI suffix, and publication date are intentionally left as
editorial placeholders:

- `VOLUME XX(X), 2026`
- `10.47839/ijc.XX.X.XX`
- `Date of publication to be assigned`
