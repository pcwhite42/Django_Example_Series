<!-- REF-HEADER-START -->
Points To:
- GettingStartedHowTo.md
- docs/BEGINNER_GLOSSARY.md
- docs/TROUBLESHOOTING.md
- docs/TUTORIAL_SERIES.md
Referenced By:
- GettingStartedHowTo.md
<!-- REF-HEADER-END -->




# FILE PURPOSE: Provide bite-sized Django + pandas examples that absolute beginners can build after finishing the base tutorial.
# CAME FROM: GettingStartedHowTo.md -> Add-on resources can point here for more practice ideas.
# NEXT: After trying an example, jot notes in your own journal to reinforce what you learned. See ::--:: GettingStartedHowTo.md for the main flow.

## Before You Start (applies to every example)
- Activate your virtual environment and start the dev server (`python manage.py runserver`); leave it running so Django auto-reloads.
- Keep these files open side-by-side: `dashboard/views.py`, `dashboard/templates/dashboard/index.html`, and `dashboard/urls.py`.
- Run `python manage.py test dashboard` after each example to confirm the smoke tests still pass.
- When you change data files, save them in `data/` and refresh the page to see pandas reload the CSV.
- Don't forget about your Beginner Glossary and Troubleshooting Guides See ::--:: docs/BEGINNER_GLOSSARY.md  and  See ::--:: docs/TROUBLESHOOTING.md

## Example 1: Highlight Rows Above a Threshold
- Goal: Add a column to the existing DataFrame that flags rows where `visitors` exceed 170.
- Steps:
  1. In `dashboard/views.py`, right after the DataFrame loads, add:
     ```python
     data_frame["is_popular"] = data_frame["visitors"] > 170
     ```
  2. Keep returning `table_html` as-is; `to_html` automatically includes the new column.
  3. Refresh the browser and inspect the new boolean column (True/False).
- Why it helps: Reinforces how pandas manipulates data before the template renders anything.
- Why (conceptual): Helps you learn column creation and simple comparisons without changing templates.

## Example 2: Swap the Data Source
- Goal: Point the dashboard at a new CSV file containing quarterly revenue.
- Steps:
  1. Copy `data/sample.csv` to `data/quarterly_revenue.csv` and adjust the headers to `quarter,total_sales`.
  2. In `dashboard/views.py`, set `csv_path = Path(BASE_DIR) / "data" / "quarterly_revenue.csv"`.
  3. Update the template header text to mention "Quarterly Revenue" so the UI matches the data.
  4. Refresh the browser and confirm the new column names appear in the table.
- Why it helps: Demonstrates that changing data sources only requires small edits thanks to the existing breadcrumbs.
- Why (conceptual): Shows the separation of data source vs. rendering so you can swap inputs safely.

## Example 3: Add a Simple Form for Filtering
- Goal: Let learners filter the table by month using a GET parameter (no database required).
- Steps:
  1. In `dashboard/views.py`, add:
     ```python
     requested_month = request.GET.get("month")
     if requested_month:
         data_frame = data_frame[data_frame["month"] == requested_month]
     months = data_frame["month"].unique().tolist()
     ```
     When you build the `context` dictionary later in the view, include `months` so the template can render the options (e.g., `context = {..., "months": months}`).
  2. In `dashboard/templates/dashboard/index.html`, add a simple GET form near the top:
     ```html
     <form method="get">
       <label for="month">Filter by month:</label>
       <select id="month" name="month">
         <option value="">Show all</option>
         {% for month in months %}
           <option value="{{ month }}" {% if request.GET.month == month %}selected{% endif %}>{{ month }}</option>
         {% endfor %}
       </select>
       <button type="submit">Apply</button>
     </form>
     ```
     (If you add more filters later, include their option lists in the `context` dictionary in the view.)
  3. Refresh the page, pick a month, and verify the table trims to matching rows; clear the dropdown to show all rows again.
- Why it helps: Introduces request handling without touching the ORM.
- Why (conceptual): Teaches GET params, filtering, and context passing without revealing the full implementation beyond the outline already shown.

## Example 4: Export Summary Statistics
- Goal: Give learners a download button for the summary DataFrame.
- Steps:
  1. In `dashboard/views.py`, add a view (near the existing ones):
     ```python
     from django.http import HttpResponse  # at the top of the file

     def summary_csv(request):
         csv_path = Path(settings.BASE_DIR) / "data" / "sample.csv"
         data_frame = pd.read_csv(csv_path, comment="#")
         summary = data_frame.describe().loc[["count", "mean", "min", "max"]]
         response = HttpResponse(summary.to_csv(index=True), content_type="text/csv")
         response["Content-Disposition"] = 'attachment; filename="summary.csv"'
         return response
     ```
  2. Register the route in `dashboard/urls.py`:
     ```python
     path("summary.csv", views.summary_csv, name="summary_csv"),
     ```
  3. Add a link or button in the dashboard template:
     ```html
     <p><a href="{% url 'dashboard:summary_csv' %}">Download summary as CSV</a></p>
     ```
  4. Click the link in your browser and confirm a CSV file downloads with the expected columns.
- Why it helps: Shows how to return non-HTML responses while staying within the same stack.
- Why (conceptual): Introduces content negotiation and file responses without changing the core page.

## Example 5: Inline Documentation
- Goal: Encourage note-taking by adding `# CAME FROM` and `# NEXT` breadcrumbs to the new code you write.
- Steps:
  1. Pick any example above and implement it.
  2. Write fresh breadcrumbs near the lines you touched, explaining where learners should hop next (e.g., `# NEXT: dashboard/templates/...`).
- Why it helps: Reinforces the teaching style and ensures the tutorial remains beginner-friendly even as new features appear.
- Why (conceptual): Builds the habit of documenting flow without giving away the full solution.

## Example 6: "Hello, Django" Mini Page
- Goal: Create the simplest possible page to reinforce the URL → view → template flow.
- Steps:
  1. In `dashboard/views.py`, add:
     ```python
     def hello(request):
         # CAME FROM: dashboard/urls.py -> hello route.
         # NEXT: dashboard/templates/dashboard/hello.html
         return render(request, "dashboard/hello.html", {"message": "Hello, Django learner!"})
     ```
  2. In `dashboard/urls.py`, register the route:
     ```python
     path("hello/", views.hello, name="hello")
     ```
  3. Create `dashboard/templates/dashboard/hello.html` so it shows the message and a back link:
     ```html
     <!DOCTYPE html>
     <html>
       <head><title>Hello</title></head>
       <body>
         <h1>{{ message }}</h1>
         <p><a href="{% url 'dashboard:home' %}">Back to dashboard</a></p>
       </body>
     </html>
     ```
  4. Start the server [if not already running] (`python manage.py runserver`) and visit `http://127.0.0.1:8000/hello/` to confirm it loads.
- Why it helps: This mirrors classic starter tutorials while fitting the breadcrumb style used here.
- Why (conceptual): Reinforces the URL -> view -> template path in the smallest possible example.

## Example 7: Intro to Template Inheritance (Base Layout)
- Goal: Build a base template and reuse it for the dashboard without changing functionality.
- Steps:
  1. Create `dashboard/templates/dashboard/base.html`:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
       <title>{% block title %}Beginner Dashboard{% endblock %}</title>
       <link rel="stylesheet" href="{% static 'dashboard/styles.css' %}">
     </head>
     <body>
       <header><a href="{% url 'dashboard:home' %}">Home</a> | <a href="{% url 'dashboard:about' %}">About</a></header>
       <main>{% block content %}{% endblock %}</main>
     </body>
     </html>
     ```
  2. Update `dashboard/templates/dashboard/index.html` to extend it:
     ```html
     {% extends "dashboard/base.html" %}
     {% block title %}Dashboard{% endblock %}
     {% block content %}
       <!-- existing content goes here -->
     {% endblock %}
     ```
  3. Do the same for `dashboard/templates/dashboard/about.html` (and `hello.html` if you built Example 6).
  4. Refresh `/` and `/about/` to confirm the layout still renders; run `python manage.py test dashboard`.
- Why it helps: Shows beginners how to avoid duplication using standard Django patterns they will see in other tutorials.
- Why (conceptual): Demonstrates DRY templating without altering business logic.

## Example 8: Static Asset Swap (Custom CSS)
- Goal: Practice replacing the CSS file without touching Python code.
- Steps:
  1. Drop a new stylesheet into `dashboard/static/dashboard/styles.css` (or back it up and paste a temporary alternative).
  2. Confirm the `<link>` in `base.html` (Example 7) or `index.html` points to `{% static 'dashboard/styles.css' %}`.
  3. Run `python manage.py collectstatic` (if you want to simulate production) or just refresh the dev server to see changes locally.
  4. Note what changed in the UI and consider how to roll it back (copy the old file from git history if needed).
- Why it helps: Matches beginner tutorials that teach static files and reinforces safe CSS experimentation.
- Why (conceptual): Teaches safe static file swaps and rollback thinking without new Python code.

## See ::--:: docs/TUTORIAL_SERIES.md
