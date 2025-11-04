import csv
from jinja2 import Template
from typing import List, Dict
import os

HTML_TEMPLATE = """
<html>
<head><title>Log Analyzer Report</title></head>
<body>
<h1>Log Analyzer Report</h1>
<p>Generated report with {{alerts|length}} alerts</p>
<table border="1" cellpadding="4">
<tr><th>ID</th><th>Severity</th><th>Description</th><th>Details</th></tr>
{% for a in alerts %}
<tr>
  <td>{{a.id}}</td>
  <td>{{a.severity}}</td>
  <td>{{a.description}}</td>
  <td><pre>{{a | tojson}}</pre></td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

def write_csv(alerts: List[Dict], outpath: str):
    keys = set()
    for a in alerts:
        keys.update(a.keys())
    keys = list(keys)
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for a in alerts:
            writer.writerow(a)

def write_html(alerts: List[Dict], outpath: str):
    tpl = Template(HTML_TEMPLATE)
    rendered = tpl.render(alerts=alerts)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(rendered)
