import os

from django.shortcuts import render
from django.http import  HttpResponse
from django.utils.datetime_safe import datetime
from pymongo import MongoClient
from datetime import datetime, timedelta
from django.template.loader import get_template
from mongoengine import Document, fields
from . import utils
from django.core.files.storage import FileSystemStorage


# Create your views here.
def getLastDocuments(request):
    template = get_template('HADSHANOT/getPDFLast.html')
    imgs = {'IMG': []}
    now = datetime.utcnow()
    last_30d = now - timedelta(days=30)
    since_last_month = db.documents.find(
        {"Accountant": request.COOKIES['UserID'], "CUSTOMER": request.COOKIES['CUSTOMER'],
         "DATE": {"$gte": last_30d}})
    for doc in since_last_month:
        img = doc['IMG']
        imgs['IMG'].append(img)
    html = template.render(imgs)
    pdf = utils.render_to_pdf('HADSHANOT/getPDFLast.html', imgs)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
        return HttpResponse("Not found")

def getAllDocuments(request):
    template = get_template('HADSHANOT/getPDF.html')
    imgs = {'IMG': []}
    y = list(db.documents.find({"Accountant": request.COOKIES['UserID'], "CUSTOMER": request.COOKIES['CUSTOMER']}))
    for doc in y:
        img = doc['IMG']
        imgs['IMG'].append(img)
    html = template.render(imgs)
    pdf = utils.render_to_pdf('HADSHANOT/getPDF.html', imgs)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
        return HttpResponse("Not found")

client = MongoClient(host="localhost", port=27017)
db = client["try"]
def HomePage(request):
    return render(request,'HADSHANOT/HomePage.html')
def SIGNUP(request):
    return render(request,'HADSHANOT/SignUp.html')
def login(request):
    return render(request,'HADSHANOT/login.html')
def addDocument(request):
    return render(request,'HADSHANOT/addDocument.html')
def SignUpDone(response):
    if response.method == 'POST':
        SV = db.accountant
        user = {
            "ID":response.POST.get('ID'),
            "PASSWORD":response.POST.get('PASSWORD'),
            "EMAIL": response.POST.get('EMAIL'),
        }
        SV.insert_one(user)
        client.close()
    return render(response, 'HADSHANOT/SignupDone.html')
def LoginStatus(response):
    if response.method=='POST':
        findUser=db.accountant.find_one({"ID": response.POST.get('ID') , "PASSWORD": response.POST.get("PASSWORD")})
    if(findUser!=None):
        result=render(response,'HADSHANOT/loginstatus.html')
        result.set_cookie('UserID',response.POST.get('ID'))
    else:
        result=render(response,'HADSHANOT/HomePage.html')
    return result
def UserHomePage(request):
    return render(request, 'HADSHANOT/UserHomePage.html')
def addFile(response):
    if response.method == 'POST':
        SV = db.documents
        d = datetime.strptime(response.POST.get('DATE'),'%Y-%m-%d')
        user = {
            "Accountant" : response.COOKIES['UserID'],
            "DATE":d,
            "IMG":response.POST.get('IMG'),
            "CUSTOMER": response.POST.get('CUSTOMER'),
        }
        SV.insert_one(user)
        client.close()
    return render(response,'HADSHANOT/addDocument.html')
def findDocument(request):
    return render(request,'HADSHANOT/findDocument.html')
def logout(request):
    response=render(request,'HADSHANOT/HomePage.html')
    response.set_cookie('UserID','NONE')
    return response
def showDocument(response):
    if response.method == 'POST':
       imgs={'IMG':[]}
       y=list(db.documents.find({"Accountant": response.COOKIES['UserID'], "CUSTOMER": response.POST.get('CUSTOMER')}))
       for doc in y :
           img = doc['IMG']
           imgs['IMG'].append(img)
    result=render(response,'HADSHANOT/showDocument.html',imgs)
    result.set_cookie('CUSTOMER',response.POST.get('CUSTOMER'),max_age=180)
    return result
def findLast(request):
    return render(request,'HADSHANOT/findLast.html')
def showLast(response):
    imgs = {'IMG': []}
    now = datetime.utcnow()
    last_30d = now - timedelta(days=30)
    since_last_month = db.documents.find(
        {"Accountant": response.COOKIES['UserID'], "CUSTOMER": response.COOKIES['CUSTOMER'],
         "DATE": {"$gte": last_30d}})
    for doc in since_last_month:
        img = doc['IMG']
        imgs['IMG'].append(img)
    return render(response, 'HADSHANOT/showLast.html',imgs)
def SendMail(request):
    return render(request,'HADSHANOT/sendMail.html')
def sendEmail(response):
    if response.method == 'POST':
        emails = {'EMAIL': []}
        email = response.POST.get('EMAIL')
        print(email)
        emails['EMAIL'].append(email)
        result = render(response, 'HADSHANOT/sendEmail.html',emails)
    else:
        result = render(response, 'HADSHANOT/HomePage.html')
    return result