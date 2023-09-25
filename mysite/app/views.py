from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request,id):
    ls = ToDoList.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c"+str(item.id)) == "clicked":
                    print(request.POST.get("c"+str(item.id), " clicked"))
                    item.complete = True
                else:
                    print(request.POST.get("c"+str(item.id), " unclicked"))
                    item.complete = False
                t = request.POST.get("t"+str(item.id))
                item.text = t
                item.save()
            return redirect('/view')

        elif request.POST.get('newItem'):
            print(request.POST)
            txt = request.POST.get("new")

            if len(txt)> 2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")

    return render(request, 'app/list.html', {"ls":ls})

def home(request):
    return render(request, 'app/home.html', {})

@login_required(login_url='/login')
def create(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            # t = request.user.todolist_set.create(name=n)

            t = ToDoList(name=n,user=request.user)
            t.save()
            return HttpResponseRedirect("/view/%i" %t.id)
    else:
        form = CreateNewList()
    return render(request, 'app/create.html',{"form":form})

@login_required(login_url='/login')
def delete_to_do(request,id):
    to_do = ToDoList.objects.get(id=id)
    to_do.delete()
    return redirect('/view')

# def delete_item(request,id):
#     item = Item.objects.get(id=id)
#     to_do = ToDoList.objects.get(item=item)
#     item.delete()
#     return redirect("/view/"+str(to_do.id))

@csrf_exempt
@login_required(login_url='/login')
@require_http_methods(["POST"])
def delete_item(request):

    id = request.POST.get('id')
    print("ID------->",id)
    try:
        item = Item.objects.get(id=id)
        item.delete()
        return JsonResponse({'success': True})
    except Item.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item does not exist'})


@login_required(login_url='/login')
def lists(request):
    my_lists = ToDoList.objects.filter(user=request.user)
    return render(request, 'app/view.html',{"lists":my_lists})
