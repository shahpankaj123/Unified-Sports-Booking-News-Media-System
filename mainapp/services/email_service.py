from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from threading import Thread

from venue import models as vmd

def send_activation_email(recipient_email, activation_url):
    try:
        thread = Thread(target=__activate_email ,args=(recipient_email,activation_url))
        thread.start()
    except Exception as e:
        print(e)
        pass    

def  __activate_email(recipient_email,activation_url):

    subject = 'Activate your account on '
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string('accounts/activate_email.html', {'activation_url': activation_url,'topic':'Activation Mail','desc':'You are receiving this email because you need to finish activation process.'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
    print('successfully send') 
    
def send_reset_password_email(recipient_email, activation_url):
    try:
        thread = Thread(target=__reset_password ,args=(recipient_email,activation_url))
        thread.start()
    except Exception as e:
        print(e)
        pass    

def __reset_password(recipient_email, activation_url):

    subject = 'Reset Password'
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string('accounts/send_otp.html', {'activation_url': activation_url,'topic':'Reset Password Mail','desc':'You are receiving this email because you need to Reset Password process.Your OTP Code:'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
    print('successfully send') 

def send_event_book_email(recipient_email, event_data : vmd.EventRegisteredRecord):
    try:
        thread = Thread(target=__event_booking_mail ,args=(recipient_email, event_data))
        thread.start()
    except Exception as e:
        print(e)
        pass    

def __event_booking_mail(recipient_email, event_data :vmd.EventRegisteredRecord):
    subject = 'Event Booking Confirmation'
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string(
        'event_booking_mail.html',
        {
            'eventTitle':event_data.Event.EventTitle,
            'courtName':event_data.Event.Court.Name,
            'date':event_data.Event.Date,
            'time':event_data.Event.Time,
            'token':event_data.Token
        }
    )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_payment_email(recipient_email, payment_data : vmd.PaymentTransaction):
    try:
        thread = Thread(target=__payment_success_mail ,args=(recipient_email,payment_data))
        thread.start()
    except Exception as e:
        print(e)
        pass        

def __payment_success_mail(recipient_email, payment_invoice_url):
    subject = 'Payment Successful'
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string(
        'payment_success_mail.html',
        {
            'activation_url': payment_invoice_url,
            'topic': 'Payment Successful',
            'desc': 'We have successfully received your payment. You can download your invoice below.'
        }
    )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()



