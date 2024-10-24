from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('homepage/',views.index,name='index'),
    path('homepage/signup',views.signup,name='signup'),
    path('homepage/login',views.login,name='login'),
    path('homepage/',views.index,name='logout'),
    path('homepage/aboutus',views.aboutus,name='aboutus'),


    #Student
    path('homepage/student_page',views.student_page,name='student_page'),
    path('homepage/student_page/view_history',views.view_history,name='view_history'),
    path('homepage/view_campaign/<str:campaignid>',views.view_campaign,name='view_campaign'),
    path('homepage/view_campaign/donation/<str:campaignid>',views.donation,name='donation'),
    path('homepage/view_campaign/donation/save_donation/<str:campaignid>', views.save_donation, name='save_donation'),
    path('homepage/view_campaign/donation/save_donation/<str:campaignid>/receipt', views.receipt, name='receipt'),

    
    
    #Staff
    path('homepage/staff_page',views.staff_page,name='staff_page'),
    path('homepage/staff_page/view_list_student',views.view_list_student,name='view_list_student'),
    path('homepage/staff_page/update_student/<str:studentid>',views.update_student,name='update_student'),
    path('homepage/staff_page/update_student/save_update_student/<str:studentid>',views.save_update_student,name='save_update_student'),
    path('homepage/staff_page/delete_student/<str:studentid>',views.delete_student,name='delete_student'),
    path('homepage/staff_page/manage_campaign',views.manage_campaign,name='manage_campaign'),
    path('homepage/staff_page/update_campaign/<str:campaignid>',views.update_campaign,name='update_campaign'),
    path('homepage/staff_page/update_campaign/save_update_campaign/<str:campaignid>',views.save_update_campaign,name='save_update_campaign'),
    path('homepage/staff_page/delete_campaign/<str:campaignid>',views.delete_campaign,name='delete_campaign'),
    

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)