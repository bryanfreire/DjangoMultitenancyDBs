from rest_framework import serializers

import apps.polls.models as pollsmodels


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = pollsmodels.Poll
        fields = (
            'id',
            'question',
            'pub_date'
        )
