# FinAgent: AI-Powered Financial Analysis Framework

A example framework for financial analysis and trading decision support using Strands Agents, featuring both cloud (Amazon Bedrock) and local LLM (Ollama) integration options.

## Project Overview

This project demonstrates how to build sophisticated AI agents for capital markets applications using [Strands python SDK](https://github.com/strands-agents/sdk-python). It includes:

1. **Market Data Agents**: Multiple deployment options for retrieving market data:
   - AWS Bedrock (Claude models)
   - Local deployment (Ollama)

2. **Trading Analysis System**: A comprehensive multi-agent system with specialized agents for:
   - Fundamental analysis
   - Technical analysis
   - Sentiment analysis
   - Risk assessment
   - Trading coordination

## Requirements

- Python 3.12+
- Dependencies (automatically installed by uv):
  - `strands-agents[ollama]>=1.0.1`
  - `strands-agents-tools>=0.2.1`
  - `rich>=14.0.0`
  - AWS credentials (for Bedrock agent)
  - Ollama (for Ollama agent)

## Installation

```bash
# Clone the repository
git clone https://github.com/praveenc/strands-agents-examples.git
cd strands-agents-examples/capital_markets

# Activate a virtual environment
pip install uv
uv venv
source .venv/bin/activate

# Install dependencies
uv sync
```

## Usage

### Market Data Agent

The Market Data Agent provides access to financial data for any ticker symbol through different model backends.

```shell
# Run with AWS Bedrock (requires AWS credentials)
uv run market_data/agent_bedrock.py

# Run with local Ollama (requires Ollama running locally)
uv run market_data/agent_ollama.py
```

See [market_data/README.md](market_data/README.md) for detailed setup instructions.

### Trading Analysis System

The Trading Analysis System provides comprehensive financial analysis through a multi-agent architecture.

```shell
python trading_analysis/agent.py
```

#### Available Analysis Types

Refer to [agent.py](trading_analysis/agent.py) for full implementation details.

- `fundamental`: Valuation, growth prospects, and investment recommendations
- `technical`: Chart patterns, indicators, and entry/exit points
- `sentiment`: Market sentiment based on news and social media
- `risk`: Risk profile including market risk, volatility, and portfolio impact
- `comprehensive`: Complete analysis covering all aspects (default)

## Agent Architecture

### Market Data Agent

A flexible agent with model-specific implementations:

- `agent_bedrock.py`: Uses AWS Bedrock with Claude models
- `agent_ollama.py`: Uses locally hosted models via Ollama

### Trading Analysis System

A hierarchical multi-agent system with:

1. **Specialist Agents**:
   - Fundamental Analysis Agent
   - Technical Analysis Agent
   - Sentiment Analysis Agent
   - Risk Assessment Agent

2. **Coordinator Agent**:
   - Trading Advisor that synthesizes insights from specialist agents

Each specialist agent has access to specific tools relevant to their domain of expertise.

## Data Flow

1. User queries the Trading Advisor with a question about a stock
2. Trading Advisor delegates to specialist agents as needed
3. Specialist agents use their tools to gather relevant data
4. Trading Advisor synthesizes the information into a comprehensive answer
5. Final recommendation is returned to the user

## Note

This is a demonstration project using mock data generators. In a production environment, these would be replaced with real data sources and APIs.