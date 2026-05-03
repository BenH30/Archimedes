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

PROJECTS = [
    {
        "category": "Panel Wall Systems",
        "description": "Large-scale canopies, enclosing and non-enclosing partitions",
        "items": [
            {
                "name": "Partition 01",
                "location": "Office Reception | Denton, TX",
                "description": "A decorative wall panel system installed behind a reception desk at a new building's main entrance. The panel mimics the look of a grille on a semitruck, featuring offset ellipses as the perforation pattern. Constructed from ½″ aluminum with a chrome finish, the backlit panels were engineered for a seamless appearance with no exposed fasteners or visible welds.",
            },
            {
                "name": "Partition 02",
                "location": "Spec Suite | Dallas, TX",
                "description": "Floor-to-ceiling partition panels fabricated from ¼″ aluminum featuring a square perforation pattern that provides visual interest and spatial separation. The panels create a lightweight yet structurally stable divider that defines the space without fully enclosing it.",
            },
            {
                "name": "Outdoor Canopy",
                "location": "Porte-Cochère of Experience Center | Coppell, TX",
                "description": "A canopy structure built using a 5-by-7 array of perforated aluminum panels designed to provide sun relief while maintaining an open, airy visual connection to the surrounding area. Each panel is crafted from ¼″ thick sheet aluminum, powder coated to match the building’s exterior.",
            },
        ],
    },
    {
        "category": "Interior & Exterior Signage",
        "description": "Wayfinding signs, wall hangings, property and community identification",
        "items": [
            {
                "name": "Identification Signage 01",
                "location": "Wildflower Community | Pagosa Springs, CO",
                "description": "Entry signage for a residential community at the edge of the San Juan National Forest. Designed with creative freedom, the sign incorporates the silhouette of Pagosa Peak and celebrates the area’s signature wildflower landscape.",
            },
            {
                "name": "Identification Signage 02",
                "location": "Eagle Surveying | Denton, TX",
                "description": "Main building signage set against a matte black panel with precision-cut lettering and a dimensional blue eagle logo. Soft backlighting creates a warm halo effect in the evening while maintaining a refined, understated appearance during the day.",
            },
            {
                "name": "Identification Signage 03",
                "location": "Eagle Surveying | Denton, TX",
                "description": "A wrap-around feature displaying the building number and street name in cut-through lettering with hidden bracketry and lighting that creates a floating halo effect. The black metal, warm lighting, and wood accents work in concert with the architectural transition from wood to brick.",
            },
            {
                "name": "Wayfinding Signage 01",
                "location": "Conference Room Corridor | Frisco, TX",
                "description": "Conference room wayfinding with a creative edge — each matte black panel is mounted on a horizontal bracket and features a cutout NFL team logo (Broncos, Cowboys, Saints, Texans), creating consistent visual flow and character throughout the corridor.",
            },
        ],
    },
    {
        "category": "Surface Covers",
        "description": "Paneling that adds decorative flair to walls, vent hoods, counter faces, and more",
        "items": [
            {
                "name": "Surface Cover 01 & 02",
                "location": "Pizza Counter in Experience Center | Coppell, TX",
                "description": "A large overhead vent hood cover in ⅛″ aluminum with a matte brown finish, paired with a perforated white aluminum bar face featuring a repeating triangular pattern. Aluminum sectioning camouflages the seams. Integrated lighting casts soft highlights that accentuate the depth of the cutouts.",
            },
            {
                "name": "Surface Cover 03",
                "location": "Kitchen in Experience Center | Coppell, TX",
                "description": "Copper-colored panels spanning a dramatic 28 by 36 feet across two columns and a furdown above the kitchen area. A button-mount placement method created the illusion of an overlaid diamond lattice before permanent adhesion.",
            },
            {
                "name": "Surface Cover 04",
                "location": "Elevator Lobby Area | Dallas, TX",
                "description": "Perforated ⅛″ aluminum panels finished in matte flat black powder coat, mirroring existing lobby panels while incorporating subtle modifications to integrate with surrounding millwork. The perforations reveal the painted millwork underneath, providing dimension and breaking up the monochromatic tone.",
            },
        ],
    },
    {
        "category": "Post-and-Panel Fencing",
        "description": "Louvered and flat panel fence systems for privacy, HVAC screening, and access control",
        "items": [
            {
                "name": "Louvered Fence 01",
                "location": "HVAC Privacy & Retainment Area | Coppell, TX",
                "description": "A 275-foot perimeter fence enclosing a service area with HVAC equipment and dumpsters. Every post was mapped, anchored, and leveled despite significant grade challenges. Finished in grey powder coat with saloon-style swing gates throughout for easy service access.",
            },
            {
                "name": "Louvered Fence 02",
                "location": "Privacy Entryway | Dallas, TX",
                "description": "A privacy barrier built with a sturdy tube frame, combining solid panels and vertical louver blades for airflow without full enclosure. A custom ½″ aluminum bowtie brace adds visual interest. A push gate allows resident access while restricting external entry.",
            },
        ],
    },
    {
        "category": "Floating Shelving Units",
        "description": "Shelving with no visible supports",
        "items": [
            {
                "name": "Floating Shelving 01",
                "location": "Coffee Counter in Experience Center | Coppell, TX",
                "description": "An 18.5-foot shelf with a smooth oval form that subtly echoes the shape of a coffee bean. Hidden mounting tabs create the floating effect. Anodized to a deep coffee brown that complements surrounding textures. Curved vertical ends provide a bold visual anchor without appearing bulky.",
            },
            {
                "name": "Floating Shelving 02",
                "location": "Bar Area in Experience Center | Coppell, TX",
                "description": "Only 1″ thick overall, these shelves achieve their floating effect through an aluminum sheath covering an internal frame that mounts directly inside the wall. A satin black finish balances visual weight with refined detailing.",
            },
        ],
    },
    {
        "category": "Custom-Fit Framing & Trim",
        "description": "Aluminum extrusions that provide visual transitions between focal points and their surroundings",
        "items": [
            {
                "name": "Custom-Fit Framing 01",
                "location": "Showroom in Experience Center | Coppell, TX",
                "description": "A display frame constructed from stacked square aluminum tubing (3″×3″ and 2″×2″), creating a recessed channel for integrated lighting. Corners are secured with internal joints and mechanical fasteners. Hidden bracketry continues the minimal floating aesthetic.",
            },
            {
                "name": "Custom-Fit Framing 02",
                "location": "Indoor-Outdoor Patio | Dallas, TX",
                "description": "Fountain frames designed to address safety hazards and resident dissatisfaction while elevating the space’s clean, modern aesthetic. The covers minimize overspray, protecting patio furniture and residents from the water feature.",
            },
            {
                "name": "Decorative Trim 01",
                "location": "Lounge Area in Experience Center | Coppell, TX",
                "description": "A minimalist aluminum angle piece wrapping the full perimeter of a fireplace opening, providing a clean transition between large-format stone tile and glass. Anodized satin black with no exposed fasteners, keeping the element visually quiet.",
            },
            {
                "name": "Decorative Trim 02",
                "location": "Experience Center | Coppell, TX",
                "description": "Custom-formed aluminum trim lining curved archways, hand-shaped to follow each arch’s curve. Anodized to a warm champagne brass tone, providing an elegant transition between tile-clad walls and interior spaces.",
            },
            {
                "name": "Decorative Trim 03",
                "location": "Warewash Area in Experience Center | Coppell, TX",
                "description": "Stainless steel top trim capping the tile-clad wall surrounding a dishwashing conveyor. Fit-in-field with a hand-brushed finish, this industrial trim harmonizes with the machinery and polishes off the open-concept layout.",
            },
        ],
    },
    {
        "category": "Brass Features",
        "description": "High-finish brass fabrication for chandeliers, handrails, and architectural details",
        "items": [
            {
                "name": "Brass Chandelier",
                "location": "Deli Counter in Experience Center | Coppell, TX",
                "description": "A statement chandelier with a cage-like frame made from 2″×2″ brushed brass tubing, stretching just over 25 feet in length. Composed of 63 individually fabricated segments with custom aluminum tube joinery hidden inside each connection. Globe pendant lights align rhythmically with the counter below.",
            },
            {
                "name": "Brass Handrails",
                "location": "Hotel Lobby | Dallas, TX",
                "description": "A retrofit of secondary railing supports and anchoring for ADA compliance, fabricated from brushed brass bar stock. Installed in an alternating off-center pattern — a small but intentional detail that adds visual interest without compromising function.",
            },
        ],
    },
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


def projects(request):
    return render(request, "projects.html", {"project_categories": PROJECTS})
