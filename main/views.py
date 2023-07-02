from django.shortcuts import render,redirect
from .models import task
from .forms import taskform

from transformers import T5Tokenizer, T5ForConditionalGeneration

import requests
from bs4 import BeautifulSoup

tokenizer = T5Tokenizer.from_pretrained("t5-large")
model = T5ForConditionalGeneration.from_pretrained("t5-large")


# Create your views here.


def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text

def index(request):
    tasks = task.objects.order_by('-id')
    return render(request, 'mainindex.html',{"title":"Main site page",'tasks': tasks})

def about(request):
    return render(request, 'aboutindex.html')

def create(request):
    error=""
    if request.method=="POST":
        form = taskform(request.POST)
        if form.is_valid():

            s = form.instance.title
            inpu=get_text(s)

            strr="summarize:  "+inpu
            ####
            input_ids = tokenizer(strr, return_tensors="pt").input_ids
            outputs = model.generate(input_ids)
            #####



            form.instance.task = str(tokenizer.decode(outputs[0], skip_special_tokens=True))
            form.save()
            return redirect('home')
        else:
            error = "form invalid"
    form = taskform()
    contex = {
        "form": form,
        "error": error
    }
    return render(request, 'createindex.html',contex)