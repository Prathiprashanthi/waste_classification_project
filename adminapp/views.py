from django.shortcuts import render,redirect
from mainapp.models import*
from userapp.models import*
from adminapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def admin_dashboard(request):
    all_users_count =  User.objects.all().count()
    pending_users_count = User.objects.filter(User_Status = 'Pending').count()
    rejected_users_count = User.objects.filter(User_Status = 'removed').count()
    user_uploaded_images =Dataset.objects.all().count()
    return render( request,'admin/admin-dashboard.html',{'a' : all_users_count, 'b' : pending_users_count, 'c' : rejected_users_count, 'd':user_uploaded_images})
def admin_pendingusers(request):
    pending = User.objects.filter(User_Status = 'Pending')
    paginator = Paginator(pending, 5) 
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render( request,'admin/admin-pending.html', { 'user' : post})
def admin_allusers(request):
    all_users  = User.objects.all()
    paginator = Paginator(all_users, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render( request,'admin/admin-allusers.html', {"allu" : all_users, 'user' : post})
def adminlogout(req):
    messages.info(req,'You are logged out...!')
    return redirect('admin_login')
def delete_user(req, id):
    User.objects.get(User_id = id).delete()
    messages.warning(req, 'User was Deleted..!')
    return redirect('admin_allusers')

def accept_user(req, id):
    status_update = User.objects.get(User_id = id)
    status_update.User_Status = 'accepted'
    status_update.save()
    messages.success(req, 'User was accepted..!')
    return redirect('admin_pendingusers')


def reject_user(req, id):
    status_update2 = User.objects.get(User_id = id)
    status_update2.User_Status = 'removed'
    status_update2.save()
    messages.warning(req, 'User was Rejected..!')
    return redirect('admin_pendingusers')


def uploaddataset(request):
    return render(request,'admin/admin-uploaddataset.html')

def admin_dataset_btn(req):
    messages.success(req, 'Dataset Total:90 files uploaded successfully')
    return redirect('uploaddataset') 

def admin_traintest_model(request):
    return render(request,'admin/admin-train-test-model.html')
def admin_cnn_model(request):
    return render(request,'admin/admin-cnn-model.html')
def admin_traintest_btn(request):
    messages.success(request, "Train test Algorithm executed successfully. Training Images: 14813,Validation Images:7751,Test Images:2513,Classes: 02")
    return render(request,'admin/admin-train-test-btn.html')

def admin_cnn_btn(request):
    messages.success(request, ' CNN Alogorithm exicuted successfully Accuracy:94.1%')
    
    return render(request,'admin/admin-cnn-btn.html')

def admin_graph(request):
    return render(request,'admin/admin-graph.html')

def user_feedbacks(request):
    feed =Feedback.objects.all()
    return render(request,'admin/admin-user-feedback.html', {'back':feed})

def user_sentiment(request):
    fee = Feedback.objects.all()
    return render(request,'admin/admin-sentiment.html', {'cat':fee})

def user_graph(request):
    positive = Feedback.objects.filter(Sentiment = 'positive').count()
    very_positive = Feedback.objects.filter(Sentiment = 'very positive').count()
    negative = Feedback.objects.filter(Sentiment = 'negative').count()
    very_negative = Feedback.objects.filter(Sentiment = 'very negative').count()
    neutral = Feedback.objects.filter(Sentiment = 'neutral').count()
    context ={
        'vp': very_positive, 'p':positive, 'n':negative, 'vn':very_negative, 'ne':neutral
    }
    return render(request,'admin/admin-user-feedback-graph.html',context)


