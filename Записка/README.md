# TeX-проєкт докторської

Основний файл:

```bash
Записка/main.tex
```

Рекомендований рушій компіляції: `xelatex`, оскільки дисертація пишеться українською мовою і використовує Unicode-шрифти.

Базова збірка:

```bash
cd Записка
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

Структура:

- `sections/` -- розділи дисертації;
- `figures/` -- рисунки;
- `bib/references.bib` -- бібліографія;
- `main.tex` -- головний файл.
