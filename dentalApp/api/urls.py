from rest_framework.routers import DefaultRouter
from .views import (
    ClinicViewSet, DoctorViewSet, 
    PatientViewSet, VisitViewSet, 
    AppointmentViewSet, AffiliationViewSet, 
    LoginViewSet
)

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'affiliations', AffiliationViewSet)
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = router.urls
