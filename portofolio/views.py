import os
import mimetypes

from django.conf import settings
from django.core.mail import send_mail
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, HttpResponseRedirect

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

        Kform = KontakForm(request.POST)
        if Kform.is_valid():
            form = Kform.cleaned_data
            nama = form['Name']
            email = form['Email']
            pesan= form['Message']
            tentang = form['Subject']
            subject= 'Pesan dari {} tentang {}'.format(nama,tentang)
            message= 'nama: {} \nemail: {} \nmessage: {}'.format(nama,email,pesan)
            email_from= "alvian-backend@gmail.com"
            email_to= 'alviandk@gmail.com'
            sender = "Hi {}, my backend has sent your message. I will respond immedeatly. Thanks".format(nama)
            send_mail(subject, message, email_from, [email_to], fail_silently=False)
            send_mail("Message Sent",sender, email_from, [email], fail_silently=False)

            return HttpResponseRedirect('/')
        else:

            return render(request,self.template_name,{'form':Kform})


class CVDownload(View):

	def get (self,request):

		filename='/home/alviandk/private-upload/static/CV.pdf'
		wrapper      = FileWrapper(open(filename))
		content_type = mimetypes.guess_type(filename)[0]
		response     = HttpResponse(wrapper,content_type=content_type)
		response['Content-Length']      = os.path.getsize(filename)
		response['Content-Disposition'] = "attachment; filename=CV.pdf"
		return response
