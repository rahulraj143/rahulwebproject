from django.shortcuts import render, redirect
from .models import webapps
from .forms import MovieForm
def index(request):
  webss=webapps.objects.all()
  content={
    "mys":webss
  }
  return render(request,"index.html",content)
def detail(request,web_id):
  movie=webapps.objects.get(id=web_id)
  return render(request,"detail.html",{"mo":movie})
def addmovie(request):
  if request.method == 'POST':
    name=request.POST.get('name')
    desc = request.POST.get('desc')
    year = request.POST.get('year')
    img = request.FILES['img']
    movi=webapps(name=name,desc=desc,year=year,img=img)
    movi.save()
  return render(request,"add.html")
def update(request,id):
    movie = webapps.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"up.html" ,{"form":form ,"movie":movie})
def delete(request,id):
    if request.method=="POST":
        movie=webapps.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
