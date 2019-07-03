from holidaydream_project.web.models import Footer


def view(request):
    footer = Footer.for_site(request.site)
