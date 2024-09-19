from rest_framework import viewsets, status
from rest_framework.response import Response
from dentalApp.models import (
    Clinic, Doctor, 
    Patient, Visit, 
    Appointment, Affiliation
)
from .serializers import (
    ClinicSerializer, DoctorSerializer, 
    PatientSerializer, VisitSerializer, 
    AppointmentSerializer, AffiliationSerializer
)
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login

# Login ViewSet
class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        """
        Handle login requests with session-based authentication.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user with email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in and create a session
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

# Clinic ViewSet
class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        """
        List all clinics with affiliated doctors and patients count.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Get clinic details including affiliated doctors.
        """
        clinic = self.get_object()
        serializer = self.get_serializer(clinic)
        return Response(serializer.data)


# Doctor ViewSet
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def list(self, request, *args, **kwargs):
        """
        List all doctors with affiliated clinics and patients count.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Get doctor details with affiliated clinics and patients.
        """
        doctor = self.get_object()
        serializer = self.get_serializer(doctor)
        return Response(serializer.data)


# Patient ViewSet
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        """
        List all patients with last visit and next appointment information.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Get patient details with visit history and next appointment.
        """
        patient = self.get_object()
        serializer = self.get_serializer(patient)
        return Response(serializer.data)


# Visit ViewSet
class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def create(self, request, *args, **kwargs):
        """
        Add a new visit for a patient.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Appointment ViewSet
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        """
        Schedule a new appointment for a patient.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Affiliation ViewSet
class AffiliationViewSet(viewsets.ModelViewSet):
    queryset = Affiliation.objects.all()
    serializer_class = AffiliationSerializer

    def create(self, request, *args, **kwargs):
        """
        Add a new affiliation between a doctor and a clinic.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
