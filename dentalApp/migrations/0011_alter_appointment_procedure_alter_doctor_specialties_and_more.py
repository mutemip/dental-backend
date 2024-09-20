# Generated by Django 5.1.1 on 2024-09-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalApp', '0010_alter_appointment_procedure_alter_clinic_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='procedure',
            field=models.CharField(choices=[('crown', 'Crown'), ('teeth whitening', 'Teeth Whitening'), ('cleaning', 'Cleaning'), ('filling', 'Filling'), ('root canal', 'Root Canal')], default='cleaning', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.CharField(choices=[('crown', 'Crown'), ('teeth whitening', 'Teeth Whitening'), ('cleaning', 'Cleaning'), ('filling', 'Filling'), ('root canal', 'Root Canal')], default='cleaning', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')], default='female', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_visit_procedure',
            field=models.CharField(blank=True, choices=[('crown', 'Crown'), ('teeth whitening', 'Teeth Whitening'), ('cleaning', 'Cleaning'), ('filling', 'Filling'), ('root canal', 'Root Canal')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_visit_procedure',
            field=models.CharField(blank=True, choices=[('crown', 'Crown'), ('teeth whitening', 'Teeth Whitening'), ('cleaning', 'Cleaning'), ('filling', 'Filling'), ('root canal', 'Root Canal')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='procedures_done',
            field=models.CharField(choices=[('crown', 'Crown'), ('teeth whitening', 'Teeth Whitening'), ('cleaning', 'Cleaning'), ('filling', 'Filling'), ('root canal', 'Root Canal')], default='cleaning', max_length=50),
        ),
    ]
