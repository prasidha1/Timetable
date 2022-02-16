from student.models import Activity,Program, Centre, Professor
from django import forms
from multiselectfield import MultiSelectField

class ProgramForm(forms.ModelForm):
    
    class Meta:
        model = Program
        fields = "__all__"

class CentreForm(forms.ModelForm):
    
    class Meta:
        model = Centre
        fields = "__all__"

class ProfessorForm(forms.ModelForm):
    
    class Meta:
        model = Professor
        fields = "__all__"
        
class ActivityForm(forms.ModelForm):
    
    class Meta:
        model = Activity
        fields = "__all__"
        widgets = {"start_time": forms.TimeInput(attrs={'type': 'time'}), "end_time":forms.TimeInput(attrs={'type': 'time'})}