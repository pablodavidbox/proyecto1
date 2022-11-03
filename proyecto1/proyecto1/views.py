from django.shortcuts import render

def prueba_render_template(request):
    return render(request,"hola.html")