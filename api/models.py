import uuid

from django.db import models


class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    bg_url = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'branch'

class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'semester'

class SubjectType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    semester_code = models.CharField(max_length=6)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subject'

class QuestionPaper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=6)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester_code = models.CharField(max_length=6)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    file_id = models.CharField(max_length=255)
    file_size = models.IntegerField()
    file_format = models.CharField(max_length=20)
    thumb = models.URLField()
    subject_code = models.CharField(max_length=6)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Question Paper for {self.subject} - Year {self.year}"
    
    class Meta:
        db_table = 'questionpaper'

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=6)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester_code = models.CharField(max_length=6)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
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