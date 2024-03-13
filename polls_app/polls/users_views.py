from django.db import transaction
from rest_framework import generics, viewsets
from rest_framework.fields import datetime
from rest_framework.mixins import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from .models import MultipleChoicesAnswer, Poll, SingleChoiceAnswer, TextAnswer
from .serializers import (
    MultipleChoicesAnswerSerializer,
    PassedPollSerializer,
    PollSerializer,
    SingleChoiceAnswerSerializer,
    TextAnswerSerializer,
)


class UsersPollsListAPIView(generics.ListAPIView):
    queryset = Poll.objects.filter(end_date__gte=datetime.datetime.utcnow())
    serializer_class = PollSerializer


# These will work by themselves
class UsersTextAnswersListCreateAPIView(generics.ListCreateAPIView):
    queryset = TextAnswer.objects.all()
    serializer_class = TextAnswerSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create

    #     return TextAnswer.objects.create()


class UsersSingleChoiceAnswersListCreateAPIView(generics.ListCreateAPIView):
    queryset = SingleChoiceAnswer.objects.all()
    serializer_class = SingleChoiceAnswerSerializer


class UsersMultipleChoicesAnswersListCreateAPIView(generics.ListCreateAPIView):
    queryset = MultipleChoicesAnswer.objects.all()
    serializer_class = MultipleChoicesAnswerSerializer


class UsersPassedPollsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PassedPollSerializer

    def list(self, request: Request) -> Response:
        user = request.user.id

        passed_polls = (
            Poll.objects.filter(id__in=TextAnswer.objects.filter(user=user))
            | Poll.objects.filter(id__in=SingleChoiceAnswer.objects.filter(user=user))
            | Poll.objects.filter(
                id__in=MultipleChoicesAnswer.objects.filter(user=user)
            )
        )

        serializer = self.serializer_class(passed_polls, many=True)

        return Response(data={"polls": serializer.data})
