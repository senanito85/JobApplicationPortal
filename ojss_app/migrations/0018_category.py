# Generated by Django 2.0.4 on 2018-05-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0017_message_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
    ]