# FILE PURPOSE: Lightweight smoke tests that ensure the core tutorial routes keep responding.
# CAME FROM: README.md -> Run it checklist now points here for `python manage.py test dashboard`.
# NEXT: Run `python manage.py test dashboard` whenever you tweak URLs or views to catch regressions early.

from django.test import TestCase
from django.urls import reverse


class PageSmokeTests(TestCase):
    # COMMENT: Loop over the named URLs so the test fails if any mapping breaks.
    def test_public_pages(self):
        for name in ("dashboard:home", "dashboard:about"):
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200)

    # COMMENT: Anonymous users should be redirected to the login page at /admin/.
    def test_admin_redirects(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 302)
