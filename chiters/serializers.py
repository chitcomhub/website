from rest_framework.serializers import ModelSerializer
from .models import Chiter


class ChiterSerializer(ModelSerializer):

    class Meta:
        model = Chiter
        fields = ('id', 'name', 'nickname', 'direction', 'technology', 'date')
        read_only_fields = ('date',)