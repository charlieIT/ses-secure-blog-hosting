from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm

# Create authorisation Groups
readers = Group.objects.create(name="readers")
authors = Group.objects.create(name="authors")
api_users = Group.objects.create(name="api_users")
moderator = Group.objects.create(name="moderator")

# Create authorisation permissions
#assign_perm('read_blog', readers)

