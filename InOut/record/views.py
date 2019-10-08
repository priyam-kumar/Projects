from django.shortcuts import render

# Create your views here.
from . models import studentsrecord

def extractid(request):
    if request.method == 'POST':
        id=request.POST.get('registerid')
        print(id)
        try:
            stuinfo = studentsrecord.objects.get(registration_no=id)
            context = {'a': stuinfo}
            print (stuinfo)
        except stuinfo.DoesNotExist:
            raise Http404("Question does not exist")

    return render(request,'display.html',context)
