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
        context['staticPage'] = components.type(StaticPage)
        return context


@register_setting
class Footer(BaseSetting):
    title_left = models.CharField(max_length=250)
    list_item1_left = models.CharField(max_length=250, blank=True, null=True)
    list_item2_left = models.CharField(max_length=250, blank=True, null=True)
    list_item3_left = models.CharField(max_length=250, blank=True, null=True)
    list_item4_left = models.CharField(max_length=250, blank=True, null=True)
    list_item5_left = models.CharField(max_length=250, blank=True, null=True)
    list_item6_left = models.CharField(max_length=250, blank=True, null=True)
    logo_left = models.CharField(max_length=250, blank=True, null=True)

    title_right = models.CharField(max_length=250)
    list_item1_right = models.CharField(max_length=250, blank=True, null=True)
    list_item2_right = models.CharField(max_length=250, blank=True, null=True)
    list_item3_right = models.CharField(max_length=250, blank=True, null=True)
    list_item4_right = models.CharField(max_length=250, blank=True, null=True)
    list_item5_right = models.CharField(max_length=250, blank=True, null=True)
    list_item6_right = models.CharField(max_length=250, blank=True, null=True)
    logo_right = models.ImageField(
        upload_to='images/', default='images/areto.jpg')

    content_panels = Page.content_panels + [
        FieldPanel('title_left '),
        FieldPanel('list_item1_left'),
        FieldPanel('list_item2_left'),
        FieldPanel('list_item3_left'),
        FieldPanel('list_item4_left'),
        FieldPanel('list_item5_left'),

        FieldPanel('title_right'),
        FieldPanel('list_item1_right'),
        FieldPanel('list_item2_right'),
        FieldPanel('list_item3_right'),
        FieldPanel('list_item4_right'),
        FieldPanel('list_item5_right'),
    ]

    class Meta:
        verbose_name = 'footer settings'


@register_setting
class NewsletterCustomSettings(BaseSetting):
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


class StaticPage(Page):
    body = StreamField([
        ('title', blocks.CharBlock(blank=True)),
        ('lead', blocks.CharBlock(blank=True)),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(blank=True)),
        ('quote', BlockQuoteBlock(blank=True)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    newsletter_form_page = ParentalKey('NewsletterFormPage', on_delete=models.CASCADE,
                                       related_name='form_fields')


class NewsletterFormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_title = models.CharField(max_length=250, blank=True, null=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_title'),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
