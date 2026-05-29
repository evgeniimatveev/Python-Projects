# ♒ Zodiac & Numerology Analyzer

> Name + birthdate → full astrology report with PDF export

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/♒-zodiac-sign-finder/zodiac_sign.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## Report includes

| Field | Example |
|-------|---------|
| Zodiac Sign | Pisces |
| Life-Path Number | 1 (numerology) |
| Lucky Element | Water |
| Lucky Color | Sea Green 🌊 |
| Lucky Numbers | 3 personalised numbers |
| Mystical Message | Random inspirational quote |

## Two ways to use

**Notebook demo** — run the "Pure Python Demo" cell, no GUI needed:
```python
print(build_report("Evgenii", 15, 3, 1990))
```

**Full GUI** — run the last cell, enter your details, click Generate, optionally Save as PDF.

## Quick Start

```bash
git checkout ♒-zodiac-sign-finder
pip install reportlab   # optional, for PDF export only
jupyter notebook zodiac_sign.ipynb
```

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)