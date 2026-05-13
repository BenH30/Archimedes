import json
import logging
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import Http404, HttpResponse

logger = logging.getLogger(__name__)


SERVICES = [
    {"name": "Engineered Design", "slug": "engineered-design", "hero_image": "framing-01", "description": "Design consultation, CAD modeling, shop drawings, submittal packages, and field measurement — the full pre-production engineering scope.", "url": "/services/engineered-design/"},
    {"name": "Fabrication & Site Services", "slug": "fabrication-site-services", "hero_image": "outdoor-canopy", "description": "Complete in-house fabrication and commercial installation for architectural metal scopes of all sizes.", "url": "/services/fabrication-site-services/"},
    {"name": "CNC Routing", "slug": "cnc-routing", "hero_image": "partition-02", "description": "Precision CNC cutting for custom perforation patterns, dimensional lettering, logo cutouts, and architectural panel components.", "url": "/services/cnc-routing/"},
    {"name": "Press Brake", "slug": "press-brake", "hero_image": "trim-03", "description": "Precision sheet metal bending and forming for custom trim profiles, panel returns, and complex architectural components.", "url": "/services/press-brake/"},
    {"name": "Welding", "slug": "welding", "hero_image": "weld-02", "description": "Aluminum TIG, stainless steel, mild steel, and brass welding for structural and architectural metal scopes.", "url": "/services/welding/"},
    {"name": "Coatings & Finishes", "slug": "coatings-finishes", "hero_image": "coat-02", "description": "Powder coating, brushed finishes, anodizing, and painted panel systems for commercial architectural metalwork.", "url": "/services/coatings-finishes/"},
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
        "slug": "panel-wall-systems",
        "service_url": "/services/fabrication-site-services/",
        "description": "Large-scale canopies, enclosing and non-enclosing partitions",
        "items": [
            {
                "name": "Partition 01",
                "location": "Office Reception | Denton, TX",
                "image": "partition-01",
                "images": ["partition-01"],
                "description": "A decorative wall panel system installed behind a reception desk at a new building's main entrance. The panel mimics the look of a grille on a semitruck, featuring offset ellipses as the perforation pattern. Constructed from ½″ aluminum with a chrome finish, the backlit panels were engineered for a seamless appearance with no exposed fasteners or visible welds.",
            },
            {
                "name": "Partition 02",
                "location": "Spec Suite | Dallas, TX",
                "image": "partition-02",
                "images": ["partition-02", "partition-02-2"],
                "description": "Floor-to-ceiling partition panels fabricated from ¼″ aluminum featuring a square perforation pattern that provides visual interest and spatial separation. The panels create a lightweight yet structurally stable divider that defines the space without fully enclosing it.",
            },
            {
                "name": "Outdoor Canopy",
                "location": "Porte-Cochère of Experience Center | Coppell, TX",
                "image": "outdoor-canopy",
                "images": ["outdoor-canopy", "outdoor-canopy-2", "outdoor-canopy-3"],
                "description": "A canopy structure built using a 5-by-7 array of perforated aluminum panels designed to provide sun relief while maintaining an open, airy visual connection to the surrounding area. Each panel is crafted from ¼″ thick sheet aluminum, powder coated to match the building's exterior.",
            },
        ],
    },
    {
        "category": "Interior & Exterior Signage",
        "slug": "signage",
        "service_url": "/services/fabrication-site-services/",
        "description": "Wayfinding signs, wall hangings, property and community identification",
        "items": [
            {
                "name": "Identification Signage 01",
                "location": "Wildflower Community | Pagosa Springs, CO",
                "image": "signage-wildflower",
                "images": ["signage-wildflower", "signage-wildflower-gallery", "signage-wildflower-gallery-2", "signage-wildflower-gallery-3"],
                "description": "Entry signage for a residential community at the edge of the San Juan National Forest. Designed with creative freedom, the sign incorporates the silhouette of Pagosa Peak and celebrates the area's signature wildflower landscape.",
            },
            {
                "name": "Identification Signage 02",
                "location": "Eagle Surveying | Denton, TX",
                "image": "signage-eagle-02",
                "images": ["signage-eagle-02"],
                "description": "Main building signage set against a matte black panel with precision-cut lettering and a dimensional blue eagle logo. Soft backlighting creates a warm halo effect in the evening while maintaining a refined, understated appearance during the day.",
            },
            {
                "name": "Identification Signage 03",
                "location": "Eagle Surveying | Denton, TX",
                "image": "signage-eagle-03",
                "images": ["signage-eagle-03", "signage-eagle-03-2"],
                "description": "A wrap-around feature displaying the building number and street name in cut-through lettering with hidden bracketry and lighting that creates a floating halo effect. The black metal, warm lighting, and wood accents work in concert with the architectural transition from wood to brick.",
            },
            {
                "name": "Wayfinding Signage 01",
                "location": "Conference Room Corridor | Frisco, TX",
                "image": "signage-wayfinding",
                "images": ["signage-wayfinding", "signage-wayfinding-2"],
                "description": "Conference room wayfinding with a creative edge — each matte black panel is mounted on a horizontal bracket and features a cutout NFL team logo (Broncos, Cowboys, Saints, Texans), creating consistent visual flow and character throughout the corridor.",
            },
        ],
    },
    {
        "category": "Surface Covers",
        "slug": "surface-covers",
        "service_url": "/services/cnc-routing/",
        "description": "Paneling that adds decorative flair to walls, vent hoods, counter faces, and more",
        "items": [
            {
                "name": "Surface Cover 01 & 02",
                "location": "Pizza Counter in Experience Center | Coppell, TX",
                "image": "surface-cover-01-02",
                "images": ["surface-cover-01-02", "surface-cover-01-02-2", "surface-cover-01-02-3"],
                "description": "A large overhead vent hood cover in ⅛″ aluminum with a matte brown finish, paired with a perforated white aluminum bar face featuring a repeating triangular pattern. Aluminum sectioning camouflages the seams. Integrated lighting casts soft highlights that accentuate the depth of the cutouts.",
            },
            {
                "name": "Surface Cover 03",
                "location": "Kitchen in Experience Center | Coppell, TX",
                "image": "surface-cover-03",
                "images": ["surface-cover-03", "surface-cover-03-2", "surface-cover-03-3"],
                "description": "Copper-colored panels spanning a dramatic 28 by 36 feet across two columns and a furdown above the kitchen area. A button-mount placement method created the illusion of an overlaid diamond lattice before permanent adhesion.",
            },
            {
                "name": "Surface Cover 04",
                "location": "Elevator Lobby Area | Dallas, TX",
                "image": "surface-cover-04",
                "images": ["surface-cover-04", "surface-cover-04-2"],
                "description": "Perforated ⅛″ aluminum panels finished in matte flat black powder coat, mirroring existing lobby panels while incorporating subtle modifications to integrate with surrounding millwork. The perforations reveal the painted millwork underneath, providing dimension and breaking up the monochromatic tone.",
            },
        ],
    },
    {
        "category": "Post-and-Panel Fencing",
        "slug": "fencing",
        "service_url": "/services/fabrication-site-services/",
        "description": "Louvered and flat panel fence systems for privacy, HVAC screening, and access control",
        "items": [
            {
                "name": "Louvered Fence 01",
                "location": "HVAC Privacy & Retainment Area | Coppell, TX",
                "image": "fence-louvered-01",
                "images": ["fence-louvered-01"],
                "description": "A 275-foot perimeter fence enclosing a service area with HVAC equipment and dumpsters. Every post was mapped, anchored, and leveled despite significant grade challenges. Finished in grey powder coat with saloon-style swing gates throughout for easy service access.",
            },
            {
                "name": "Louvered Fence 02",
                "location": "Privacy Entryway | Dallas, TX",
                "image": "fence-louvered-02",
                "images": ["fence-louvered-02", "fence-louvered-02-2"],
                "description": "A privacy barrier built with a sturdy tube frame, combining solid panels and vertical louver blades for airflow without full enclosure. A custom ½″ aluminum bowtie brace adds visual interest. A push gate allows resident access while restricting external entry.",
            },
        ],
    },
    {
        "category": "Floating Shelving Units",
        "slug": "floating-shelving",
        "service_url": "/services/fabrication-site-services/",
        "description": "Shelving with no visible supports",
        "items": [
            {
                "name": "Floating Shelving 01",
                "location": "Coffee Counter in Experience Center | Coppell, TX",
                "image": "shelving-01",
                "images": ["shelving-01"],
                "description": "An 18.5-foot shelf with a smooth oval form that subtly echoes the shape of a coffee bean. Hidden mounting tabs create the floating effect. Anodized to a deep coffee brown that complements surrounding textures. Curved vertical ends provide a bold visual anchor without appearing bulky.",
            },
            {
                "name": "Floating Shelving 02",
                "location": "Bar Area in Experience Center | Coppell, TX",
                "image": "shelving-02",
                "images": ["shelving-02", "shelving-02-2"],
                "description": "Only 1″ thick overall, these shelves achieve their floating effect through an aluminum sheath covering an internal frame that mounts directly inside the wall. A satin black finish balances visual weight with refined detailing.",
            },
        ],
    },
    {
        "category": "Custom-Fit Framing & Trim",
        "slug": "framing-trim",
        "service_url": "/services/press-brake/",
        "description": "Aluminum extrusions that provide visual transitions between focal points and their surroundings",
        "items": [
            {
                "name": "Custom-Fit Framing 01",
                "location": "Showroom in Experience Center | Coppell, TX",
                "image": "framing-01",
                "images": ["framing-01", "framing-01-2"],
                "description": "A display frame constructed from stacked square aluminum tubing (3″×3″ and 2″×2″), creating a recessed channel for integrated lighting. Corners are secured with internal joints and mechanical fasteners. Hidden bracketry continues the minimal floating aesthetic.",
            },
            {
                "name": "Custom-Fit Framing 02",
                "location": "Indoor-Outdoor Patio | Dallas, TX",
                "image": "framing-02",
                "images": ["framing-02"],
                "description": "Fountain frames designed to address safety hazards and resident dissatisfaction while elevating the space's clean, modern aesthetic. The covers minimize overspray, protecting patio furniture and residents from the water feature.",
            },
            {
                "name": "Decorative Trim 01",
                "location": "Lounge Area in Experience Center | Coppell, TX",
                "image": "trim-01",
                "images": ["trim-01"],
                "description": "A minimalist aluminum angle piece wrapping the full perimeter of a fireplace opening, providing a clean transition between large-format stone tile and glass. Anodized satin black with no exposed fasteners, keeping the element visually quiet.",
            },
            {
                "name": "Decorative Trim 02",
                "location": "Experience Center | Coppell, TX",
                "image": "trim-02",
                "images": ["trim-02"],
                "description": "Custom-formed aluminum trim lining curved archways, hand-shaped to follow each arch's curve. Anodized to a warm champagne brass tone, providing an elegant transition between tile-clad walls and interior spaces.",
            },
            {
                "name": "Decorative Trim 03",
                "location": "Warewash Area in Experience Center | Coppell, TX",
                "image": "trim-03",
                "images": ["trim-03", "trim-03-2"],
                "description": "Stainless steel top trim capping the tile-clad wall surrounding a dishwashing conveyor. Fit-in-field with a hand-brushed finish, this industrial trim harmonizes with the machinery and polishes off the open-concept layout.",
            },
        ],
    },
    {
        "category": "Brass Features",
        "slug": "brass-features",
        "service_url": "/services/fabrication-site-services/",
        "description": "High-finish brass fabrication for chandeliers, handrails, and architectural details",
        "items": [
            {
                "name": "Brass Chandelier",
                "location": "Deli Counter in Experience Center | Coppell, TX",
                "image": "brass-chandelier",
                "images": ["brass-chandelier", "brass-chandelier-2", "brass-chandelier-3"],
                "description": "A statement chandelier with a cage-like frame made from 2″×2″ brushed brass tubing, stretching just over 25 feet in length. Composed of 63 individually fabricated segments with custom aluminum tube joinery hidden inside each connection. Globe pendant lights align rhythmically with the counter below.",
            },
            {
                "name": "Brass Handrails",
                "location": "Hotel Lobby | Dallas, TX",
                "image": "brass-handrails",
                "images": ["brass-handrails"],
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

SERVICES_DETAIL = {
    "engineered-design": {
        "name": "Engineered Design",
        "tagline": "Design, documentation, and engineering for custom metal scopes",
        "description": [
            "Every successful custom metal project starts with engineering it right. We bring design consultation, CAD modeling, field measurement, shop drawing production, and submittal support together into one coordinated pre-production package — the work that happens before any material is cut.",
            "We work directly with architects, interior designers, and general contractors to interpret design intent, resolve fabrication constraints, and produce drawings the project team can review, approve, and build from. Design is not a step we skip or hand off — it's how we prevent expensive problems downstream.",
        ],
        "capabilities": [
            "Design consultation and concept development",
            "CAD modeling and 3D design",
            "Shop drawings and fabrication documentation",
            "Submittal packages for architect and owner approval",
            "Field measurement and as-built documentation",
            "Finish samples and approval coordination",
        ],
        "featured_images": ["framing-01", "framing-02", "partition-02", "trim-01"],
        "faqs": [
            {
                "question": "What does Archimedes Metals include in its Engineered Design service?",
                "answer": "Engineered Design covers the full pre-production phase of a custom metal project: design consultation, CAD modeling, shop drawing production, submittal package preparation, field measurement, finish sample coordination, and approval documentation. It's the process that converts an architect's design intent into a buildable, approvable fabrication package.",
            },
            {
                "question": "Do you provide shop drawings and submittal packages for commercial metalwork?",
                "answer": "Yes. Shop drawings, finish samples, and submittal packages are a standard part of our workflow for commercial scopes. These documents support the architect's and general contractor's coordination process, reduce field surprises, and give the project team the documentation needed for approval and installation.",
            },
            {
                "question": "Can you field-measure before fabrication on commercial construction projects?",
                "answer": "Yes. We offer field measurement and as-built documentation as part of our design service. For precision-fit scopes — canopy systems, panel walls, trim profiles, lobby features — measuring in the field before fabrication ensures pieces fit the as-built conditions and eliminates costly modifications at installation.",
            },
        ],
    },
    "fabrication-site-services": {
        "name": "Fabrication & Site Services",
        "tagline": "Complete fabrication from raw material to finished installation",
        "description": [
            "Most of our work is delivered as a complete scope — we fabricate the piece and we install it. Fabrication & Site Services covers the full range of custom metal work: cutting, forming, welding, finishing, delivery, and field installation for commercial architectural metal scopes of all sizes.",
            "From large-scale canopy structures and decorative wall systems to perforated panels, signage, fencing, and interior features, we manage the complete process in-house and coordinate directly with the general contractor and other trades in the field.",
        ],
        "capabilities": [
            "Complete in-house fabrication from concept to delivery",
            "Commercial interior and exterior installation",
            "Field measurement, delivery, and site coordination",
            "Material procurement and job-spec sourcing",
            "Large-format and complex multi-component assembly",
            "Multi-trade coordination for commercial construction scopes",
        ],
        "featured_images": ["outdoor-canopy", "partition-01", "fence-louvered-01", "brass-chandelier"],
        "faqs": [
            {
                "question": "Does Archimedes Metals handle both fabrication and installation?",
                "answer": "Yes. We deliver most scopes as a complete package — fabrication and installation. We handle field measurement, shop fabrication, delivery, and field installation, coordinating directly with the general contractor and other trades. For clients who need fabrication only (no installation), we can deliver finished pieces ready for owner or GC installation.",
            },
            {
                "question": "What types of commercial metal scopes does Archimedes Metals fabricate and install?",
                "answer": "We fabricate and install decorative partition and panel wall systems, outdoor canopy structures, signage, post-and-panel fencing and enclosures, floating shelving, architectural trim, brass chandeliers, and a wide range of custom interior and exterior commercial metalwork. If it's custom metal and it needs to be built and installed, we can scope it.",
            },
            {
                "question": "How do you coordinate with general contractors and other trades on commercial projects?",
                "answer": "We work as a direct subcontractor to the general contractor. We provide shop drawings and submittals for approval, confirm field dimensions before fabrication, communicate schedule and delivery milestones, and coordinate access and sequencing with other trades during installation. Clear communication is a core part of how we operate on commercial sites.",
            },
        ],
    },
    "cnc-routing": {
        "name": "CNC Routing",
        "tagline": "Precision cutting for patterns, shapes, and architectural panel components",
        "description": [
            "CNC routing is how we turn sheet metal into custom panels, dimensional lettering, perforation patterns, and precision-fit architectural components. Our CNC router cuts aluminum, mild steel, and stainless steel to exact dimensions with consistent accuracy across full production runs.",
            "CNC capability is central to our perforated panel work, custom signage, and architectural trim. It's how a 28-foot wall panel maintains a consistent diamond perforation pattern with no visible misalignment, and how dimensional sign letters stay identical when multiple runs are fabricated for a phased project.",
        ],
        "capabilities": [
            "Custom perforation patterns in aluminum and steel",
            "Dimensional lettering and logo cutouts",
            "Precision-fit architectural panel components",
            "Complex geometric shapes and repeating patterns",
            "Consistent production-run accuracy",
            "Fabrication from CAD file or reference drawing",
        ],
        "featured_images": ["partition-02", "surface-cover-03", "partition-01", "signage-eagle-02"],
        "faqs": [
            {
                "question": "What materials can Archimedes Metals CNC rout?",
                "answer": "Our CNC router handles aluminum, mild steel, and stainless steel at commercial architectural gauges — from lightweight sheet aluminum to heavier plate. Aluminum is the most common material for perforated panel and signage work due to its weight and workability, but we regularly route mild steel and stainless for structural and decorative components as well.",
            },
            {
                "question": "Can you create custom perforation patterns for architectural panels?",
                "answer": "Yes. We produce custom perforation patterns including geometric repeating patterns — squares, ellipses, triangles, diamonds — open-field perforations, and company-specific logo cutouts. Patterns are engineered to balance design intent with the structural requirements of the panel span and the material thickness.",
            },
            {
                "question": "Can you fabricate CNC-routed components from a CAD file or drawing?",
                "answer": "Yes. We work from CAD files, architect drawings, or reference sketches to produce CNC-cut components. For complex or precision-fit work, we model the part in CAD before cutting to verify geometry and fit. We can also develop CNC patterns from a design brief if no file exists yet.",
            },
        ],
    },
    "press-brake": {
        "name": "Press Brake",
        "tagline": "Precision sheet metal bending for complex custom profiles",
        "description": [
            "Our in-house press brake is a 12-foot, 140-ton capacity machine capable of forming complex bends in aluminum, mild steel, and stainless steel. This allows us to produce custom sheet metal components with tight tolerances, consistent profiles, and repeatable accuracy — without outsourcing to a secondary shop.",
            "Press brake capability is the foundation of most of our architectural work. Custom trim profiles, panel returns, enclosure components, and structural frames all require precision bending. Having this in-house gives us direct control over quality, lead time, and cost.",
        ],
        "capabilities": [
            "12-foot, 140-ton press brake capacity",
            "Aluminum, mild steel, and stainless steel forming",
            "Complex multi-bend profiles and returns",
            "Custom extrusion profiles and transitions",
            "Tight-tolerance work for architectural applications",
            "CAD modeling prior to forming for fit verification",
        ],
        "featured_images": ["trim-03", "framing-01", "trim-02", "partition-02"],
        "faqs": [
            {
                "question": "What is Archimedes Metals' press brake capacity?",
                "answer": "Our in-house press brake is a 12-foot, 140-ton CNC machine. This allows us to form large architectural components — trim profiles, panel returns, structural frames, and enclosure parts — with consistent profiles and tight tolerances, without outsourcing to a secondary shop. In-house forming gives us direct control over quality, lead time, and cost.",
            },
            {
                "question": "What materials can your press brake form?",
                "answer": "Our press brake handles aluminum, mild steel, and stainless steel. We work regularly with architectural gauges from 22-gauge sheet to ½″ plate depending on the material and application, forming custom extrusion profiles, panel returns, trim channels, and structural components.",
            },
            {
                "question": "Do you perform CAD modeling before press brake forming?",
                "answer": "Yes. For complex profiles, custom extrusions, or precision-fit architectural components, we model the part in CAD before forming. This step lets us verify the final geometry, confirm the bend sequence, and identify fit issues before material is cut — reducing waste and ensuring the finished piece meets the specified dimensions.",
            },
        ],
    },
    "welding": {
        "name": "Welding",
        "tagline": "Structural and architectural welding at the highest standard",
        "description": [
            "Welding is the foundation of our shop. While high-end aluminum TIG welding is our specialty, our team is equally capable in mild steel, stainless steel, and brass — structural and decorative, interior and exterior, commercial and architectural.",
            "We hold welds to the standard of the finished product. For visible architectural metalwork, that means full-penetration welds, proper filler selection, and ground and polished surfaces where required. For structural applications, it means consistent quality that meets the load requirements of the assembly.",
        ],
        "capabilities": [
            "Aluminum TIG welding — structural and decorative",
            "Stainless steel welding — interior and exterior",
            "Mild steel MIG and TIG welding",
            "Brass welding and brazing",
            "Weld grinding and finish blending for architectural applications",
            "Structural welding for commercial construction",
        ],
        "featured_images": ["weld-02", "brass-chandelier", "fence-louvered-01", "partition-01"],
        "faqs": [
            {
                "question": "What types of welding does Archimedes Metals offer?",
                "answer": "We offer aluminum TIG welding, stainless steel TIG and MIG welding, mild steel MIG and TIG welding, and brass welding and brazing. Our team is experienced in both structural welding for load-bearing commercial construction scopes and decorative welding for visible architectural metalwork where weld appearance is part of the finished product.",
            },
            {
                "question": "Is aluminum TIG welding a specialty at Archimedes Metals?",
                "answer": "Yes. Aluminum TIG welding is our shop's core specialty. We weld aluminum for structural and decorative architectural applications — canopy frames, partition systems, shelving, signage, and trim — with full-penetration welds, appropriate filler selection, and ground-and-polished surfaces where the weld will be visible in the finished installation.",
            },
            {
                "question": "How do you finish welds on architectural metalwork where the weld is visible?",
                "answer": "For visible architectural metalwork, we grind, blend, and polish welds to the degree required by the finished surface specification. On anodized aluminum, welds are blended flush before anodizing so the surface has no visible weld line. On powder-coated work, we prep the weld surface to remove porosity and undercut before finish is applied.",
            },
        ],
    },
    "coatings-finishes": {
        "name": "Coatings & Finishes",
        "tagline": "The finish is the last thing people see — and the first thing they judge",
        "description": [
            "The right finish makes the difference between a good-looking piece and a piece that belongs in the space. We offer powder coating in custom colors, brushed and polished mechanical finishes, anodizing in a range of tones, and painted aluminum panel systems — all matched to the design intent and the environment the piece will live in.",
            "We treat finish as a deliverable, not an afterthought — with finish samples, approval submittals, and documentation as part of the project package.",
        ],
        "capabilities": [
            "Powder coating in custom RAL and color-match",
            "Brushed and hand-polished mechanical finishes",
            "Anodizing — clear, satin black, champagne brass, and custom",
            "Painted aluminum panel systems",
            "Field touch-up and finish coordination",
            "Finish samples and submittal support",
        ],
        "featured_images": ["coat-02", "trim-02", "shelving-01", "partition-02"],
        "faqs": [
            {
                "question": "What finish options does Archimedes Metals offer for fabricated metalwork?",
                "answer": "We offer powder coating in custom RAL colors and color-match, brushed and hand-polished mechanical finishes in multiple grit levels, anodizing in clear, satin black, champagne brass, and custom tones, and painted aluminum panel systems. Finish selection is specified based on the environment, design intent, and durability requirements of each project.",
            },
            {
                "question": "Can you match a specific powder coat color or architectural finish standard?",
                "answer": "Yes. We work from RAL numbers, color-match chips, and architect-specified samples to achieve the correct powder coat color for each project. For mechanical finishes, we produce samples at the specified grit and direction for approval before fabrication. Matching an existing installed finish is also possible with physical reference samples.",
            },
            {
                "question": "Do you provide finish samples and approval submittals before fabrication?",
                "answer": "Yes. Finish samples and approval submittals are a standard part of our project package for commercial work. Samples are produced at the specified material and finish, submitted for approval by the architect or owner, and documented before fabrication begins — preventing costly finish disputes at the end of a project.",
            },
        ],
    },
}


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
        name = request.POST.get("name", "").strip()
        company = request.POST.get("company", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        role = request.POST.get("role", "").strip()
        location = request.POST.get("location", "").strip()
        timeline = request.POST.get("timeline", "").strip()
        service = request.POST.get("service", "").strip()
        drawings_available = request.POST.get("drawings_available", "").strip()
        installation = request.POST.get("installation", "").strip()
        description = request.POST.get("description", "").strip()

        subject = f"Quote Request — {name}" + (f" | {company}" if company else "")
        body = (
            f"New quote request submitted via archimedesmetals.com\n"
            f"{'='*50}\n\n"
            f"Name:              {name}\n"
            f"Company:           {company}\n"
            f"Email:             {email}\n"
            f"Phone:             {phone}\n"
            f"Role:              {role}\n\n"
            f"Project Location:  {location}\n"
            f"Timeline:          {timeline}\n"
            f"Service Needed:    {service}\n"
            f"Drawings:          {drawings_available}\n"
            f"Installation:      {installation}\n\n"
            f"Project Description:\n{description}\n"
        )

        try:
            msg = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email] if email else [],
            )
            for f in request.FILES.getlist("attachments"):
                msg.attach(f.name, f.read(), f.content_type)
            msg.send()
            return render(request, "contact.html", {"submitted": True, "quote_needs": QUOTE_NEEDS})
        except Exception:
            logger.exception("Failed to send quote request email")
            return render(request, "contact.html", {"submitted": False, "send_error": True, "quote_needs": QUOTE_NEEDS})

    return render(request, "contact.html", {"submitted": False, "quote_needs": QUOTE_NEEDS})


def privacy(request):
    return render(request, "privacy.html")


def projects(request):
    # Build flat project list for lightbox JS
    projects_flat = []
    for cat in PROJECTS:
        for p in cat["items"]:
            projects_flat.append({
                "category": cat["category"],
                "service_url": cat.get("service_url", ""),
                "name": p["name"],
                "location": p["location"],
                "description": p["description"],
                "images": p.get("images", [p["image"]]),
            })
    return render(request, "projects.html", {
        "project_categories": PROJECTS,
        "projects_json": json.dumps(projects_flat),
    })


def services_index(request):
    return render(request, "services.html", {"services": SERVICES})


def service_detail(request, slug):
    service = SERVICES_DETAIL.get(slug)
    if not service:
        raise Http404
    return render(request, "service_detail.html", {"service": service, "slug": slug})


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "Sitemap: https://archimedesmetals.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
