from re import S
from tkinter.tix import Select
from django.http import HttpRequest
from django.shortcuts import redirect, render
from posts.models import Categoria, Comentario, Post

def index(request):
    i=0
    posts = Post.objects.all()
    while i < 3:
        posts2 = Post.objects.all().order_by('-fecha')[:3]
        i=i+1
    print (posts2)
    posts3 = Post.objects.all().order_by('-fecha')[:1]
    
    posts4 = Post.objects.all()

    categoria = Categoria.objects.all()[:1]
    
    return render(request, 'home.html', {
        'posts':posts,
        'posts2': posts2,
        'posts3': posts3,
        'posts4':posts4,
        'categoria':categoria
        })
    
def post(request, id):
    post = Post.objects.raw('SELECT posts_post.id,posts_post.titulo,posts_post.descripcion,posts_post.img,posts_post.contenido,posts_post.fecha,posts_autor.au_nombre,posts_autor.foto,posts_autor.descripcionAutor FROM `posts_post` JOIN posts_autor ON posts_post.f_autor = posts_autor.id WHERE posts_post.id = %s',str(id))
    comentario = Post.objects.raw('SELECT * FROM posts_comentario WHERE f_post_id = %s',str(id))
    
    if request.method == 'POST': 
        postC = Comentario(
            com_contenido = request.POST['contenido'],
            f_post_id = id
        )
        postC.save()

    return render(request, 'post.html', {
        'post':post,
        'comentario':comentario
        })

def categoria(request,nombre):
    categoria = Categoria.objects.raw("SELECT * FROM posts_categoria JOIN posts_post ON posts_post.f_categoria=posts_categoria.id WHERE ca_nombre LIKE '"+nombre+"'")
    

    return render(request, 'postCategoria.html', {
        #'categoria':categoria,
        })