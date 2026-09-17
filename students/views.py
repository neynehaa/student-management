from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)   #browser returns whole form data in request.POST

        if form.is_valid():
            form.save()

            return redirect("student-list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form,
        "is_update": False}
    )

def student_update(request, id):
    student = Student.objects.get(id=id)


    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  #instead of creating a new empty form take the newly submitted data and apply it to this existing student. also we could write literally anything instead of student. The same variable name which we have used here student = student.objects.all(id=id)

        if form.is_valid():
            form.save()

            return redirect("student-list")

    else: 
        form = StudentForm(instance=student)     #The user hasn't submitted anything yet, so show the edit form with this student's existing data already filled in

    return render (request, "students/student_form.html", {"form": form, "is_update": True})

def student_delete(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()

        return redirect("student-list")

    return render(
        request,
        "students/student_delete.html",
        {"student": student}
    )