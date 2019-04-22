from django.contrib import admin
from ask.models import Question, Usr, Tag, Answer, QuestionLike, AnswerLike

admin.site.register(Question)
admin.site.register(Usr)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(QuestionLike)
admin.site.register(AnswerLike)
