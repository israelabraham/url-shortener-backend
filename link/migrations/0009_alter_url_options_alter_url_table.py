# Generated by Django 4.1 on 2022-09-09 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("link", "0008_auto_20200811_0006")]

    operations = [
        migrations.AlterModelOptions(
            name="url", options={"verbose_name_plural": "URLs"}
        ),
        migrations.AlterModelTable(name="url", table="urls"),
    ]
