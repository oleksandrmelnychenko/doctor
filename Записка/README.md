# TeX-проєкт докторської записки

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

Поточна логіка структури:

- `sections/chapter1_analysis.tex` -- аналіз проблеми приватного контекстного захисту;
- `sections/chapter2_general_idea.tex` -- концепція AURA Runtime-орієнтованої технології;
- `sections/chapter3_contextual_risk.tex` -- метод контекстної оцінки інформаційного ризику;
- `sections/chapter4_policy_decisions.tex` -- метод policy-aware safety-рішень;
- `sections/chapter5_crypto_foundation.tex` -- криптографічна основа приватного AURA Runtime;
- `sections/chapter6_supervision_relay.tex` -- серверно-сліпий канал нагляду;
- `sections/chapter7_information_technology.tex` -- інформаційна технологія та експериментальна перевірка;
- `figures/` -- рисунки;
- `bib/references.bib` -- бібліографія;
- `main.tex` -- головний файл.
