# Generated by Django 5.1.1 on 2024-09-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalApp', '0007_alter_appointment_procedure_alter_doctor_specialties_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='next_visit',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='procedure',
            field=models.CharField(choices=[('root canal', 'Root Canal'), ('crown', 'Crown'), ('filling', 'Filling'), ('cleaning', 'Cleaning'), ('teeth whitening', 'Teeth Whitening')], default='cleaning', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.CharField(choices=[('root canal', 'Root Canal'), ('crown', 'Crown'), ('filling', 'Filling'), ('cleaning', 'Cleaning'), ('teeth whitening', 'Teeth Whitening')], default='cleaning', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('other', 'Other'), ('female', 'Female'), ('male', 'Male')], default='female', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_visit_procedure',
            field=models.CharField(blank=True, choices=[('root canal', 'Root Canal'), ('crown', 'Crown'), ('filling', 'Filling'), ('cleaning', 'Cleaning'), ('teeth whitening', 'Teeth Whitening')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_visit_procedure',
            field=models.CharField(blank=True, choices=[('root canal', 'Root Canal'), ('crown', 'Crown'), ('filling', 'Filling'), ('cleaning', 'Cleaning'), ('teeth whitening', 'Teeth Whitening')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='visit',
            name='procedures_done',
            field=models.CharField(choices=[('root canal', 'Root Canal'), ('crown', 'Crown'), ('filling', 'Filling'), ('cleaning', 'Cleaning'), ('teeth whitening', 'Teeth Whitening')], default='cleaning', max_length=50),
        ),
    ]
