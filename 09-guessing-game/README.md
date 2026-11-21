# ❓ Guess the Number

> 3 difficulty levels · AI-powered adaptive hints · ASCII victory art

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](guessing_game.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## Difficulty Levels

| Level | Range | Challenge |
|-------|-------|-----------|
| Easy | 1–10 | Warm up |
| Medium | 1–49 | Getting harder |
| Hard | 1–100 | Full challenge |

## AI Hint System

Hints scale dynamically based on how far off your guess is:

- Way off → directional hint (go higher/lower by N)
- Getting closer → narrows the range
- Very close → "within N numbers"
- Super close → "within 3 numbers!"

## Victory

Random ASCII cat art + victory message on win. Timer tracks how long you took.

## Quick Start

```bash
git clone https://github.com/evgeniimatveev/Python-Projects.git
cd Python-Projects/09-guessing-game
jupyter notebook guessing_game.ipynb
```

Standard library only. Run the last cell.

---

← [All projects](../README.md)