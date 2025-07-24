"""
Sentiment analysis tools.

This module provides tools for sentiment analysis of stocks, including
news sentiment analysis, social media trends, and market narrative analysis.
"""

import random
from typing import Any

from strands import tool
from strands.types.tools import ToolResult, ToolUse

from tools.data_generators import generate_mock_sentiment_data

# Tool specs
TOOL_SPEC_ANALYZE_NEWS_SENTIMENT = {
    "name": "analyze_news_sentiment",
    "description": "Analyze sentiment from recent news articles and press releases.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "AMZN" for Amazon)',
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days to look back for news",
                    "default": 7,
                },
            },
            "required": ["ticker"],
        },
    },
}

TOOL_SPEC_SOCIAL_MEDIA_TRENDS = {
    "name": "social_media_trends",
    "description": "Analyze social media mentions and sentiment trends.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "GME" for GameStop)',
                },
            },
            "required": ["ticker"],
        },
    },
}


# Tool implementations
def analyze_news_sentiment(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Analyze sentiment from recent news articles and press releases.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with news sentiment analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]
    days = tool["input"].get("days", 7)

    data = generate_mock_sentiment_data(ticker)

    analysis = f"""
    News Sentiment Analysis for {ticker} (Last {days} days):

    Sentiment Scores:
    - News Sentiment: {data["news_sentiment"]:.2f} (-1 to +1 scale)
    - Social Media: {data["social_sentiment"]:.2f}
    - Analyst Sentiment: {data["analyst_sentiment"]:.2f}
    - Overall Sentiment: {data["overall_sentiment"]:.2f}

    Sentiment Trend: {data["sentiment_trend"].title()}
    News Volume: {data["news_volume"]} articles

    Key Themes: {", ".join(data["key_themes"])}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


def social_media_trends(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Analyze social media mentions and sentiment trends.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with social media analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]

    data = generate_mock_sentiment_data(ticker)

    # Generate mock social media metrics
    mentions = random.randint(100, 5000)
    engagement = random.uniform(0.02, 0.15)

    analysis = f"""
    Social Media Analysis for {ticker}:

    Activity Metrics:
    - Total Mentions: {mentions}
    - Engagement Rate: {engagement * 100:.1f}%
    - Sentiment Trend: {data["sentiment_trend"].title()}

    Sentiment Breakdown:
    - Positive: {max(0, data["social_sentiment"] * 50 + 50):.0f}%
    - Negative: {max(0, -data["social_sentiment"] * 50 + 50):.0f}%
    - Neutral: {100 - abs(data["social_sentiment"] * 100):.0f}%

    Viral Topics: {", ".join(random.sample(data["key_themes"], 2))}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


# Function-style tools for backward compatibility and direct testing
@tool
def analyze_news_sentiment_func(ticker: str, days: int = 7) -> str:
    """
    Analyze sentiment from recent news articles and press releases.

    Use this tool to understand market perception based on recent news coverage.
    It provides sentiment scores, trends, and key themes from news coverage.

    Args:
        ticker: Stock ticker symbol (e.g., "AMZN" for Amazon)
        days: Number of days to look back for news (default: 7)

    Returns:
        Formatted string with news sentiment analysis

    """
    data = generate_mock_sentiment_data(ticker)

    analysis = f"""
    News Sentiment Analysis for {ticker} (Last {days} days):

    Sentiment Scores:
    - News Sentiment: {data["news_sentiment"]:.2f} (-1 to +1 scale)
    - Social Media: {data["social_sentiment"]:.2f}
    - Analyst Sentiment: {data["analyst_sentiment"]:.2f}
    - Overall Sentiment: {data["overall_sentiment"]:.2f}

    Sentiment Trend: {data["sentiment_trend"].title()}
    News Volume: {data["news_volume"]} articles

    Key Themes: {", ".join(data["key_themes"])}
    """

    return analysis


@tool
def social_media_trends_func(ticker: str) -> str:
    """
    Analyze social media mentions and sentiment trends.

    Use this tool to gauge retail investor sentiment and social media activity.
    It provides metrics on mentions, engagement, and sentiment breakdowns.

    Args:
        ticker: Stock ticker symbol (e.g., "GME" for GameStop)

    Returns:
        Formatted string with social media analysis

    """
    data = generate_mock_sentiment_data(ticker)

    # Generate mock social media metrics
    mentions = random.randint(100, 5000)
    engagement = random.uniform(0.02, 0.15)

    analysis = f"""
    Social Media Analysis for {ticker}:

    Activity Metrics:
    - Total Mentions: {mentions}
    - Engagement Rate: {engagement * 100:.1f}%
    - Sentiment Trend: {data["sentiment_trend"].title()}

    Sentiment Breakdown:
    - Positive: {max(0, data["social_sentiment"] * 50 + 50):.0f}%
    - Negative: {max(0, -data["social_sentiment"] * 50 + 50):.0f}%
    - Neutral: {100 - abs(data["social_sentiment"] * 100):.0f}%

    Viral Topics: {", ".join(random.sample(data["key_themes"], 2))}
    """

    return analysis
