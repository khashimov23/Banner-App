from django.urls import path
from .views import views
from .views import form_views as fv
from .views import register_views as rv


urlpatterns=[
    path('', views.home, name='home'),

    path('places/', views.place, name='place'),
    path('place/<str:pk>/', views.place_detail, name='place_detail'),
    path('tadbirkors/', views.tadbirkor, name='tadbirkor'),
    path('orders/', views.order, name='orders'),
    path('tadbirkor/<str:pk>/', views.tadbirkor_detail, name='tadbirkor_detail'),
    path('joylar/', views.joylar, name='joylar'),
    path('joy/<str:pk>/', views.joy_detail, name='joy_detail'),
    
    # Register
    path('register/', rv.registerPage, name='register'),
    path('login/', rv.loginPage, name='login'),
    path('logout/', rv.logOutUser, name='logout'),
    

    # CRUD
    path('create_order/', fv.createOrder, name='create_order'),
    path('update_order/<str:pk>/', fv.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', fv.deleteOrder, name='delete_order'),

    path('create_owner/', fv.createOwner, name='create_owner'),
    path('update_owner/<str:pk>/', fv.updateOwner, name='update_owner'),
    path('delete_owner/<str:pk>/', fv.deleteOwner, name='delete_owner'),

    path('create_tadbirkor/', fv.createTadbirkor, name='create_tadbirkor'),
    path('update_tadbirkor/<str:pk>/', fv.updateTadbirkor, name='update_tadbirkor'),
    path('delete_tadbirkor/<str:pk>/', fv.deleteTadbirkor, name='delete_tadbirkor'),

    path('create_place/', fv.createJoy, name='create_joy'),
    path('update_place/<str:pk>/', fv.updateJoy, name='update_joy'),
    path('delete_place/<str:pk>/', fv.deleteJoy, name='delete_joy'),
]
