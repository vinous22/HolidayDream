from django import template
from holidaydream_project.web.models import NewsletterCustomSettings

register = template.Library()


@register.simple_tag(takes_context=True)
def get_newsletter_form(context):
    request = context['request']
    newsletter_custom_settings = NewsletterCustomSettings.for_site(
        request.site)
    newsletter_form_page = newsletter_custom_settings.newsletter_form_page.specific
    form = newsletter_form_page.get_form(
        page=newsletter_form_page, user=request.user)
    return {'page': newsletter_form_page, 'form': form}
