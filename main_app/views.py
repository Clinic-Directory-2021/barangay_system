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
    list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_clearance').get()

    issued_certificate = []

    for certificate in list_of_issued_certificate:
        value = certificate.to_dict()
        issued_certificate.append(value)
    
    data = {
        'certificates': issued_certificate,
    }
    return render(request,'manage_certificate.html', data)

def indigency(request):
    list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_indigent').get()

    issued_certificate = []

    for certificate in list_of_issued_certificate:
        value = certificate.to_dict()
        issued_certificate.append(value)
    
    data = {
        'certificates': issued_certificate,
    }
    return render(request,'indigency.html', data)

def business(request):
    list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_building').get()

    issued_certificate = []

    for certificate in list_of_issued_certificate:
        value = certificate.to_dict()
        issued_certificate.append(value)
    
    data = {
        'certificates': issued_certificate,
    }
    return render(request,'business.html', data)

def residency(request):
    list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_residency').get()

    issued_certificate = []

    for certificate in list_of_issued_certificate:
        value = certificate.to_dict()
        issued_certificate.append(value)
    
    data = {
        'certificates': issued_certificate,
    }
    return render(request,'residency.html', data)
    
def summary(request):
    list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_wiring').get()

    issued_certificate = []

    for certificate in list_of_issued_certificate:
        value = certificate.to_dict()
        issued_certificate.append(value)
    
    data = {
        'certificates': issued_certificate,
    }
    return render(request,'summary.html', data)

def report(request):
    residents = firestoreDB.collection('resident_list').get()

    building_permits = firestoreDB.collection('list_of_issued_certificate_building').get()
    clearances = firestoreDB.collection('list_of_issued_certificate_clearance').get()
    excavation_clearance = firestoreDB.collection('list_of_issued_certificate_excavation').get()
    fencing_clearance = firestoreDB.collection('list_of_issued_certificate_fencing').get()
    indigency = firestoreDB.collection('list_of_issued_certificate_indigent').get()
    residency = firestoreDB.collection('list_of_issued_certificate_residency').get()
    water_installation = firestoreDB.collection('list_of_issued_certificate_water').get()
    wiring_permit = firestoreDB.collection('list_of_issued_certificate_wiring').get()

    total_residents = 0
    total_certificates = 0

    for resident in residents:
        total_residents += 1
    
    for bldg in building_permits:
        total_certificates += 1

    for clr in clearances:
        total_certificates += 1

    for exca in excavation_clearance:
        total_certificates += 1

    for fence in fencing_clearance:
        total_certificates += 1

    for indgent in indigency:
        total_certificates += 1

    for res in residency:
        total_certificates += 1

    for water in water_installation:
        total_certificates += 1

    for wiring in wiring_permit:
        total_certificates += 1


    data = {
        'total_residents': total_residents,
        'total_certificates': total_certificates,
    }
    return render(request,'report.html', data)

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
        birthplace = request.POST.get('birthplace')
        
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
                'birthplace': birthplace,
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

        purpose = purpose.upper()

        template_path = 'pdf_generated/indigency.html'

        context = {
            'purpose': purpose,
            'date': date, 
            'indigent_full_name': indigent_full_name,
            'indigent_age': indigent_age,
            }


        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(indigent_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_indigent').document()

            pdf_file_directory = indigent_resident_id + "/resident_indigent/" + doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'indigent_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'indigent_pdf_directory' : pdf_file_directory,
                })


            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'indigent_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'indigent_pdf_directory' : pdf_file_directory,
                'resident_id': indigent_resident_id,
                'purpose': purpose,
                'date': date, 
                'resident_full_name': indigent_full_name,
                'resident_age': indigent_age,
                'clearance_type': 'Indigent Certificate',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_clearance(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        clearance_full_name = request.POST.get('clearance_full_name')
        clearance_age = request.POST.get('clearance_age')
        clearance_resident_id = request.POST.get('clearance_resident_id')


        template_path = 'pdf_generated/clearance.html'

        context = {
            'date': date, 
            'clearance_full_name': clearance_full_name,
            'clearance_age': clearance_age,
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(clearance_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_clearance').document()

            pdf_file_directory = clearance_resident_id + "/resident_clearance/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'clearance_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'clearance_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'clearance_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'clearance_pdf_directory' : pdf_file_directory,
                'resident_id': clearance_resident_id,
                'date': date, 
                'resident_full_name': clearance_full_name,
                'resident_age': clearance_age,
                'clearance_type': 'Clearance Certificate',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_building(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        building_full_name = request.POST.get('building_full_name')
        building_age = request.POST.get('building_age')
        building_resident_id = request.POST.get('building_resident_id')


        template_path = 'pdf_generated/building_permit.html'

        context = {
            'date': date, 
            'clearance_full_name': building_full_name,
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(building_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_building').document()

            pdf_file_directory = building_resident_id + "/resident_building_permit/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'building_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'building_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'building_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'building_pdf_directory' : pdf_file_directory,
                'resident_id': building_resident_id,
                'date': date, 
                'resident_full_name': building_full_name,
                'resident_age': building_age,
                'clearance_type': 'Building Permit/Clearance',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_residency(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        residency_full_name = request.POST.get('residency_full_name')
        residency_age = request.POST.get('residency_age')
        residency_resident_id = request.POST.get('residency_resident_id')
        birthplace = request.POST.get('residency_birthplace')
        residency_civil_status = request.POST.get('residency_civil_status')
        residency_birthdate = request.POST.get('residency_birthdate')


        template_path = 'pdf_generated/residency.html'

        context = {
            'date': date, 
            'residency_full_name': residency_full_name,
            'residency_age': residency_age,
            'birthplace': birthplace,
            'residency_civil_status': residency_civil_status,
            'residency_birthdate': residency_birthdate,
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(residency_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_residency').document()

            pdf_file_directory = residency_resident_id + "/resident_residency/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'residency_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'residency_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'residency_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'residency_pdf_directory' : pdf_file_directory,
                'resident_id': residency_resident_id,
                'date': date, 
                'resident_full_name': residency_full_name,
                'resident_age': residency_age,
                'resident_birthplace': birthplace,
                'resident_civil_status': residency_civil_status,
                'resident_birthdate': residency_birthdate,
                'clearance_type': 'Barangay Residency',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None


def generate_wiring(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        wiring_full_name = request.POST.get('wiring_full_name')
        wiring_resident_id = request.POST.get('wiring_resident_id')
        house_location = request.POST.get('house_location')


        template_path = 'pdf_generated/wiring_permit.html'

        context = {
            'date': date, 
            'wiring_full_name': wiring_full_name,
            'house_location': house_location,
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(wiring_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_wiring').document()

            pdf_file_directory = wiring_resident_id + "/resident_wiring/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'wiring_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'wiring_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'wiring_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'wiring_pdf_directory' : pdf_file_directory,
                'resident_id': wiring_resident_id,
                'date': date, 
                'resident_full_name': wiring_full_name,
                'resident_house_location': house_location,
                'clearance_type': 'Electrical Inspection/Wiring Permit',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_excavation(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        excavation_full_name = request.POST.get('excavation_full_name')
        excavation_resident_id = request.POST.get('excavation_resident_id')


        template_path = 'pdf_generated/excavation_clearance.html'

        context = {
            'date': date, 
            'excavation_full_name': excavation_full_name,
            
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(excavation_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_excavation').document()

            pdf_file_directory = excavation_resident_id + "/resident_excavation/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'excavation_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'excavation_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'excavation_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'excavation_pdf_directory' : pdf_file_directory,
                'resident_id': excavation_resident_id,
                'date': date, 
                'resident_full_name': excavation_full_name,
                'clearance_type': 'Excavation Clearance',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_fencing(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        fencing_full_name = request.POST.get('fencing_full_name')
        fencing_resident_id = request.POST.get('fencing_resident_id')


        template_path = 'pdf_generated/fencing_clearance.html'

        context = {
            'date': date, 
            'fencing_full_name': fencing_full_name,
            
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(fencing_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_fencing').document()

            pdf_file_directory = fencing_resident_id + "/resident_fencing/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'fencing_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'fencing_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'fencing_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'fencing_pdf_directory' : pdf_file_directory,
                'resident_id': fencing_resident_id,
                'date': date, 
                'resident_full_name': fencing_full_name,
                'clearance_type': 'Fencing Clearance',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

def generate_water(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        water_full_name = request.POST.get('water_full_name')
        water_resident_id = request.POST.get('water_resident_id')


        template_path = 'pdf_generated/water_installation_permit.html'

        context = {
            'date': date, 
            'water_full_name': water_full_name,
            
            }

        # # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
        if not pdf.err:

            doc_ref = firestoreDB.collection('resident_list').document(water_resident_id)

            doc_ref_list_of_issued_certificate = firestoreDB.collection('list_of_issued_certificate_water').document()

            pdf_file_directory = water_resident_id + "/resident_water/"+doc_ref_list_of_issued_certificate.id + ".pdf"  

            doc_ref.update({
                'water_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'water_pdf_directory' : pdf_file_directory,
                })

            doc_ref_list_of_issued_certificate.set({
                'certificate_id' : doc_ref_list_of_issued_certificate.id,
                'water_pdf_url' : storage.child(pdf_file_directory).get_url(None),
                'water_pdf_directory' : pdf_file_directory,
                'resident_id': water_resident_id,
                'date': date, 
                'resident_full_name': water_full_name,
                'clearance_type': 'Water Installation Permit',
                })

            storage.child(pdf_file_directory).put(result.getvalue())

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