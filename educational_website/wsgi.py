"""
WSGI config for educational_website project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educational_website.settings')

application = get_wsgi_application()

# Vercel looks for a variable named "app"
app = application

# Vercel lo database /tmp lo untundi (prathi cold start lo empty), anduke tables create chestam.
if os.environ.get("VERCEL"):
    from django.core.management import call_command
    call_command("migrate", interactive=False, verbosity=0)
