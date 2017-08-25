from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', { 'content': ['Hello, you can contact me on my email-id', 'My email is abc@gmail.com'] })
