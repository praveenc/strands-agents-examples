"""
Fundamental analysis tools.

This module provides tools for fundamental analysis of stocks, including
financial statements analysis, valuation metrics, and industry comparisons.
"""

import random
from typing import Any

from strands import tool
from strands.types.tools import ToolResult, ToolUse

from tools.data_generators import generate_mock_financials

# Tool specs
TOOL_SPEC_GET_COMPANY_FINANCIALS = {
    "name": "get_company_financials",
    "description": "Retrieve comprehensive financial data for a company including income statement, balance sheet, and cash flow metrics.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "AAPL" for Apple Inc.)',
                },
            },
            "required": ["ticker"],
        },
    },
}

TOOL_SPEC_CALCULATE_RATIOS = {
    "name": "calculate_ratios",
    "description": "Calculate and compare financial ratios against sector or market benchmarks.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "MSFT" for Microsoft)',
                },
                "comparison_type": {
                    "type": "string",
                    "description": 'The benchmark type to compare against (e.g., "sector", "market", "industry")',
                    "default": "sector",
                },
            },
            "required": ["ticker"],
        },
    },
}


# Tool implementations
def get_company_financials(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Retrieve comprehensive financial data for a company.

    Args:
        tool: Tool use information

    Returns:
        Tool result with formatted financial analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]

    data = generate_mock_financials(ticker)

    analysis = f"""
    Financial Analysis for {ticker}:

    Valuation Metrics:
    - Market Cap: ${data["market_cap"] / 1e9:.1f}B
    - P/E Ratio: {data["pe_ratio"]:.1f}
    - Current Analyst Rating: {data["analyst_rating"]}

    Growth & Profitability:
    - Revenue Growth: {data["revenue_growth"] * 100:+.1f}%
    - Profit Margin: {data["profit_margin"] * 100:.1f}%
    - ROE: {data["roe"] * 100:.1f}%

    Financial Health:
    - Debt-to-Equity: {data["debt_to_equity"]:.2f}
    - Current Ratio: {data["current_ratio"]:.2f}
    - Recent Earnings: {data["earnings_surprise"]}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


def calculate_ratios(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Calculate and compare financial ratios against sector or market benchmarks.

    Args:
        tool: Tool use information

    Returns:
        Tool result with ratio analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]
    comparison_type = tool["input"].get("comparison_type", "sector")

    data = generate_mock_financials(ticker)

    # Mock sector averages
    sector_pe = random.uniform(15, 25)
    sector_roe = random.uniform(0.10, 0.20)
    sector_margin = random.uniform(0.08, 0.18)

    analysis = f"""
    Ratio Analysis for {ticker} vs {comparison_type} average:

    Valuation Comparison:
    - P/E Ratio: {data["pe_ratio"]:.1f} (Sector: {sector_pe:.1f})
    - Relative Valuation: {"Premium" if data["pe_ratio"] > sector_pe else "Discount"}

    Profitability Comparison:
    - ROE: {data["roe"] * 100:.1f}% (Sector: {sector_roe * 100:.1f}%)
    - Profit Margin: {data["profit_margin"] * 100:.1f}% (Sector: {sector_margin * 100:.1f}%)

    Performance vs Peers: {"Outperforming" if data["roe"] > sector_roe else "Underperforming"}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


# Function-style tools for backward compatibility and direct testing
@tool
def get_company_financials_func(ticker: str) -> str:
    """
    Retrieve comprehensive financial data for a company including income statement,
    balance sheet, and cash flow metrics.

    Use this tool to get key financial metrics for fundamental analysis. The data includes
    valuation metrics, growth and profitability metrics, and financial health indicators.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL" for Apple Inc.)

    Returns:
        Formatted string with financial analysis for the company

    """  # noqa: D205
    data = generate_mock_financials(ticker)

    analysis = f"""
    Financial Analysis for {ticker}:

    Valuation Metrics:
    - Market Cap: ${data["market_cap"] / 1e9:.1f}B
    - P/E Ratio: {data["pe_ratio"]:.1f}
    - Current Analyst Rating: {data["analyst_rating"]}

    Growth & Profitability:
    - Revenue Growth: {data["revenue_growth"] * 100:+.1f}%
    - Profit Margin: {data["profit_margin"] * 100:.1f}%
    - ROE: {data["roe"] * 100:.1f}%

    Financial Health:
    - Debt-to-Equity: {data["debt_to_equity"]:.2f}
    - Current Ratio: {data["current_ratio"]:.2f}
    - Recent Earnings: {data["earnings_surprise"]}
    """

    return analysis


@tool
def calculate_ratios_func(ticker: str, comparison_type: str = "sector") -> str:
    """
    Calculate and compare financial ratios against sector or market benchmarks.

    Use this tool to compare a company's financial metrics against its sector or market
    averages to determine relative valuation and performance.

    Args:
        ticker: Stock ticker symbol (e.g., "MSFT" for Microsoft)
        comparison_type: The benchmark type to compare against (default: "sector")
                         Other options: "market", "industry"

    Returns:
        Formatted string with ratio analysis comparing the company to benchmarks

    """
    data = generate_mock_financials(ticker)

    # Mock sector averages
    sector_pe = random.uniform(15, 25)
    sector_roe = random.uniform(0.10, 0.20)
    sector_margin = random.uniform(0.08, 0.18)

    analysis = f"""
    Ratio Analysis for {ticker} vs {comparison_type} average:

    Valuation Comparison:
    - P/E Ratio: {data["pe_ratio"]:.1f} (Sector: {sector_pe:.1f})
    - Relative Valuation: {"Premium" if data["pe_ratio"] > sector_pe else "Discount"}

    Profitability Comparison:
    - ROE: {data["roe"] * 100:.1f}% (Sector: {sector_roe * 100:.1f}%)
    - Profit Margin: {data["profit_margin"] * 100:.1f}% (Sector: {sector_margin * 100:.1f}%)

    Performance vs Peers: {"Outperforming" if data["roe"] > sector_roe else "Underperforming"}
    """

    return analysis
