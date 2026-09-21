from django.forms import *

from main.models import Education, Project, Experience

class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = [
            "school",
            "degree",
            "description",
            "started_at",
            "ended_at",
        ]

        labels = {
            "school": "Sekolah / Universitas",
            "degree": "Jenjang / Gelar",
            "description": "Deskripsi",
            "started_at": "Tahun Mulai",
            "ended_at": "Tahun Selesai",
        }

        widgets = {
            "school": TextInput(),
            "degree": TextInput(),
            "started_at": TextInput(),
            "ended_at": TextInput(),
        }
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
class ExperienceForm(ModelForm):
    is_ongoing = TypedChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        coerce=lambda val: val == 'True',
        widget=RadioSelect(attrs={'class': 'form-radio-input'}),
        label="On-going"
    )
    class Meta:
        model = Experience
        fields = [
            "title", 
            "description",
            "category", 
            "thumbnail", 
            "started_at", 
            "ended_at", 
            "is_ongoing"
        ]
        labels = {
            "title":"Nama Experience", 
            "description":"Deskripsi Experience",
            "category":"Category experience", 
            "thumbnail":"URL Thumbnail", 
            "started_at":"Waktu dimulai", 
            "ended_at":"Waktu berakhir", 
        }
        widgets = {
            "title": TextInput(), 
            "description":Textarea(),
            "category": Select(attrs={'class': 'project-search__input'}),
            "thumbnail":URLInput(), 
            "started_at": DateInput(attrs={'class': 'project-search__input', 'type': 'date'}),
            "ended_at": DateInput(attrs={'class': 'project-search__input', 'type': 'date'}),
            
            
        }