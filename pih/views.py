from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context)


def aboutus(request):
	context = {}
	template = "about-us.html"
	return render(request, template, context)	

def contactus(request):
	context = {}
	template = "contact-us.html"
	return render(request, template, context)

def blog(request):
	context = {}
	template = "blog.html"
	return render(request, template, context)	

