"""
Technical analysis tools.

This module provides tools for technical analysis of stocks, including
price chart analysis, pattern recognition, and technical indicators.
"""

import random
from typing import Any

from strands import tool
from strands.types.tools import ToolResult, ToolUse
from tools.data_generators import generate_mock_technical_data

# Tool specs
TOOL_SPEC_GET_PRICE_HISTORY = {
    "name": "get_price_history",
    "description": "Retrieve historical price data and basic technical indicators.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "TSLA" for Tesla)',
                },
            },
            "required": ["ticker"],
        },
    },
}

TOOL_SPEC_IDENTIFY_PATTERNS = {
    "name": "identify_patterns",
    "description": "Identify chart patterns and technical signals.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "NVDA" for NVIDIA)',
                },
            },
            "required": ["ticker"],
        },
    },
}


# Tool implementations
def get_price_history(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Retrieve historical price data and basic technical indicators.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with technical analysis data

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]

    data = generate_mock_technical_data(ticker)

    analysis = f"""
    Technical Analysis for {ticker}:

    Price Action:
    - Current Price: ${data["current_price"]:.2f}
    - 50-day SMA: ${data["sma_50"]:.2f}
    - 200-day SMA: ${data["sma_200"]:.2f}
    - Overall Trend: {data["trend"].title()}

    Key Levels:
    - Support: ${data["support_level"]:.2f}
    - Resistance: ${data["resistance_level"]:.2f}

    Volume Analysis:
    - Volume Trend: {data["volume_trend"].title()}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


def identify_patterns(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Identify chart patterns and technical signals.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with pattern analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]

    data = generate_mock_technical_data(ticker)

    # Generate mock pattern analysis
    patterns = [
        "ascending triangle",
        "head and shoulders",
        "double bottom",
        "bull flag",
        "wedge",
        "channel breakout",
    ]
    detected_pattern = random.choice(patterns)

    analysis = f"""
    Pattern Analysis for {ticker}:

    Technical Indicators:
    - RSI: {data["rsi"]:.1f} ({"Overbought" if data["rsi"] > 70 else "Oversold" if data["rsi"] < 30 else "Neutral"})
    - MACD Signal: {data["macd_signal"].title()}
    - Bollinger Bands: Price at {data["bollinger_position"]} band

    Pattern Recognition:
    - Detected Pattern: {detected_pattern.title()}
    - Pattern Reliability: {random.choice(["High", "Medium", "Low"])}
    - Suggested Action: {random.choice(["Buy", "Sell", "Hold", "Wait for breakout"])}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


# Function-style tools for backward compatibility and direct testing
@tool
def get_price_history_func(ticker: str) -> str:
    """
    Retrieve historical price data and basic technical indicators.

    Use this tool to get price action information and key technical levels for a stock.
    The data includes moving averages, support/resistance levels, and trend information.

    Args:
        ticker: Stock ticker symbol (e.g., "TSLA" for Tesla)

    Returns:
        Formatted string with technical price analysis

    """
    data = generate_mock_technical_data(ticker)

    analysis = f"""
    Technical Analysis for {ticker}:

    Price Action:
    - Current Price: ${data["current_price"]:.2f}
    - 50-day SMA: ${data["sma_50"]:.2f}
    - 200-day SMA: ${data["sma_200"]:.2f}
    - Overall Trend: {data["trend"].title()}

    Key Levels:
    - Support: ${data["support_level"]:.2f}
    - Resistance: ${data["resistance_level"]:.2f}

    Volume Analysis:
    - Volume Trend: {data["volume_trend"].title()}
    """

    return analysis


@tool
def identify_patterns_func(ticker: str) -> str:
    """
    Identify chart patterns and technical signals.

    Use this tool to get technical indicator readings and pattern recognition analysis.
    This helps identify potential trading setups and entry/exit signals.

    Args:
        ticker: Stock ticker symbol (e.g., "NVDA" for NVIDIA)

    Returns:
        Formatted string with pattern analysis and technical indicators

    """
    data = generate_mock_technical_data(ticker)

    # Constants for indicator thresholds
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30

    # Generate mock pattern analysis
    patterns = [
        "ascending triangle",
        "head and shoulders",
        "double bottom",
        "bull flag",
        "wedge",
        "channel breakout",
    ]
    detected_pattern = random.choice(patterns)

    analysis = f"""
    Pattern Analysis for {ticker}:

    Technical Indicators:
    - RSI: {data["rsi"]:.1f} ({"Overbought" if data["rsi"] > RSI_OVERBOUGHT else "Oversold" if data["rsi"] < RSI_OVERSOLD else "Neutral"})
    - MACD Signal: {data["macd_signal"].title()}
    - Bollinger Bands: Price at {data["bollinger_position"]} band

    Pattern Recognition:
    - Detected Pattern: {detected_pattern.title()}
    - Pattern Reliability: {random.choice(["High", "Medium", "Low"])}
    - Suggested Action: {random.choice(["Buy", "Sell", "Hold", "Wait for breakout"])}
    """

    return analysis
