from django.shortcuts import render , redirect

# Create your views here.
from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    items = TodoItem.objects.all()
    form = TodoItemForm()
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todoapp/index.html', {'items': items, 'form': form})

def delete_item(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')
