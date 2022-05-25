from django.shortcuts import render
import json
from datetime import datetime
from .models import Game

def game_view(request):
    return render(request, 'game.html')

def game_statistics(request):
    
    if request.method == 'POST':
        game = Game()
        data = request.body.decode('utf-8')
        date = json.loads(data)
        game.duration = date['duration']
        # game.duration = datetime.fromtimestamp(date['duration'])
        game.guessing_time = datetime.fromtimestamp(date['guessing_time'])
        game.moves_number = date['moves_number']
        game.save()
    game = Game.objects.all()
    context = {
            'game': game
        }
    return render(request, 'statistics.html', context)