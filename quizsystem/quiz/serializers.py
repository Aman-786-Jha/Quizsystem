from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz 
        fields= ['id','answers','questions','option1','option2','option3','option4']