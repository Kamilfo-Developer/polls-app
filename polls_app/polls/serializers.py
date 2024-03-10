from rest_framework import serializers

from .models import (
    MultipleChoicesAnswer,
    MultipleChoicesOption,
    MultipleChoicesQuestion,
    Poll,
    SingleChoiceAnswer,
    SingleChoiceOption,
    SingleChoiceQuestion,
    TextAnswer,
    TextQuestion,
)


# Options serializers
class SingleChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceOption
        fields = "__all__"


class MultipleChoicesOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoicesOption
        fields = "__all__"


# Answers serializers
class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnswer
        fields = "__all__"


class SingleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceAnswer
        fields = "__all__"

    selected_option = SingleChoiceOptionSerializer(many=False)


class MultipleChoicesAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoicesAnswer
        fields = "__all__"

    selected_options = MultipleChoicesOptionSerializer(many=True)


# Questions serializers


class MultipleChoicesQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoicesQuestion
        fields = "__all__"

    multiple_choice_options = MultipleChoicesOptionSerializer(many=True)


class SingleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceQuestion
        fields = "__all__"

    single_choice_options = SingleChoiceOptionSerializer(many=True)


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        fields = "__all__"


# Poll serializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

    text_questions = TextQuestionSerializer(many=True)
    single_choice_questions = SingleChoiceQuestionSerializer(many=True)
    multiple_choices_questions = MultipleChoicesQuestionSerializer(many=True)


class PassedPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"
