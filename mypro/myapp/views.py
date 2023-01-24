from django.shortcuts import render

# Create your views here.
def volumeofcuboid(request):
    context={}
    context['length']="0" 
    context['breadth']="0"
    context['height']="0"
    context['volume']="0"
    if request.method=='POST':
        print("POST method is used . . .")
        length=request.POST.get("length",0)
        breadth=request.POST.get("breadth",0)
        height=request.POST.get("height",0)
        l_num=int(length)
        b_num=int(breadth)
        h_num=int(height)

        volume=l_num*b_num*h_num
        context['length']=length
        context['breadth']=breadth
        context['height']=height       
        context['volume']=volume
    return render(request,"myapp/area.html",context)

