from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.watchlist, name='watchlist'),
    path('add/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('update/<int:item_id>/', views.update_watchlist_rating, name='update_watchlist_rating'),
    path('remove/<int:item_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]