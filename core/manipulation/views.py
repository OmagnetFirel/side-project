from django.shortcuts import render,HttpResponse
from .forms import ImageForm
from PIL import Image

# Create your views here.

def index(request):
    """Processa imagens enviadas pelo usuario"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            flipImage(img_obj)
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request,'index.html', {'form':form})

def flipImage(img_obj,axis="horizontal"):
    """Recebe uma imagem e a inverte"""
    print(img_obj.image.path)
    # with  Image.open(img_obj.image.path) as img:
    #     if(axis=="horizontal"):
    #         img.transpose(Image.FLIP_LEFT_RIGHT).save("img_fliped.jpg")
    #         print("Sucess!!!")
            
    #     elif(axis=="vertical"):
    #         img.transpose(Image.FLIP_TOP_BOTTOM).save("img_fliped.jpg")
    #         print("Sucess!!!")