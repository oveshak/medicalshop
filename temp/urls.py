from django.urls import path
from temp.views import Bariatric_Department, Blog, BlogDetails, Cancer_Department, Cardiologists_Department, Colorectal_Department, Contact, Doctor_Details, Doctor_Team, Gastroenterology_Department, Index, Neuroscience_Department, Orthopaedics_Department, Protfolio, Shop_Details, Shop_List, Spine_Department
urlpatterns = [
    path('',Index.as_view(),name='index'),
   path('doctorteam/',Doctor_Team.as_view(),name='doctor_team'),
   path('doctordetails/<slug>/',Doctor_Details.as_view(),name='doctor_details'),
   
   path('protfolio/',Protfolio.as_view(),name='protfolio'),
   path('blog/',Blog.as_view(),name='blog'),
   path('blogs/<slug>/',BlogDetails.as_view(),name='blog_details'),
   path('contact/',Contact.as_view(),name='contact'),
   

   path('cardiologists_department/',Cardiologists_Department.as_view(),name='cardiologists_dept'),
   path('orthopaedics_department/',Orthopaedics_Department.as_view(),name='orthopaedics_dept'),
   path('gastroenterology_department/',Gastroenterology_Department.as_view(),name='gastroenterology_dept'),
   path('neuroscience_department/',Neuroscience_Department.as_view(),name='neuroscience_dept'),
   path('spine_department/',Spine_Department.as_view(),name='spine_dept'),
   path('cancer_department/',Cancer_Department.as_view(),name='cancer_dept'),
   path('colorectal_department/',Colorectal_Department.as_view(),name='colorectal_dept'),
   path('bariatric_department/',Bariatric_Department.as_view(),name='bariatric_dept'),

   path('shop/',Shop_List.as_view(),name='shop'),
   path('shop_details/',Shop_Details.as_view(),name='shop_details'),
]