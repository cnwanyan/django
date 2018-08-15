from django.contrib import admin

# Register your models here.
from .models import Grades,Students

#学生信息添加栏
class StudentsInfo(admin.TabularInline):
                #或者admin.StackedInline
                #只是显示效果不同
    model= Students
    extra = 2

#自定义管理页面
class GradesAdmin(admin.ModelAdmin):
    #列表页属性

    #加两行学生的添加
    inlines = [StudentsInfo]

    #显示字段
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']

    #过滤器 过滤字段
    list_filter = ['gname']

    #搜索条件
    search_fields = ['gname']

    #分页配置
    list_per_page = 5

    #添加修改页属性

    #规定显示哪些属性以及顺序
    #fields = ['gname','ggirlnum','gboynum','isDelete']

    #与fields不能同时使用
    fieldsets = [
        (
            "base",{"fields":["gname",'gdate',"isDelete"]}
        ),
        (
            "num", {"fields": ['ggirlnum', 'gboynum']}
        )
    ]

class StudentAdmin(admin.ModelAdmin):
    #渲染字段内容
    def sgender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    #设置列名称
    sgender.short_description = "性别"

    list_display = ['pk', 'sname', sgender, 'sage', 'scontend', 'sgrade','isDelete']
    list_per_page = 5


#注册
admin.site.register(Grades,GradesAdmin)

admin.site.register(Students,StudentAdmin)