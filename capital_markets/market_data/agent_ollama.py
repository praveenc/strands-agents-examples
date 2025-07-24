import sys

import requests
from rich import print as rprint
from strands import Agent, tool
from strands.models.ollama import OllamaModel


@tool
def market_data(ticker: str) -> dict:
    """Retrieve current market data for a given ticker symbol."""
    # Implementation to fetch real-time market data
    return {"ticker": ticker, "price": 123.45, "volume": 1000000}


def check_ollama_availability(host: str = "http://localhost:11434") -> tuple[bool, str]:
    """
    Check if Ollama is running and accessible.

    Args:
        host: Ollama host URL

    Returns:
        Tuple of (is_available, error_message)

    """
    try:
        response = requests.get(f"{host}/api/tags", timeout=5)
        if response.status_code == 200:
            return True, ""
        return False, f"Ollama server responded with status {response.status_code}"  # noqa: TRY300
    except requests.exceptions.ConnectionError:
        return False, "Cannot connect to Ollama server. Is Ollama running?"
    except requests.exceptions.Timeout:
        return False, "Connection to Ollama server timed out"
    except Exception as e:
        return False, f"Unexpected error connecting to Ollama: {e}"


def check_model_availability(host: str, model_id: str) -> tuple[bool, str]:
    """
    Check if the specified model is available in Ollama.

    Args:
        host: Ollama host URL
        model_id: Model identifier to check

    Returns:
        Tuple of (is_available, error_message)

    """
    try:
        response = requests.get(f"{host}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            available_models = [model["name"] for model in models]
            if model_id in available_models:
                return True, ""
            return False, f"Model '{model_id}' not found. Available models: {', '.join(available_models) if available_models else 'None'}"
        return False, f"Cannot retrieve model list from Ollama (status {response.status_code})"  # noqa: TRY300
    except Exception as e:  # noqa: BLE001
        return False, f"Error checking model availability: {e}"


def create_ollama_agent() -> Agent | None:
    """
    Create an Ollama-based agent with proper error handling.

    Returns:
        Agent instance if successful, None if Ollama is not available

    """
    host = "http://localhost:11434"
    model_id = "qwen3:8b-q8_0"

    # Check if Ollama is running
    is_available, error_msg = check_ollama_availability(host)
    if not is_available:
        rprint(f"[red]❌ Ollama Error:[/red] {error_msg}")
        rprint("[yellow]💡 To fix this:[/yellow]")
        rprint("   1. Install Ollama from https://ollama.ai/")
        rprint("   2. Start Ollama: [cyan]ollama serve[/cyan]")
        rprint(f"   3. Pull the required model: [cyan]ollama pull {model_id}[/cyan]")
        return None

    # Check if the model is available
    model_available, model_error = check_model_availability(host, model_id)
    if not model_available:
        rprint(f"[red]❌ Model Error:[/red] {model_error}")
        rprint(f"[yellow]💡 To fix this:[/yellow] Run [cyan]ollama pull {model_id}[/cyan]")
        return None

    try:
        ollama_model = OllamaModel(
            host=host,
            model_id=model_id,
            temperature=0.1,
            top_p=0.5,
            max_tokens=2048,
        )

        agent = Agent(
            system_prompt="You are a financial analyst assistant specialized in market data analysis.",
            tools=[market_data],
            model=ollama_model,
            callback_handler=None,  # comment this line to get a full trace
        )

        rprint(f"[green]✅ Ollama agent initialized successfully with model {model_id}[/green]")
        return agent  # noqa: TRY300

    except Exception as e:  # noqa: BLE001
        rprint(f"[red]❌ Error creating Ollama agent:[/red] {e}")
        return None


# Initialize agent with error handling
agent = create_ollama_agent()


def main():
    """Main function with error handling for agent execution."""
    if agent is None:
        rprint("[red]❌ Cannot run analysis: Ollama agent failed to initialize[/red]")
        rprint("[yellow]Please fix the Ollama setup issues above and try again.[/yellow]")
        sys.exit(1)

    try:
        rprint("[blue]🔍 Running market data analysis...[/blue]")
        result = agent("What's the current trading volume for AAPL?")

        rprint("\n" + "=" * 50 + "\n")
        rprint(f"[green]Analysis for AAPL:[/green]\n {result.message['content'][0]['text']}")
        rprint(f"[cyan]Total tokens:[/cyan] {result.metrics.accumulated_usage['totalTokens']}")
        rprint(f"[cyan]Execution time:[/cyan] {sum(result.metrics.cycle_durations):.2f} seconds")
        rprint(f"[cyan]Tools used:[/cyan] {list(result.metrics.tool_metrics.keys())}")
        rprint("\n" + "=" * 50 + "\n")

    except requests.exceptions.ConnectionError:
        rprint("[red]❌ Connection Error:[/red] Lost connection to Ollama during analysis")
        rprint("[yellow]💡 Check if Ollama is still running:[/yellow] [cyan]ollama serve[/cyan]")
        sys.exit(1)
    except KeyError as e:
        rprint(f"[red]❌ Response Format Error:[/red] Unexpected response structure: {e}")
        rprint("[yellow]This might indicate a model compatibility issue.[/yellow]")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        rprint(f"[red]❌ Analysis Error:[/red] {e}")
        rprint("[yellow]An unexpected error occurred during analysis.[/yellow]")
        sys.exit(1)


if __name__ == "__main__":
    main()
