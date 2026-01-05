from django.contrib import admin
from .models import Theme, Course, Lesson
from .models import CoursePurchase, LessonPurchase, LessonValidation, CourseValidation, Certification


admin.site.register(Theme)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CoursePurchase)
admin.site.register(LessonPurchase)
admin.site.register(LessonValidation)
admin.site.register(CourseValidation)
admin.site.register(Certification)