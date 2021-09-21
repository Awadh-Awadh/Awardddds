from django.shortcuts import render, redirect
from .models import CustomUSer
from .forms import CustomUserCreationForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def register(request):
      if request.method == "POST":
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              username = form.cleaned_data['username']
              email = form.cleaned_data['email']
              subject = "welcome to Awardds"             
              message = f"Hello {username}, thank you for registering to Awardds"
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [email]
              send_mail(subject, message, email_from,recipient_list)
              return redirect('login')
           
      else:
          form = CustomUserCreationForm()
      return render(request, 'accounts/register.html',{'form':form})
