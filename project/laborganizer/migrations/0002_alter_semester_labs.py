# Generated by Django 4.0.1 on 2022-02-02 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborganizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='labs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='laborganizer.lab'),
        ),
    ]
