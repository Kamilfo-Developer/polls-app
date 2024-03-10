from django.contrib import admin

from .models import (
    MultipleChoicesAnswer,
    MultipleChoicesOption,
    MultipleChoicesQuestion,
    Poll,
    SingleChoiceAnswer,
    SingleChoiceOption,
    SingleChoiceQuestion,
    TextAnswer,
    TextQuestion,
)

# Register your models here.


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    readonly_fields = ["start_date"]


admin.site.register(SingleChoiceAnswer)
admin.site.register(MultipleChoicesAnswer)
admin.site.register(TextAnswer)

admin.site.register(TextQuestion)
admin.site.register(MultipleChoicesQuestion)
admin.site.register(SingleChoiceQuestion)
admin.site.register(MultipleChoicesOption)
admin.site.register(SingleChoiceOption)
