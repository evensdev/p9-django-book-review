# Generated by Django 4.0.2 on 2022-07-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_userfollows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
