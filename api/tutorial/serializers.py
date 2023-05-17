from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = '__all__'

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                {'message': 'title and description can not be same!'})
        return data
