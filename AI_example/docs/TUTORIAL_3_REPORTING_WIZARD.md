<!-- REF-HEADER-START -->
Points To:
Referenced By:
- docs\TUTORIAL_SERIES.md
<!-- REF-HEADER-END -->



# Tutorial 3: Mini Reporting Wizard
# FILE PURPOSE: Teach filtering, context messaging, and CSV export in one flow.
# GOAL (DONE WHEN): `/wizard/` lets you filter data, see a preview table, and (optionally) download a summary.
# PREREQS: Tutorial 1 (CSV on `/`), Tutorial 2 (passing structured data), and Example 3 (filter form) from `docs/BEGINNER_EXAMPLES.md`.

## Step-by-Step (with “what/why/how”)
1) Add the route
   - What: In `dashboard/urls.py`, add `path("wizard/", views.wizard, name="wizard")`.
   - How: Mirror the pattern used for `home` or `about` within urls.py.

2) Build the view
   - What: In `dashboard/views.py`, create `wizard()` that:
     - Reads query params (e.g., `month`, `min_revenue`).
     - Filters the DataFrame accordingly.
     - Adds human-friendly status messages (e.g., “Showing rows for June with revenue >= 1000”).
     - Optionally prepares a summary CSV string for download.
   - Why: Demonstrates GET param handling, filtering, and messaging in one place.
   - How (sketch):
     ```python
     def wizard(request):
         month = request.GET.get("month")
         min_revenue = request.GET.get("min_revenue")
         df = load_your_dataframe_somehow()
         if month:
             df = df[df["month"] == month]
         if min_revenue:
             df = df[df["revenue"] >= float(min_revenue)]
         message = "Showing filtered results" if month or min_revenue else "Showing all results"
         # optional summary
         summary_csv = df.describe().to_csv(index=True)
         return render(
             request,
             "dashboard/wizard.html",
             {"rows": df.to_dict(orient="records"), "message": message, "summary_csv": summary_csv},
         )
     ```

3) Create the template
   - What: `dashboard/templates/dashboard/wizard.html` with:
     - A small GET form (month, min_revenue).
     - A preview table (loop over `rows`).
     - A download link/endpoint for the summary if desired.
   - Why: Lets users interactively filter and see results without leaving the page.
   - How (sketch):
     ```html
     {% extends "dashboard/base.html" %}
     {% block title %}Reporting Wizard{% endblock %}
     {% block content %}
       <h1>Reporting Wizard</h1>
       <form method="get">
         <label>Month <input name="month" value="{{ request.GET.month }}"></label>
         <label>Min revenue <input name="min_revenue" value="{{ request.GET.min_revenue }}"></label>
         <button type="submit">Apply</button>
       </form>

       <p>{{ message }}</p>
       <table>
         <thead><tr>{% if rows %}{% for key in rows.0.keys %}<th>{{ key }}</th>{% endfor %}{% endif %}</tr></thead>
         <tbody>
           {% for row in rows %}
             <tr>{% for val in row.values %}<td>{{ val }}</td>{% endfor %}</tr>
           {% endfor %}
         </tbody>
       </table>

       {# Optional: link to a download view if you implement one #}
       {# <p><a href="{% url 'dashboard:summary_csv' %}">Download summary CSV</a></p> #}
     {% endblock %}
     ```

4) Document your work
   - What: Note which filters you added, any summary export, and commands run.
   - Why: Logging changes helps you and teammates repeat or debug later.

## Why This Tutorial Matters
- Combines GET params, filtering, messaging, and (optionally) exporting in a single page.
- Reinforces view -> template wiring
