# Generated by Django 4.0.1 on 2022-03-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimization', '0010_alter_history_relative_node_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='relative_node_id',
            field=models.IntegerField(null=True),
        ),
    ]
