from django.shortcuts import render
from datetime import datetime, timedelta
from celery import group, chain, chord
from .tasks import send_mail, send_welcome_mail, send_tip_mail, send_newsletter_mail, update_mails_sent

# Create your views here.
def index(request):    
    mail_sent = False  
      
    if request.method == "POST":
        email = request.POST.get("email")
        
        # MÉTODO DELAY:
        send_mail.delay(email)    
        
        # MÉTODO APPLY_SYNC:
        #send_mail.apply_async(
        #    args=[email],
        #    countdown=5,
        #    # eta=datetime.now() + timedelta(seconds=5),
        #) 
        
        # TAREAS AGRUPADAS:  
        #tasks = group(
    	#    send_welcome_mail.s(email),
    	#    send_tip_mail.s(email), 
    	#    send_newsletter_mail.s(email),
	    #)
        #tasks.apply_async(
        #    countdown=5,
        #)
        
        # ENCADENAR TAREAS:  
        #tasks = chain(
    	#    send_welcome_mail.s(email),
    	#    send_tip_mail.s(), 
    	#    send_newsletter_mail.s(),
	    #)
        #tasks.apply_async(
        #    countdown=5,
        #)

        # TAREAS ENCADENADAS CON CHORD:  
        #chord(
	    #    [
    	#    	send_welcome_mail.s(email),
    	#    	send_tip_mail.s(), 
    	#    	send_newsletter_mail.s(),
	    #    ]
	    #)(
	    #    update_mails_sent.s()
	    #)
        
        mail_sent = True   
               
    return render(request, "index.html", {
        "mail_sent": mail_sent
        })
