# Generated by Django 4.1 on 2024-01-31 17:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0006_alter_book_book_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="book_id",
        ),
    ]
