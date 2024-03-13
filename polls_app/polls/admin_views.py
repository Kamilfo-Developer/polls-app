from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.fields import datetime
from rest_framework.generics import ListAPIView
from rest_framework.mixins import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request

from .models import MultipleChoicesAnswer, Poll, SingleChoiceAnswer, TextAnswer
from .serializers import (
    MultipleChoicesAnswerSerializer,
    PollSerializer,
    SingleChoiceAnswerSerializer,
    TextAnswerSerializer,
)

# Create your views here.


class AdminPollsViewSet(
    generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView
):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
