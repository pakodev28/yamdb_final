# Generated by Django 2.2.16 on 2021-08-16 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("media_content", "0002_auto_20210816_1548"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="title",
            options={
                "ordering": ("-name",),
                "verbose_name": "Тайтл",
                "verbose_name_plural": "Тайтлы",
            },
        ),
    ]