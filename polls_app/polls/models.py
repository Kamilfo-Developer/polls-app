import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateTimeField(default=datetime.datetime.utcnow)
    end_date = models.DateTimeField()
    desciption = models.TextField()


class BaseQuestion(models.Model):
    question_content = models.TextField()

    class Meta:
        abstract = True


class TextQuestion(BaseQuestion):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="text_questions"
    )


class SingleChoiceQuestion(BaseQuestion):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="single_choice_questions"
    )


class MultipleChoicesQuestion(BaseQuestion):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="multiple_choices_questions",
    )


# Options


class BaseOption(models.Model):
    option_content = models.TextField()

    class Meta:
        abstract = True


class SingleChoiceOption(BaseOption):
    question = models.ForeignKey(
        SingleChoiceQuestion,
        on_delete=models.CASCADE,
        related_name="single_choice_options",
    )


class MultipleChoicesOption(BaseOption):
    question = models.ForeignKey(
        MultipleChoicesQuestion,
        on_delete=models.CASCADE,
        related_name="multiple_choice_options",
    )


# Answers
class BaseAnswer(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TextAnswer(BaseAnswer):
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE)
    answer_content = models.TextField()


class MultipleChoicesAnswer(BaseAnswer):
    question = models.ForeignKey(MultipleChoicesQuestion, on_delete=models.CASCADE)
    selected_options = models.ManyToManyField(MultipleChoicesOption)


class SingleChoiceAnswer(BaseAnswer):
    question = models.ForeignKey(SingleChoiceQuestion, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(SingleChoiceOption, on_delete=models.PROTECT)
