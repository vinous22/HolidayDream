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

    def get_context(self, request):
        context = super().get_context(request)
        components = self.get_children()
        context['featured'] = components.type(FeaturedIndexPage)
        context['teams'] = components.type(TeamIndexPage)
        context['activities'] = components.type(ActivityIndexPage)
        return context

# featured area


class FeaturedIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


class FeaturedPage(Page):
    body = StreamField([
        ('image', ImageChooserBlock(blank=True)),
        ('button', blocks.CharBlock(blank=True)),
        ('paragraph', blocks.CharBlock(blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

# team area


class TeamIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


class TeamMemberPage(Page):

    body = StreamField([
        ('image', ImageChooserBlock(blank=True)),
        ('name', blocks.CharBlock(blank=True)),
        ('paragraph', blocks.CharBlock(blank=True)),
        ('button', blocks.CharBlock(blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ActivityIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


class ActivityPage(Page):
    body = StreamField([
        ('image', ImageChooserBlock(blank=True)),
        ('name', blocks.CharBlock(blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
