# Generated by Django 5.2 on 2025-04-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='user-photo/'),
        ),
    ]
