from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from .forms import *
from markdownx.admin import MarkdownxModelAdmin 
from markdownx.widgets import AdminMarkdownxWidget

#SummernoteModelAdmin
class PostAdmin(GuardedModelAdmin):
    form = PostForm
    list_display = ('title', 'slug', 'author', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    #summernote_fields = ('content', 'abstract')
    
    def get_queryset (self, request):
       return Post.objects.filter(author = request.user)

    def get_form(self, request, *args, **kwargs):
        form = super(PostAdmin, self).get_form(request, *args, **kwargs)
        form.current_user = request.user
        return form
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    permission_required = ('create_user')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'thumbnail')
    list_filter = ("slug",)
    search_fields = ['title', 'subtitle']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'post', 'created_on', 'visible')
    list_filter = ('visible', 'created_on')
    search_fields = ('user', 'comment', 'post')
    fields = ('post', 'comment', 'visible')
    actions = ['approve_comments']

    def get_queryset (self, request):
       not_user_posts = Post.objects.exclude(author = request.user)
       return Comment.objects.exclude(post__in = not_user_posts)

    def approve_comments(self, request, queryset):
        queryset.update(visible=True)

    def get_form(self, request, *args, **kwargs):
        form = super(CommentAdmin, self).get_form(request, *args, **kwargs)
        form.current_user = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post,       PostAdmin)
admin.site.register(Author,     AuthorAdmin)
admin.site.register(Category,   CategoryAdmin)
admin.site.register(Comment,    CommentAdmin)