from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import student
from django.contrib import messages
from  multiprocessing import Process
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from azure.storage.filedatalake import DataLakeServiceClient
import threading 
from azure.storage.blob import BlobServiceClient


container='whatsapp'
sub_dir='Documents'
service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
    "https", "leapsurgebi"), credential="ar1apFEmU7ObhgDi8xwa658yyjCFjXvIxuZfBlSVjZNN627YgypuyrvCS0HyKY4+tCVG7saJGYDOXZStfEHE6Q==")

def upload_file_to_directory_bulk(container,sub_dir,image,file_name):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)
        directory_client = file_system_client.get_directory_client(sub_dir)
        file_client = directory_client.get_file_client(image)
        file_client.upload_data(file_name, overwrite=True)
        print("file Uploaded...")
        return "File Uploaded Successfully."
    except Exception as e:
      print(e)




@csrf_exempt
def upload_image(request):
    try:
        file_name= request.FILES.getlist('file')
        for image in file_name:
            first_thread = threading.Thread(target= upload_file_to_directory_bulk , args=(container,sub_dir,image,image))
            first_thread.run()
        print(threading.current_thread())
        if first_thread.is_alive():
            print("Thread is still working.")
        else:
            print("Thread has finished its work.")
            response = str(image) + "File Uploaded Successfully"
            return JsonResponse(response, safe=False)
    
    except Exception as e:
      print(e)
      return HttpResponse(e)

# Create your views here.
def home(request):
    try:
        return render(request,'home.html')
    except Exception as e:
      print(e)
      return HttpResponse(e)

def insert(request):
    try:
        if request.method== 'POST' :
        # if request.POST['studentname'] and request.POST['age'] and request.POST['gender'] and request.POST['standard'] and request.POST['marks1'] and request.POST['marks2'] and request.POST['marks3'] and request.POST['marks4'] and request.POST['sem']:
            student.objects.create(
                name=request.POST['studentname'],
                age=request.POST['age'],
                gender=request.POST['gender'],
                standard=request.POST['standard'],
                marks1=request.POST['marks1'],
                marks2=request.POST['marks2'],
                marks3=request.POST['marks3'],
                marks4=request.POST['marks4'],
                sem=request.POST['sem'],
                # image=request.FILES['image']
                )
            return render(request,'display.html')

        return render(request,'display.html')
    except Exception as e:
      print(e)
      return HttpResponse(e)


def database(request):
    try:
        data=student.objects.all()
        # if request.method=="POST":
        #     sem=request.POST.get('sem')
        #     search=student.objects.filter(sem=sem)
        #     return render(request,'database.html',{'b':search})
        if request.method=='POST':
            d=request.POST['delete']
            st=delete(d)
            if st=='delete':
                messages.info(request,"the data deleted")
                return redirect('database')
            else:
                messages.info(request,"We don't want to delete")
                return redirect('database')
        return render(request,'database.html',{'b':data })
    except Exception as e:
      print(e)
      return HttpResponse(e)
    

def edit(request,id):
    try:
        data=student.objects.get(id=id)
        if request.method=='POST':
            if "edit" in request.POST:
                id=request.POST['id']
                name=request.POST['name']
                age=request.POST['age']
                gender=request.POST['gender']
                standard=request.POST['standard']
                marks1=request.POST['marks1']
                marks2=request.POST['marks2']
                marks3=request.POST['marks3']
                sem=request.POST['sem']

                student.objects.filter(id=id).update(
                id=id,
                name=name,
                age=age,
                gender=gender,
                standard=standard,
                marks1=marks1,
                marks2=marks2,
                marks3=marks3,
                sem=sem
                )
                return redirect('database')

        return render(request,'edit.html',{'b':data,})
    except Exception as e:
      print(e)
      return HttpResponse(e)

def delete(id):
    try:
        student.objects.filter(id=id).delete()
        return 'delete'
    except Exception as e:
      print(e)
      return HttpResponse(e)
    
def result(request):
    try:
        #s=student.objects.raw('select name from student group by name having count(name)=1')
        s=student.objects.values('name').distinct()
        return render(request,'result.html',{'Result':s})
    except Exception as e:
      print(e)
      return HttpResponse(e)

def res(request):
    try:
        if request.method=='POST':
            if request.POST['res']:
                return redirect('percentage')
            return render (request,'percentage.html') 
    except Exception as e:
      print(e)
      return HttpResponse(e)


def percentage(request,name):
    try:
        s=student.objects.filter(name=name)
        if request.method=="POST":
            id=request.POST.get('semm')
            search=student.objects.filter(id=id).get()
            summ=search.marks1 + search.marks2 + search.marks3 + search.marks4
            p=(summ/400)*100
            if p>90:
                g='A'
            elif p>60:
                g='B'
            else:
                g='C'
                
            return render(request,'percentage.html',{'student':s,'per':search ,'sum':summ,'percentage':p,'grade':g })
        return render(request,'percentage.html',{'student':s})
    except Exception as e:
      print(e)
      return HttpResponse(e)


    