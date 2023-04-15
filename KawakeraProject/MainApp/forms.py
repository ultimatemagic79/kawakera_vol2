from django import forms
from .models import MainApp


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = MainApp
        fields = ("photo",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
