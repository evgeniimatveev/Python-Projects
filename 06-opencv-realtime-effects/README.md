# 🔍 OpenCV Real-time Webcam Effects

> 9 live webcam filter modes, switchable with keyboard, FPS overlay

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/🔍-opencv-realtime/opencv_realtime.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## Controls

| Key | Effect |
|-----|--------|
| `1` | Cartoon (`cv2.stylization`) |
| `2` | Pencil Sketch B&W |
| `3` | Pencil Sketch Color |
| `4` | Detail Enhancement |
| `5` | Edge Preserving Filter |
| `6` | Gaussian Blur |
| `7` | Canny Edge Detection |
| `8` | Heatmap (COLORMAP_JET) |
| `9` | Ocean (COLORMAP_OCEAN) |
| `q` / `Esc` | Quit |

A HUD overlay shows the active effect name and live FPS counter.

## Quick Start

```bash
git checkout 🔍-opencv-realtime
pip install opencv-contrib-python
jupyter notebook opencv_realtime.ipynb
```

> Requires a webcam.

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)