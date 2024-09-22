from django.db import models
from django.utils import timezone


PROCEDURES = [
    ('cleaning', "Cleaning"),
    ('filling', 'Filling'),
    ('root canal', 'Root Canal'),
    ('crown', 'Crown'),
    ('teeth whitening', 'Teeth Whitening')
]

GENDER = [
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'Other')
]


class Clinic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def affiliated_doctors_count(self):
        return Doctor.objects.filter(clinics=self).count()

    def affiliated_patients_count(self):
        return Patient.objects.filter(appointments__clinic=self).distinct().count()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    npi = models.CharField(max_length=20, unique=True)  # National Provider Identifier
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    specialties = models.CharField(
        max_length=50,
        choices=PROCEDURES,
        default='cleaning'
    )
    clinics = models.ManyToManyField(Clinic, through='Affiliation')
    
    def affiliated_clinics_count(self):
        return self.clinics.count()

    def affiliated_patients_count(self):
        return Patient.objects.filter(appointments__doctor=self).distinct().count()
    

    def __str__(self):
        return self.name


class Affiliation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='affiliations')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='affiliations')
    office_address = models.TextField()
    working_schedule = models.TextField() 

    class Meta:
        unique_together = ['doctor', 'clinic']


class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    ssn_no = models.CharField(max_length=4, unique=True)
    gender = models.CharField(
        max_length=50,
        choices=GENDER, 
        default='female'
        )
    last_visit_procedure = models.CharField(max_length=100, choices=PROCEDURES, null=True, blank=True)
    next_visit_procedure = models.CharField(max_length=100, choices=PROCEDURES, null=True, blank=True)


    def last_visit(self):
        return self.visits.order_by('-date').first()

    def next_appointment_date(self):
        next_appointment = self.appointments.filter(date__gte=timezone.now()).order_by('date').first()
        return next_appointment.date if next_appointment else None
    
    def last_visited_doctor(self):
        last_visit = self.visits.order_by('-date').first()
        return last_visit.doctor if last_visit else None
    
    def last_visit_date(self):
        last_visit = self.visits.order_by('-date').first()
        return last_visit.date if last_visit else None
    
    def next_appointment_doctor(self):
        next_appointment = self.appointments.filter(date__gte=timezone.now()).order_by('date').first()
        return next_appointment.doctor if next_appointment else None
    
    def next_appointment(self):
        return self.appointments.filter(date__gte=timezone.now()).order_by('date').first()

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    procedures_done = models.CharField(
        max_length=50,
        choices=PROCEDURES, 
        default='cleaning'
        )
    doctor_notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    procedure = models.CharField(
        max_length=50,
        choices=PROCEDURES, 
        default='cleaning'
        )
    date = models.DateTimeField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date} ({self.procedure})"
