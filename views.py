from rest_framework import viewsets, permissions
from quiz import models
from quiz.serializers import QuizSerializer, QuestionSerializer, OptionSerializer, QuizAttemptSerializer, QuizResponseSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class OptionViewSet(viewsets.ModelViewSet):
    queryset = models.Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = models.QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizResponseViewSet(viewsets.ModelViewSet):
    queryset = models.QuizResponse.objects.all()
    serializer_class = QuizResponseSerializer
    permission_classes = [permissions.IsAuthenticated]
