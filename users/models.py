import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class User(AbstractUser):
    """
    Custom user model for the Knowledge Learning platform.

    Extends Django's AbstractUser to add:
    - role management (admin or client)
    - account activation via email
    - audit fields (created_at, updated_at, created_by, updated_by)
    """

    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('CLIENT', 'Client'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )

    activation_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    created_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_users'
    )

    updated_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='updated_users'
    )

    def __str__(self):
        """
        Returns the string representation of the user.
        """
        return self.username

    def send_activation_email(self):
        """
        Sends an account activation email to the user.

        The email contains a unique activation link based on a UUID token.
        The account remains inactive until the link is clicked.
        """
        activation_link = (
            f"http://127.0.0.1:8000/users/activate/{self.activation_token}/"
        )

        message = (
            "Click the link below to activate your Knowledge Learning account:\n\n"
            f"{activation_link}"
        )

        send_mail(
            subject="Activate your Knowledge Learning account",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
            fail_silently=False,
        )
