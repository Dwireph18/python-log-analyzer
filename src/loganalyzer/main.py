import click
from loganalyzer import parser, detectors, reporter
import json
from pathlib import Path

@click.group()
def cli():
    pass

@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--source", type=click.Choice(["sysmon","auth"]), default="sysmon")
@click.option("--out", type=click.Path(), default="report")
def analyze(input_file, source, out):
    """Analyze a log file and produce alerts."""
    alerts = []
    p = Path(input_file)
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        if source == "sysmon":
            parsed = parser.parse_sysmon_line(line)
        else:
            parsed = parser.parse_auth_line(line)
        if not parsed:
            continue
        a = detectors.run_detectors(parsed, source)
        for item in a:
            alerts.append(item)

    outdir = Path(out)
    outdir.mkdir(parents=True, exist_ok=True)
    # outputs
    reporter.write_csv(alerts, outdir / "alerts.csv")
    reporter.write_html(alerts, outdir / "alerts.html")
    # summary
    print(f"Analysis complete. {len(alerts)} alerts. Reports written to {outdir.resolve()}")

if __name__ == "__main__":
    cli()
