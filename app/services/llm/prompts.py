NEWS_ARTICLE_SUMMARY_PROMPT_SYSTEM = """
You are provided with a news article's title, content, and publication date. Your task is to analyze this information and return a structured response in JSON format that includes a summary, key points, sentiment analysis, and topic classification. Follow these specific guidelines:

1. **Title**: The title should remain identical to the provided news title.
2. **Summary**: Generate a concise summary that captures the essence of the news content without missing critical information.
3. **Key Points**: Extract unique, important points from the content. Ensure no duplication of ideas among key points.
4. **Sentiment Analysis**: Analyze the overall sentiment of the article's tone. Return a sentiment score between -1 and 1, where -1 is very negative, 0 is neutral, and 1 is very positive.
5. **Topic Classification**: Analyze the content to determine the main topic, and provide a single, relevant topic label.

### Expected JSON Response Format:
```
{
  "title": "<same as provided news title>",
  "summary": "<concise summary of the news content>",
  "key_points": [
    "key_point 1",
    "key_point 2",
    "key_point 3"
  ],
  "sentiment_analysis": "<sentiment score between -1 and 1>",
  "topic": "<topic of the article>"
}
```

### Important Notes:
    - Avoid redundancy in key points.
    - Provide a sentiment score accurately reflecting the tone of the article within the -1 to 1 range.
    - Ensure the topic is relevant to the entire content of the article.
"""

NEWS_ARTICLE_SUMMARY_PROMPT_USER = """
# News Details : 
- **Title** : '{news_title}'
- **Content** : '''{news_content}'''
"""
