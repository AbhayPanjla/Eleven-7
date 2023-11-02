from django.contrib import admin
from.models import SSC 
from.models import GD 
from.models import Free 
from.models import Form 
from.models import Context 
from.models import Omen
# Register your models here.

admin.site.register(SSC)
admin.site.register(GD)
admin.site.register(Free)
admin.site.register(Form)
admin.site.register(Context)
admin.site.register(Omen)
admin.site.site_header = "Eleven-7"
admin.site.index_title = "Welcome to Eleven-7 Tutorial"
admin.site.site_title = "Eleven-7 Tutorial"
