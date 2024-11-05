import os
from dotenv import load_dotenv

load_dotenv()

# LLM
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_OPENAI_MODEL = os.getenv("DEFAULT_OPENAI_MODEL")

# News API
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

# Directory Paths
DATA_DIRECTORY = "app/data"
NEWSAPI_DIRECTORY = os.path.join(DATA_DIRECTORY, "news_api")

# NewsAPI File Paths
NEWSAPI_RAW_DATA_FILEPATH = os.path.join(NEWSAPI_DIRECTORY, "raw_data.json")
NEWSAPI_FILTERED_DATA_FILEPATH = os.path.join(NEWSAPI_DIRECTORY, "filtered_data.json")
NEWSAPI_GENERATED_DATA_FILEPATH = os.path.join(NEWSAPI_DIRECTORY, "generated_data.json")
