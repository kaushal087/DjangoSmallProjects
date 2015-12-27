from django.contrib import admin

# Register your models here.
from .models import T_URL
from .models import T_Tag
from .models import T_URL_Tag

admin.site.register(T_URL)
admin.site.register(T_Tag)
admin.site.register(T_URL_Tag)
