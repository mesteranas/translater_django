import googletrans
from django.shortcuts import render

# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def Translate(r):
    langs=[]
    for key,value in googletrans.LANGUAGES.items():
        langs.append(value)
    result=""
    translater=googletrans.Translator()
    if r.method=="POST":
        if r.POST["From"]=="Auto":
            From=translater.detect(r.POST["Text"]).lang
        else:
            From=r.POST["From"]
        result=translater.translate(r.POST["Text"],src=From,dest=r.POST["To"]).text
    return render(r,"translate.html",{"languages":langs,"result":result})