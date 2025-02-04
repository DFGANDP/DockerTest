import requests
import json
import os
import sys

OUTPUT_DIR = "/app/output"  # Katalog w kontenerze


def fetch_reviews(appid, num_requests=3, num_per_page=20):
    url = f"https://store.steampowered.com/appreviews/{appid}"
    cursor = '*'
    reviews = []

    for i in range(num_requests):
        params = {
            'json': 1,
            'num_per_page': num_per_page,
            'cursor': cursor
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            reviews.extend(data.get('reviews', []))
            cursor = data.get('cursor', None)

            print(f"Request {i + 1}: Retrieved {len(data.get('reviews', []))} reviews")
            if not cursor:
                print("No more reviews to fetch.")
                break
        else:
            print(f"Error: {response.status_code}")
            break

    # Tworzymy katalog, jeśli nie istnieje
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Zapisujemy recenzje do pliku w volume
    file_path = os.path.join(OUTPUT_DIR, f"reviews_{appid}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)
    
    print(f"Total reviews fetched: {len(reviews)} - saved to {file_path}")
    return reviews


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_reviews.py <appid>")
        sys.exit(1)

    appid = sys.argv[1]
    fetch_reviews(appid)
