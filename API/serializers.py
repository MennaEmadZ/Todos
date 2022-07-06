from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToDo


class UNIXTimestampField(serializers.DateTimeField):

    def __init__(self):
        super().__init__()
        self.datetime_field = serializers.DateTimeField()

    def to_representation(self, value):
        return int(value.timestamp()*1000)

    def to_internal_value(self, value):
        return self.datetime_field.to_internal_value(value)


class ToDoSerializer(serializers.ModelSerializer):
    due = UNIXTimestampField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'due', 'completed', ]

    def create(self, validated_data):
        user = User.objects.get(id=self.context['user_id'])
        todo = ToDo.objects.create(user=user,
                                    title=validated_data['title'],
                                   description=validated_data['description'],
                                   completed=validated_data['completed'],
                                   due=validated_data['due'])
        return todo
