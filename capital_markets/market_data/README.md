# Market Data Agents

This folder contains implementations of market data retrieval agents using different model backends.

>Note: This is a demonstration project using **mock data generators**. In a production environment, these would be replaced with real data sources and APIs.

## Available Agents

### AWS Bedrock Agent (`agent_bedrock.py`)

This agent uses Claude models via AWS Bedrock to answer financial questions and retrieve market data.

#### Prerequisites

1. AWS account with Bedrock access
2. AWS credentials configured (one of the following):
   - AWS environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
   - AWS credentials file (`~/.aws/credentials`)
   - IAM role (when running on AWS)

#### Configuration

Edit `agent_bedrock.py` to configure:

```python
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",  # Change model if needed
    region_name="us-west-2",  # Change to your AWS region
    temperature=0.1,  # Change to desired temperature
    top_p=0.5,  # Change to desired top_p
    # max_tokens=2048,  # Change to desired max_tokens
)
```

For custom AWS session:

- Uncomment and configure the session parameters in the `boto3.Session()` section
- Uncomment the `boto_session=session` line in the `BedrockModel` configuration

#### Running the Agent

```bash
# From repository root with active venv
uv run market_data/agent_bedrock.py
```

### Ollama Agent (`agent_ollama.py`)

This agent uses locally hosted models via [Ollama](https://ollama.ai/) for market data retrieval.

#### Prerequisites for Ollama

1. [Ollama](https://ollama.ai/) installed and running on your machine
2. The specified model pulled (`qwen3:8b-q8_0`) or any reasoning model from Ollama

#### Configuration for Ollama

Edit `agent_ollama.py` to configure:

```python
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Change if Ollama is on a different host/port
    model_id="qwen3:8b-q8_0",       # Change to any model available in Ollama
    temperature=0.1,
    top_p=0.5,
    max_tokens=2048,
)
```

#### Running the Agent with Ollama models

```bash
# From repository root with active venv
python market_data/agent_ollama.py
```

## Customizing the Market Data Tool

Both agents use a simplified mock implementation of the `market_data` tool. In a production environment, modify this function to connect to real financial data APIs:

```python
@tool
def market_data(ticker: str) -> dict:
    """Retrieve current market data for a given ticker symbol."""
    # Replace this with a real API call
    # Example:
    # response = requests.get(f"https://api.financialdata.com/v1/stocks/{ticker}")
    # return response.json()

    return {"ticker": ticker, "price": 123.45, "volume": 1000000}
```

## Example Queries

Once the agent is running, you can ask questions like:

- "What's the current trading volume for AAPL?"
- "What's the current price of TSLA?"
- "Should I buy MSFT based on its current data?"
