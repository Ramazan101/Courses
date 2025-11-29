from .models import (User, Category, SubCategory, Course, Lesson,
                    Assignment, Option, Question, Exam)

from modeltranslation.translator import TranslationOptions, register

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name',)


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_name',)


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

