import json
import os

from openai import OpenAI

from app.core import constants
from app.services.llm.prompts import (
    NEWS_ARTICLE_SUMMARY_PROMPT_SYSTEM,
    NEWS_ARTICLE_SUMMARY_PROMPT_USER,
)

client = OpenAI(api_key=constants.OPENAI_API_KEY)


def get_formatted_output(result):
    """
    Parse and return the JSON response
    """

    result = result.replace("```", "").replace("\n", "").replace("json", "")
    result = json.loads(result)
    return result


def generate_news_analysis(news_title, news_content, news_datetime):
    try:
        system_prompt = NEWS_ARTICLE_SUMMARY_PROMPT_SYSTEM
        user_prompt = (
            NEWS_ARTICLE_SUMMARY_PROMPT_USER.replace("{news_title}", news_title)
            .replace("{news_content}", news_content)
            .replace("{news_date}", news_datetime)
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        completion = client.chat.completions.create(
            model=constants.DEFAULT_OPENAI_MODEL,
            messages=messages,
        )

        # Parse and return the JSON response
        result = completion.choices[0].message.content

        # Store Generated Response
        existing_data = list()
        output_path = constants.NEWSAPI_GENERATED_DATA_FILEPATH

        formatted_response = get_formatted_output(result=result)
        formatted_response["content"] = news_content
        formatted_response["published_date"] = news_datetime

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save to JSON file
        with open(output_path, "r") as f:
            existing_data_content = json.load(f)

            if existing_data_content:
                existing_data_content.append(formatted_response)
                existing_data = existing_data_content
            else:
                existing_data = [formatted_response]

        with open(output_path, "w") as f:
            json.dump(existing_data, f, indent=2)

        return formatted_response

    except Exception as e:
        print("An error occurred while processing the response:", e)
        raise e
