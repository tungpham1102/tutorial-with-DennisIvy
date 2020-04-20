from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        message = request.POST['message']
        # send_mail(subject, message, configured email, reciver, fail_silently)
        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['phamtung1377@gmail.com'],
                  fail_silently=False)
    return render(request, 'sendemail/send_email.html')
