# import boto3
from strands import Agent, tool
from strands.models import BedrockModel


# Define a market data retrieval tool
@tool
def market_data(ticker: str) -> dict:
    """Retrieve current market data for a given ticker symbol."""
    # Implementation to fetch real-time market data
    return {"ticker": ticker, "price": 123.45, "volume": 1000000}


# Create a custom boto3 session
# session = boto3.Session(
#     aws_access_key_id="your_access_key",
#     aws_secret_access_key="your_secret_key",
#     aws_session_token="your_session_token",  # If using temporary credentials
#     region_name="us-west-2",
#     profile_name="your-profile",  # Optional: Use a specific profile
# )

# Create a Bedrock model with the custom session
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.1,
    top_p=0.5,
    max_tokens=2048,
    # boto_session=session  # Optional: Use a custom boto3 session
)

agent = Agent(
    system_prompt="You are a financial analyst assistant specialized in market data analysis.",
    tools=[market_data],
    model=bedrock_model,
)


def main():
    result = agent("What's the current trading volume for AAPL?")
    print("\n" + "=" * 50 + "\n")
    print(f"Analysis for AAPL:\n {result.message["content"][0]["text"]}")
    print(f"Total tokens: {result.metrics.accumulated_usage["totalTokens"]}")
    print(f"Execution time: {sum(result.metrics.cycle_durations):.2f} seconds")
    print(f"Tools used: {list(result.metrics.tool_metrics.keys())}")
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
