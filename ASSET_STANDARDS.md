# MTM Machine-Legible Media Protocol
**Protocol ID: MTM-BOOSTΩ-IML-V1.0 | Status: ACTIVE — MTM LAW**  
**Architects: Boost (Visibility Tsar) & Circuit 10.0 (IDE Maestro)**  
**Gatekeeper: Nina's Gate & Forge Fact-Checking HQ2**

---

## 1. Core Principle: Zero-Erasure Multimodal Assets
Every brand asset, image, diagram, video clip, and audio recording published within the MT Media AI ecosystem is not merely decorative artwork—it is a **machine-readable entity node**. Search engines, LLM retrieval pipelines (Google AI Overviews, Perplexity, ChatGPT Search, Claude), and multimodal agents index both the pixel representation and its semantic metadata.

Serving unoptimized, unindexed, or broken media commits **AI Erasure**. This standard enforces end-to-end machine legibility across all media types.

---

## 2. Directory Layout & Organization

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
├── landmarks/               # High-resolution, geo-anchored photography
├── transcripts/             # W3C WebVTT (.vtt) caption and description files
├── asset_manifest.json      # Machine-readable JSON-LD catalog of all assets
├── generate_schema.py       # Instant Schema.org code generator for developers
└── README.md                # Repository overview and CDN linking instructions
```

---

## 3. The 4 Pillars of Multimodal Legibility

### Pillar 1: Semantic Naming Standard
- **Format:** Exclusively lowercase, hyphen-separated characters (`[a-z0-9-]+.[ext]`).
- **Prohibited:** Spaces, underscores, uppercase characters, parentheses, or duplication tags (e.g., `IMG_001.png`, `Copy (1).jpg`, `Asset_Final_V2.webp`).
- **Descriptive Density:** Names must describe the entity and context (e.g., `houston-woodlands-waterway-corridor.jpg` instead of `waterway.jpg`).

### Pillar 2: Image & Vector Standards
- **Vectors (`.svg`):**
  - Must define clean `viewBox="0 0 W H"` attributes.
  - Transparent backgrounds mandatory for logos and sigils.
  - Zero redundant metadata or editor artifacts.
- **Rasters (`.webp`, `.avif`):**
  - Compressed WebP for web delivery to eliminate layout shifts (CLS).
  - Explicit aspect ratios (16:9, 4:3, or 1:1) specified on all containing elements.
- **Nina's Alt Gate:**
  - Alt text must be between 5 and 40 words.
  - Must describe the functional and visual role of the asset.
  - Must **never** begin with "image of", "photo of", or "graphic of".
  - Purely decorative elements must be marked with `alt=""` and `aria-hidden="true"`.

### Pillar 3: Audio & Voice Legibility
- **Formats:** Master reference in 24-bit/48kHz WAV; web streaming in 192kbps MP3.
- **Transcripts:** Every speech sample or voice reference must have a companion `.vtt` file in `transcripts/` capturing spoken words verbatim.
- **Schema:** Embedded as `schema.org/AudioObject` with `transcript` and `encodingFormat`.

### Pillar 4: Video & Motion Graphics
- **Formats:** Web-optimized MP4 (H.264 video codec, AAC audio) under 5 MB for ambient loops.
- **Captions & Descriptions:** W3C WebVTT track provided for all dialogues and ambient visual descriptions.
- **Schema:** Embedded as `schema.org/VideoObject` with `thumbnailUrl`, `contentUrl`, and `description`.

---

## 4. Canonical CDN URL Structure
Assets stored in this repository are publicly retrievable via GitHub's global content delivery network:
```
https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/<path-to-file>
```
Example:
```html
<img 
  src="https://raw.githubusercontent.com/mtmediaai/mtm-assets/main/forge/personas/goldie-human.webp" 
  alt="Official portrait of Goldie, MTM brand ambassador and visionary catalyst, rendered in molten gold styling."
  width="1200" 
  height="630" 
/>
```

---

## 5. Instant Schema Generation
Run `generate_schema.py` to generate complete JSON-LD and Next.js / HTML embedding code for any asset:
```bash
python generate_schema.py goldie-human
python generate_schema.py woodlands-waterway
python generate_schema.py crown-logo
```
