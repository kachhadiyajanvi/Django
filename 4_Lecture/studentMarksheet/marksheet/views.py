from django.shortcuts import render

# Create your views here.
student_data = {
    "1001": {
        "name": "John Doe",
        "math": 95,
        "english": 88,
        "science": 92,
        "history": 85,
    },
    "1002": {
        "name": "Jane Smith",
        "math": 80,
        "english": 75,
        "science": 82,
        "history": 78,
    },
    "1003": {
        "name": "Michael Johnson",
        "math": 98,
        "english": 91,
        "science": 94,
        "history": 89,
    },
    "1004": {
        "name": "Emily Davis",
        "math": 70,
        "english": 65,
        "science": 72,
        "history": 60,
    },
    "1005": {
        "name": "Chris Lee",
        "math": 23,
        "english": 25,
        "science": 26,
        "history": 28,
    },
}

def home(request):
    return render(request, "marksheet/home.html")

def result(request):
    enroll_no = request.GET.get("enroll_no")
    student = None
    error = None

    if enroll_no:
        if enroll_no in student_data:
            marks = student_data[enroll_no]
            total = marks["math"] + marks["english"] + marks["science"] + marks["history"]
            percentage = total / 4

            student = {
                "enroll_no": enroll_no,
                "name": marks["name"],
                "math": marks["math"],
                "english": marks["english"],
                "science": marks["science"],
                "history": marks["history"],
                "total": total,
                "percentage": percentage,
            }
        else:
            error = "Student not found!"

    return render(request, "marksheet/result.html", {
        "student": student,
        "error": error
    })

def all_students(request):
    students = [{"enroll_no": enroll_no, "name": student["name"]} for enroll_no, student in student_data.items()]
    return render(request, "marksheet/students_list.html", {
        "students": students
    })