# Generated by Django 4.0.5 on 2022-08-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]
