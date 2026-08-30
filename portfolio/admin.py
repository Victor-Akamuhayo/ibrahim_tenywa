from django import forms
from django.contrib import admin

from .models import Certificate, Education, Experience, Profile, Project, Skill


MAX_UPLOAD_SIZE = 4 * 1024 * 1024


def validate_upload_size(file):
    if file and file.size > MAX_UPLOAD_SIZE:
        raise forms.ValidationError(
            'Please upload an image smaller than 4 MB for Vercel/Cloudinary.'
        )


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_profile_photo(self):
        file = self.cleaned_data.get('profile_photo')
        validate_upload_size(file)
        return file


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean_project_image(self):
        file = self.cleaned_data.get('project_image')
        validate_upload_size(file)
        return file


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'qualification',
        'institution',
        'location',
        'start_date',
        'end_date',
        'is_current',
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = (
        'name',
        'title',
        'current_position',
        'years_of_experience',
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'issuing_organization',
        'issue_date',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = (
        'title',
        'location',
        'client',
        'role',
        'project_date',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company',
        'location',
        'start_date',
        'end_date',
        'is_current',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'proficiency',
    )