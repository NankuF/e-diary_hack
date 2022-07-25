import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation


def get_child(full_name):
    """
    Сервисная функция для обработки получения ученика.
    """
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except MultipleObjectsReturned:
        print('Введите полностью ФИО.')
    except ObjectDoesNotExist:
        print('Такого ФИО нет в базе данных.')


def fix_marks(full_name):
    """
    Исправляет оценки ученика. Все тройки меняет на пятерки.

    :param full_name: фамилия, имя и отчество.
    """
    child = get_child(full_name)
    points = Mark.objects.filter(schoolkid=child, points__lte=3)
    points.update(points=5)


def remove_chastisements(full_name):
    """
    Удаляет замечания от учителей.

    :param full_name: фамилия, имя и отчество.
    """
    child = get_child(full_name)
    Chastisement.objects.filter(schoolkid=child).delete()


def create_commendation(full_name):
    """
    Добавляет похвалу от учителя.

    :param full_name: фамилия, имя и отчество.
    :param lesson_name: название урока.
    """
    texts = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
    ]

    child = get_child(full_name)
    while True:
        lesson_name = input('Введите название урока: ').strip()
        lesson = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title=lesson_name)
        if not len(lesson):
            print('Такого урока не существует.')
            continue
        break
    first_lesson = lesson.order_by('-date').first()
    Commendation.objects.create(text=random.choice(texts), created=first_lesson.date, subject=first_lesson.subject,
                                teacher=first_lesson.teacher, schoolkid=child)
