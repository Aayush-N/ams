from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.db.models.signals import post_save, pre_delete
from .middleware import RequestMiddleware

# Create your models here.


class UserType(models.Model):
    """
        UserType: Used to store the type of user Ex: Student, Principal, Professor etc.
    """

    name = models.CharField("Type of User", max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
        User: Used for storing user details
    """

    phone = models.CharField("Phone", max_length=15, null=True, blank=True)
    subjects = models.ManyToManyField("subject", blank=True)
    email = models.EmailField("Email", max_length=250, null=True, blank=True)
    sem = models.CharField("Semester", null=True, blank=True, max_length=50)
    sec = models.CharField("Section", max_length=10, null=True, blank=True)
    department = models.ForeignKey("department", null=True, blank=True)
    user_type = models.ManyToManyField("UserType")
    father = models.CharField("Father's Name", max_length=50, null=True, blank=True)
    mother = models.CharField("Mother's Name", max_length=50, null=True, blank=True)
    phone_parent = models.CharField(
        "Parent's Phone Number", max_length=50, null=True, blank=True
    )


class Subject(models.Model):
    """
        Subject: Holds details about each subject
    """

    name = models.CharField("Subject Name", max_length=50)
    code = models.CharField("Subject Code", max_length=50)

    theory = models.BooleanField(default=True)
    elective = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name + "->" + self.code)


class Teaches(models.Model):
    """
        Teaches: Holds details about the subject that the teacher teaches.
        It links the Subject and the Teacher with the sem, sec and department that they are teaching.
        We are storing sem, sec, deaprtment of the student to get the name of the teacher by matching the
        details with the user table.
    """

    teacher = models.ForeignKey("user")
    subject = models.ForeignKey("subject")

    sem = models.CharField("Student's Semester", max_length=50)
    sec = models.CharField("Student's Section", max_length=50)
    department = models.ForeignKey("department", null=True)

    # 	batch = models.CharField("Student's Batch", max_length=50, null=True, blank=True)
    # 	sub_batch = models.CharField("Student's sub batch", max_length=50, null=True, blank=True)
    # 	ug = models.BooleanField(default=False)

    count = models.IntegerField("Student Count", default=0, null=True, blank=True)

    def __str__(self):
        return (
            self.department.name
            + " -> "
            + self.subject.name
            + " -> "
            + self.sem
            + " "
            + self.sec
        )


class Department(models.Model):
    """
        Department
    """

    name = models.CharField("Department Name", max_length=50)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    """
        Attendance: It stores class details even if no one is absent. 
        It acts as a proof that, that particular class was there.
    """

    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    teaches = models.ForeignKey("teaches", null=True)

    def __str__(self):
        return f"{self.teaches.teacher.first_name} -> {self.date_time}"


class Absentees(models.Model):
    """
        Absentees: Stores the absentees
    """

    user = models.ForeignKey("user")
    attendance = models.ForeignKey("attendance")

    def __str__(self):
        return self.user.first_name


class ChangeStatus(models.Model):
    """
        Stores the details of when the attendance is changed, by whom and to what
    """

    user = models.ForeignKey("user")
    datetime = models.DateTimeField(auto_now_add=True)
    attendance = models.ForeignKey("attendance")
    detail = models.TextField()

    def __str__(self):
        return self.detail

    class Meta:
        verbose_name_plural = "Logs"


def create_status(sender, instance, created=None, **kwargs):
    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    if request.user.is_superuser:
        if created:
            detail = f"Admin marked {instance.user.first_name} absentee for class {instance.attendance.teaches.subject}"
        else:
            detail = f"Admin marked {instance.user.first_name} present for class {instance.attendance.teaches.subject}"
        ChangeStatus.objects.create(
            user=request.user, attendance=instance.attendance, detail=detail
        )


post_save.connect(create_status, sender=Absentees)
pre_delete.connect(create_status, sender=Absentees)
