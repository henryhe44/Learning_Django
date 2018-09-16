from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'form_app/index.html')

def form_view(request):
    form = forms.proto_Form
    if request.method == "POST":
        form = forms.proto_Form(request.POST)
        if form.is_valid():
            print("IT WORKS! WAHOO!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request, 'form_app/form_page.html', {"form":form})