from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import manager_views, views,employee_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'), 

    #LOGIN PATH
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),

   #register path

    path('register',views.REGISTER,name='register'),

    #LOGOUT PATH
    path('dologout',views.doLogout,name='logout'),

    #PROFILE UPDATE
    path('profile',views.PROFILE,name='profile'),

    #MANAGER PATH
    path('manager/Home',manager_views.HOME,name='manager_home'),
    path('manager/addData',manager_views.addData, name='add_data'),
     path('manager/viewData',manager_views.viewData, name='view_data'),

 #resources path
    path('manager/resources',manager_views.RESOURCES,name='manager_resources'),

    #events path
    path('events',views.EVENTS,name='add_event'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
