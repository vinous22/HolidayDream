from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import BlockQuoteBlock
from django import template


from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel, PageChooserPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import BaseSetting, register_setting

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


@register_setting
class MyCustomSettings(BaseSetting):
    newsletter_form_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)
    content_panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('newsletter_form_page', [
                         'web.NewsletterFormPage']),
    ]


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


class FormField(AbstractFormField):
    newsletter_form_page = ParentalKey('NewsletterFormPage', on_delete=models.CASCADE,
                                       related_name='form_fields')


class NewsletterFormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
