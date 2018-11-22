from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='all_goods'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add/', add_good, name='add_good'),
    path('<good_id>/sold/', sold, name='sold'),
    path('<good_id>/edit/', edit_good, name='edit_good'),
    path('<good_id>/delete/', delete_good, name='delete_good'),
    path('<good_id>/coming/', good_is_coming, name='good_is_coming'),

]
