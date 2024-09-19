from rest_framework import serializers
from dentalApp.models import Clinic, Doctor, Patient, Visit, Appointment, Affiliation

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


class PatientSerializer(serializers.ModelSerializer):
    last_visited_doctor = serializers.SerializerMethodField(read_only=True)
    last_visit_date = serializers.SerializerMethodField(read_only=True)
    next_appointment_date = serializers.SerializerMethodField(read_only=True)
    next_appointment_doctor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'address', 'phone_number', 
                  'ssn_no','gender', 'last_visit_date', 'last_visited_doctor', 
                  'last_visit_procedure', 'next_appointment_date', 
                  'next_visit_procedure', 'next_appointment_doctor']
        
    def get_last_visited_doctor(self, obj):
        doctor = obj.last_visited_doctor()
        return doctor.name if doctor else None
    
    def get_last_visit_date(self, obj):
        return obj.last_visit_date()
    
    def get_next_appointment_date(self, obj):
        return obj.next_appointment_date()
    
    def get_next_appointment_doctor(self, obj):
        doctor = obj.next_appointment_doctor()
        return doctor.name if doctor else None


class VisitSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
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
        fields = ['id', 'patient', 'doctor', 'clinic', 'procedure', 
                  'date', 'date_booked']
        extra_kwargs = {
            'patient': {'required': True},
            'doctor': {'required': True},
            'clinic': {'required': True}
        }
