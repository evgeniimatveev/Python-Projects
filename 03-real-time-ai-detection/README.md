# ✨ Real-Time AI Detection & Filters

> YOLOv5 object detection + MediaPipe hands & pose + 9 live webcam filters

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/✨-real-time-ai-detection/real_time_ai_detection.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## What it does

Three AI systems running simultaneously on the webcam feed:

| System | What it detects |
|--------|----------------|
| **YOLOv5s** (Ultralytics) | Objects with bounding boxes & confidence labels |
| **MediaPipe Hands** | 21 landmarks per hand |
| **MediaPipe Pose** | 33 full-body pose landmarks |

## Filter modes (keys 1–9)

`1` Grayscale · `2` Edge Detection · `3` Blur · `4` Inverted · `5` Heatmap · `6` Thermal · `7` Ocean · `8` Cartoon · `9` Detail Enhancement

## Extra toggles

| Key | Effect |
|-----|--------|
| `b` | AI glow overlay |
| `v` | Particle system (follows fingertip) |
| `c` | Split-screen (original + filtered) |
| `q` / `Esc` | Quit |

## Quick Start

```bash
git checkout ✨-real-time-ai-detection
pip install opencv-python torch torchvision mediapipe
jupyter notebook real_time_ai_detection.ipynb
```

> Requires a webcam and display environment.

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)