"""
sync_contenttypes
=================

Originally from Patrick Altman:
http://paltman.com/2008/apr/11/keeping-contenttypes-and-permissions-updated-without-syncdb/
http://www.djangosnippets.org/snippets/696/

When adding models to the database schema by hand instead of using syncdb, one
has to take care that content type records are created (if using
django.contrib.contenttypes).

This command adds missing content type records.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Adds missing content type records."

    def handle(self, *args, **options):
        # Add any missing content types
        from django.contrib.contenttypes.management \
            import update_all_contenttypes
        update_all_contenttypes()

        # Add any missing permissions
        from django.contrib.auth.management import create_permissions
        from django.db.models import get_apps
        for app in get_apps():
            create_permissions(app, None, 2)
