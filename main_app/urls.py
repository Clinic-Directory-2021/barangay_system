"""barangay_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('homepage/', views.homepage, name="homepage"),
    path('list_of_official/', views.list_of_official, name="list_of_official"),
    path('manage_official/', views.manage_official, name="manage_official"),
    path('resident_record/', views.resident_record, name="resident_record"),
    path('resident_profile/', views.resident_profile, name="resident_profile"),
    path('case_involved/', views.case_involved, name="case_involved"),
    path('add_resident/', views.add_resident, name="add_resident"),
    path('blotter_records/', views.blotter_records, name="blotter_records"),
    path('edit_blotter_records/', views.edit_blotter_records, name="edit_blotter_records"),
    path('issue_certificate/', views.issue_certificate, name="issue_certificate"),
    path('manage_certificate/', views.manage_certificate, name="manage_certificate"),
    path('indegency', views.indigency, name="indigency"),
    path('business/', views.business, name="business"),
    path('residency/', views.residency, name="residency"),
    path('summary/', views.summary, name="summary"),
    path('report/', views.report, name="report"),
    path('login_validation/', views.login_validation, name="login_validation"),
    path('logout/', views.logout, name="logout"),
    path('addResident/', views.addResident, name="addResident"),

    path('delete_resident/', views.delete_resident, name="delete_resident"),
    
    #render_pdf files
    path('generate_indigent/', views.generate_indigent, name="generate_indigent"),
    path('generate_clearance/', views.generate_clearance, name="generate_clearance"),
    path('generate_building/', views.generate_building, name="generate_building"),
    path('generate_residency/', views.generate_residency, name="generate_residency"),
    path('generate_wiring/', views.generate_wiring, name="generate_wiring"),
    path('generate_excavation/', views.generate_excavation, name="generate_excavation"),
    path('generate_fencing/', views.generate_fencing, name="generate_fencing"),
    path('generate_water/', views.generate_water, name="generate_water"),
]
