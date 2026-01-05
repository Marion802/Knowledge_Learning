from django.db import models
from users.models import User


class Theme(models.Model):
    """
    Represents a training theme.
    A theme is the highest level of organization and contains one or more courses.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='themes_created'
    )
    updated_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='themes_updated'
    )

    def __str__(self):
        return self.title


class Course(models.Model):
    """
    Represents a training course.
    A course belongs to a theme and is composed of multiple lessons.
    """
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='courses_created'
    )
    updated_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='courses_updated'
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Represents a lesson within a course.
    A lesson contains educational content and an associated video.
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='lessons_created'
    )
    updated_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='lessons_updated'
    )

    def __str__(self):
        return self.title


class CoursePurchase(models.Model):
    """
    Represents the purchase of a course by a user.
    Used to simulate an e-commerce transaction.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='course_purchases'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.course}"


class LessonPurchase(models.Model):
    """
    Represents the purchase of a single lesson by a user.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lesson_purchases'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.lesson}"


class LessonValidation(models.Model):
    """
    Represents the validation of a lesson by a user.
    A lesson can only be validated once per user.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lesson_validations'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    validated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user} validated {self.lesson}"


class CourseValidation(models.Model):
    """
    Represents the validation of a course by a user.
    A course is validated automatically when all its lessons are validated.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='course_validations'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    validated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} validated {self.course}"


class Certification(models.Model):
    """
    Represents a certification obtained by a user.
    A certification is awarded when all courses of a theme are validated.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='certifications'
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE
    )
    obtained_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'theme')

    def __str__(self):
        return f"{self.user} - {self.theme}"
