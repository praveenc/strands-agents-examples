"""
Risk assessment tools.

This module provides tools for risk assessment of stocks, including
market risk metrics, volatility analysis, and portfolio impact evaluation.
"""

import random
from typing import Any

from strands import tool
from strands.types.tools import ToolResult, ToolUse

from tools.data_generators import generate_mock_risk_data

# Constants
BETA_HIGH = 1.5
BETA_MEDIUM = 0.8

# Tool specs
TOOL_SPEC_CALCULATE_RISK_METRICS = {
    "name": "calculate_risk_metrics",
    "description": "Calculate comprehensive risk metrics for the security.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "JPM" for JP Morgan)',
                },
            },
            "required": ["ticker"],
        },
    },
}

TOOL_SPEC_PORTFOLIO_IMPACT_ANALYSIS = {
    "name": "portfolio_impact_analysis",
    "description": "Analyze the impact of adding this position to a diversified portfolio.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": 'Stock ticker symbol (e.g., "DIS" for Disney)',
                },
                "position_size": {
                    "type": "number",
                    "description": "Fractional allocation to this position",
                    "default": 0.05,
                },
            },
            "required": ["ticker"],
        },
    },
}


# Tool implementations
def calculate_risk_metrics(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Calculate comprehensive risk metrics for the security.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with risk assessment metrics

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]

    data = generate_mock_risk_data(ticker)

    analysis = f"""
    Risk Assessment for {ticker}:

    Market Risk:
    - Beta: {data["beta"]:.2f} ({"High" if data["beta"] > BETA_HIGH else "Medium" if data["beta"] > BETA_MEDIUM else "Low"} market risk)
    - Volatility: {data["volatility"] * 100:.1f}% (annualized)
    - 95% VaR: {data["var_95"] * 100:.1f}% (daily)

    Correlation & Liquidity:
    - S&P 500 Correlation: {data["correlation_spy"]:.2f}
    - Liquidity Score: {data["liquidity_score"]:.2f}/1.0

    Other Risk Factors:
    - Sector Risk: {data["sector_risk"].title()}
    - Regulatory Risk: {data["regulatory_risk"].title()}
    - ESG Score: {data["esg_score"]:.0f}/100
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


def portfolio_impact_analysis(tool: ToolUse, **kwargs: Any) -> ToolResult:
    """
    Analyze the impact of adding this position to a diversified portfolio.

    Args:
        tool: Tool use information
        **kwargs: Additional arguments

    Returns:
        Tool result with portfolio impact analysis

    """
    tool_use_id = tool["toolUseId"]
    ticker = tool["input"]["ticker"]
    position_size = tool["input"].get("position_size", 0.05)

    data = generate_mock_risk_data(ticker)

    # Mock portfolio impact calculations
    portfolio_beta_impact = data["beta"] * position_size
    diversification_benefit = random.uniform(0.7, 0.95)

    analysis = f"""
    Portfolio Impact Analysis for {ticker} (Position Size: {position_size * 100:.1f}%):

    Risk Contribution:
    - Beta Impact on Portfolio: +{portfolio_beta_impact:.3f}
    - Volatility Contribution: {data["volatility"] * position_size * 100:.2f}%
    - Diversification Benefit: {diversification_benefit:.1%}

    Recommendations:
    - Maximum Position Size: {min(0.10, 1 / data["beta"] * 0.05) * 100:.1f}%
    - Risk-Adjusted Position: {position_size * diversification_benefit * 100:.1f}%
    - Hedging Requirement: {"Yes" if data["beta"] > BETA_HIGH else "No"}
    """

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": analysis}],
    }


# Function-style tools for backward compatibility and direct testing
@tool
def calculate_risk_metrics_func(ticker: str) -> str:
    """
    Calculate comprehensive risk metrics for the security.

    Use this tool to assess various risk factors for a stock including market risk,
    volatility, correlation, and other risk indicators.

    Args:
        ticker: Stock ticker symbol (e.g., "JPM" for JP Morgan)

    Returns:
        Formatted string with risk assessment metrics

    """
    data = generate_mock_risk_data(ticker)

    analysis = f"""
    Risk Assessment for {ticker}:

    Market Risk:
    - Beta: {data["beta"]:.2f} ({"High" if data["beta"] > BETA_HIGH else "Medium" if data["beta"] > BETA_MEDIUM else "Low"} market risk)
    - Volatility: {data["volatility"] * 100:.1f}% (annualized)
    - 95% VaR: {data["var_95"] * 100:.1f}% (daily)

    Correlation & Liquidity:
    - S&P 500 Correlation: {data["correlation_spy"]:.2f}
    - Liquidity Score: {data["liquidity_score"]:.2f}/1.0

    Other Risk Factors:
    - Sector Risk: {data["sector_risk"].title()}
    - Regulatory Risk: {data["regulatory_risk"].title()}
    - ESG Score: {data["esg_score"]:.0f}/100
    """

    return analysis


@tool
def portfolio_impact_analysis_func(ticker: str, position_size: float = 0.05) -> str:
    """
    Analyze the impact of adding this position to a diversified portfolio.

    Use this tool to understand how adding a stock affects overall portfolio risk and
    to get recommendations on position sizing based on risk characteristics.

    Args:
        ticker: Stock ticker symbol (e.g., "DIS" for Disney)
        position_size: Fractional allocation to this position (default: 0.05 or 5%)

    Returns:
        Formatted string with portfolio impact analysis

    """
    data = generate_mock_risk_data(ticker)

    # Mock portfolio impact calculations
    portfolio_beta_impact = data["beta"] * position_size
    diversification_benefit = random.uniform(0.7, 0.95)

    analysis = f"""
    Portfolio Impact Analysis for {ticker} (Position Size: {position_size * 100:.1f}%):

    Risk Contribution:
    - Beta Impact on Portfolio: +{portfolio_beta_impact:.3f}
    - Volatility Contribution: {data["volatility"] * position_size * 100:.2f}%
    - Diversification Benefit: {diversification_benefit:.1%}

    Recommendations:
    - Maximum Position Size: {min(0.10, 1 / data["beta"] * 0.05) * 100:.1f}%
    - Risk-Adjusted Position: {position_size * diversification_benefit * 100:.1f}%
    - Hedging Requirement: {"Yes" if data["beta"] > BETA_HIGH else "No"}
    """

    return analysis
