# 🖼️ Image Processing App

> 9 OpenCV visual effects with tkinter GUI — load, apply, save

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/🖼️-image-processing/image_processing.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## Effects

| Effect | OpenCV method |
|--------|--------------|
| Grayscale | `cv2.cvtColor` |
| Cartoon | `cv2.stylization` |
| Pencil Sketch | `cv2.pencilSketch` |
| Blur | `cv2.GaussianBlur` |
| Edge Detection | `cv2.Canny` |
| Oil Painting | `cv2.xphoto.oilPainting` |
| Sepia | custom matrix transform |
| Inverted Colors | `cv2.bitwise_not` |
| Emboss | custom kernel `cv2.filter2D` |

## Two ways to run

**1. Notebook demo** (no GUI) — run the matplotlib comparison cell, set `IMAGE_PATH` to any local image.

**2. Full GUI** — run the last cell, a tkinter window opens: Upload → Select Effect → Apply → Save.

## Quick Start

```bash
git checkout 🖼️-image-processing
pip install opencv-contrib-python pillow
jupyter notebook image_processing.ipynb
```

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)