from django.contrib import admin
from .models import Dog, BoardingVisit
from .forms import BoardingVisitForm
# Register your models here.
admin.site.register(Dog)

class BoardAdminForm(admin.ModelAdmin):
    form = BoardingVisitForm
admin.site.register(BoardingVisit,BoardAdminForm)
