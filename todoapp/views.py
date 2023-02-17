from django.shortcuts import render,HttpResponse
from.forms import CreationForm,UpdateForm
from django .http import JsonResponse
from .models import CreateModel
# Create your views here.
def create(request):
    if request.method=='POST':
        fm=CreationForm(request.POST)
        if fm.is_valid():
            fm.save()
        
    else:
        fm=CreationForm()
    return render(request,'todoapp/create.html',{"form":fm})

def read_data(request):
    data=CreateModel.objects.values()
    print(data)
    
    return JsonResponse(list(data),safe=False)

# def update_data(request):
        
  
#         if request.method=='POST':
#             fm=UpdateForm(request.POST,instance=request.user)
#             if fm.is_valid():
#                 fm.save()
#         else:
#             fm=UpdateForm(instance=request.user) 
#         return render(request,'todoapp/update.html',{"name":request.user,"form":fm})  
# 

def update_data(request, id):
    fm = UpdateForm(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            tittle=fm.cleaned_data['tittle']
            content=fm.cleaned_data['content']
            completed=fm.cleaned_data['completed']
            
            reg = CreateModel(id=id,content=content,tittle=tittle,completed=completed)
            reg.save()
            return HttpResponse(' Data  Updated !!!...')
        else:
            return HttpResponse(' Enter Valid Id')
    return render(request, 'todoapp/update.html', {'form': fm})
       