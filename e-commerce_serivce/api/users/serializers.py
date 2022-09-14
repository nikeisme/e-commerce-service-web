from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: is_staff
    is_staff = serializers.BooleanField(allow_null=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['is_staff'] = self.validated_data.get('is_staff', '')

        return data