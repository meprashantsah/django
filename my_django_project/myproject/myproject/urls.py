"""
URL configuration for myproject project.

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
from django.urls import path,include

# from app1.views import CurrentDateTime

# from app2.views import offsetCurrentDateTime

from listapp.views import show_fruits_and_students

from InheritLayout.views import show_homepage
from InheritLayout.views import show_aboutus
from InheritLayout.views import show_contactus

# from studcourseenrollapp.views import register,course_search


# from prog8.views import addProject

from modelForm.views import addProject

from genericClassView.views import StudentListView
from genericClassView.views import StudentDetailView

from uper.views import CustomerDetailView,CustomerListView,addCustomer,gen_pdf,gen_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    # app1
    # path('currdt',CurrentDateTime),
    # # app2
    # path('offsetdt',offsetCurrentDateTime),
    # listapp
    path('showfs',show_fruits_and_students),
    # InheritLayout
    path('home/',show_homepage),
    path('aboutus/',show_aboutus),
    path('contactus/',show_contactus),
    # studcourseenrollapp
    # path('register',register),
    # path('search',course_search),

    # path('',include('searchform.urls')),
    # path('',include('feedbackform.urls'))

    # prog8
    # path('prog8/register',addProject)

    # modelForm
    path('add/',addProject),

    # genericClassView
    path('list/',StudentListView.as_view()),
    path('details/<pk>/',StudentDetailView.as_view(),name='stud_details'),

    # uper
    path('list1/',CustomerListView.as_view()),
    path('list1/details1/<pk>/',CustomerDetailView.as_view()),
    path('add1',addCustomer),
    path('pdf',gen_pdf),
    path('csv',gen_csv)
]
