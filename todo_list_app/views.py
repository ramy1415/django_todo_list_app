from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def home_page(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, "todo_list/home_page.html",context)

#Ajax add new todo item
# Method POST --> /additem
def add_todo_item(request):
    descrition = request.POST.get('description')
    if request.method == 'POST':
        if descrition:
            new_item = Item(description = descrition )
            new_item.save()
            #if item was saved return a response with the item id
            if new_item.id:
                return JsonResponse({'id': new_item.id ,'message':"Added new item"})

            return JsonResponse(status=500, data={'message':"Couldn't add"})
