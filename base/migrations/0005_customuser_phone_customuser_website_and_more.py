# Generated by Django 5.0.4 on 2024-04-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_ispurchased_purchased_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='ispurchased',
            name='purchased_on',
            field=models.DateTimeField(auto_created=True),
        ),
    ]