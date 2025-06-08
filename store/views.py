from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render

from store.forms import StoreForm
from store.models import store
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here
@login_required
def index(request):
    lib_objs=store.objects.all()
    return render(request, "store/index.html",{'lib_objs':lib_objs})
def details(request,id):
    lib_obj=store.objects.get(id=id)
    return render(request,"store/details.html",{'lib_obj':lib_obj})
def add_book(request):
    if request.method=="POST":
        form=StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:                                                                                             
        form=StoreForm()
    return render(request,"store/add_book.html",{'form':form})
def success(request):
    return render(request, "store/success.html")
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'store/register.html',{'form':form})
def updateData(request,id):
    d=store.objects.get(id=id)
    if request.method=="POST":
        book_id=request.POST.get("book_id")
        title=request.POST.get("title")
        author=request.POST.get("author")
        publisher=request.POST.get("publisher")
        category=request.POST.get("category")
        year_of_pub=request.POST.get("year_of_pub")
        Total_copies=request.POST.get("Total_copies")
        available_copies=request.POST.get("available_copies")
        shelf_location=request.POST.get("shelf_location")
        d1=store.objects.get(id=id)
        d1.book_id=book_id
        d1.title=title
        d1.author=author
        d1.publisher=publisher
        d1.category=category
        d1.year_of_pub=year_of_pub
        d1.Total_copies=Total_copies
        d1.available_copies=available_copies
        d1.shelf_location=shelf_location
        d1.save()
        return redirect('details',id=d.id)
    return render(request,'store/edit.html',{'d':d})
def deleteData(request,id):
    d=store.objects.get(id=id)
    d.delete()
    return redirect("/")