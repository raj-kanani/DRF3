from rest_framework import serializers
from .models import Student


#  using model-serializer with CRUD
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
