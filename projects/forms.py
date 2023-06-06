from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
            "due_date",
        )
