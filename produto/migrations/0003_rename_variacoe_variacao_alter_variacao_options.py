# Generated by Django 5.1 on 2024-09-09 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacoe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variacoe',
            new_name='Variacao',
        ),
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]