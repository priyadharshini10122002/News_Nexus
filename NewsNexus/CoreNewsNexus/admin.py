from django.contrib import admin
from .models import Admin_Registration,User_Registration,News_Feed,Saved_Feed

# Register your models here.


admin.site.register(Admin_Registration)
admin.site.register(User_Registration)
admin.site.register(News_Feed)
admin.site.register(Saved_Feed)

