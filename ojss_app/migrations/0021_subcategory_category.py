# Generated by Django 2.0.4 on 2018-05-09 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0020_auto_20180509_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ojss_app.Category'),
            preserve_default=False,
        ),
    ]