# Generated by Django 4.2 on 2023-05-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_featured_delete_post2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
