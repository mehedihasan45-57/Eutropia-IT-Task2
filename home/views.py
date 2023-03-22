from django.shortcuts import render
from django.http import JsonResponse
from .models import TCloths,SCloths,WCloths,Laptop,Mobile,Computer,Jumkas,Kangans,Necklaces
from itertools import zip_longest
# Create your views here.

def index(request):
    jumka=Jumkas.objects.all()
    kangan=Kangans.objects.all()
    Necklace=Necklaces.objects.all()

    #<-------- Electronics Data  fetching from  model------>
    computer= Computer.objects.all()
    laptop =Laptop.objects.all()
    mobile = Mobile.objects.all()

    #<-------- Clothes Data  fetching from  model------>
    tcloths =TCloths.objects.all()
    wcloths =WCloths.objects.all()
    scloths =SCloths.objects.all()

    
    zipped = zip_longest(tcloths, scloths,wcloths)
    zipped1 = zip_longest(tcloths, scloths,wcloths)
    electronics=zip_longest(laptop,mobile,computer)
    electronics1=zip_longest(laptop,mobile,computer)
    Jewellery =zip_longest(jumka,Necklace,kangan)
    Jewellery1 =zip_longest(jumka,Necklace,kangan)

    context = {
        "zipped":zipped,
        "zipped1":zipped1,
        "electronics":electronics,
        "electronics1":electronics1,
        "Jewellery":Jewellery,
        "Jewellery1":Jewellery1 

    }
    return render(request, 'index.html', context=context)

