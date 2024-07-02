from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter

from .models import Question, Choice
from .serializers import QuestionSerializer

# http://127.0.0.1:8000/apifilters/questions/?search=Samsung
# http://127.0.0.1:8000/apifilters/questions/?search=ned
# http://127.0.0.1:8000/apifilters/questions/?search=Samsung more


class QuestionsAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    search_fields = ["question_text", "author"]
    #search_fields = ["question_text", "author",'choice__choice_text']
    #search_fields = ["^question_text", "author"]
    filter_backends = (SearchFilter,)
    