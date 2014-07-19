# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from projeto.animais.forms import AnimalForm
from projeto.animais.models import Animal
#comment


def home(request):
    return render(request,'animais/home.html')

def animals(request):
    animals = Animal.objects.all()
    return render(request,'animais/animals.html',{'animals':animals})


def animal_edit(request,id): 
    '''
        @animal_edit: View para determinar se é um GET ou POST para editar um animal
    '''
    animal = get_object_or_404(Animal,id=id)
    if request.method == 'POST':
        return edit_animal(request,animal)
    else:
        return request_animal(request,animal)

#not tested ( be careful if need refactor)
def edit_animal(request,animal):
    '''
        @edit_animal: View para alterar os dados de um animal
    '''    
    form = AnimalForm(request.POST,instance=animal)
    if form.is_valid():
        animal = form.save(commit=False)
        animal.save()
        return HttpResponseRedirect(animal.detail())
    else:
        return render(request,'animais/animal_edit.html',{'form':form})

def request_animal(request,animal):
    '''
        @request_animal: View para obter os dados de um determinado animal
    '''    
    form = AnimalForm(instance=animal)
    return render(request, 'animais/animal_edit.html', {'form': form,'animal':animal})

def animal_detail(request,id):
    '''
        @animal_detail: View para exibir os detalhes de um determinado animal
    '''
    animal = get_object_or_404(Animal,id=id)
    return render(request,'animais/animal_detail.html',
        {'animal':animal}
        )

def animal_create(request):
    if request.method == 'POST':        
        return create_animal(request)
    else:
        return new_animal(request)

def new_animal(request):
    return render(request, 'animais/animal_form.html',
        {'form': AnimalForm()})

def create_animal(request):
    form = AnimalForm(request.POST)
    if not form.is_valid():
        return render(request, 'animais/animal_form.html',
            {'form': form})
    obj = form.save()
    obj.save()
    return HttpResponseRedirect(obj.detail())
