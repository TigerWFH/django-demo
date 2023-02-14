from django.contrib import admin
from .models import Question

admin.site.register(Question)
admin.site.site_title = "系统后台"
admin.site.site_header = "WFH项目管理系统"
admin.site.index_title = "后台主页"