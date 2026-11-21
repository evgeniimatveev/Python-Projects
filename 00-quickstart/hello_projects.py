"""
Quick demo script for the Python-Projects repo.

It prints a small overview of the project folders and their short descriptions.
(fixed: projects used to live on separate git branches; they are now numbered folders)
"""

projects = [
    ("01-avocado-price-forecasting", "Avocado price forecasting with Prophet"),
    ("02-amazon-reviews-analysis", "Amazon reviews sentiment analysis (NLP)"),
    ("03-real-time-ai-detection", "Real-time AI detection and filters (YOLOv5, MediaPipe)"),
    ("04-movie-recommendation", "Movie recommendation by age"),
    ("05-image-processing-app", "Image processing app: 9 OpenCV effects and a GUI"),
    ("06-opencv-realtime-effects", "Real-time webcam effects with OpenCV"),
    ("07-tic-tac-toe", "Tic Tac Toe with an unbeatable minimax AI"),
    ("08-fortune-teller", "Fortune teller game"),
    ("09-guessing-game", "Number guessing game with hints"),
    ("10-zodiac-sign-finder", "Zodiac sign finder with numerology"),
]


def print_projects_table():
    print("\n🚀 Python Projects Hub – quick overview\n")
    print(f"{'Folder':<30} | Description")
    print("-" * 80)
    for folder, desc in projects:
        print(f"{folder:<30} | {desc}")
    print("\nTip: open a folder (for example `cd 01-avocado-price-forecasting`) and read its README.\n")


if __name__ == "__main__":
    print_projects_table()
