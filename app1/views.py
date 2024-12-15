from django.shortcuts import render
from .models import Developer ,Game

# Create your views here.


def home(request):
    return render(request, 'app1/home.html')

def list(request):
    game = Game.objects.all()  
    return render(request, 'app1/list.html', {'game':game})

def insert_data():
    developer1 = Developer.objects.create(name="Epic Games")
    developer2 = Developer.objects.create(name="Valve")
    developer3 = Developer.objects.create(name="CD Projekt Red")
    developer4 = Developer.objects.create(name="Ubisoft")
    developer5 = Developer.objects.create(name="Rockstar Games")

    Game.objects.create(title="Fortnite", developer=developer1)
    Game.objects.create(title="Half-Life", developer=developer2)
    Game.objects.create(title="The Witcher 3", developer=developer3)
    Game.objects.create(title="Assassin's Creed", developer=developer4)
    Game.objects.create(title="Grand Theft Auto V", developer=developer5)
    Game.objects.create(title="Cyberpunk 2077", developer=developer3)
    Game.objects.create(title="Far Cry", developer=developer4)
    Game.objects.create(title="Red Dead Redemption 2", developer=developer5)
    Game.objects.create(title="Portal", developer=developer2)
    Game.objects.create(title="Unreal Tournament", developer=developer1)
