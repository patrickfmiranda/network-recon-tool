from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def generate_html_report(data: dict, output_path: str = "report.html"):
    """Gera relatório HTML a partir dos dados do scan."""

    # Caminho para a pasta templates
    templates_dir = Path(__file__).parent.parent.parent / "templates"

    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    template = env.get_template("report.html")

    html = template.render(
        target=data["target"],
        scan_time=data["scan_time"],
        duration=data["duration_s"],
        open_ports=data["open_ports"],
        services=data["services"],
    )

    with open(output_path, "w") as f:
        f.write(html)

    print(f"[*] HTML report saved: {output_path}")
    return output_path