import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def hello():
    """Welcome to the AI-Powered Personal Finance Tracker"""
    console.print("🤖 AI-Powered Personal Finance Tracker", style="bold green")
    console.print("Welcome to your intelligent finance management system!")

@app.command() 
def import_statements():
    """Import financial statements from CSV, Excel, or PDF files"""
    console.print("📄 Statement Import", style="bold blue")
    console.print("This feature will import and process your financial statements")

@app.command()
def categorize():
    """Use AI to categorize transactions"""
    console.print("🧠 AI Categorization", style="bold purple")
    console.print("This feature will use Claude AI to categorize your transactions")

@app.command()
def budget():
    """Manage budgets and spending tracking"""
    console.print("💰 Budget Management", style="bold yellow")
    console.print("This feature will help you manage budgets and track spending")

@app.command()
def chat():
    """Start conversational interface for finance queries"""
    console.print("💬 Finance Chat", style="bold cyan")
    console.print("Ask questions about your spending patterns and budget status")

if __name__ == "__main__":
    app()