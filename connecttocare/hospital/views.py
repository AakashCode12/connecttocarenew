from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required


def index(request):
    return render(request,"index.html")

@permission_required('session.can_view_session')
def patient_dashboard(request):
    return render(request, "patients/index.html")
