from django.db import models

from django.db import models
from django.contrib.auth.models import User
import inspect
from .utility import report_gen

# Create your models here.


class Student(models.Model):
    # student_id pulled from Canvas_API
    student_id = models.IntegerField()
    # first_name from Canvas_API based on Student_ID
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    # class_key from Canvas_API (student instances should only be
    # created for students whose class_code are equivalant to "401")
    # if a class is somehow deleted, class_key will be set to None. implement
    class_key = models.ForeignKey(ClassList, to_field='class_code')
    instructor_key = models.ForeignKey(Instructors,to_field='instructor_id')
    # class_hist is a list of class_id instances that the Student has been enrolled in.
    class_hist = models.JSONField()
    scheduled = models.BooleanField(default=False)
    attempts = models.IntegerField()
    email = models.URLField()





    def __str__(self):
        return self.first_name + self.last_name + self.student_id


    # method to check if student is scheduled
    def _is_scheduled__(self):
        pass

    # method fetches data from db regarding all wb records where student_key and
    # and class_key match student record student_id and class_key (composite key??)
    def _get_history(self):
        pass
    


class ClassList(models.Model):
    class_code = models.CharField(max_len=64)
    instructor_key = models.ForeignKey(Instructors, to_field='instructor_id')




    def __str__(self):
        return str(self.class_code)
    

    def __repr__(self):
        return self.pk

    



class Instructors(models.Model):
    # TODO: determine if we should use default pk or assign pk based on Canvas info. 
    instructor_id = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    # pulled from Slack upon first sign-in
    email = models.URLField()
    # we may need to add a dropdown to the my_class_view allowing the instructor to select
    # which of their classes they wish to view, unless the Canvas info has an indicator of 
    # which class is currently  assigned to the instructor
    class_key = models.ForeignKey(ClassList, to_field='class_code')




    def __str__(self):
        return str(self.first_name + self.last_name + self.instructor_id)



class Whiteboard(models.Model):
    student_key = models.ForeignKey(Student, to_field='student_id')
    interviewer_key = models.ForeignKey(Instructors, to_field='instructor_id' )
    # problem_domain_key may actually just be a URL field referencign the github api endpoint. no need for a seperate table.
    problem_domain_url = models.URLField()
    category_notes_key = models.ForeignKey(CategoryNotes, on_delete=models.CASCADE)
    score_key = models.ForeignKey(ScoreTable, on_delete=models.CASCADE)
    wb_image = models.ForeignKey(WhiteboardImage, on_delete=models.CASCADE)
    date = models.DateTimeField()
    passed = models.BooleanField(default=False)
    


    def __str__(self):
        return str(self.problem_domain_key + self.date + self.student_key + self.passed)


    # checks if whiteboard is pending or complete. returns ---> "pending" + self.date
    def _status(self):
        pass



class WhiteboardImage(models.Model):
    whiteboard_key = models.ForeignKey(Whiteboard)
    student_whiteboard = models.ImageField(defualt=Null, null=True, blank=True)


    def __str__(self):
        # FIXME: does a plain image file have a defualt property of Name?? how would it be referenced from this field???
        # is it format dependent? is there a default if no name is supplied? I should know this!
        return str(self.student_whiteboard)



class CategoryNotes(models.Model):
    whiteboard_key = models.ForeignKey(Whiteboard)
    interpretation = models.TextField(default='')
    solved_technical = models.TextField(default='')
    analyzed_solution = models.TextField(default='')
    communication = models.TextField(default='')
    general = models.TextField(default='')


    def __str__(self):
        return str([cat[:16] for cat in self._meta.fields])



class ScoreTable(models.Model):
    
    whiteboard_key = models.ForeignKey(Whiteboard)
    identified = models.IntegerField()
    visual = models.IntegerField()
    ident_optimal = models.IntegerField()
    presented = models.IntegerField()
    syntax = models.IntegerField()
    idioms = models.IntegerField()
    best_solve = models.IntegerField()
    asked = models.IntegerField()
    step_through = models.IntegerField()
    big_o = models.IntegerField()
    testing = models.IntegerField()
    verbal = models.IntegerField()
    terms = models.IntegerField()
    time = models.IntegerField()
    over = models.IntegerField()
    under = models.IntegerField()
    readable = models.IntegerField()









    
    




