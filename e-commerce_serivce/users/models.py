from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from commons.models import TimeStampedModel


class UserManager(BaseUserManager):

    def create_user(self, email, password,username, is_staff, **extra_fields):
        if not username:
            raise ValueError("아이디를 반드시 입력해주세요")
        if not email:
            raise ValueError("이메일을 반드시 입력해주세요")
        if not password:
            raise ValueError("비밀번호를 반드시 입력해주세요")
        if not is_staff:
            raise ValueError("판매자 여부를 설정해주세요")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email = email,
            password=password,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password,email,is_staff ,**extra_fields):

        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff,
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user



class User(AbstractUser, PermissionsMixin, TimeStampedModel):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_('아이디'), max_length=20, unique=True,
                                help_text=_('Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                validators=[username_validator],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                },
                                )
    email = models.EmailField(_('이메일'), max_length=30, unique=True)
    is_staff = models.BooleanField(_('판매자 여부'),default=False)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email","is_staff"]


    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    # @ 뒤에 부분을 소문자로 변경해주는 함수
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.username
