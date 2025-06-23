# AI-Powered Personal Finance Tracker

## Overview
An intelligent personal finance management system that automatically categorizes financial transactions using AI and provides conversational budget tracking capabilities. Built with Claude AI integration for smart categorization and natural language querying.

## Core Features
- **Smart Transaction Import**: Processes CSV, Excel, and PDF statements from multiple financial institutions
- **AI-Powered Categorization**: Uses Claude API to intelligently categorize transactions with privacy-first approach
- **Duplicate Detection**: Automatically identifies and prevents duplicate transaction entries
- **Custom Budget Management**: User-defined budget categories with spending tracking
- **Conversational Interface**: Terminal-based chat to query spending ("Am I over my restaurant budget this month?")
- **Multi-Account Support**: Handles checking, savings, and credit card accounts from Chase, Bank of America, and American Express
- **Time-based Analytics**: Track spending weekly, monthly, quarterly, and yearly

## Technical Architecture
- **Backend**: Python with FastAPI
- **Database**: SQLite (local) → PostgreSQL (cloud migration)
- **AI Integration**: Anthropic Claude API for categorization and queries
- **Cloud Target**: AWS deployment (Lambda, RDS, S3)
- **Interface**: CLI-based terminal interaction
- **Data Processing**: Pandas for statement parsing, custom parsers for different bank formats

## Privacy & Security
- Personal information stripped before AI processing
- Only transaction descriptions and amounts sent to Claude API
- Local encryption for sensitive data storage
- Secure credential management for API keys

## Development Approach
- Local development first, cloud migration later
- Incremental feature development using feature branches
- Claude Code for AI-assisted development
- GitHub for version control with branch-based workflow

## Project Structure
```
finance-tracker/
├── src/
│   ├── data_ingestion/     # Statement parsers
│   ├── categorization/     # AI categorization service
│   ├── storage/           # Database models and operations
│   ├── budgets/           # Budget management
│   ├── agents/            # Conversational AI agent
│   └── cli/               # Terminal interface
├── data/                  # Local statement files
├── tests/                 # Test suites
├── docs/                  # Documentation
└── deploy/                # Cloud deployment configs
```

## Goals
1. Build practical AI-driven finance tool
2. Learn Claude Code development workflow
3. Implement agentic AI system for financial insights
4. Create foundation for advanced financial analytics

## Development Commands
- Run application: `python -m src.cli.main`
- Run tests: `pytest`
- Format code: `black src/`
- Type check: `mypy src/`
- Lint: `flake8 src/`