from django.shortcuts import render


SERVICES = [
    {
        "name": "Architectural Metalwork",
        "description": "Custom metal features for commercial interiors and exteriors — panels, trim, framing, and design-forward details.",
        "icon": "🏗️",
        "url": "/services/architectural-metalwork/",
    },
    {
        "name": "Metal Wall Panels",
        "description": "Architectural metal wall panel systems and cladding for commercial interiors and building exteriors.",
        "icon": "🔲",
        "url": "/services/metal-wall-panels/",
    },
    {
        "name": "Custom Metal Signage",
        "description": "Interior and exterior metal signs, logo features, and building identification for commercial spaces.",
        "icon": "🪧",
        "url": "/services/custom-metal-signage/",
    },
    {
        "name": "Fencing, Screens & Enclosures",
        "description": "Post-and-panel fencing, privacy screens, dumpster enclosures, and HVAC equipment screens.",
        "icon": "🛡️",
        "url": "/services/fencing-screens-enclosures/",
    },
    {
        "name": "Shelving, Trim & Brass Features",
        "description": "Floating metal shelves, custom-fit framing, decorative trim, and high-finish brass features.",
        "icon": "✨",
        "url": "/services/shelving-trim-brass/",
    },
    {
        "name": "Press Brake & Forming",
        "description": "Precision sheet metal bending and forming for custom aluminum, stainless steel, and steel components.",
        "icon": "⚙️",
        "url": "/services/press-brake-forming/",
    },
    {
        "name": "Welding",
        "description": "Aluminum TIG, stainless steel, and commercial welding for architectural and structural metal scopes.",
        "icon": "🔥",
        "url": "/services/welding/",
    },
    {
        "name": "Coatings & Finishes",
        "description": "Powder coating, brushed finishes, anodizing, polishing, and painted aluminum panels.",
        "icon": "🎨",
        "url": "/services/coatings-finishes/",
    },
]


def home(request):
    return render(request, "home.html", {"services": SERVICES})
