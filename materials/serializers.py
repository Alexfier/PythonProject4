from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    amount_of_lessons_in_course = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_amount_of_lessons_in_course(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = '__all__'






