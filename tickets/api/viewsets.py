from rest_framework.serializers import ModelSerializer
from projetoFinal.tickets.models import Tickets


class TicketsSerializer(ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['descricao']
