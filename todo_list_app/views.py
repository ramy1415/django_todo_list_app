from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "todo_list/home_page.html")
