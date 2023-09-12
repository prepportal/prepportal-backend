from django.contrib import admin
from api.models import Branch, Semester, Subject, SubjectType, QuestionPaper, Note

# Register your models here.
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(SubjectType)
admin.site.register(QuestionPaper)
admin.site.register(Note)