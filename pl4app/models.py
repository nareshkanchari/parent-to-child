from django.db import models


class Course_Category(models.Model):
    ccid = models.AutoField(primary_key=True)
    c_category = models.CharField(max_length=50)

    class Meta:
        db_table = "course_category"

    def __str__(self):
        return self.c_category


class Courses_Data(models.Model):
    course_category=models.ForeignKey(Course_Category,on_delete=models.CASCADE)
    cid = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_disctription = models.TextField(null=True)
    course_duration = models.IntegerField(null=True)
    course_price = models.IntegerField(null=True)

    class Meta:
        db_table = "courses_data"

    def __str__(self):
        return self.course_name
