import random, string, validators

from django.shortcuts import render, redirect
from .models import ShortUrl
from .form import ShortnerForm

def shortner(request):
    DOMAIN = "127.0.0.1:8000/"
    if(request.GET.get("o")):
        originalURL = ShortUrl.objects.all().filter(shortUrl = request.GET.get("o"))[0]
        return redirect(originalURL.originalUrl)

    elif(request.method == "GET"):
        form = ShortnerForm()
        return render(request, 'shortnerForm.html', {'form': form})
   
    elif(request.method == "POST"):
        form = ShortnerForm(request.POST)

        if(form.is_valid() and validators.url(form.cleaned_data["urlToShort"])):
                shortenPath = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                ShortUrl.objects.create(originalUrl = form.cleaned_data["urlToShort"], shortUrl = shortenPath)
                return render(request, 'thanks.html', { 
                     'shortURL' : "?o=" + shortenPath,
                     'domain': DOMAIN 
                     })
        else:
            form = ShortnerForm()
            return render(request, 'shortnerForm.html', { 
                'form': form,
                'nonValidUrl': True 
            })


    