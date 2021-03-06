from rest_framework import serializers
from question.models import Question

class QuestionSerializer(serializers.ModelSerializer):

  class Meta:
    model = Question
    fields = (
      'id',
      'talent_position_type',
      'talent_position_sub_type',
      'content'
    )
