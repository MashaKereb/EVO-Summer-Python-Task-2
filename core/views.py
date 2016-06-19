# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.db.models import F



def home(request):
	return render(request, 'core/index.html')

def test(request):
	text = request.GET.get('name')

	try:
		user = User.objects.get(name=text)
		return HttpResponse(u'Рад тебя видеть снова, ' + unicode(user.desc.name)+ u' ' + unicode(user.name) + u'!')
	except:
		set = Description.objects.order_by("flag")
		user = User(name=text, desc=set[0])
		Description.objects.filter(name = set[0]).update(flag = F('flag')+1)
		user.save()
		return HttpResponse(u'Рад тебя видеть, ' + unicode(user.desc.name)+ u' ' + unicode(user.name) + u'!')