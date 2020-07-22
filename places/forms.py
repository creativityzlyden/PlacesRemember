from django.forms import ModelForm
from .models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'What\'s on your mind?'})


