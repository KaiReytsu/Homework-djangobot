from multiprocessing import context
from django.shortcuts import render
from . import models

def index(request):
    lessons = models.Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'lessons/lessons.html', context)


def marks(request):
    studs_vs_marks = []
    context = {'data':[]}
    for mark in models.Student.objects.all():
        for lesson in models.Lesson.objects.all():
            subjects = models.Mark.objects.filter(student = mark).filter(lesson=lesson)
            if len(subjects):
                studs_vs_marks.append(subjects)
    for stud in studs_vs_marks:
        mean = 0

        for subject in stud:
            print([subject.lesson])
            mean += subject.grade
        context['data'].append({'student':stud[0].student, 'lesson':stud[0].lesson, 'mark': mean/float(len(stud))})

    return render(request, 'lessons/students.html', context)