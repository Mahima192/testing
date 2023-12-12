from django.urls import path, include
from .views import (
    PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    NurseListView, NurseDetailView, NurseCreateView, NurseUpdateView, NurseDeleteView,
    EPHIListView, EPHIDetailView, EPHICreateView, EPHIUpdateView, EPHIDeleteView,
    InsuranceListView, InsuranceDetailView, InsuranceCreateView, InsuranceUpdateView, InsuranceDeleteView,
)



app_name = 'app'

urlpatterns = [
    path('patient/', include([
        path('list/', PatientListView.as_view(), name='patient_list'),
        path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
        path('create/', PatientCreateView.as_view(), name='patient_create'),
        path('update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
        path('delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    ])),

    path('doctor/', include([
        path('list/', DoctorListView.as_view(), name='doctor_list'),
        path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
        path('create/', DoctorCreateView.as_view(), name='doctor_create'),
        path('update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
        path('delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
    ])),

    path('nurse/', include([
        path('list/', NurseListView.as_view(), name='nurse_list'),
        path('<int:pk>/', NurseDetailView.as_view(), name='nurse_detail'),
        path('create/', NurseCreateView.as_view(), name='nurse_create'),
        path('update/<int:pk>/', NurseUpdateView.as_view(), name='nurse_update'),
        path('delete/<int:pk>/', NurseDeleteView.as_view(), name='nurse_delete'),
    ])),

    path('ephi/', include([
        path('list/', EPHIListView.as_view(), name='ephi_list'),
        path('<int:pk>/', EPHIDetailView.as_view(), name='ephi_detail'),
        path('create/', EPHICreateView.as_view(), name='ephi_create'),
        path('update/<int:pk>/', EPHIUpdateView.as_view(), name='ephi_update'),
        path('delete/<int:pk>/', EPHIDeleteView.as_view(), name='ephi_delete'),
    ])),

    path('insurance/', include([
        path('list/', InsuranceListView.as_view(), name='insurance_list'),
        path('<int:pk>/', InsuranceDetailView.as_view(), name='insurance_detail'),
        path('create/', InsuranceCreateView.as_view(), name='insurance_create'),
        path('update/<int:pk>/', InsuranceUpdateView.as_view(), name='insurance_update'),
        path('delete/<int:pk>/', InsuranceDeleteView.as_view(), name='insurance_delete'),
    ])),
]
