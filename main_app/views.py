from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests
import json

import pyrebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  'apiKey': "AIzaSyADDBAM7_9VlZDRAGwyDeNne29tWPmcXb8",
  'authDomain': "barangay-system-2021-b00f3.firebaseapp.com",
  'projectId': "barangay-system-2021-b00f3",
  'databaseURL': "https://barangay-system-2021-b00f3-default-rtdb.firebaseio.com/",
  'storageBucket': "barangay-system-2021-b00f3.appspot.com",
  'messagingSenderId': "587251378360",
  'appId': "1:587251378360:web:a1081d0988c94817a3ec4d"
}

firebase = pyrebase.initialize_app(config)
cred = credentials.Certificate("main_app/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

auth = firebase.auth()

firestoreDB = firestore.client()

storage = firebase.storage()

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/homepage')
    else:
        return render(request,'index.html')

def login_validation(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')

            user = auth.sign_in_with_email_and_password(email, password)

            request.session['user_id'] = user['localId']

            return HttpResponse('Success!')
        except:
            return HttpResponse('Invalid Email or Password!')

def register(request):
    return render(request,'register.html')
def homepage(request):
    if 'user_id' in request.session:
        return render(request,'homepage.html')
    else:
        return redirect('/')

def list_of_official(request):
    return render(request,'list_of_official.html')
def manage_official(request):
    return render(request,'manage_official.html')

def resident_record(request):
    residents = firestoreDB.collection('resident_list').get()

    resident_data = []

    for resident in residents:
        value = resident.to_dict()
        resident_data.append(value)
    
    data = {
        'resident_data': resident_data,
    }

    return render(request,'resident_record.html', data)

def resident_profile(request):
    return render(request,'resident_profile.html')

def case_involved(request):
    return render(request,'case_involved.html')
    
def add_resident(request):
    return render(request,'add_resident.html')

def blotter_records(request):
    return render(request,'blotter_records.html')

def edit_blotter_records(request):
    return render(request,'edit_blotter_records.html')

def issue_certificate(request):
    return render(request,'issue_certificate.html')
    
def manage_certificate(request):
    return render(request,'manage_certificate.html')

def indigency(request):
    return render(request,'indigency.html')

def business(request):
    return render(request,'business.html')

def residency(request):
    return render(request,'residency.html')
    
def summary(request):
    return render(request,'summary.html')

def report(request):
    return render(request,'report.html')

def logout(request):
    try:
        del request.session['user_id']
    except:
        return redirect('/')
    return redirect('/')

def addResident(request):
    if request.method == 'POST':
        resident_image =  request.FILES['resident_image']
        fileName = request.POST.get('fileName')
        

        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        middle_name = request.POST.get('middle_name')
        street = request.POST.get('street')
        last_name = request.POST.get('last_name')
        purok = request.POST.get('purok')
        gender = request.POST.get('gender')
        citizenship = request.POST.get('citizenship')
        civil_status = request.POST.get('civil_status')
        diff_disabled = request.POST.get('diff_disabled')
        age = request.POST.get('age')
        relation = request.POST.get('relation')
        birthdate = request.POST.get('birthdate')
        religion = request.POST.get('religion')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('status')
        
        password = 'BARANGAYRESIDENT'+first_name+last_name

        try:
            #register email and password to firebase auth
            user = auth.create_user_with_email_and_password(email, password)

            img_file_directory = email+"/clinic_images/"+ fileName
        
            doc_ref = firestoreDB.collection('resident_list').document(user['localId'])

            doc_ref.set({
                'resident_id': doc_ref.id,
                'resident_img_url' : storage.child(img_file_directory).get_url(None),
                'resident_img_directory' : img_file_directory,
                'first_name': first_name,
                'email': email,
                'middle_name': middle_name,
                'street': street,
                'last_name': last_name,
                'purok': purok,
                'gender': gender,
                'citizenship': citizenship,
                'civil_status': civil_status,
                'diff_disabled': diff_disabled,
                'age': age,
                'relation': relation,
                'birthdate': birthdate,
                'religion': religion,
                'phone_number': phone_number,
                'status': status,
            })

            

            #upload product image
            storage.child(img_file_directory).put(resident_image)

            return HttpResponse('Success!')
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "EMAIL_EXISTS":
                return HttpResponse('Email Already Exists!')