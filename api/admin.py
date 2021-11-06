from django.contrib import admin
from .models import *
# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Responder)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
