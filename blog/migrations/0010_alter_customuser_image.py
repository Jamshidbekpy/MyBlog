# Generated by Django 5.2 on 2025-04-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='user-photo/user-default.jpg', upload_to='user-photo/'),
        ),
    ]
