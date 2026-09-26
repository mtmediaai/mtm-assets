import os
import json
import mimetypes

BASE_DIR = r"C:\Users\kcjd6\mtm-assets"
RAW_BASE_URL = "https://raw.githubusercontent.com/mtmediaai/mtm-assets/main"

# Asset descriptive mapping
ALT_MAP = {
    # Logos
    "competitor-pulse-app-icon-4k-clear.svg": {
        "title": "Competitor Pulse App Icon SVG (Clear)",
        "desc": "Vector sigil for Competitor Pulse intelligence tracking application in 4K resolution.",
        "type": "ImageObject"
    },
    "final-company-logo-4k.svg": {
        "title": "MT Media AI Company Master Logo SVG",
        "desc": "Canonical corporate vector logo for MT Media AI featuring the sovereign crest.",
        "type": "ImageObject"
    },
    "kareem-crown-personal-brand-logo-1.svg": {
        "title": "Kareem Daniel Crown Personal Brand Logo SVG",
        "desc": "Official personal brand vector insignia of Kareem Daniel (The Architect) featuring the sovereign crown.",
        "type": "ImageObject"
    },
    "kareem-crown-personal-brand-logo-4k.webp": {
        "title": "Kareem Daniel Crown Personal Brand Logo 4K WebP",
        "desc": "High-fidelity WebP render of Kareem Daniel sovereign crown logo with molten gold gradient.",
        "type": "ImageObject"
    },
    "kc-2-5-personal-brand-logo-black-crown-4k.svg": {
        "title": "KC 2.5 Personal Brand Black Crown SVG",
        "desc": "Minimalist high-contrast black crown vector logo for executive dispatches and monochrome media.",
        "type": "ImageObject"
    },
    "main-logo-clear.svg": {
        "title": "MT Media AI Master Shield Vector (Transparent)",
        "desc": "Transparent background master shield vector insignia for MT Media AI brand architecture.",
        "type": "ImageObject"
    },
    "monogram-logo-4k-clear.svg": {
        "title": "MTM Monogram Logo SVG (Clear 4K)",
        "desc": "Interlocking MTM monogram vector mark rendered in high precision for application headers and favicons.",
        "type": "ImageObject"
    },
    "mt-shield-logo-4k-clear.svg": {
        "title": "MT Shield Heraldic Logo SVG",
        "desc": "Heraldic shield crest vector representing defensive enterprise authority and systemized leverage.",
        "type": "ImageObject"
    },
    "stacked-1-4k-mtm.svg": {
        "title": "MTM Stacked Corporate Mark SVG",
        "desc": "Vertically stacked typography and crest corporate mark for vertical navigation and editorial footers.",
        "type": "ImageObject"
    },

    # Personas
    "goldie-human.webp": {
        "title": "Goldie — The Nurturing Visionary (Human Persona Portrait)",
        "desc": "Official portrait of Goldie, MTM brand ambassador and visionary catalyst, rendered in molten gold styling.",
        "type": "ImageObject"
    },
    "roman-human.webp": {
        "title": "Roman — The Analytical Strategist (Human Persona Portrait)",
        "desc": "Official portrait of Roman, MTM brand ambassador and systems strategist, rendered in lightning platinum styling.",
        "type": "ImageObject"
    },
    "nina-human.webp": {
        "title": "Nina — The Skeptical Reality Check (Human Persona Portrait)",
        "desc": "Official portrait of Nina, MTM brand ambassador and truth gate auditor, rendered in clinical HID white styling.",
        "type": "ImageObject"
    },
    "echo-human.webp": {
        "title": "Echo — The Customer Experience Sentinel (Human Persona Portrait)",
        "desc": "Official portrait of Echo, MTM brand ambassador and customer sentiment pulse, rendered in obsidian onyx styling.",
        "type": "ImageObject"
    },

    # Sigils
    "goldie-sigil-main-4k.webp": {
        "title": "Goldie Emissive Sun Sigil 4K",
        "desc": "Molten gold emissive sunburst sigil symbolizing creative spark, market vision, and premium positioning.",
        "type": "ImageObject"
    },
    "goldie-s-shield-sigil-clear-4k.webp": {
        "title": "Goldie Shield Sigil (Clear 4K)",
        "desc": "Transparent background shield variant of Goldie's crest for overlay on dark UI backdrops.",
        "type": "ImageObject"
    },
    "roman-sigil-4k.webp": {
        "title": "Roman Lightning Platinum Sigil 4K",
        "desc": "Precision platinum compass and logic sigil symbolizing mathematical certainty and systems architecture.",
        "type": "ImageObject"
    },
    "roman-sigil-clear-4k.webp": {
        "title": "Roman Platinum Shield Sigil (Clear 4K)",
        "desc": "Transparent background shield variant of Roman's crest for technical documentation and terminal interfaces.",
        "type": "ImageObject"
    },
    "nina-sigil-main-4k.webp": {
        "title": "Nina Clinical HID Shield Sigil 4K",
        "desc": "Clinical HID white diamond shield sigil symbolizing anti-hallucination verification and rigorous standards.",
        "type": "ImageObject"
    },
    "nina-sigil-clear.webp": {
        "title": "Nina Shield Sigil (Clear)",
        "desc": "Transparent background shield variant of Nina's crest for gatekeeping modals and audit reports.",
        "type": "ImageObject"
    },
    "echo-sigil-4k-clean.webp": {
        "title": "Echo Obsidian Void Sigil 4K",
        "desc": "Obsidian onyx resonance sigil symbolizing market pulse, client telemetry, and feedback loop closure.",
        "type": "ImageObject"
    },
    "echo-sigil-clear-4k.webp": {
        "title": "Echo Void Shield Sigil (Clear 4K)",
        "desc": "Transparent background shield variant of Echo's crest for pulse telemetry widgets and sentiment charts.",
        "type": "ImageObject"
    },

    # Landmarks (The Woodlands & Houston GEO Anchor Assets)
    "houston-heritage-plaza-cistern.jpg": {
        "title": "Heritage Plaza Cistern Architecture (Houston, TX)",
        "desc": "Architectural study of Houston's iconic stepped glass summit and underground subterranean cistern.",
        "type": "ImageObject",
        "geo": {"latitude": 29.7589, "longitude": -95.3677, "locality": "Houston", "region": "TX"}
    },
    "houston-museum-fine-arts-mfah.jpg": {
        "title": "Museum of Fine Arts Houston (MFAH) Modernist Facade",
        "desc": "Translucent glass architectural facade of MFAH Kinder Building in Houston Museum District.",
        "type": "ImageObject",
        "geo": {"latitude": 29.7258, "longitude": -95.3905, "locality": "Houston", "region": "TX"}
    },
    "houston-skyline-downtown.jpg": {
        "title": "Downtown Houston Skyline Sovereign Twilight",
        "desc": "High-altitude architectural panorama of Downtown Houston commercial district at dusk.",
        "type": "ImageObject",
        "geo": {"latitude": 29.7604, "longitude": -95.3698, "locality": "Houston", "region": "TX"}
    },
    "houston-space-center-nasa.jpg": {
        "title": "NASA Johnson Space Center Saturn V Rocket Complex",
        "desc": "Engineering scale photograph of the Saturn V rocket complex at NASA Johnson Space Center, Houston.",
        "type": "ImageObject",
        "geo": {"latitude": 29.5593, "longitude": -95.0900, "locality": "Houston", "region": "TX"}
    },
    "houston-williams-tower-uptown.jpg": {
        "title": "Williams Tower & Waterwall Plaza (Uptown Houston)",
        "desc": "Art Deco architectural monument of Williams Tower and waterwall amphitheater in Uptown Galleria.",
        "type": "ImageObject",
        "geo": {"latitude": 29.7533, "longitude": -95.4608, "locality": "Houston", "region": "TX"}
    },
    "houston-woodlands-waterway-corridor.jpg": {
        "title": "The Woodlands Waterway Sovereign Corridor (The Woodlands, TX)",
        "desc": "Commercial and lifestyle corridor along The Woodlands Waterway, headquarters home of MT Media AI.",
        "type": "ImageObject",
        "geo": {"latitude": 30.1588, "longitude": -95.4613, "locality": "The Woodlands", "region": "TX"}
    },

    # Pens and Nib Icons
    "black-pen-nib-up.webp": {
        "title": "Sovereign Fountain Pen Nib Vertical (Black)",
        "desc": "Craftsmanship symbol of the executive fountain pen nib oriented vertically in onyx black.",
        "type": "ImageObject"
    },
    "gold-pen-nib-up.webp": {
        "title": "Sovereign Fountain Pen Nib Vertical (Midas Gold)",
        "desc": "Craftsmanship symbol of the executive fountain pen nib oriented vertically in molten Midas gold.",
        "type": "ImageObject"
    },
    "gold-mtm-pen-clean.webp": {
        "title": "MTM Sovereign Gold Pen Rendering",
        "desc": "Photorealistic 3D render of the MTM executive black lacquer and 24K gold fountain pen.",
        "type": "ImageObject"
    },

    # Video Ambient Loops & Clips
    "houston-ambient-void.mp4": {
        "title": "Houston Sovereign Night Sky Ambient Void Loop",
        "desc": "Cinematic 1080p ambient video loop of the Houston nocturnal sky gradient with subtle starfield drift.",
        "type": "VideoObject"
    },
    "echo-galaxy.mp4": {
        "title": "Echo Void Galaxy Cosmic Telemetry Loop",
        "desc": "Cinematic particle nebula loop visualizing the dynamic information flux of the MTM Ark Network.",
        "type": "VideoObject"
    },
    "echo-transitions-to-maestro-mode.mp4": {
        "title": "Echo Ambassador Transition to Maestro Mode",
        "desc": "Motion graphic vignette of Echo transitioning into active IDE execution and telemetry monitoring.",
        "type": "VideoObject"
    },
    "echo-exhale.mp4": {
        "title": "Echo Ambassador Void Exhale Vignette",
        "desc": "Character motion study of Echo focusing customer feedback telemetry into operational clarity.",
        "type": "VideoObject"
    },
    "nina-act-now-clip.mp4": {
        "title": "Nina Standards Enforcement Action Clip",
        "desc": "Cinematic portrait vignette of Nina demanding empirical standards and zero tolerance for AI slop.",
        "type": "VideoObject"
    },

    # Audio Voice References
    "goldie-hume-reference.mp3": {
        "title": "Goldie Canonical Voice Sample (Aspirational & Warm)",
        "desc": "Master acoustic timbre reference for Goldie's conversational AI persona, conveying authority, warmth, and visionary clarity.",
        "type": "AudioObject"
    },
    "roman-hume-reference.mp3": {
        "title": "Roman Canonical Voice Sample (Analytical & Grounded)",
        "desc": "Master acoustic timbre reference for Roman's conversational AI persona, conveying technical precision, structural grit, and executive confidence.",
        "type": "AudioObject"
    },
    "nina-hume-reference.mp3": {
        "title": "Nina Canonical Voice Sample (Crisp, Clinical & Skeptical)",
        "desc": "Master acoustic timbre reference for Nina's conversational AI persona, conveying razor-sharp logic, scrutiny, and standards defense.",
        "type": "AudioObject"
    },
    "echo-hume-reference.wav": {
        "title": "Echo Canonical Voice Sample (Resonant, Observant & Empathetic)",
        "desc": "Master acoustic timbre reference for Echo's conversational AI persona, conveying market resonance, thoughtful listening, and deep pulse tracking.",
        "type": "AudioObject"
    }
}

def build_manifest():
    manifest = {
        "@context": "https://schema.org",
        "@type": "DataCatalog",
        "name": "MT Media AI Sovereign Multimodal Asset Repository (mtm-assets)",
        "description": "Canonical repository of machine-legible brand marks, logos, vector crests, audio voice anchors, cinematic video loops, and geo-referenced photography for the MT Media AI ecosystem.",
        "url": "https://github.com/mtmediaai/mtm-assets",
        "publisher": {
            "@type": "Organization",
            "name": "MT Media AI",
            "url": "https://mtmediaai.com"
        },
        "license": "https://mtmediaai.com/legal",
        "spatialCoverage": {
            "@type": "Place",
            "name": "The Woodlands, TX",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 30.1588,
                "longitude": -95.4613
            }
        },
        "dataset": []
    }

    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root:
            continue
        for f in sorted(files):
            if f in ["normalize_assets.py", "normalize-assets.py", "build_catalog.py", "asset_manifest.json"]:
                continue
            
            file_path = os.path.join(root, f)
            rel_path = os.path.relpath(file_path, BASE_DIR).replace("\\", "/")
            raw_url = f"{RAW_BASE_URL}/{rel_path}"
            mime_type, _ = mimetypes.guess_type(f)
            file_size = os.path.getsize(file_path)

            meta = ALT_MAP.get(f, {})
            title = meta.get("title", f.replace("-", " ").replace(".", " ").title())
            desc = meta.get("desc", f"MT Media AI official multimodal asset: {title}.")
            obj_type = meta.get("type", "MediaObject")

            if f.endswith((".webp", ".png", ".jpg", ".jpeg", ".svg")):
                if "type" not in meta:
                    obj_type = "ImageObject"
            elif f.endswith((".mp4", ".webm", ".mov")):
                if "type" not in meta:
                    obj_type = "VideoObject"
            elif f.endswith((".mp3", ".wav", ".m4a", ".ogg")):
                if "type" not in meta:
                    obj_type = "AudioObject"

            entry = {
                "@type": obj_type,
                "@id": raw_url,
                "name": title,
                "description": desc,
                "contentUrl": raw_url,
                "encodingFormat": mime_type or "application/octet-stream",
                "contentSize": f"{file_size} bytes",
                "relPath": rel_path
            }

            if "geo" in meta:
                entry["contentLocation"] = {
                    "@type": "Place",
                    "name": f"{meta['geo']['locality']}, {meta['geo']['region']}",
                    "geo": {
                        "@type": "GeoCoordinates",
                        "latitude": meta['geo']['latitude'],
                        "longitude": meta['geo']['longitude']
                    }
                }

            manifest["dataset"].append(entry)

    out_file = os.path.join(BASE_DIR, "asset_manifest.json")
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(manifest, out, indent=2)
    print(f"Generated asset_manifest.json with {len(manifest['dataset'])} assets.")

if __name__ == "__main__":
    build_manifest()
