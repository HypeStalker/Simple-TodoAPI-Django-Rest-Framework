from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "body",
            "status",
            "created_at",
            "updated_at",
        )
        model = Todo