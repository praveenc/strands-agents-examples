# Strands Agents Examples

Sample single and multi-agent impelementation using Strands Agents.

## Step 0: Install Prerequisites

### Requirements

- Python 3.12+
- Dependencies (automatically installed by uv):
  - `strands-agents[ollama]>=1.0.1`
  - `strands-agents-tools>=0.2.1`
  - `rich>=14.0.0`
  - AWS credentials (for Bedrock agent)
  - Ollama (for Ollama agent)

### Installation

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

## Next

See usage instructions in [capital_markets](capital_markets/#usage) folder.

## Note

All examples use mock data generators to simulate agent calls to tools and external services.