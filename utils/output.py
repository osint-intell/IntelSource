"""Output formatting utilities."""
import json
from typing import Any, Dict
from colorama import Fore, Style, init

init(autoreset=True)


def print_header(text: str) -> None:
    """Print a colored section header."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{text:^60}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")


def print_success(text: str) -> None:
    """Print success message in green."""
    print(f"{Fore.GREEN}✓ {text}{Style.RESET_ALL}")


def print_error(text: str) -> None:
    """Print error message in red."""
    print(f"{Fore.RED}✗ {text}{Style.RESET_ALL}")


def print_warning(text: str) -> None:
    """Print warning message in yellow."""
    print(f"{Fore.YELLOW}⚠ {text}{Style.RESET_ALL}")


def print_info(text: str) -> None:
    """Print info message in blue."""
    print(f"{Fore.BLUE}ℹ {text}{Style.RESET_ALL}")


def format_json(data: Dict[str, Any], indent: int = 2) -> str:
    """Format data as JSON string."""
    return json.dumps(data, indent=indent, default=str)


def print_json(data: Dict[str, Any], indent: int = 2) -> None:
    """Print data as formatted JSON."""
    print(format_json(data, indent))


def print_table(headers: list, rows: list) -> None:
    """Print simple ASCII table."""
    if not rows:
        print_warning("No data to display")
        return
    
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print header
    header_line = " | ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers))
    print(f"{Fore.CYAN}{header_line}{Style.RESET_ALL}")
    print("-" * len(header_line))
    
    # Print rows
    for row in rows:
        row_line = " | ".join(f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row))
        print(row_line)
