from django.test import TestCase
from django.urls import reverse
from users.models import User
from .models import Theme, Course, CoursePurchase
from .models import Lesson, LessonValidation


class CoursePurchaseTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='buyer',
            password='password123',
            is_active=True
        )
        self.client.login(username='buyer', password='password123')

        self.theme = Theme.objects.create(title='Test Theme', description='Desc')
        self.course = Course.objects.create(
            theme=self.theme,
            title='Test Course',
            description='Desc',
            price=50
        )

    def test_user_can_buy_course(self):
        response = self.client.get(
            reverse('buy_course', args=[self.course.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            CoursePurchase.objects.count(),
            1
        )



class LessonValidationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='student',
            password='password123',
            is_active=True
        )
        self.client.login(username='student', password='password123')

        self.theme = Theme.objects.create(title='Theme', description='Desc')
        self.course = Course.objects.create(
            theme=self.theme,
            title='Course',
            description='Desc',
            price=50
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='Lesson',
            content='Lorem ipsum',
            video_url='https://example.com',
            price=25
        )

    def test_user_can_validate_lesson(self):
        response = self.client.get(
            reverse('validate_lesson', args=[self.lesson.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            LessonValidation.objects.count(),
            1
        )
