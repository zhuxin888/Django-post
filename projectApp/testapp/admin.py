# Register your models here.
from django.db import models
from django.contrib import admin
from .models import Question, Choice
from .models import Posts


# admin.site.register(Question)
# admin.site.register(Post)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Posts)
