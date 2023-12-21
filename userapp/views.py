from django.shortcuts import render,redirect
from django.contrib import messages
import time
from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth import login
from django.utils import timezone
from mainapp.models import *
from userapp.models import *
from adminapp.models import *
import pytz
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
# Create your views here.

def user_dashboard(req):
    images_count =  User.objects.all().count()
    print(images_count)
    user_id = req.session["User_id"]
    user = User.objects.get(User_id = user_id)
    
    if user.Last_Login_Time is None:
        IST = pytz.timezone('Asia/Kolkata')
        current_time_ist = datetime.now(IST).time()
        user.Last_Login_Time = current_time_ist
        user.save()
    return render(req,'user/user-dashboard.html', {'detect' : images_count, 'la' : user})




# Load your pre-trained model
model = load_model('waste_classification/model_waste.h5')
ref={
    0:'organic',
    1:'recyclable',
}
# Function to predict based on an image path
def prediction(path):
  img = image.load_img(path, target_size=(224, 224))
  i = image.img_to_array(img)
  i = np.expand_dims(i, axis=0)
  img = preprocess_input(i)
  pred = np.argmax(model.predict(img), axis=1)
  return ref[pred[0]]
  

# Your Django view function
def user_predict(req):
    result = {"message": "No image uploaded"}  # Initialize the result as a dictionary
    uploaded_image_url = None

    if req.method == "POST" and 'img' in req.FILES:
        uploaded_image = req.FILES['img']
        Dataset.objects.create(Image= uploaded_image)
        file_path = default_storage.save(uploaded_image.name, uploaded_image)
        path = settings.MEDIA_ROOT + '/' + file_path
        uploaded_image_url = default_storage.url(file_path)
        result = prediction(path)  # Assuming prediction() returns a dictionary
        req.session['result'] = result
        req.session['uploaded_image_url']=uploaded_image_url
        messages.success(req,'Uploaded image successfully')
        return redirect('result')
    
    return render(req, 'user/user-predict.html', {'result': result, 'uploaded_image_url': uploaded_image_url})

# View for displaying the result
def result(req):
    result = req.session.get('result', {"message": "No result available"})
    uploaded_image_url = req.session.get('uploaded_image_url', None)
    messages.success(req, 'Waste Classification')
    return render(req, 'user/user-result.html', {'result': result, 'uploaded_image_url': uploaded_image_url})



def user_profile(req):
    user_id = req.session["User_id"]
    user = User.objects.get(User_id = user_id)
    if req.method == 'POST':
        user_name = req.POST.get('firstname')
        user_age = req.POST.get('age')
        user_phone = req.POST.get('phone')
        user_email = req.POST.get('email')
        user_address = req.POST.get("address")
        
        user.Full_name = user_name
        user.Age = user_age
        user.Address = user_address
        user.Phone_Number = user_phone
        user.Email=user_email
       

        if len(req.FILES) != 0:
            image = req.FILES['pic']
            user.Image = image
            user.Full_name = user_name
            user.Age = user_age
            user.Address = user_address
            user.Phone_Number = user_phone
            user.Email=user_email
            user.Address=user_address
            
            user.save()
            messages.success(req, 'Updated SUccessfully...!')
        else:
            user. Full_name = user_name
            user.Age = user_age
            user.save()
            messages.success(req, 'Updated SUccessfully...!')
            
    context = {"i":user}
    return render(req,'user/user-profile.html',context)
def user_feedback(req):
    id=req.session["User_id"]
    uusser=User.objects.get(User_id=id)
    if req.method == "POST":
        rating=req.POST.get("rating")
        review=req.POST.get("review")
        # print(sentiment)        
        # print(rating,feed)
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(review)
        sentiment=None
        if score['compound']>0 and score['compound']<=0.5:
            sentiment='positive'
        elif score['compound']>=0.5:
            sentiment='very positive'
        elif score['compound']<-0.5:
            sentiment='very negative'
        elif score['compound']<0 and score['compound']>=-0.5:
            sentiment='negative'
        else :
            sentiment='neutral'
        Feedback.objects.create(Rating=rating, Review=review,Sentiment=sentiment, Reviewer=uusser)
        messages.success(req,'Feedback recorded')
        return redirect('user_feedback')
    return render(req,'user/user-feedback.html')
def user_logout(req):
    user_id = req.session["User_id"]
    user = User.objects.get(User_id = user_id)
    t = time.localtime()
    user.Last_Login_Time = t
    current_time = time.strftime('%H:%M:%S', t)
    user.Last_Login_Time = current_time
    current_date = time.strftime('%Y-%m-%d')
    user.Last_Login_Date = current_date
    user.save()
    messages.info(req, 'You are logged out..')
    return render(req,'user/user-login.html')
