# Generated by Django 4.1 on 2024-01-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_alter_book_book_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=100,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="book_id",
            field=models.IntegerField(default=100),
        ),
    ]