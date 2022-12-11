from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        user = self.context["request"].user
        objects = Advertisement.objects.filter(status='OPEN', creator=user).count()
        method = self.context["request"].method
        status = self.initial_data.get("status")
        if objects >= 10 and method == 'POST':
            raise ValidationError("Превышение открытых объявлений")
        if objects >= 10 and method == 'PATCH' and status == "OPEN":
            raise ValidationError("Превышение открытых объявлений")
        return data
