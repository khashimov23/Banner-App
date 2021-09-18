from django.urls import path
from .views import views
from .views import form_views as fv


urlpatterns=[
    path('', views.home, name='home'),

    path('owners/', views.owners, name='owners'),
    path('owner/<str:pk>/', views.owner_detail, name='owner_detail'),
    path('tadbirkors/', views.tadbirkor, name='tadbirkor'),
    path('tadbirkor/<str:pk>/', views.tadbirkor_detail, name='tadbirkor_detail'),
    
    path('orders/', views.order, name='orders'),
    path('joylar/', views.joylar, name='joylar'),
    path('joy/<str:pk>/', views.joy_detail, name='joy_detail'),

    #users
    path('owner-page/<int:pk>/', views.userPage, name='user_page'),
    
    # Register
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logOutUser, name='logout'),
    

    # CRUD
    path('create_order/', fv.createOrder, name='create_order'),
    path('update_order/<str:pk>/', fv.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', fv.deleteOrder, name='delete_order'),
    
    path('create_owner/', fv.createOwner, name='create_owner'),
    path('update_owner/<str:pk>/', fv.updateOwner, name='update_owner'),
    path('delete_owner/<str:pk>/', fv.deleteOwner, name='delete_owner'),

    path('create_tadbirkor/', fv.createTadbirkor, name='create_tadbirkor'),
    path('update_tadbirkor/<int:pk>/', fv.updateTadbirkor, name='update_tadbirkor'),
    path('delete_tadbirkor/<int:pk>/', fv.deleteTadbirkor, name='delete_tadbirkor'),

    path('create_place/', fv.createJoy, name='create_joy'),
    path('update_place/<int:pk>/', fv.updateJoy, name='update_joy'),
    path('delete_place/<int:pk>/', fv.deleteJoy, name='delete_joy'),
]
