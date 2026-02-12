
from django.shortcuts import get_object_or_404, render, redirect
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegisterForm

def home(request):
    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request,'home.html',{'data':data})
    else:
        return render(request,'home.html')
    
def insert(request):
    if request.method=='POST':
        form=MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Data inserted successfully.')
                return redirect('Home')
            except:
                pass
    else:
        form=MyRegisterForm()
        return render(request,'register.html',{'form':form})


def update(request, id):
    data = get_object_or_404(RegisterForm, id=id)

    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.age = int(request.POST.get('age'))
        data.address = request.POST.get('address')
        data.contact = request.POST.get('contact')
        data.email = request.POST.get('email')

        data.save()
        messages.success(request, 'Data updated successfully.')

        return redirect('Home')

    return render(request, 'update.html', {'data': data})

def delete(request, id):
    data = get_object_or_404(RegisterForm, id=id)
    data.delete()
    messages.error(request, 'Data deleted successfully.')
    return redirect('Home')



