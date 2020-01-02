"""Projectcollege URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from college.views import home_view, student_details_view, student_create_view, register_view, login_view, logout_view, loggedin_home, student_detail_display_view, render_initial_data, student_delete_view,admin_home_view, student_details_delete_view, student_details_edit_view, student_view_details
urlpatterns = [
   
	path('student/', student_details_view, name="student_details"),
    path('studen/<int:my_id>/', student_detail_display_view, name='student-details-display-id'),
    path('', home_view),
    path('admin/', admin.site.urls),
 	path('create/', student_create_view),   
 	path('register/', register_view, name="register"),
 	path('login/', login_view, name="login"),
 	path('logout/', logout_view, name="Logout"),
 	path('home/', loggedin_home ,name='home'),
    path('student_edit/<int:my_id>/', render_initial_data, name='student-edit-id'),
    path('student_details_delete/<int:my_id>/', student_delete_view, name='student-details-delete-id'),
    path('student_details_delete/', student_details_delete_view, name="student_details_delete_view" ),
    path('student_edit/', student_details_edit_view, name="student_details_edit_view"),
    path("admin_home/", admin_home_view, name="admin_home_view"),
    path("student_view_details/", student_view_details, name="student_view_details")
]


