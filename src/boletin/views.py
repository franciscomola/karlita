from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrados

def inicio(request):
    titulo = "HOLA"
    mensaje = None

    if request.user.is_authenticated:
        titulo = "Bienvenido %s" % request.user

    if request.method == "POST":
        form = RegModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if not instance.nombre:
                instance.nombre = "persona"
            instance.save()
            mensaje = "Gracias por registrarte, %s!" % instance.nombre
    else:
        form = RegModelForm()

    context = {
        "title": titulo,
        "el_form": form,
        "mensaje": mensaje,
    }

    return render(request, "base.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        form_email = form.cleaned_data.get("email")
        
        asunto = 'Form de contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, 'franciscomanuel.monjo.lancharro.alu@iesfernandoaguilar.es']
        email_mensaje = f"{form_nombre}: {form_mensaje} enviado por {form_email}"
        
        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True
        )

        print(form_email, form_mensaje, form_nombre)

    context = {
        "form": form,
    }
    return render(request, "form.html", context)