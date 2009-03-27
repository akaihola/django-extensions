"""
sync_permissions
================

Originally from Patrick Altman:
http://paltman.com/2008/apr/11/keeping-contenttypes-and-permissions-updated-without-syncdb/
http://www.djangosnippets.org/snippets/696/

When adding models to the database schema by hand instead of using syncdb, one
has to take care that permission records are created (if using
django.contrib.auth).

Also, after adding custom permissions to existing models, the syncdb command
doesn't update the permission records.

This command updates the permission records according to custom permissions in
all models.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Adds missing permission records."

    def handle(self, *args, **options):
        # Add any missing permissions
        from django.contrib.auth.management import create_permissions
        from django.db.models import get_apps
        for app in get_apps():
            create_permissions(app, None, 2)
