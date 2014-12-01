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


def ourwork(request):
	context = {}
	template = "ourwork.html"
	return render(request, template, context)		

def mission(request):
	context = {}
	template = "mission.html"
	return render(request, template, context)	

def history(request):
	context = {}
	template = "history.html"
	return render(request, template, context)	

def founders(request):
	context = {}
	template = "founders.html"
	return render(request, template, context)	

def governance(request):
	context = {}
	template = "governance.html"
	return render(request, template, context)	

def events(request):
	context = {}
	template = "events.html"
	return render(request, template, context)	

def donate(request):
	context = {}
	template = "donate.html"
	return render(request, template, context)			

