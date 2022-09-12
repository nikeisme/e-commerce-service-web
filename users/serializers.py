from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):

    # 이메일 중복 검증
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    # 비밀번호 검증
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    # 비밀번호 확인
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ('username','password','password2','email','address','phone','gender','is_staff')



    # 비밀번호 일치 검증
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})

        return data

    # token 발행
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True, write_only=True)

    def validate(self,data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError({"error":"알맞은 토큰이 아닙니다."})