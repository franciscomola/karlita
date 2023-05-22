from django.contrib import admin
from .models import Registrados
from .forms import RegModelForm
class AdminRegistrados(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    form = RegModelForm
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]

admin.site.register(Registrados, AdminRegistrados)
