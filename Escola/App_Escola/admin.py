from django.contrib import admin
from .models import Professor, Turma, Atividade

# Register your models here.
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Atividade)