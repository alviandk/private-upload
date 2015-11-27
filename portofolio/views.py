import os
import mimetypes

from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .form import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class HomeView(View):
    template_name = 'portofolio/index.html'
    def get(self,request):

        form = KontakForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):

        form = KontakForm(request.POST or None)
        if form.is_valid():
            kontak=form.save(commit=False)            
            nama = kontak.Name
            email = kontak.Email
            pesan= kontak.Message
            tentang = kontak.Subject
            subject= 'Pesan dari {} tentang {}'.format(nama,tentang)
            message= 'nama: {} \nemail: {} \nno telepon: {} \nmessage: {}'.format(nama,email,pesan)
            email_from= settings.EMAIL_HOST_USER
            email_to= 'alviandk@gmail.com'
            sender = "AlvianDK Backend", "Hi {}, my backend has sent your message. I will respond immedeatly. Thanks".format(nama)
            send_mail(subject, message, email_from, [email_to], fail_silently=False)
            send_mail("Message Sent",sender, email_from, [email], fail_silently=False)
            messages.success(request,'Your comment has been successfully sent')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'An error has occured, please try again')
            return render(request,self.template_name,{'form':form})

    
class CVDownload(View):
	
	def get (self,request):   		
		
		filename=os.path.join(BASE_DIR, 'static/CV.pdf')
		wrapper      = FileWrapper(open(filename))
		content_type = mimetypes.guess_type(filename)[0]
		response     = HttpResponse(wrapper,content_type=content_type)
		response['Content-Length']      = os.path.getsize(filename)
		response['Content-Disposition'] = "attachment; filename=CV.pdf"
		return response
