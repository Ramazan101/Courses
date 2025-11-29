from django.contrib import admin
from .models import  (User,  Category, SubCategory, Course, Lesson,
                     Assignment, Question, Option, Exam, Certificate,
                     Review)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
