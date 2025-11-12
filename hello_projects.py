"""
Quick demo script for the Python-Projects repo.

It prints a small overview of projects and their short descriptions.
"""

projects = [
    ("avocado-prices", "Avocado Prices Prediction with Prophet & visualization"),
    ("amazon-reviews-nlp", "Amazon reviews sentiment analysis (NLP)"),
    ("realtime-ai-filters", "Real-time AI detection & filters with OpenCV / YOLO"),
    ("fortune-teller", "Fun fortune teller game in Python"),
    ("guessing-game", "Classic number guessing game"),
    ("image-processing-app", "Real-time image processing with OpenCV"),
    ("zodiac-finder", "Zodiac sign finder by birth date"),
    ("tic-tac-toe-ai", "Tic Tac Toe with simple AI"),
    ("opencv-realtime", "Real-time image modifications with OpenCV"),
    ("movie-recommender", "Movie recommendation app using ML"),
]


def print_projects_table():
    print("\n🚀 Python Projects Hub – quick overview\n")
    print(f"{'Branch':<20} | Description")
    print("-" * 70)
    for branch, desc in projects:
        print(f"{branch:<20} | {desc}")
    print("\nTip: use `git checkout <branch>` to explore a specific project.\n")


if __name__ == "__main__":
    print_projects_table()
