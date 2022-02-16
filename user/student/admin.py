from django.contrib import admin
from student.models import Activity,Program, Centre, Professor


admin.site.register(Program)
admin.site.register(Centre)
admin.site.register(Professor)
admin.site.register(Activity)