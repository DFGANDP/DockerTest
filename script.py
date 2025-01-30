import json
import os
import steamreviews

def download_and_save_reviews(app_id: int, output_file: str) -> None:
    """
    Pobiera i zapisuje recenzje Steam dla danego App ID.

    Args:
        app_id (int): Steam App ID gry.
        output_file (str): Ścieżka do pliku JSON.
    """
    request_params = {
        "language": "all",
        "review_type": "all",
        "filter": "recent"
    }

    review_dict, query_count = steamreviews.download_reviews_for_app_id(
        app_id, chosen_request_params=request_params
    )

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(review_dict, file, indent=4, ensure_ascii=False)

    print(f"📥 Pobranie zakończone! Wykonano {query_count} zapytań. Plik zapisano w: {output_file}")

if __name__ == "__main__":
    APP_ID = int(os.getenv("APP_ID", "2477340"))  # Domyślnie ID gry 2477340
    OUTPUT_FILE = os.getenv("OUTPUT_FILE", f"/output/steam_reviews_{APP_ID}.json")

    download_and_save_reviews(APP_ID, OUTPUT_FILE)
