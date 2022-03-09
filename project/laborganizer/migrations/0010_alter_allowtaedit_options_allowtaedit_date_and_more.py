# Generated by Django 4.0.1 on 2022-03-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborganizer', '0009_allowtaedit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allowtaedit',
            options={'verbose_name': 'Allow TA Edit', 'verbose_name_plural': 'Allow TA Edits'},
        ),
        migrations.AddField(
            model_name='allowtaedit',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allowtaedit',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='allowtaedit',
            name='allowed',
            field=models.BooleanField(default=False, verbose_name="Allow TA's to edit"),
        ),
    ]