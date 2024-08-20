from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
from posts.models import Post

# Create your views here.
def publication_detail(request, pk):
    publication = get_object_or_404(Post, pk=pk)
    commentaires = publication.commentaires.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.publication = publication
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('publication_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'posts/publication_detail.html', {
        'publication': publication,
        'commentaires': commentaires,
        'form': form,
    })