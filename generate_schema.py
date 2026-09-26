#!/usr/bin/env python3
"""
MTM Multimodal Asset Schema Generator (MTM-BOOSTΩ-IML-V1.0)
Generates machine-readable Schema.org JSON-LD snippets (ImageObject, VideoObject, AudioObject)
for any asset in the mtm-assets repository.
"""

import sys
import os
import json
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(BASE_DIR, "asset_manifest.json")

def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        print(f"Error: Manifest not found at {MANIFEST_PATH}. Run build_catalog.py first.", file=sys.stderr)
        sys.exit(1)
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_asset(query, manifest):
    query = query.replace("\\", "/").lower().strip()
    matches = []
    for item in manifest.get("dataset", []):
        rel_path = item.get("relPath", "").lower()
        name = item.get("name", "").lower()
        if query in rel_path or query in name:
            matches.append(item)
    return matches

def generate_json_ld(asset):
    schema = {
        "@context": "https://schema.org",
        "@type": asset.get("@type", "MediaObject"),
        "@id": asset.get("@id"),
        "name": asset.get("name"),
        "description": asset.get("description"),
        "contentUrl": asset.get("contentUrl"),
        "encodingFormat": asset.get("encodingFormat"),
        "author": {
            "@type": "Organization",
            "name": "MT Media AI",
            "url": "https://mtmediaai.com"
        }
    }
    if "contentLocation" in asset:
        schema["contentLocation"] = asset["contentLocation"]
    return schema

def main():
    parser = argparse.ArgumentParser(description="Generate Schema.org markup for MTM multimodal assets.")
    parser.add_argument("query", help="Asset filename or partial path (e.g. goldie-human.webp, landmarks, crown)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON only")
    args = parser.parse_args()

    manifest = load_manifest()
    results = find_asset(args.query, manifest)

    if not results:
        print(f"No asset found matching '{args.query}'", file=sys.stderr)
        sys.exit(1)

    for asset in results:
        schema = generate_json_ld(asset)
        if args.json:
            print(json.dumps(schema, indent=2))
        else:
            print("=" * 60)
            print(f"ASSET: {asset['name']} ({asset['relPath']})")
            print("=" * 60)
            print("\n<!-- Next.js / HTML JSON-LD Script -->")
            print('<script type="application/ld+json">')
            print(json.dumps(schema, indent=2))
            print('</script>\n')
            
            if asset.get("@type") == "ImageObject":
                print("<!-- Next.js Image Component -->")
                print(f'<Image src="{asset["contentUrl"]}" alt="{asset["description"]}" width={{1200}} height={{630}} priority />')
            elif asset.get("@type") == "VideoObject":
                print("<!-- HTML5 Video Component with VTT -->")
                print(f'<video controls poster="/assets/fallback.webp">')
                print(f'  <source src="{asset["contentUrl"]}" type="{asset["encodingFormat"]}">')
                print(f'  <track src="/transcripts/{os.path.splitext(os.path.basename(asset["relPath"]))[0]}.vtt" kind="captions" srclang="en" label="English">')
                print('</video>')
            elif asset.get("@type") == "AudioObject":
                print("<!-- HTML5 Audio Component with Transcript -->")
                print(f'<audio controls src="{asset["contentUrl"]}">')
                print(f'  <track src="/transcripts/{os.path.splitext(os.path.basename(asset["relPath"]))[0]}.vtt" kind="captions" srclang="en" label="English">')
                print('</audio>')
            print()

if __name__ == "__main__":
    main()
