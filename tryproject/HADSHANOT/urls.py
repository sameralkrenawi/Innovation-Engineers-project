from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views
#from ..tryproject import settings

urlpatterns=[
    path('',views.HomePage, name='homepage'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('SIGNUP',views.SIGNUP, name='SIGNUP'),
    path("LOGIN",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path('SignUpDone',views.SignUpDone,name='SignUpDone'),
    path('LoginStatus',views.LoginStatus,name='LoginStatus'),
    path('UserHomePage',views.UserHomePage,name='UserHomePage'),
    path('addDocument',views.addDocument,name='addDocument'),
    path('addFile',views.addFile,name='addFile'),
    path('findDocument',views.findDocument,name='findDocument'),
    path('showDocument',views.showDocument,name='showDocument'),
    path('findLast',views.findLast,name='findLast'),
    path('showLast',views.showLast,name='showLast'),
    path('getAllDocuments',views.getAllDocuments,name='getAllDocuments'),
    path('getLastDocuments',views.getLastDocuments,name='getLastDocuments'),
    path('SendMail',views.SendMail,name='SendMail'),
    path('sendEmail',views.sendEmail,name='sendEmail')
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)