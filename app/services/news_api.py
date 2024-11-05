import os
import json
from typing import List

from eventregistry import EventRegistry, QueryArticlesIter, QueryItems

import app.core.constants as constants

er_client = EventRegistry(apiKey=constants.NEWSAPI_API_KEY)


def get_article_list_from_news_api(keywords: List[str] = list(), maxItems: int = 100):
    file_path = constants.NEWSAPI_RAW_DATA_FILEPATH

    # Check if file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_data = json.load(file)
            print("Returning existing data from file.")
            return existing_data

    q = QueryArticlesIter(
        keywords=QueryItems.OR(keywords),
        dataType=["news"],
    )

    article_list = list(q.execQuery(er_client, sortBy="date", maxItems=maxItems))

    # Save to JSON file
    with open(file_path, "w") as file:
        json.dump(article_list, file, indent=4)

    print("New data saved to file.")

    return article_list
