from re import template
from django.shortcuts import render
from . models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.


def accept(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        linkedin = request.POST.get("linkedin", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        class10 = request.POST.get("class10", "")
        class12 = request.POST.get("class12", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        projects = request.POST.get("projects", "")
        skills = request.POST.get("skills", "")
        profile = Profile(name=name, email=email, phone=phone,linkedin=linkedin, summary=summary, degree=degree,
                          class10=class10,class12=class12, university=university, previous_work=previous_work, skills=skills,projects=projects)
        profile.save()
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {'page-size': 'Letter', 'encoding': 'UTF-8'}
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
