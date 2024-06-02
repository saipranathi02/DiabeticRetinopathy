import tensorflow as tf
from keras.models import load_model
from django.core.files.storage import FileSystemStorage
import tensorflow_hub as hub
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect,redirect
from main.models import Student
from main.forms import UploadForm
from django.contrib import messages
import numpy as np
from keras.models import load_model
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Create your views here.


def home(request):
    return render(request,'home.html')
#def register(request):
 #   if request.method=="POST":
  #      name=request.POST.get('name')
  #      rollno=request.POST.get('rno')
  #      email=request.POST.get('email')
  #      phone=request.POST.get('phno')
  #      student = Student(name=name,rollno=rollno,phone=phone,mailid=email)
  #      student.save()
   #     messages.success(request, 'Successfully registered!')
   # return render(request,'register.html')
def update(request):
    allTasks = Student.objects.all()
    context={'records':allTasks}
    return render(request,'update.html',context)
def delete(request):
    allTasks = Student.objects.all()
    context={'records':allTasks}
    if request.method=="POST":
        pi=Student.object.get(name)
        pi.delete()
    return render(request,'delete.html',context)
def result(request):
    return render(request,'result.html')
def predict(img,model):
    img1=mpimg.imread(img)
    img1=cv2.resize(img1,(224,224),3)
    img1=np.array(img1)/255.0
    img1[np.newaxis,...].shape
    prediction=model.predict(img1[np.newaxis,...])
    prediction=np.argmax(prediction)
    # ar=np.array([left])
    # prediction=model.predict()
    # print(prediction)
    if (prediction==0):
        res='no dr'
    elif(prediction==1):
        res= 'mild dr'
    elif(prediction==2):
        res= 'moderate dr'
    elif(prediction==3):
        res= 'severe'
    else:
        res= 'proliferate'  
    return res
def upload(request):
    # '''form=UploadForm(request.POST,request.FILES)
    # print(request.FILES)
    # if form.is_valid():
    #     form.save()
    # return render(request,'upload.html',{'form':form})'''
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        limage = request.FILES.get('limage')
        rimage = request.FILES.get('rimage')
        model=tf.keras.models.load_model('drmodel.h5', custom_objects={'KerasLayer':hub.KerasLayer})
        res1=predict(limage,model)
        print(predict(r"C:\Users\DELL\Downloads\WhatsApp Image 2021-10-20 at 21.09.37.jpeg",model))
        res2=predict(rimage,model)
        fs=FileSystemStorage()
        f1=fs.save(limage.name,limage)
        f2=fs.save(rimage.name,rimage)
        f1=fs.url(limage)
        f2=fs.url(rimage)
        patient=Student(name=name,age=age,phone=phone,gender=gender,limage=limage,rimage=rimage,res1=res1,res2=res2)
        patient.save()
        print(res1)
        print(res2)
        d={'name':name,'age':age,'phone':phone,'limage':f1,'rimage':f2,'ans1':res1,'ans2':res2}
        return render(request,'result.html',d)
    return render(request,'upload.html')
        
    # ''' fs =FileSystemStorage()
    #     filename1 = fs.save(limage.name,image)
    #     filename1 = fs.url(limage)
    #     filename2 = fs.save(rimage.name,rimage)
    #     filename2 = fs.url(rimage)
    #     labels=[]
    #     image = load_img('.'+filename1, target_size=(224, 224))
    #     img = np.array(image)
    #     img = img / 255.0
    #     img = img.reshape(1,224,224,3)
    #     label = model.predict(img)
    #     label_id = label[0].tolist()
    #     eye_left=label_id.index(max(label_id))
    #     print(labels)
    #     l=[]
    #     image = load_img(filename2, target_size=(224, 224))
    #     img = np.array(image)
    #     img = img / 255.0
    #     img = img.reshape(1,224,224,3)
    #     label = model.predict(img)
    #     label_id = label[0].tolist()
    #     eye_right=label_id.index(max(label_id))
    #     patient.save()
    #     messages.success(request,"Successfully uploaded")'''


'''def remove(request,id):
    if request.method=="POST":
        pi=Student.object.get(pk=name)
        pi.delete()
        return HttpResponseRedirect('/')'''
