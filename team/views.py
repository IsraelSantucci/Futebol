from django.shortcuts import render,redirect
from .models import Team
from django.views.decorators.csrf import csrf_protect
import datetime

def getCODE():
    from datetime import datetime
    dataHora = datetime.now()
    code = str(dataHora.year)
    code += str(dataHora.month)
    code += str(dataHora.day)
    code += str(dataHora.minute)
    code += str(dataHora.second)
    code = str(int(round(int(code)/2, 0)))
    return code


def teams(request):
    title = "Cadastro de Times"
    teams = Team.objects.all()
    return render(request,'teams.html',{'title':title, 'teams': teams})

def new(request):
    title = "Inserção de Times"
    return render(request,'newTeam.html')

@csrf_protect
def saveNew(request):
    code = getCODE()
    name = request.POST.get('name')
    country = request.POST.get('country')
    dateFounded = request.POST.get('dateFounded')
    
    objTeam = Team(
        code=code,
        name=name,
        country=country,
        dateFounded=dateFounded
    )
    
    objTeam.save()
    
    return redirect('/time')

def delete(request, code):
    
    title = 'Exclusão de Times'
    team = Team.objects.get(code=code)
    print(team.dateFounded)
    return render(request, 'deleteTeam.html', {'title': title, 'team': team})

def saveDelete(request):
    code = request.POST.get('code')
    
    objTeam = Team.objects.get(code=code)
    
    objTeam.delete()
    
    return redirect('/time')

def edit(request, code):
    
    title = 'Edição de times'
    
    team = Team.objects.get(code=code)
    
    return render(request, 'editTeam.html',{'title': title, 'team': team})

def saveEdit(request):
    
    code = request.POST.get('code')
    name = request.POST.get('name')
    country = request.POST.get('country')
    
    dateFounded = request.POST.get('dateFounded')
    
    Team.objects.filter(code=code).update(
        name = name,
        country = country,
        dateFounded = dateFounded
    )
    
    return redirect('/time')
