# Generated by Django 4.0.7 on 2023-05-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_id_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
