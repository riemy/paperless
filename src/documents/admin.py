from django.conf import settings
from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):

    search_fields = ("sender", "title", "content",)
    list_display = ("created", "sender", "title", "thumbnail", "pdf")
    list_filter = ("created", "sender")
    save_on_top = True

    def thumbnail(self, obj):
        return '<a href="{media}documents/img/{pk:07}.jpg" target="_blank">' \
                 '<img src="{media}documents/img/{pk:07}.jpg" width="100" />' \
               '</a>'.format(media=settings.MEDIA_URL, pk=obj.pk)
    thumbnail.allow_tags = True

    def pdf(self, obj):
        return '<a href="{}documents/pdf/{:07}.pdf">Download</a>'.format(
            settings.MEDIA_URL, obj.pk)
    pdf.allow_tags = True

admin.site.register(Document, DocumentAdmin)
