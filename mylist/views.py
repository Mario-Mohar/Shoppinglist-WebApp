from django.shortcuts import render
from .models import shoppingItem

# Create your views here.
def mylist(request):
    if request.method == "POST":
        shoppingItem.objects.create(name = request.POST['name'])
    all_items = shoppingItem.objects.all()
    return render(request, "shoppinglist.html", {"all_items": all_items}) 