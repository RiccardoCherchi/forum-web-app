from django import forms
from .models import Discussione, Post


class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "di cosa vuoi parlarci?"}),
        max_length=3000,
        label="Primo Messaggio")

    class Meta:
        model = Discussione
        field = ["titolo", "contentuo"]
        exclude = ['autore_discussione', 'sezione_appartenenza']
        widgets = {
           "titolo": forms.TextInput(attrs={"placeholder": "Titolo della Discussione"})}


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['contenuto']
        widgets = {
            "contenuto": forms.Textarea(attrs={'rows':'5'})
        }
        labels = {
            "contenuto": "Messaggio"
        }