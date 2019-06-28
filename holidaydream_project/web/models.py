from django.db import models
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import BlockQuoteBlock

# Create your models here.


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    body = StreamField([
        ('image', ImageChooserBlock(blank=True)),
        ('button', blocks.CharBlock(blank=True)),
        ('paragraph', blocks.CharBlock(blank=True)),
        ('quote', BlockQuoteBlock(blank=True)),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]
