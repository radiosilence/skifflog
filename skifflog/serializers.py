from rest_framework import serializers

from skifflog.models import Block

class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('start', 'duration', 'comment')
