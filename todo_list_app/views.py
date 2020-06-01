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


#Ajax edit todo item status
# Method GET --> /togglestatus
def toggle_status(request):
    item_id = request.GET.get('item_id')
    # getting the item
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        # if item was not found return error message
        return JsonResponse(status=404, data={'message':"Couldn't update"})
    else:
        item.is_done = not item.is_done
        item.save()
        return JsonResponse({'id': item.id ,'message':"updated item"})
            

