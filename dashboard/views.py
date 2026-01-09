# FILE PURPOSE: Contains view functions that prepare data and return responses for the dashboard app.

# IMPORT: Path lets us build filesystem paths relative to this file for CSV access.
from pathlib import Path

# IMPORT: pandas handles CSV reading and data analysis so we can show tables and stats.
import pandas as pd

# IMPORT: settings exposes project-wide constants like BASE_DIR for consistent path building.
from django.conf import settings

# IMPORT: render loads a template, fills it with context data, and returns an HTTP response.
from django.shortcuts import render


# FUNCTION: home receives HTTP requests for "/" and returns the dashboard page.
# WHY: This is our main teaching view that reads a CSV, summarizes data, and renders HTML.
def home(request):
    # COMMENT: Locate the sample CSV next to the project so the tutorial stays portable.
    csv_path = Path(settings.BASE_DIR) / "data" / "sample.csv"
    # NEXT: open data/sample.csv to inspect the raw values pandas ingests.

    # COMMENT: Read the CSV into a DataFrame (pandas structure optimized for tabular data).
    # PERFORMANCE NOTE: pandas.read_csv loads entire files into memory; perfect for small classroom CSVs,
    # but stream or chunk uploads when learners begin importing larger (>10MB) datasets.
    # EXTRA: comment="#" tells pandas to treat lines starting with "#" as documentation, keeping the dataset clean.
    data_frame = pd.read_csv(csv_path, comment="#")
    # SECURITY REMINDER: If you ever accept user-supplied CSVs, validate and sanitize before rendering to avoid XSS payloads.
    # DEBUG TIP: Uncomment `print(data_frame.head())` while developing to inspect the first rows, then remove or comment it out before committing.

    # COMMENT: Generate quick summary statistics (count, mean, min, max) for numeric columns.
    # PERFORMANCE NOTE: describe() is vectorized, but avoid calling it repeatedly in hot paths; cache results if needed.
    summary = data_frame.describe().loc[["count", "mean", "min", "max"]]

    # COMMENT: Convert the DataFrame to HTML; index=False drops the pandas index column so tables stay clean for readers.
    # PERFORMANCE NOTE: to_html renders the entire dataset at once - great for tiny teaching files, but paginate or sample large datasets.
    # TRUST BOUNDARY: This output is marked safe in the template - only do this for CSVs you trust or have sanitized.
    table_html = data_frame.to_html(
        classes="data-table", index=False, border=0, justify="center"
    )

    # COMMENT: Convert the summary to HTML with indexes so readers see which statistic is displayed.
    summary_html = summary.to_html(
        classes="summary-table", border=0, justify="center"
    )

    # COMMENT: The context dictionary passes data into the template for rendering.
    context = {
        "table_html": table_html,  # Template will embed this raw HTML table.
        "summary_html": summary_html,  # Template will embed summary stats.
        "csv_name": csv_path.name,  # Helps learners see which file is loaded.
        "row_count": len(data_frame),  # Quick metric for text callouts.
    }

    # NEXT: open beginner_dashboard/urls.py to see how this view is routed into the site root.
    # NEXT: open dashboard/templates/dashboard/index.html to understand how the context is rendered.
    # COMMENT: render() picks dashboard/templates/dashboard/index.html and fills it with context.
    return render(request, "dashboard/index.html", context)


# FUNCTION: about provides a gentle explainer page that links developers through the breadcrumb trail.
# CAME FROM: dashboard/urls.py -> path("about/", views.about, name="about").
# NEXT: open dashboard/templates/dashboard/about.html to review the teaching copy.
def about(request):
    # COMMENT: Keeping context small shows how Django can render static teaching pages with minimal code.
    return render(
        request,
        "dashboard/about.html",
        {
            "project_name": "Beginner Django Dashboard",
        },
    )
