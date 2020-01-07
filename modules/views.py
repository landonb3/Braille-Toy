from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
def home_view(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        points = int(request.user.last_name)
        level = int(points / 100)
        remainder = int(points % 100)
        points_to_go = 100 - remainder
        if points_to_go == 1:
            ptg_text = str(points_to_go) + " point left until level " + str(level+1) + '!'
        else:
            ptg_text = str(points_to_go) + " points left until level " + str(level+1) + '!'
        return render(request, 'home.html', {'points': points,'level': level,'remainder': remainder, 'ptg': ptg_text, 'name': name})
    else:
        return redirect("/")

def level_select_view(request, id):
    if request.user.is_authenticated:
        name = request.user.first_name
        points = int(request.user.last_name)
        return render(request,'levelselect.html',{'points':points,'name':name,'game':id})
    else:
        return redirect("/")

def get_vocab_list(level):
    with open(r"modules\vocab lists\Level" + str(level) + ".txt") as file:
        data = file.read()
        return [x.strip().lower() for x in data.split(',')]

def clockrace_view(request,id):
    if request.user.is_authenticated:
        lst = get_vocab_list(id)
        name = request.user.first_name
        points = int(request.user.last_name)
        return render(request,'clockrace.html',{'points':points,'name':name})        
    else:
        return redirect("/")

def flashcards_view(request,id):
    if request.user.is_authenticated:
        if len(id) == 1:
            lst = get_vocab_list(id)
            user = User.objects.get(id = request.user.id)
            name = user.first_name
            points = int(user.last_name)
            print(user.last_name)
            word = random.choice(lst)
            length = len(word)
            if length < 6:
                fs = 140
            elif length < 8:
                fs = 100
            elif length < 10:
                fs = 85
            elif length < 12:
                fs = 65
            else:
                fs = 50
            return render(request,'flashcards.html',{'points':points,'name':name,'word':word, 'fs':fs,'id':id}) 
        else:
            points = int(id[1:])
            user = User.objects.get(id = request.user.id)
            user.last_name = str(int(user.last_name) + points)
            user.save()
            return redirect('/flashcards/' + id[0])
    else:
        return redirect("/")

def freeplay_view(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        points = int(request.user.last_name)
        return render(request,'freeplay.html',{'points':points,'name':name})        
    else:
        return redirect("/")

def spaceman_view(request,id):
    if request.user.is_authenticated:
        lst = get_vocab_list(id)
        name = request.user.first_name
        points = int(request.user.last_name)
        return render(request,'spaceman.html',{'points':points,'name':name})        
    else:
        return redirect("/")