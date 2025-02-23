from rest_framework import serializers
from quiz import models

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = '__all__'

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizAttempt
        fields = '__all__'

class QuizResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizResponse
        fields = '__all__'
