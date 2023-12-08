from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField

User = get_user_model()

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Hidden")
)

DEFAULT_USERNAME = "Anonymous"

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    abstract = MarkdownxField(max_length=500, default="", blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField(Category, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.CharField(max_length=80, default=DEFAULT_USERNAME)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user)


# Authorisation schemes
from django.contrib.auth.models import User, Group, Permission
from guardian.shortcuts import assign_perm

# Create authorisation Groups
readers, readers_created = Group.objects.get_or_create(name="readers")
authors, authors_created = Group.objects.get_or_create(name="authors")
api_users, api_created = Group.objects.get_or_create(name="api_users")
moderator, moderator_created = Group.objects.get_or_create(name="moderator")

author_perms = [
    'add_post', 'change_post', 'delete_post', 'view_post',
    'add_comment', 'change_comment', 'delete_comment', 'view_comment',
    'add_category', 'change_category', 'view_category',
    'add_attachment', 'change_attachment', 'delete_attachment', 'view_attachment'
]

def get_perm_by_name(name: str): 
    try: 
        Permission.objects.filter(name=name)
    except:
        return False

# Create authorisation permissions
def set_authors_auth_scheme():
    for perm in author_perms:
        permission = get_perm_by_name(perm)
        if permission is not False:
            authors.permissions.add(permission)
    authors.save()

set_authors_auth_scheme()