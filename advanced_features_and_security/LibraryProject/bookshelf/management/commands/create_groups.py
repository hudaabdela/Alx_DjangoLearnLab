from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Get content type for the Book model
        content_type = ContentType.objects.get_for_model(Book)

        # Define permissions
        permissions = {
            'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
            'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
            'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
            'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
        }

        # Create groups and assign permissions
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        editors_group.permissions.add(permissions['can_create'], permissions['can_edit'])
        viewers_group.permissions.add(permissions['can_view'])
        admins_group.permissions.set(permissions.values())

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully!'))
