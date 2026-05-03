from django.shortcuts import render, redirect


SERVICES = [
    {"name": "Architectural Metalwork", "description": "Custom metal features for commercial interiors and exteriors — panels, trim, framing, and design-forward details.", "url": "/services/architectural-metalwork/"},
    {"name": "Metal Wall Panels", "description": "Architectural metal wall panel systems and cladding for commercial interiors and building exteriors.", "url": "/services/metal-wall-panels/"},
    {"name": "Custom Metal Signage", "description": "Interior and exterior metal signs, logo features, and building identification for commercial spaces.", "url": "/services/custom-metal-signage/"},
    {"name": "Fencing, Screens & Enclosures", "description": "Post-and-panel fencing, privacy screens, dumpster enclosures, and HVAC equipment screens.", "url": "/services/fencing-screens-enclosures/"},
    {"name": "Shelving, Trim & Brass Features", "description": "Floating metal shelves, custom-fit framing, decorative trim, and high-finish brass features.", "url": "/services/shelving-trim-brass/"},
    {"name": "Press Brake & Forming", "description": "Precision sheet metal bending and forming for custom aluminum, stainless steel, and steel components.", "url": "/services/press-brake-forming/"},
    {"name": "Welding", "description": "Aluminum TIG, stainless steel, and commercial welding for architectural and structural metal scopes.", "url": "/services/welding/"},
    {"name": "Coatings & Finishes", "description": "Powder coating, brushed finishes, anodizing, polishing, and painted aluminum panels.", "url": "/services/coatings-finishes/"},
]

AUDIENCES = [
    {"name": "General Contractors", "description": "Clean coordination, precise fabrication, strong submittals, and fewer field surprises."},
    {"name": "Architects & Interior Designers", "description": "From concept to installed detail — buildable, durable, high-finish architectural elements."},
    {"name": "Commercial Owners & Developers", "description": "Better curb appeal, longer-lasting signage, cleaner service areas, stronger brand presence."},
    {"name": "Sign & Millwork Companies", "description": "Specialty metal capability and added bandwidth — without threatening your customer relationships."},
    {"name": "Restaurants, Retail & Hospitality", "description": "Metal features that look sharp, hold up to daily use, and match your brand vision."},
]

DIFFERENTIATORS = [
    {"name": "Craftsmanship + Communication", "description": "Many fabricators can weld. Fewer can communicate scope, constraints, finish expectations, and schedule risks clearly from day one."},
    {"name": "Commercial Construction Ready", "description": "Field measurement, submittal support, shop drawings, finish samples, and installation planning — the full coordination package."},
    {"name": "Custom Problem-Solving", "description": "Design-forward work: signage, panels, shelving, fencing, brass features, and custom trim. Non-standard scopes are our standard."},
    {"name": "High-Finish Metalwork", "description": "Our work belongs in spaces where the metal is seen, touched, photographed, and judged. We take that seriously."},
]

ABOUT_VALUES = [
    {"title": "We Care About Design", "body": "Decorative metalwork is often highly visible. It has to support the architecture, the brand, and the experience of the space. We pay attention to proportion, finish, alignment, and the way each detail fits into the larger environment."},
    {"title": "We Communicate Clearly", "body": "Custom fabrication involves decisions, constraints, and trade-offs. We believe in being transparent about scope, schedule, budget, materials, finishes, and fabrication realities so the project team can make good decisions early."},
    {"title": "We Solve Problems", "body": "Some scopes do not come with a perfect template. That is where we thrive. We help turn sketches, drawings, concepts, field conditions, and unusual requirements into practical fabricated solutions."},
    {"title": "We Care About the Result", "body": "Good enough is not the standard. Our goal is to deliver work that looks right, fits correctly, holds up over time, and reflects well on everyone involved in the project."},
]

QUOTE_NEEDS = [
    "Drawings, sketches, or reference photos",
    "Material type (aluminum, stainless, mild steel, brass)",
    "Dimensions and quantities",
    "Finish requirements (powder coat color, brushed, polished, etc.)",
    "Timeline or bid deadline",
    "Installation needed or fabrication only",
    "Tolerance expectations for precision work",
]


def home(request):
    return render(request, "home.html", {
        "services": SERVICES,
        "audiences": AUDIENCES,
        "differentiators": DIFFERENTIATORS,
    })


def about(request):
    return render(request, "about.html", {"values": ABOUT_VALUES})


def contact(request):
    if request.method == "POST":
        # Form submission received — placeholder for email sending
        return render(request, "contact.html", {
            "submitted": True,
            "quote_needs": QUOTE_NEEDS,
        })
    return render(request, "contact.html", {
        "submitted": False,
        "quote_needs": QUOTE_NEEDS,
    })


def privacy(request):
    return render(request, "privacy.html")
