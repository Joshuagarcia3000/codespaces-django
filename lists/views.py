from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import List, Item
from .forms import ListForm, ItemForm

#@login_required
#def create_list(request):
#    if request.method == 'POST':
#        form = ListForm(request.POST)
#        if form.is_valid():
#            list = form.save(commit=False)
#            list.created_by = request.user
#            list.save()
#            return redirect('list_detail', list_id=list.id)
#    else:
#        form = ListForm()
#    return render(request, 'create_list.html', {'form': form})

# List all available lists 
def list_lists(request):
    lists = List.objects.all()
    return render(request, 'lists/list_lists.html', {'lists': lists})

def list_detail(request, list_id):
    list = get_object_or_404(List, id=list_id)
    items = list.items.all()
    return render(request, 'lists/list_detail.html', {'list': list, 'items': items})

@login_required
def add_item(request, list_id):
    list = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list = list
            item.created_by = request.user
            item.save()
            return redirect('list_detail', list_id=list.id)
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form, 'list': list})

@login_required
def vote_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.votes.upvote(request.user)
    return redirect('list_detail', list_id=item.list.id)

