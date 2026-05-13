from django.conf import settings


def site_url(request):
    return {"SITE_URL": getattr(settings, "SITE_URL", "https://archimedesmetals.com")}


def nav_data(request):
    from django.utils.text import slugify
    from core.views import SERVICES, PROJECTS
    return {
        "nav_services": [{"name": s["name"], "url": s["url"]} for s in SERVICES],
        "nav_project_categories": [
            {"name": c["category"], "anchor": slugify(c["category"])}
            for c in PROJECTS
        ],
    }
