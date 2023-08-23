from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    form = TodoForm()
    todos = Todo.objects.all()

    return render(request, 'myapp/index.html', {"form": form, "todos": todos})


@csrf_exempt
def saveData(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todoid = request.POST['todoid']
            title = request.POST['title']
            details = request.POST['details']

            if todoid == '':
                todo = Todo(title=title, details=details, user=request.user)
            else:
                todo = Todo(id=todoid, title=title, details=details, user=request.user)
            
            todo.save()
            todos = Todo.objects.values()
            todo_data = list(todos)

            return JsonResponse({'status': 'Save', 'todo_data': todo_data})
        
        else:
            return JsonResponse({'status': 0})
        

@csrf_exempt
def deleteData(request):
    if request.method == 'POST':
        id = request.POST['sid']
        pi = Todo.objects.get(id=id)
        pi.delete()

        return JsonResponse({'status': 1})

    else:
        return JsonResponse({'status': 1})
    

@csrf_exempt
def editData(request):
    if request.method == 'POST':
        id = request.POST['sid']
        title = request.POST['title']
        details = request.POST['details']

        edit_todo = Todo.objects.get(id=id)

        edit_todo.title = title
        edit_todo.details = details
        edit_todo.save()

        todo = Todo.objects.get(id=id)

        return JsonResponse({'status': 'Save', 'todo_data': "todo"})
        
    
    else:
        id = request.GET['sid']
        todo = Todo.objects.get(pk=id)
        todo_data = {"id": todo.id, "title": todo.title, "details": todo.details}

        return JsonResponse(todo_data)
