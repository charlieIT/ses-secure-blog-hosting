# Generated by Django 4.2 on 2023-05-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_body_comment_comment_post_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Post2',
        ),
    ]
