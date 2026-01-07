from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Theme,
    Course,
    Lesson,
    CoursePurchase,
    LessonPurchase,
    LessonValidation,
    CourseValidation,
    Certification
)
from django.contrib import messages





def theme_list(request):
    """
    Displays the list of all training themes.
    Each theme contains one or more courses.
    """
    themes = Theme.objects.all()
    return render(request, 'courses/theme_list.html', {'themes': themes})


def course_detail(request, course_id):
    """
    Displays course details.

    Determines whether the authenticated user has already
    purchased or validated the course in order to adapt
    the user interface accordingly.
    """
    course = get_object_or_404(Course, id=course_id)

    has_purchased = False
    is_validated = False

    if request.user.is_authenticated:
        # Check if the user has already purchased the course
        has_purchased = CoursePurchase.objects.filter(
            user=request.user,
            course=course
        ).exists()

        # Check if the course has already been validated
        is_validated = CourseValidation.objects.filter(
            user=request.user,
            course=course
        ).exists()

    return render(
        request,
        'courses/course_detail.html',
        {
            'course': course,
            'has_purchased': has_purchased,
            'is_validated': is_validated
        }
    )





def lesson_detail(request, lesson_id):
    """
    Displays lesson details.

    Access is granted only if the lesson or the related course
    has been purchased. The validation status is also checked
    to prevent duplicate validations.
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)

    has_access = False
    is_validated = False

    if request.user.is_authenticated:
        # Check access rights (lesson or course purchased)
        has_access = (
            LessonPurchase.objects.filter(
                user=request.user,
                lesson=lesson
            ).exists()
            or
            CoursePurchase.objects.filter(
                user=request.user,
                course=lesson.course
            ).exists()
        )

        # Check if the lesson has already been validated
        is_validated = LessonValidation.objects.filter(
            user=request.user,
            lesson=lesson
        ).exists()

    return render(
        request,
        'courses/lesson_detail.html',
        {
            'lesson': lesson,
            'has_access': has_access,
            'is_validated': is_validated
        }
    )


@login_required
def buy_course(request, course_id):
    """
    Simulates the purchase of a course.
    Creates a CoursePurchase entry for the authenticated user.
    """
    course = get_object_or_404(Course, id=course_id)

    purchase, created = CoursePurchase.objects.get_or_create(
        user=request.user,
        course=course
    )

    if created:
        messages.success(request, "Course successfully purchased.")
    else:
        messages.info(request, "You have already purchased this course.")


    return redirect('course_detail', course_id=course.id)


@login_required
def buy_lesson(request, lesson_id):
    """
    Simulates the purchase of a single lesson.
    Creates a LessonPurchase entry for the authenticated user.
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)

    purchase, created = LessonPurchase.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )

    if created:
        messages.success(request, "Lesson successfully purchased.")
    else:
        messages.info(request, "You have already purchased this lesson.")

    return redirect('lesson_detail', lesson_id=lesson.id)



@login_required
def validate_lesson(request, lesson_id):
    """
    Validates a lesson for the authenticated user.
    If all lessons of the related course are validated,
    the course is automatically validated.
    If all courses of the related theme are validated,
    a certification is automatically awarded.
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)

    LessonValidation.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )

    course = lesson.course
    total_lessons = course.lessons.count()
    validated_lessons = LessonValidation.objects.filter(
        user=request.user,
        lesson__course=course
    ).count()

    if total_lessons == validated_lessons:
        CourseValidation.objects.get_or_create(
            user=request.user,
            course=course
        )

        theme = course.theme
        total_courses = theme.courses.count()
        validated_courses = CourseValidation.objects.filter(
            user=request.user,
            course__theme=theme
        ).count()

        if total_courses == validated_courses:
            Certification.objects.get_or_create(
                user=request.user,
                theme=theme
            )

    return redirect('lesson_detail', lesson_id=lesson.id)


@login_required
def my_certifications(request):
    """
    Displays the list of certifications obtained by the authenticated user.
    """
    certifications = Certification.objects.filter(user=request.user)
    return render(
        request,
        'courses/my_certifications.html',
        {'certifications': certifications}
    )
