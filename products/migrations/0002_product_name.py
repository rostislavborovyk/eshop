# Generated by Django 3.1.3 on 2020-11-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
