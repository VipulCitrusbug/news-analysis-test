from fastapi import APIRouter, status
from app.core.custom_response import CustomResponse
from app.services.llm.openai import generate_news_analysis
from app.services.news_api import get_article_list_from_news_api
from app.utility.text_processing import newsapi_process_data, newsapi_save_filtered_data

router = APIRouter()


@router.get("/news/analyze/")
async def analyze_news(keywords: str):
    """
    ## API endpoint for fetching news and show the analysis.

    Parameters:
    - keywords: Keywords to search for news. (use comma (,) to separate multiple keywords)
    """

    if "," in keywords:
        keywords_list = keywords.split(",")  # Split by comma for multiple keywords
    else:
        keywords_list = keywords.split(" ")  # Split by space for single keyword

    try:
        news_list = get_article_list_from_news_api(keywords=keywords_list, maxItems=1)

        if not news_list:
            return CustomResponse(
                status_code=status.HTTP_404_NOT_FOUND, message="No news found."
            ).response()

        processed_data = newsapi_process_data(news_list)
        newsapi_save_filtered_data(processed_data)

        if processed_data:
            result = generate_news_analysis(
                news_title=processed_data[0]["title"],
                news_content=processed_data[0]["content"],
                news_datetime=processed_data[0]["date"],
            )
            return CustomResponse(
                status_code=status.HTTP_200_OK, data=result, message="Success"
            ).response()

    except Exception as e:
        return CustomResponse(
            status_code=status.HTTP_400_BAD_REQUEST, message="Error: " + str(e)
        ).response()
