# Generated by Django 4.0.1 on 2022-02-28 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachingassistant', '0018_remove_ta_assigned_labs_ta_assigned_labs'),
        ('laborganizer', '0008_alter_lab_course_id'),
        ('optimization', '0002_templateassignments_semester'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TemplateAssignments',
            new_name='TemplateAssignment',
        ),
    ]