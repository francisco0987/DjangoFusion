# Generated by Django 2.2.3 on 2022-05-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Notebook'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Design moderno'), ('lni-layers', 'Templates'), ('lni-leaf', 'Formas')], max_length=20, verbose_name='Icone'),
        ),
    ]