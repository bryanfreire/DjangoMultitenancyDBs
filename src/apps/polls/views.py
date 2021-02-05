from rest_framework import viewsets

import apps.polls.models as pollsmodels
import apps.polls.serializers as pollssers

class PollView(viewsets.ModelViewSet):
    queryset = pollsmodels.Poll.objects.all()
    serializer_class =  pollssers.PollSerializer
