# Generated by Django 4.2 on 2023-05-12 14:20

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=markdownx.models.MarkdownxField(blank=True, default='', max_length=500),
        ),
    ]
