from types import SimpleNamespace

from django.db.utils import OperationalError
from django.shortcuts import render

from .models import Certificate, Education, Experience, Profile, Project, Skill


def _fallback_profile():
    return SimpleNamespace(
        title='Mining Engineer',
        name='Eng. Tenywa Ibrahim',
        bio='Professional portfolio and project showcase.',
        profile_photo=None,
        cv=None,
        current_position='',
        years_of_experience=0,
        location='',
        email='',
        phone='',
        linkedin='',
    )


def home(request):
    try:
        profile = Profile.objects.first() or _fallback_profile()
        certificates = Certificate.objects.all()
        experiences = Experience.objects.all()
        education = Education.objects.all()
        projects = Project.objects.all()
        skills = Skill.objects.all()
    except OperationalError:
        profile = _fallback_profile()
        certificates = []
        experiences = []
        education = []
        projects = []
        skills = []

    context = {
        'profile': profile,
        'certificates': certificates,
        'experiences': experiences,
        'education': education,
        'projects': projects,
        'skills': skills,
        'fallback_profile_photo_url': '/static/portfolio/images/hero.jpeg',
    }

    return render(request, 'portfolio/home.html', context)
