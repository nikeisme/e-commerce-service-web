from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


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
        fields = ('username','password','password2','email')



    # 비밀번호 일치 검증
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})

        return data

    # token 발행
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
