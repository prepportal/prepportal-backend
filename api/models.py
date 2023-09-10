import uuid

from django.db import models


class Branch(models.Model):
    branch_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    bg_url = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'branch'

class SemesterGroup(models.Model):
    semester_group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'semestergroup'

class Semester(models.Model):
    semester_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    semester_group = models.ForeignKey(SemesterGroup, on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch, related_name="semester")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'semester'

class SubjectType(models.Model):
    subject_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subjecttype'

class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subject'

class QuestionPaper(models.Model):
    question_paper_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    file_id = models.CharField(max_length=255)
    file_size = models.IntegerField()
    file_format = models.CharField(max_length=20)
    thumb = models.URLField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Question Paper for {self.subject} - Year {self.year}"
    
    class Meta:
        db_table = 'questionpaper'

class Note(models.Model):
    note_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255)
    file_size = models.IntegerField()
    file_format = models.CharField(max_length=20)
    thumb = models.URLField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'note'