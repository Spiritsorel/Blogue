from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentaires')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Commentaire de {self.auteur} sur {self.publication}'