# Trading Analysis System

A comprehensive multi-agent financial analysis system built with Strands Agents SDK.

## Overview

This trading analysis system employs a hierarchical multi-agent architecture to provide thorough stock analysis across different domains:

1. **Fundamental Analysis**: Financial statements, valuations, and business prospects
2. **Technical Analysis**: Price charts, patterns, and technical indicators
3. **Sentiment Analysis**: News, social media, and market sentiment
4. **Risk Assessment**: Risk metrics, volatility, and portfolio impact

These specialist agents are coordinated by a central Trading Advisor that synthesizes insights to deliver comprehensive investment recommendations.

## Architecture

```txt
                   ┌───────────────────┐
                   │  Trading Advisor  │
                   │    Coordinator    │
                   └─────────┬─────────┘
                             │
         ┌──────────────┬────┴────┬──────────────┐
         │              │         │              │
┌────────▼─────────┐   ┌▼───────┐ ┌▼────────┐   ┌▼──────────────┐
│    Fundamental   │   │Technical│ │Sentiment│   │     Risk      │
│     Analysis     │   │Analysis │ │Analysis │   │   Assessment  │
└──────────────────┘   └─────────┘ └─────────┘   └───────────────┘
```

## Project Structure

```shell
trading_analysis/
├── __init__.py          # Package initialization
├── agent.py             # Agent orchestration and API
├── README.md            # This documentation file
└── tools/               # Modular tool implementations
    ├── __init__.py      # Tools package
    ├── data_generators.py  # Mock data generation
    ├── fundamental.py   # Fundamental analysis tools
    ├── technical.py     # Technical analysis tools
    ├── sentiment.py     # Sentiment analysis tools
    └── risk.py          # Risk assessment tools
```

## Components

### Tool Modules

The system follows a modular approach with domain-specific tool modules:

- **data_generators.py**: Shared mock data generation functions
- **fundamental.py**: Tools for financial statement analysis and valuation metrics
- **technical.py**: Tools for price chart analysis and pattern recognition
- **sentiment.py**: Tools for news sentiment and social media analysis
- **risk.py**: Tools for risk assessment and portfolio impact analysis

Each tool module implements both module-based tools (using TOOL_SPEC) and function-style tools with decorators.

### agent.py

Implements the multi-agent orchestration:

- Command-line interface for running the analysis system:
    - Parses command-line arguments
    - Configures models
    - Processes single or batch stock analyses
    - Formats and displays results
- Creates specialist agents for each domain
- Configures the trading advisor agent
- Provides API for stock analysis
- Handles agent communication


## Usage

```bash
# Get help on command-line arguments
uv run trading_analysis/agent.py --help

usage: agent.py [-h] [--type {fundamental,technical,sentiment,risk,comprehensive}] [--region REGION] ticker

Trading Analysis System

positional arguments:
  ticker                Stock ticker symbol(s) to analyze (e.g., AAPL MSFT)

options:
  -h, --help            show this help message and exit
  --type {fundamental,technical,sentiment,risk,comprehensive}, -t {fundamental,technical,sentiment,risk,comprehensive}
                        Type of analysis to perform (default: comprehensive)
  --region REGION, -r REGION
                        AWS region for Bedrock (default: us-west-2)

```


```bash
# Navigate to the project root directory first
cd capital_markets  # or wherever the repository is cloned

# Run comprehensive analysis on a single stock
uv run trading_analysis/agent.py AAPL

# Specific analysis type for e.g. technical
uv run trading_analysis/agent.py AAPL --type technical

# Specific analysis type using shorthand for e.g. risk
uv run trading_analysis/agent.py AAPL --t risk

# Optionally specify AWS region to use Bedrock models on us-east-1
uv run trading_analysis/agent.py NVDA --region us-east-1

# Alternatively, you can run the script directly (when in the project directory)
cd trading_analysis
uv run agent.py AAPL
```

### Analysis Types

- `fundamental`: Focused on financial statements, valuation, and business prospects
- `technical`: Focused on price action, chart patterns, and trading indicators
- `sentiment`: Focused on news, social media, and market sentiment
- `risk`: Focused on risk metrics, volatility, and portfolio impact
- `comprehensive`: Full analysis covering all domains (default)

## Tool Implementation

The tools follow the Strands module-based pattern:

```python
# 1. Tool Specification
TOOL_SPEC = {
    "name": "tool_name",
    "description": "Tool description",
    "inputSchema": { ... }
}

# 2. Tool Implementation
def tool_name(tool: ToolUse, **kwargs: Any) -> ToolResult:
    tool_use_id = tool["toolUseId"]
    # Extract parameters
    param = tool["input"].get("param_name", default_value)

    # Tool implementation
    result = ...

    # Return standardized response
    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": result}]
    }
```

Additionally, function-style tools are provided for backward compatibility and direct testing.

## Customization

### Adding Real Data Sources

To replace the mock data with real financial data, modify the data generator functions in `tools/data_generators.py`:

```python
def generate_mock_financials(ticker: str) -> dict:
    """Generate real financial data for a company."""
    # Replace with actual API call, e.g.:
    # response = requests.get(f"https://api.example.com/v1/financials/{ticker}")
    # return response.json()
    ...
```

### Adding New Analysis Types

To add a new type of analysis:

1. Create a new tool module in the tools directory
2. Implement TOOL_SPEC and tool functions
3. Update agents.py to create a specialist agent
4. Add the specialist agent to the trading advisor's tools
5. Update the query templates in `analyze_stock()`

## Performance Notes

- The system uses AWS Bedrock (Claude) by default for high-quality responses
- For batch processing of many stocks, consider implementing async handling
