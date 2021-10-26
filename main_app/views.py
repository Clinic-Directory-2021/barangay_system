from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests
import json

import pyrebase

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore

# import html to pdf converter
from django.template.loader import get_template
from xhtml2pdf import pisa

from io import BytesIO
from django.core.files import File


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

auth_pyrebase = firebase.auth()

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

            user = auth_pyrebase.sign_in_with_email_and_password(email, password)

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
    resident_id = request.GET.get('resident_id')

    resident = firestoreDB.collection('resident_list').document(resident_id).get()

    data = {
        'resident': resident.to_dict,
    }

    return render(request,'resident_profile.html', data)

def case_involved(request):
    return render(request,'case_involved.html')
    
def add_resident(request):
    return render(request,'add_resident.html')

def blotter_records(request):
    return render(request,'blotter_records.html')

def edit_blotter_records(request):
    return render(request,'edit_blotter_records.html')

def issue_certificate(request):
    residents = firestoreDB.collection('resident_list').get()

    resident_data = []

    for resident in residents:
        value = resident.to_dict()
        resident_data.append(value)
    
    data = {
        'resident_data': resident_data,
    }
    return render(request,'issue_certificate.html', data)
    
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
            user = auth_pyrebase.create_user_with_email_and_password(email, password)

            img_file_directory = user['localId']+"/resident_images/"+ fileName
        
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

def delete_resident(request):
    if request.method == 'GET':
        resident_id = request.GET.get('resident_id')
        img_directory = request.GET.get('img_directory')

        # auth.delete_user(resident_id)

        # firestoreDB.collection('resident_list').document(resident_id).delete()

        storage.delete(img_directory, None)

        return redirect('resident_record')      

def generate_indigent(request):
    if request.method == 'POST':
        
        purpose = request.POST.get('purpose')
        date = request.POST.get('date')
        indigent_full_name = request.POST.get('indigent_full_name')
        indigent_age = request.POST.get('indigent_age')
        indigent_resident_id = request.POST.get('indigent_resident_id')


        template_path = 'pdf_generated/indigency.html'

        context = {
            'purpose': purpose,
            'date': date, 
            'indigent_full_name': indigent_full_name,
            'indigent_age': indigent_age,
            }

        pdf_file_directory = indigent_resident_id + "/resident_indigent/indigent.pdf"


        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:


            storage.child(pdf_file_directory).put(result.getvalue())

            doc_ref = firestoreDB.collection('resident_list').document(indigent_resident_id)

            doc_ref.update({
                'indigent_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'indigent_pdf_directory' : pdf_file_directory,
                })

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

        # # Create a Django response object, and specify content_type as pdf
        # response = HttpResponse(content_type='application/pdf')

        # #eto naman pag didisplay lang
        # response['Content-Disposition'] = 'inline; filename="indigency.pdf"'


        # #code to kapag gusto mo idownload yung pdf 
        # # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        
        # # create a pdf
        # pisa_status = pisa.CreatePDF(
        #     html, dest=response)

        # # if error then show some funy view
        # if pisa_status.err:
        #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
        
        # return response