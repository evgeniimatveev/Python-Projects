# 🥑 Avocado Price Forecasting

> EDA + Prophet time-series forecast on US avocado prices 2015–2018

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/🥑-avocado-prices-prediction/avocado_price_forecasting.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## What you get

- Price distribution, conventional vs organic boxplot, year-over-year trend
- Top 10 most expensive US avocado markets
- National price trend 2015–2018
- **Prophet forecast** — 52 weeks ahead with 95% confidence interval
- Yearly seasonality component (when are avocados cheapest?)

## Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data loading and manipulation |
| `seaborn / matplotlib` | Static visualisations |
| `plotly` | Interactive charts |
| `prophet` (Meta) | Time-series forecasting |

## Dataset

`avocado.csv` — included in this branch. Hass Avocado Board data, 18K rows, 54 regions.

## Quick Start

```bash
git clone https://github.com/evgeniimatveev/Python-Projects.git
cd Python-Projects
git checkout 🥑-avocado-prices-prediction
pip install prophet plotly seaborn pandas matplotlib
jupyter notebook avocado_price_forecasting.ipynb
```

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)