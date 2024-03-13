from django.contrib import admin
from .models import Course, Chapter,CourseCategory , InstructorDepartment , Instructor, Lesson
# Register your models here.
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(CourseCategory)
admin.site.register(InstructorDepartment)
admin.site.register(Instructor)
admin.site.register(Lesson)


# from django.contrib import admin
# from .models import InsCategory, Instructor, Category, Course, Chapter, Lesson

# @admin.register(InsCategory)
# class InsCategoryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Instructor)
# class InstructorAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Chapter)
# class ChapterAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     pass
