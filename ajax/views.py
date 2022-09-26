from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUpload



def home(request):
    

  



    img = FileUpload.objects.all()

    img = [ image.file  for image in img]

    if request.method == 'POST':

      

        
        form = FileUpload(file=request.FILES['image'])

        form.save()

      

        return render(request,'home/home.html',{"images":img})



    return render(request,'home/home.html',{"images":img})
