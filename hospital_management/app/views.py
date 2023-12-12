from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Doctor, Nurse, EPHI, Insurance, Patient

app_name = 'app'

# Doctor Views
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['first_name', 'last_name', 'specialty']

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['first_name', 'last_name', 'specialty']

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_confirm_delete.html'
    success_url = reverse_lazy('app:doctor_list')

# Nurse Views
class NurseListView(ListView):
    model = Nurse
    template_name = 'nurse_list.html'

class NurseDetailView(DetailView):
    model = Nurse
    template_name = 'nurse_detail.html'

class NurseCreateView(CreateView):
    model = Nurse
    template_name = 'nurse_form.html'
    fields = ['first_name', 'last_name']

class NurseUpdateView(UpdateView):
    model = Nurse
    template_name = 'nurse_form.html'
    fields = ['first_name', 'last_name']

class NurseDeleteView(DeleteView):
    model = Nurse
    template_name = 'nurse_confirm_delete.html'
    success_url = reverse_lazy('app:nurse_list')

# EPHI Views
class EPHIListView(ListView):
    model = EPHI
    template_name = 'ephi_list.html'

class EPHIDetailView(DetailView):
    model = EPHI
    template_name = 'ephi_detail.html'

class EPHICreateView(CreateView):
    model = EPHI
    template_name = 'ephi_form.html'
    fields = ['name', 'location']

class EPHIUpdateView(UpdateView):
    model = EPHI
    template_name = 'ephi_form.html'
    fields = ['name', 'location']

class EPHIDeleteView(DeleteView):
    model = EPHI
    template_name = 'ephi_confirm_delete.html'
    success_url = reverse_lazy('app:ephi_list')

# Insurance Views
class InsuranceListView(ListView):
    model = Insurance
    template_name = 'insurance_list.html'

class InsuranceDetailView(DetailView):
    model = Insurance
    template_name = 'insurance_detail.html'

class InsuranceCreateView(CreateView):
    model = Insurance
    template_name = 'insurance_form.html'
    fields = ['name', 'coverage_type']

class InsuranceUpdateView(UpdateView):
    model = Insurance
    template_name = 'insurance_form.html'
    fields = ['name', 'coverage_type']

class InsuranceDeleteView(DeleteView):
    model = Insurance
    template_name = 'insurance_confirm_delete.html'
    success_url = reverse_lazy('app:insurance_list')

#patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'address']

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'address']

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_confirm_delete.html'
    success_url = reverse_lazy('app:patient_list')