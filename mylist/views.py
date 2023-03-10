from django.shortcuts import render
from .models import shoppingItem

# Create your views here.
def mylist(request):
    if request.method == "POST":
        shoppingItem.objects.create(name = request.POST['name'])
    all_items = shoppingItem.objects.all()
    return render(request, "shoppinglist.html", {"all_items": all_items}) 

def delete_item(request, item_name):
    try:
        item = shoppingItem.objects.get(name=item_name)
        item.delete()
    except shoppingItem.DoesNotExist:
        return HttpResponse(f'Item with name {item_name} not found', status=404)
    return HttpResponse(f'Item with name {item_name} deleted successfully')