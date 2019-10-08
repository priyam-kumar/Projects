from django.shortcuts import render
from record.models import studentsrecord
from .models import entryrecord
from datetime import datetime
# Create your views here.
def index(request):
#    a = 3 + 4
#    context = {'a': a}
    if request.method == 'POST':
        id=request.POST.get('registerid')
        try:
            stuinfo = studentsrecord.objects.get(registration_no=id)
            if stuinfo:
                entryrec = entryrecord.objects.filter(registration_no=stuinfo).order_by('-entry_time')
                print(entryrec)
                if entryrec:
                    entryrec = entryrec[0]
                    exit = entryrec.exit_time
                    entry = entryrec.entry_time
                    entry = entry.strftime("%Y-%m-%d %H:%M:%S")
                    exit = exit.strftime("%Y-%m-%d %H:%M:%S")
                    if entry == exit:
                        print("EXIT")
                        entryrec.save()
                        return render(request,'index.html')
            context = {'std': stuinfo}
        except stuinfo.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request,'display.html',context)
    return render(request, 'index.html')
#    return render(request, 'index.html', context)

def saveRecord(request):
    if request.method == 'POST':
        rec = entryrecord()
        rec.registration_no = studentsrecord.objects.get(registration_no=request.POST.get('reg'))
        rec.purpose = request.POST.get('purpose')
        rec.place = request.POST.get('place')
        rec.save()
    return render(request, 'index.html')
