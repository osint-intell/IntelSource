"""IntelSource - Unified OSINT Aggregator
Interactive multi-source reconnaissance tool for IP, domain, and email intelligence.
"""
import os
import json
import sys
from typing import Dict, Any
from pathlib import Path
from dotenv import load_dotenv

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

from collectors.whois_collector import WHOISCollector
from collectors.dns_collector import DNSCollector
from collectors.geoip_collector import GeoIPCollector
from collectors.email_validator import EmailValidator
from utils.validators import classify_target, is_valid_ip, is_valid_domain, is_valid_email
from utils.logger import setup_logger

# Load environment variables from .env
load_dotenv()

logger = setup_logger(__name__)
console = Console()


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


class IntelSource:
    """Main OSINT aggregator application."""
    
    def __init__(self):
        self.whois_collector = WHOISCollector()
        self.dns_collector = DNSCollector()
        self.geoip_collector = GeoIPCollector()
        self.email_validator = EmailValidator()
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from environment variables and config.json."""
        try:
            config_path = Path('config/config.json')
            if config_path.exists():
                with open(config_path, 'r') as f:
                    config = json.load(f)
            else:
                config = {}
            
            # Override with environment variables if present
            config['dns_timeout'] = int(os.getenv('DNS_TIMEOUT', 5))
            config['dns_retries'] = int(os.getenv('DNS_RETRIES', 2))
            config['whois_timeout'] = int(os.getenv('WHOIS_TIMEOUT', 10))
            
            return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return {}
    
    def run(self):
        """Start the interactive menu."""
        clear_screen()
        self.show_banner()
        
        while True:
            try:
                self.show_menu()
                choice = Prompt.ask("[bold cyan]➜[/bold cyan] Enter your choice", choices=["1", "2", "3", "4", "5", "6"])
                
                if choice == '1':
                    clear_screen()
                    self.menu_ip_lookup()
                elif choice == '2':
                    clear_screen()
                    self.menu_domain_lookup()
                elif choice == '3':
                    clear_screen()
                    self.menu_email_validation()
                elif choice == '4':
                    clear_screen()
                    self.menu_full_reconnaissance()
                elif choice == '5':
                    clear_screen()
                    self.menu_bulk_import()
                elif choice == '6':
                    self.exit_app()
                
                # Return to main menu
                Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")
                clear_screen()
                self.show_banner()
            
            except KeyboardInterrupt:
                console.print()
                self.exit_app()
            except Exception as e:
                console.print(f"[bold red]✗ An error occurred: {e}[/bold red]")
                logger.error(f"Unexpected error: {e}")
    
    def show_banner(self):
        """Display application banner using Rich."""
        banner_text = """
[bold cyan]╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║            IntelSource - Unified OSINT Aggregator                ║
║                                                                   ║
║  Multi-source IP, Domain & Email reconnaissance tool             ║
║  [yellow]Fast • Accurate • Comprehensive[/yellow]                                 ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝[/bold cyan]
        """
        console.print(banner_text)
        console.print("[dim]Gathering intelligence across multiple sources...\n[/dim]")
    
    def show_menu(self):
        """Display main menu with Rich Table."""
        menu_table = Table(title="[bold magenta]IntelSource - Main Menu[/bold magenta]", show_header=False, box=None)
        menu_table.add_column(style="bold cyan", width=3)
        menu_table.add_column(style="white")
        menu_table.add_column(style="dim")
        
        menu_items = [
            ("1", "IP Address Lookup", "WHOIS, DNS, GeoIP, ASN information"),
            ("2", "Domain Lookup", "WHOIS, DNS enumeration, MX records"),
            ("3", "Email Validation", "MX record validation & deliverability"),
            ("4", "Full Reconnaissance", "Complete intel gathering for target"),
            ("5", "Bulk Import", "Process multiple targets from file"),
            ("6", "Exit", "Quit IntelSource"),
        ]
        
        for num, title, desc in menu_items:
            menu_table.add_row(num, f"[bold]{title}[/bold]", desc)
        
        console.print(menu_table)
    
    def menu_ip_lookup(self):
        """IP address lookup menu."""
        console.print(Panel("[bold cyan]IP Address Lookup[/bold cyan]", expand=False))
        
        ip_address = Prompt.ask("[bold]Enter IP address[/bold]").strip()
        
        if not is_valid_ip(ip_address):
            console.print(f"[bold red]✗ Invalid IP address: {ip_address}[/bold red]")
            return
        
        with console.status(f"[bold green]⟳ Gathering intelligence on {ip_address}...[/bold green]"):
            result = {
                'target': ip_address,
                'type': 'ip',
                'geoip': self.geoip_collector.lookup(ip_address),
                'reverse_dns': self.dns_collector.reverse_lookup(ip_address)
            }
        
        self._display_results(ip_address, result)
    
    def menu_domain_lookup(self):
        """Domain lookup menu."""
        console.print(Panel("[bold cyan]Domain Lookup[/bold cyan]", expand=False))
        
        domain = Prompt.ask("[bold]Enter domain[/bold]").strip()
        
        if not is_valid_domain(domain):
            console.print(f"[bold red]✗ Invalid domain: {domain}[/bold red]")
            return
        
        with console.status(f"[bold green]⟳ Gathering intelligence on {domain}...[/bold green]"):
            result = {
                'target': domain,
                'type': 'domain',
                'whois': self.whois_collector.lookup(domain),
                'dns': self.dns_collector.lookup(domain)
            }
        
        self._display_results(domain, result)
    
    def menu_email_validation(self):
        """Email validation menu."""
        console.print(Panel("[bold cyan]Email Validation[/bold cyan]", expand=False))
        
        email = Prompt.ask("[bold]Enter email address[/bold]").strip()
        
        if not is_valid_email(email):
            console.print(f"[bold red]✗ Invalid email address: {email}[/bold red]")
            return
        
        with console.status(f"[bold green]⟳ Validating email {email}...[/bold green]"):
            result = self.email_validator.validate(email)
        
        self._display_results(email, result)
    
    def menu_full_reconnaissance(self):
        """Full reconnaissance on a target."""
        console.print(Panel("[bold cyan]Full Reconnaissance[/bold cyan]", expand=False))
        
        target = Prompt.ask("[bold]Enter target (IP, domain, or email)[/bold]").strip()
        target_type, is_valid = classify_target(target)
        
        if not is_valid:
            console.print(f"[bold red]✗ Invalid target format: {target}[/bold red]")
            return
        
        with console.status(f"[bold green]⟳ Performing full reconnaissance on {target}...[/bold green]"):
            result = {
                'target': target,
                'type': target_type
            }
            
            try:
                if target_type == 'ip':
                    result['geoip'] = self.geoip_collector.lookup(target)
                    result['reverse_dns'] = self.dns_collector.reverse_lookup(target)
                
                elif target_type == 'domain':
                    result['whois'] = self.whois_collector.lookup(target)
                    result['dns'] = self.dns_collector.lookup(target)
                
                elif target_type == 'email':
                    result['email_validation'] = self.email_validator.validate(target)
                    if '@' in target:
                        domain = target.split('@')[1]
                        result['domain_info'] = {
                            'whois': self.whois_collector.lookup(domain),
                            'dns': self.dns_collector.lookup(domain)
                        }
            except Exception as e:
                console.print(f"[bold red]✗ Reconnaissance failed: {e}[/bold red]")
                logger.error(f"Full recon failed for {target}: {e}")
                return
        
        self._display_results(target, result)
    
    def menu_bulk_import(self):
        """Bulk import targets from file."""
        console.print(Panel("[bold cyan]Bulk Import[/bold cyan]", expand=False))
        
        file_path = Prompt.ask("[bold]Enter file path (one target per line)[/bold]").strip()
        
        if not os.path.exists(file_path):
            console.print(f"[bold red]✗ File not found: {file_path}[/bold red]")
            return
        
        try:
            with open(file_path, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
            
            results = []
            
            with console.status(f"[bold green]⟳ Processing {len(targets)} targets...[/bold green]"):
                for i, target in enumerate(targets, 1):
                    target_type, is_valid = classify_target(target)
                    
                    if not is_valid:
                        logger.warning(f"Skipping invalid target: {target}")
                        continue
                    
                    result = {'target': target, 'type': target_type}
                    
                    try:
                        if target_type == 'ip':
                            result['geoip'] = self.geoip_collector.lookup(target)
                        elif target_type == 'domain':
                            result['whois'] = self.whois_collector.lookup(target)
                            result['dns'] = self.dns_collector.lookup(target)
                        elif target_type == 'email':
                            result['email_validation'] = self.email_validator.validate(target)
                        
                        results.append(result)
                    except Exception as e:
                        logger.error(f"Bulk import error for {target}: {e}")
            
            console.print(f"[bold green]✓ Processed {len(results)}/{len(targets)} targets[/bold green]")
            
            result = {'bulk_results': results, 'total': len(results), 'processed': len(results), 'total_targets': len(targets)}
            self._display_results('Bulk Import', result)
        
        except Exception as e:
            console.print(f"[bold red]✗ Bulk import failed: {e}[/bold red]")
            logger.error(f"Bulk import error: {e}")
    
    def _display_results(self, target: str, result: Dict[str, Any]):
        """Display results with Rich formatting."""
        console.print()
        console.print(Panel(f"[bold cyan]Results for {target}[/bold cyan]", expand=False, style="cyan"))
        
        # Format JSON for display with syntax highlighting
        json_str = json.dumps(result, indent=2, default=str)
        syntax = Syntax(json_str, "json", theme="monokai", line_numbers=False)
        console.print(syntax)
        
        # Save result
        self.save_result(result)
    
    def save_result(self, result: Dict[str, Any]):
        """Save result to file."""
        try:
            results_dir = Path('results')
            results_dir.mkdir(exist_ok=True)
            
            import time
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            target = result.get('target', 'unknown').replace('/', '_').replace('@', '_')
            filename = f"{target}_{timestamp}.json"
            
            filepath = results_dir / filename
            with open(filepath, 'w') as f:
                json.dump(result, f, indent=2, default=str)
            
            console.print(f"[bold green]✓ Results saved to: [cyan]{filepath}[/cyan][/bold green]")
        
        except Exception as e:
            console.print(f"[bold yellow]⚠ Failed to save results: {e}[/bold yellow]")
            logger.error(f"Failed to save results: {e}")
    
    def exit_app(self):
        """Exit application."""
        clear_screen()
        console.print(Panel(
            "[bold cyan]Thank you for using IntelSource![/bold cyan]\n[dim]Happy hunting! 🎯[/dim]",
            expand=False,
            style="cyan"
        ))
        sys.exit(0)


def main():
    """Entry point."""
    try:
        if not os.path.exists('.env'):
            console.print("[bold yellow]⚠ Note: .env file not found.[/bold yellow]")
            console.print("[dim]Copy .env.example to .env and add your ipinfo.io token for full functionality.[/dim]\n")
        
        app = IntelSource()
        app.run()
    except Exception as e:
        console.print(f"[bold red]✗ Fatal error: {e}[/bold red]")
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

