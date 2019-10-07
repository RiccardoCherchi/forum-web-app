from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Sezione(models.Model):
    """
    le sezione dividono il sito in categorie di discussione.
    ciascuna sezione contiene svariate Discussioni
    create dagli amministatori del sito
    """
    nome_sezione = models.CharField(max_length= 80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("sezione_view", kwargs={"pk": self.pk})

    def get_last_disussion(self):
        return Discussione.objects.filter(sezione_appartenenza=self).order_by("-data_creazione")[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione_appartenenza=self).count()

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

class Discussione(models.Model):
    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussioni", null=True)
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE, related_name="sezioni", null=True)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("discussione_view", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural = "Discussioni"

class Post(models.Model):
    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.autore_post.username
