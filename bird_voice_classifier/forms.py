from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={"name": "bird-sound"}), required=True,)

