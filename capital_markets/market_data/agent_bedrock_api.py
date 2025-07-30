import argparse
import asyncio

import httpx
from loguru import logger
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from strands import Agent, tool
from strands.models import BedrockModel


API_BASE_URL = "https://api.financialdatasets.ai/prices/snapshot"
USER_AGENT = "Mozilla/0.1"


async def make_fd_api_request(ticker: str) -> dict:
    url = f"{API_BASE_URL}/?ticker={ticker}"
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            logger.error(f"Error making API request: {e}")
            return {}


# Define a market data retrieval tool
@tool
async def market_data(ticker: str) -> dict:
    """Retrieve current market data for a given ticker symbol from an API."""
    # Implementation to fetch real-time market data
    data = await make_fd_api_request(ticker)
    # logger.info(data)
    if not data:
        logger.error(f"Unable to fetch market data for ticker: {ticker}")
        return {}
    if not data.get("snapshot"):
        logger.error(f"No snapshot data found for ticker: {ticker}")
        return {}

    price = data["snapshot"]["price"]
    volume = data["snapshot"]["volume"]
    day_change = data["snapshot"]["day_change"]
    day_change_percent = data["snapshot"]["day_change_percent"]

    # Create a formatted string for display in the console
    rprint(f"\n[bold green]Fetched market data for {ticker}[/bold green] ✅")

    return {
        "ticker": ticker,
        "price": price,
        "volume": volume,
        "day_change": day_change,
        "day_change_percent": day_change_percent,
    }


# Create a Bedrock model with the custom session
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.1,
    top_p=0.5,
    max_tokens=1024,
)

agent = Agent(
    system_prompt="You are a financial analyst assistant specialized in market data analysis.",
    tools=[market_data],
    model=bedrock_model,
    callback_handler=None,  # This supresses the agent's thinking trace
)


async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Financial market data analyzer")
    parser.add_argument(
        "ticker",
        nargs="?",
        default="GOOGL",
        help="Ticker symbol to analyze (default: GOOGL)",
    )
    args = parser.parse_args()

    ticker = args.ticker.upper()
    result = agent(f"What's the current market data for {ticker}?")

    console = Console()

    # Create a panel for the analysis
    analysis_panel = Panel(
        result.message["content"][0]["text"],
        title=f"[bold cyan]Analysis for {ticker}[/bold cyan]",
        border_style="cyan",
        expand=False,
    )

    # Create a table for metrics
    metrics_table = Table(show_header=True, header_style="bold magenta")
    metrics_table.add_column("Agent Metrics", style="dim")
    metrics_table.add_column("Value")

    metrics_table.add_row(
        "Total tokens", str(result.metrics.accumulated_usage["totalTokens"]),
    )
    metrics_table.add_row(
        "Execution time", f"{sum(result.metrics.cycle_durations):.2f} seconds",
    )
    metrics_table.add_row("Tools used", ", ".join(result.metrics.tool_metrics.keys()))

    # Print the results
    console.print("\n")
    console.print(analysis_panel)
    console.print("\n")
    console.print(metrics_table)
    console.print("\n")


if __name__ == "__main__":
    asyncio.run(main())
