from rest_framework import serializers
from .models import (User,  Category, SubCategory, Course, Lesson,
                     Assignment, Question, Option, Exam, Certificate,
                     Review)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name']


class CourseListSerializer(serializers.ModelSerializer):
    get_avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image', 'price', 'get_avg_rating',
                  'price']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class SubCategoryDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_category_name']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video']

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    sub_categorys = SubCategoryListSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    created_by_teacher = UserNameSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'level' ,'sub_categorys', 'lessons',
                  'get_avg_rating', 'price', 'created_by_teacher']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    sub_categorys = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name', 'sub_categorys']

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categorys = SubCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'sub_categorys']

class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'due_date']

class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_name']

class OptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text']

class QuestionDetailSerializer(serializers.ModelSerializer):
    options = OptionDetailSerializer(many=True, read_only=True)
    class Meta:

        model = Question
        fields = ['id', 'question_text', 'question_name', 'options']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'duration']

class ExamDetailSerializer(serializers.ModelSerializer):
    exams_questions = QuestionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'

class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'student', 'course']


class CertificateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'