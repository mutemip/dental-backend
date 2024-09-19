from rest_framework import serializers
from django.utils.timezone import timedelta
from dentalApp.models import (
    Clinic, Doctor, 
    Patient, Visit, 
    Appointment, Affiliation
    )



class ClinicSerializer(serializers.ModelSerializer):
    affiliated_doctors_count = serializers.SerializerMethodField(read_only=True)
    affiliated_patients_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'phone_number', 'address', 'city', 'state', 
                  'email', 'affiliated_doctors_count',
                'affiliated_patients_count']
        
    def get_affiliated_doctors_count(self, obj):
        return obj.affiliated_doctors_count()
        

class DoctorSerializer(serializers.ModelSerializer):
    affiliated_clinics_count = serializers.IntegerField(read_only=True)
    affiliated_patients_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'npi', 'name', 'email', 'phone_number', 'specialties', 
                  'affiliated_clinics_count', 'affiliated_patients_count']


class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ['id', 'doctor', 'clinic', 
                  'office_address', 'working_schedule']
        extra_kwargs = {
            'doctor': {'required': True},
            'clinic': {'required': True}
        }


class AffiliatedDoctorSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name')
    office_address = serializers.CharField()
    working_schedule = serializers.CharField()

    class Meta:
        model = Affiliation
        fields = ['doctor_name', 'office_address', 'working_schedule']

class AffiliatedClinicSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name')
    clinic_address = serializers.CharField(source='clinic.address')
    clinic_phone = serializers.CharField(source='clinic.phone_number')

    class Meta:
        model = Affiliation
        fields = ['clinic_name', 'clinic_address', 'clinic_phone', 
                  'office_address', 'working_schedule']


class PatientSerializer(serializers.ModelSerializer):
    last_visited_doctor = serializers.SerializerMethodField(read_only=True)
    last_visit_date = serializers.SerializerMethodField(read_only=True)
    # next_appointment_date = serializers.SerializerMethodField(read_only=True)
    next_appointment_doctor = serializers.SerializerMethodField(read_only=True)
    next_appointment = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'address', 'phone_number', 
                  'ssn_no','gender', 'last_visit_date', 'last_visited_doctor', 
                  'last_visit_procedure','next_visit_procedure', 
                  'next_appointment_doctor', 'next_appointment']
        
    def get_last_visited_doctor(self, obj):
        doctor = obj.last_visited_doctor()
        return doctor.name if doctor else None
    
    def get_last_visit_date(self, obj):
        return obj.last_visit_date()
    
    # def get_next_appointment_date(self, obj):
    #     return obj.next_appointment_date()
    
    def get_next_appointment_doctor(self, obj):
        doctor = obj.next_appointment_doctor()
        return doctor.name if doctor else None
    
    def get_next_appointment(self, obj):
        next_appointment = obj.next_appointment()
        if next_appointment:
            return NextAppointmentSerializer(next_appointment).data
        return None


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'patient', 'doctor', 'clinic', 'procedures_done', 
                  'doctor_notes', 'date']
        extra_kwargs = {
            'patient': {'required': True},
            'doctor': {'required': True},
            'clinic': {'required': True}
        }

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'clinic', 'procedure', 'date', 'date_booked']
        extra_kwargs = {
            'patient': {'required': True},
            'doctor': {'required': True},
            'clinic': {'required': True},
            'date': {'required': True}
        }

    def validate(self, data):
        """
        Ensure that no other appointment is booked within a 1-hour time slot
        after the appointment start time for the same doctor at the same clinic.
        """
        doctor = data.get('doctor')
        clinic = data.get('clinic')
        appointment_start = data.get('date')

        # Define 1-hour slot (i.e., no overlapping appointments within 1 hour after the start)
        appointment_end = appointment_start + timedelta(hours=1)

        # Check if any existing appointment overlaps with the given time slot
        overlapping_appointments = Appointment.objects.filter(
            doctor=doctor,
            clinic=clinic,
            date__lt=appointment_end,  # Overlapping if starts before this appointment ends
            date__gte=appointment_start  # Overlapping if starts after or at the same time
        ).exists()

        if overlapping_appointments:
            raise serializers.ValidationError("This time slot is already booked for the selected doctor.")

        return data

class PatientVisitSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name')
    clinic_name = serializers.CharField(source='clinic.name')
    
    class Meta:
        model = Visit
        fields = ['id', 'date', 'doctor_name', 'clinic_name', 'procedures_done', 'doctor_notes']

class NextAppointmentSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name')
    doctor_name = serializers.CharField(source='doctor.name')
    
    class Meta:
        model = Appointment
        fields = ['date', 'clinic_name', 'doctor_name', 'procedure', 'date_booked']
