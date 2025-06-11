from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.now().strftime('%d.%m.%Y')
    return render(request, 'index.html', {'datet' : date})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
