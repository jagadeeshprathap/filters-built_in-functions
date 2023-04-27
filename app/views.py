from django.shortcuts import render

# Create your views here.
def insert_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HAI HOw aRe YoU','dt':dt,'c':0}
    return render(request,'insert_filter.html',d)