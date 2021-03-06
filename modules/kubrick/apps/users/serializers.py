from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users import models


class UserSerializer(serializers.ModelSerializer):
    bets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Indication.objects.all(), required=False
    )
    score = serializers.SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = [
            "id",
            "username",
            "email",
            "date_joined",
            "profile_picture",
            "bets",
            "score",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.set_password(password)
        return super().update(instance, validated_data)

    def get_score(self, obj):
        return obj.bets.filter(is_winner=True).count()

    def validate_bets(self, value):
        categories = [indication.category for indication in value]

        # Convert to set to remove the duplicates,
        # and check if the list len is still the same
        if len(categories) != len(set(categories)):
            raise serializers.ValidationError(
                "You can't place two bets to the same category!"
            )
        return value


class RoomSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.UserProfile.objects.all(), required=True
    )

    class Meta:
        model = models.Room
        fields = ["id", "name", "owner", "users", "share_code"]
        extra_kwargs = {"owner": {"read_only": True}}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: models.UserProfile):
        token = super().get_token(user)

        token["name"] = user.username

        return token
