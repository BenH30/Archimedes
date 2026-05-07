from django.contrib.sitemaps import Sitemap
from django.urls import reverse


STATIC_PAGES = [
    ("home", 1.0, "weekly"),
    ("services_index", 0.9, "monthly"),
    ("projects", 0.9, "monthly"),
    ("about", 0.6, "monthly"),
    ("contact", 0.7, "monthly"),
]

SERVICE_SLUGS = [
    "architectural-metalwork",
    "metal-wall-panels",
    "custom-metal-signage",
    "fencing-screens-enclosures",
    "shelving-trim-brass",
    "press-brake-forming",
    "welding",
    "coatings-finishes",
]


class StaticViewSitemap(Sitemap):
    def items(self):
        return STATIC_PAGES

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]


class ServiceSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return SERVICE_SLUGS

    def location(self, item):
        return reverse("service_detail", kwargs={"slug": item})
