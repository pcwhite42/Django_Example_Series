<!-- REF-HEADER-START -->
Points To:
- README.md
Referenced By:
- README.md
- docs\BEGINNER_EXAMPLES.md
<!-- REF-HEADER-END -->











# FILE PURPOSE: Plain-language glossary for the most common Django + pandas terms in this tutorial.
# CAME FROM: README.md quick index points here to help brand-new learners.
# NEXT: Skim this whenever you encounter an unfamiliar term; update it as the project grows. See ::--:: README.md for the main flow.

- **View**:-------------------------A Python function that receives a request and returns a response (HTML, CSV, etc.).
- **URLconf (urls.py)**:------------The map that connects URL patterns to view functions.
- **Template**:---------------------An HTML file with placeholders (e.g., `{{ variable }}`) that the view fills with context.
- **Context**:----------------------The dictionary a view passes to a template so it can render dynamic content (e.g., `{"table_html": ...}`).
- **Static files**:-----------------Assets like CSS/JS/images served from `dashboard/static/`; referenced in templates with `{% static %}`.
- **Migration**:--------------------A recorded database schema change; created via `makemigrations` and applied via `migrate`.
- **Superuser**:--------------------An admin account with full permissions to access `/admin/`.
- **GET parameter**:----------------Data sent in the URL query string (e.g., `?month=June`), often read with `request.GET.get(...)`.
- **pandas DataFrame**:-------------In-memory table for CSV/analysis work; converted to HTML with `to_html` in this project.
- **Virtual environment (venv)**:---An isolated Python environment so your project’s dependencies don’t conflict with global packages.
- **SECRET_KEY**:-------------------Required Django setting for security; always load from the environment, never hardcode.
