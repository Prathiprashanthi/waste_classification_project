"""
URL configuration for waste_clasification_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views
from userapp import views as userapp_views
from adminapp import views as adminapp_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #main
    path('',mainapp_views.home,name='home'),
    path('about-us',mainapp_views.about_us,name='about_us'),
    path('contact',mainapp_views.contact_us, name='contact_us'),
    path('user-login',mainapp_views.user_login,name='user_login'),
    path('admin-login',mainapp_views.admin_login,name='admin_login'),
    path('register',mainapp_views.register,name='register'),
    path('otp',mainapp_views.otp,name='otp'),
    path('forgot-pwd',mainapp_views.forgot_pwd,name='forgot_pwd'),
    #user
    path('user-dashboard',userapp_views.user_dashboard,name='user_dashboard'),
    path('user-predict',userapp_views.user_predict,name='user_predict'),
    path('user-profile',userapp_views.user_profile,name='user_profile'),
    path('user-feedback',userapp_views.user_feedback,name='user_feedback'),
    path('user-result',userapp_views.result,name='result'),
    path('user-logout',userapp_views.user_logout,name='user_logout'),
    #admin
    path('admin/', admin.site.urls),
    path('admin-dashboard',adminapp_views.admin_dashboard,name="admin_dashboard"),
    path('admin-pendingusers',adminapp_views.admin_pendingusers,name='admin_pendingusers'),
    path('admin-allusers',adminapp_views.admin_allusers,name='admin_allusers'),
    path('adminlogout',adminapp_views.adminlogout, name='adminlogout'),
    path('accept-user/<int:id>', adminapp_views.accept_user, name = 'accept_user'),
    path('reject-user/<int:id>', adminapp_views.reject_user, name = 'reject'),
    path('delete-user/<int:id>', adminapp_views.delete_user, name = 'delete_user'),
    path('uploaddataset',adminapp_views.uploaddataset,name='uploaddataset'),
    path('admin_traintest_model',adminapp_views.admin_traintest_model,name='admin_traintest_model'),
    path('admin_cnn_model',adminapp_views.admin_cnn_model,name='admin_cnn_model'),
    path('admin_traintest_btn',adminapp_views.admin_traintest_btn,name='admin_traintest_btn'),
    path('admin_graph',adminapp_views.admin_graph,name='admin_graph'),
    path('admin_cnn_btn',adminapp_views.admin_cnn_btn,name='admin_cnn_btn'),
    path('user_feedbacks',adminapp_views.user_feedbacks,name='user_feedbacks'),
    path('user_sentiment',adminapp_views.user_sentiment,name='user_sentiment'),
    path('user_graph',adminapp_views.user_graph,name='user_graph'),
    path('admin_dataset_btn',adminapp_views.admin_dataset_btn,name='admin_dataset_btn')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

