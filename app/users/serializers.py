from rest_framework import serializers
from .models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email']
        # fields = "__all__"
        # depth = 1