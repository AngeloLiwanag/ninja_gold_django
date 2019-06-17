from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    if (request.session.get('gold') == None):
        request.session['gold'] = 0

    if (request.session.get('activities_list') == None):
        request.session['activities_list'] = []
    
    if (request.session.get('dict') != None):
        dictionary = request.session['dict']
    
    return render(request,'ninja_app/index.html', dictionary)

def gold(request):
    if request.method == 'POST':
        if 'activities' in request.session:
            activities = request.session['activities']
        else:
            activities = ""
        
        if 'gold' in request.session:
            gold = request.session['gold']
        else:
            gold = 0
        
        income = 0
        activities = ""

        if request.POST['location'] == 'farm':
            income = random.randint(10,20)

        if request.POST['location'] == 'cave':
            income = random.randint(5,10)

        if request.POST['location'] == 'house':
            income = random.randint(2,5)

        if request.POST['location'] == 'casino':
            income = random.randint(-50,50)
        
        location = request.POST['location']
        if income < 0:
            activities = "Lost " + str(income) + " golds from the " + location 
            color = 'red'
        if income > 0:
            activities = "Gained " + str(income) + " golds from the " + location
            color = 'green'
        
        dictionary = {
            "class" : color,
            "activity" : activities
        }

        request.session['dict'] = dictionary
        print(dictionary)
        gold += income 
        request.session['gold'] = gold
        request.session['activities'] += activities
        request.session['activities_list'].append(activities)
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities_list']
    return redirect('/')
