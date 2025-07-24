"""
Mock data generators for financial analysis.

This module contains functions to generate mock data for different types of financial analysis.
In a production environment, these would be replaced with real API calls to financial data providers.
"""

import random


def generate_mock_financials(ticker: str) -> dict:
    """
    Generate mock financial data for a company.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary containing financial metrics

    """
    return {
        "ticker": ticker,
        "market_cap": random.uniform(50e9, 2e12),  # $50B to $2T
        "pe_ratio": random.uniform(10, 35),
        "revenue_growth": random.uniform(-0.1, 0.3),  # -10% to 30%
        "profit_margin": random.uniform(0.05, 0.25),  # 5% to 25%
        "debt_to_equity": random.uniform(0.1, 2.0),
        "roe": random.uniform(0.08, 0.25),  # 8% to 25%
        "current_ratio": random.uniform(1.0, 3.0),
        "earnings_surprise": random.choice(["beat", "miss", "inline"]),
        "analyst_rating": random.choice(
            ["Strong Buy", "Buy", "Hold", "Sell", "Strong Sell"],
        ),
    }


def generate_mock_technical_data(ticker: str) -> dict:
    """
    Generate mock technical analysis data.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary containing technical indicators and price data

    """
    current_price = random.uniform(50, 500)
    return {
        "ticker": ticker,
        "current_price": current_price,
        "sma_50": current_price * random.uniform(0.95, 1.05),
        "sma_200": current_price * random.uniform(0.90, 1.10),
        "rsi": random.uniform(20, 80),
        "macd_signal": random.choice(["bullish", "bearish", "neutral"]),
        "bollinger_position": random.choice(["upper", "middle", "lower"]),
        "volume_trend": random.choice(["increasing", "decreasing", "stable"]),
        "support_level": current_price * random.uniform(0.85, 0.95),
        "resistance_level": current_price * random.uniform(1.05, 1.15),
        "trend": random.choice(["bullish", "bearish", "sideways"]),
    }


def generate_mock_sentiment_data(ticker: str) -> dict:
    """
    Generate mock sentiment analysis data.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary containing sentiment metrics and trends

    """
    return {
        "ticker": ticker,
        "news_sentiment": random.uniform(-1, 1),  # -1 to 1 scale
        "social_sentiment": random.uniform(-1, 1),
        "analyst_sentiment": random.uniform(-1, 1),
        "overall_sentiment": random.uniform(-1, 1),
        "sentiment_trend": random.choice(["improving", "deteriorating", "stable"]),
        "key_themes": random.sample(
            [
                "earnings growth",
                "market expansion",
                "regulatory concerns",
                "innovation",
                "competition",
                "supply chain",
                "management changes",
            ],
            3,
        ),
        "news_volume": random.randint(10, 100),
    }


def generate_mock_risk_data(ticker: str) -> dict:
    """
    Generate mock risk assessment data.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary containing risk metrics

    """
    return {
        "ticker": ticker,
        "beta": random.uniform(0.5, 2.0),
        "volatility": random.uniform(0.15, 0.60),  # 15% to 60% annualized
        "var_95": random.uniform(-0.05, -0.15),  # -5% to -15% daily VaR
        "correlation_spy": random.uniform(0.3, 0.9),
        "liquidity_score": random.uniform(0.3, 1.0),  # 0.3 to 1.0
        "sector_risk": random.choice(["low", "medium", "high"]),
        "regulatory_risk": random.choice(["low", "medium", "high"]),
        "esg_score": random.uniform(30, 90),
    }
