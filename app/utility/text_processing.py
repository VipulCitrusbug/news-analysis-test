import json
import re
import os
from html import unescape

import app.core.constants as constants


def clean_text(text):
    """Clean text by removing HTML tags, handling special characters, and basic cleaning."""
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Unescape HTML entities
    text = unescape(text)

    # Handle special characters
    text = text.encode("ascii", "ignore").decode("ascii")

    # Remove extra whitespace
    text = " ".join(text.split())

    # Remove special characters except basic punctuation
    text = re.sub(r"[^\w\s.,!?-]", "", text)

    return text.strip()


# Newsapi's utility functions
def newsapi_process_data(data):
    """Process and filter news data from the input list."""
    processed_data = []

    for item in data:
        # Extract required fields
        processed_item = {
            "title": clean_text(item.get("title", "")),
            "content": clean_text(item.get("body", "")),
            "source": clean_text(item.get("source", {}).get("title", "")),
            "author": (
                clean_text(item.get("authors", [{}])[0].get("name", ""))
                if item.get("authors")
                else ""
            ),
            "date": item.get("dateTimePub", ""),
        }

        print("Processed item:", processed_item)

        # Only append if all required fields have content
        if processed_item["title"] and processed_item["content"]:
            processed_data.append(processed_item)

    return processed_data


def newsapi_save_filtered_data(
    processed_data, output_path=constants.NEWSAPI_FILTERED_DATA_FILEPATH
):
    """Save the processed data to a JSON file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)
