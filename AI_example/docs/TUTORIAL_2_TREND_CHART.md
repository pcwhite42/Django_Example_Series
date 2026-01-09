<!-- REF-HEADER-START -->
Points To:
Referenced By:
- docs\TUTORIAL_SERIES.md
<!-- REF-HEADER-END -->




# Tutorial 2: Add a Trend Chart Using pandas + Templates
# FILE PURPOSE: Show how to compute chart data in pandas and render it in a template without extra libraries.
# GOAL (DONE WHEN): `/` renders your chart data (e.g., inline bars or simple chart) alongside the table/summary, with breadcrumbs intact.
# PREREQS: Tutorial 1 (CSV loaded on `/`); you know URL -> view -> template flow and have the server running.

## Step-by-Step (with “what/why/how”)
1) Compute chart data in the view
   - What: Slice/aggregate your DataFrame (e.g., `data_frame[["month","visitors"]]`) and convert it for the template (e.g., `chart_data = data_frame[["month","visitors"]].to_dict(orient="records")`).
   - How: In `dashboard/views.py`, after reading the CSV and summaries, add the `chart_data` variable to the context `chart_data = data_frame[["month","visitors"]].to_dict(orient="records")`.

2) Render chart data in the template
   - What: Loop through `chart_data` in `dashboard/templates/dashboard/index.html` and draw a simple chart (inline SVG or a div with width based on value).
   - How (simple bar example):
     ```html
     <div class="chart">
       {% for row in chart_data %}
         <div class="bar" style="width: {{ row.visitors }}px;">
           {{ row.month }} ({{ row.visitors }})
         </div>
       {% endfor %}
     </div>
     ```
     Note: Add light CSS in `dashboard/static/dashboard/styles.css` for the "chart" and "bar" classes if you want different spacing/colors.

3) Keep breadcrumbs updated
   - What: Add/confirm `# CAME FROM` / `# NEXT` comments where you touched view/template.
   - How: Follow the existing comment style used in the project.

4) Verify and test
   - What: Run `python manage.py runserver` and load `/` to see the chart plus table/summary.

5) Capture what you learned
   - What: Note the fields you charted and any CSS tweaks in BUILD_LOG.md or personal notes.
   - Why: A quick note helps you repeat or adjust the pattern later.

## Why This Tutorial Matters
- Reinforces passing structured data from pandas to templates safely.
- Gives you a no-new-dependencies way to visualize data.
- Builds discipline around breadcrumbs, tests, and logging what changed.
