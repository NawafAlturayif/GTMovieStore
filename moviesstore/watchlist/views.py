from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Watchlist
from movies.models import Movie
from django.http import JsonResponse

@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, 'watchlist/watchlist.html', {'watchlist': watchlist})

@login_required
def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if not Watchlist.objects.filter(user=request.user, movie=movie).exists():
        Watchlist.objects.create(user=request.user, movie=movie)
    return redirect('watchlist:watchlist')

@login_required
def update_watchlist_rating(request, item_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        watchlist_item = get_object_or_404(Watchlist, pk=item_id, user=request.user)
        watchlist_item.rating = rating
        watchlist_item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def remove_from_watchlist(request, item_id):
    watchlist_item = get_object_or_404(Watchlist, pk=item_id, user=request.user)
    watchlist_item.delete()
    return redirect('watchlist:watchlist')