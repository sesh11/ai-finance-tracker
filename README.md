# AI-Powered Personal Finance Tracker

An intelligent personal finance management system that automatically categorizes financial transactions using AI and provides conversational budget tracking capabilities.

## Features

- **Smart Transaction Import**: Process CSV, Excel, and PDF statements from multiple financial institutions
- **AI-Powered Categorization**: Intelligent transaction categorization using Claude AI
- **Duplicate Detection**: Automatic identification and prevention of duplicate entries  
- **Custom Budget Management**: User-defined budget categories with spending tracking
- **Conversational Interface**: Natural language queries about spending patterns
- **Multi-Account Support**: Handle checking, savings, and credit card accounts
- **Time-based Analytics**: Track spending weekly, monthly, quarterly, and yearly

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the application**:
   ```bash
   python -m src.cli.main
   ```

## Project Structure

```
finance-tracker/
├── src/
│   ├── data_ingestion/     # Statement parsers for different banks
│   ├── categorization/     # AI categorization service
│   ├── storage/           # Database models and operations
│   ├── budgets/           # Budget management logic
│   ├── agents/            # Conversational AI agent
│   └── cli/               # Terminal interface
├── data/                  # Local statement files (gitignored)
├── tests/                 # Test suites
├── docs/                  # Documentation
└── deploy/                # Cloud deployment configs
```

## Supported Banks

- Chase Bank (CSV/PDF)
- Bank of America (CSV/Excel)
- American Express (CSV/PDF)

## Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Privacy & Security

- Personal information is stripped before AI processing
- Only transaction descriptions and amounts are sent to Claude API
- Local encryption for sensitive data storage
- Secure credential management for API keys

## License

MIT License - see LICENSE file for details