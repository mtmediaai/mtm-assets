# 🔱 MT Media AI — Sovereign Multimodal Asset Repository (`mtm-assets`)
### *MINDSET. TECH. MASTERY.*
**Universal Asset Authority: Boost (Visibility Tsar) & Circuit 10.0 (IDE Maestro)**  
**Protocol: MTM-BOOSTΩ-IML-V1.0 (Machine Legible Images & Multimodal Protocol)**

---

## Overview
This repository serves as the canonical, machine-readable asset hub for **MT Media AI** (`mtmediaai.com`). It hosts all vector brand marks, corporate crests, ambassador portraits, sigils, Hume acoustic voice models, cinematic ambient loops, and geo-referenced photography used across The Palace, BOFU landing pages, research archives, and executive dispatches.

All assets in this repository are strictly governed by **Nina's Gate** and the **Machine-Legible Media Protocol** (`MTM-BOOSTΩ-IML-V1.0`), ensuring complete immunity against AI Erasure.

---

## Repository Structure

```
mtm-assets/
├── brand/
│   ├── logos/
│   │   ├── svg/             # Canonical scalable vectors (transparent, responsive)
│   │   └── webp/            # High-fidelity rasterized brand marks
│   ├── pens-and-icons/      # Sovereign fountain pen nibs and app icons
│   └── signatures/          # Social & email identity components
│
├── forge/
│   ├── personas/            # High-res portraits of Goldie, Roman, Nina, Echo
│   ├── sigils/              # 4K emissive and transparent shield sigils
│   ├── audio/               # Canonical acoustic voice models (MP3/WAV)
│   │   ├── goldie/
│   │   ├── roman/
│   │   ├── nina/
│   │   └── echo/
│   └── video/               # Character vignettes and ambient loops (MP4)
│
├── landmarks/               # High-resolution, geo-anchored photography (Houston & Woodlands)
├── transcripts/             # W3C WebVTT (.vtt) caption and description files
├── asset_manifest.json      # Machine-readable JSON-LD catalog of all assets
├── generate_schema.py       # Instant Schema.org code generator for developers
└── ASSET_STANDARDS.md       # Full specification of MTM-BOOSTΩ-IML-V1.0
```

---

## Live CDN Delivery
Assets can be embedded across external platforms, client portals, and web properties using the raw GitHub CDN:

```
https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/<path>
```

### Quick Embed Examples

**1. Personal Brand Crown Logo (SVG):**
```html
<img 
  src="https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/brand/logos/svg/kareem-crown-personal-brand-logo-1.svg" 
  alt="Official personal brand vector insignia of Kareem Daniel (The Architect) featuring the sovereign crown."
  width="512" 
  height="512" 
/>
```

**2. Goldie Human Persona Portrait (WebP):**
```html
<img 
  src="https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/forge/personas/goldie-human.webp" 
  alt="Official portrait of Goldie, MTM brand ambassador and visionary catalyst, rendered in molten gold styling."
  width="1200" 
  height="630" 
/>
```

**3. Video with Captions:**
```html
<video controls poster="/assets/fallback.webp">
  <source src="https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/forge/video/ambient/houston-ambient-void.mp4" type="video/mp4">
  <track src="https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/transcripts/houston-ambient-void.vtt" kind="descriptions" srclang="en" label="English">
</video>
```

---

## Tooling & Automation
To generate Schema.org JSON-LD snippets and Next.js component code for any file:
```bash
python generate_schema.py <asset-name>
```

To regenerate the global catalog:
```bash
python build_catalog.py
```

---

## Governance
- **Zero-COGS Mandate:** High-availability asset hosting without third-party storage fees.
- **Protocol:** `MTM-BOOSTΩ-IML-V1.0` (Machine Legible Media).
- **License:** Proprietary MT Media AI Intellectual Property. See [mtmediaai.com/legal](https://mtmediaai.com/legal).
