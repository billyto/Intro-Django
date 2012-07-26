from django.http import HttpResponse

def hello(request):
	return HttpResponse("Learn Django they said...")