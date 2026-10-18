# Visual pitch v2

This version prioritizes full-width art, short labels, large diagrams and motion. It retains the 16-topic sequence of the earlier visual pitch. The mandatory official-template deck remains a separate deliverable.

## Brand

The user selected **Pagemi**, pronounced **PAGE-mee**, on 18 October 2026. The name is set in `brand.json`. Website display names, the official-template edition, active docs, video scripts and subtitles are synchronized. Existing cloud project, repository and public URL identifiers remain unchanged. Historical evidence and archive editions retain their original names. Web name screening is not domain or trademark clearance.

## Open

Open the standalone HTML from the output folder. Arrow keys change pages; B switches static/motion modes; Escape opens the index. The PDF is the static equivalent.

The six photographic slides include two newly generated images, two reused concept images and two actual interface captures. Photos drift subtly, a line scans the image, and the template provides sequential diagram, card and chart reveals. All added continuous motion stops in static mode; reduced-motion preference disables it.

## Asset sources

- `assets/icons/*.svg`: Phosphor Icons, light weight, downloaded 18 October 2026 from https://github.com/phosphor-icons/core/tree/main/assets/light . MIT license included in `assets/icons/LICENSE.txt`. Inline SVG colors inherit the deck palette.
- `01-reflex-loop.*`: built-in image generation, folded metal ribbon. Concept art, not a technical diagram. File stem is a working visual name, not a finalized brand.
- `03-rain-texture.*`: built-in image generation, droplets on woven fabric. Concept art, not a product test or evidence of waterproofing.
- `04-merchant-concept.jpg`, `09-evidence-concept.jpg`: reused generated editorial images from the earlier deck.
- `07-live-workbench.jpg`: actual public interface captured 18 October, before audit.
- `11-historical-storefront.jpg`: actual historical interface captured 13 October.
- Exact new generation prompts are saved in `prompts.json`; original PNGs remain in `images/`.

Sources and detailed limitations live here rather than on every slide. The slides retain synthetic-image labels, test scope, earlier failures and untested outcomes.

## Evidence

Five completed live journeys, 35 local tests, two earlier timeouts and the estimated model-call usage come from `../video-kit/assets/evidence/vertex-release-2026-10-18.json`. The evidence is unchanged. No new Gemini calls were made for this design revision. The original agent prompt and its fingerprint remain unchanged; this is a display-name-only application release.

## Rebuild

Run `build.py` from this directory. The Guizang template, print helpers and Motion bundle are included locally. Set the selected brand once in `brand.json`, rebuild, render and inspect all pages before exporting final delivery files.
