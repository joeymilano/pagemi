# Art direction and sound brief

## Film grammar

**Emotional arc:** something is wrong → evidence makes it legible → approval becomes outdated → a real repair reaches the page → the merchant keeps control.

The opening metaphor is a support ticket leaving the screen while the misleading page stays. It is an illustrative scene, not a built-in Pagemi ticket feature. Use product image, exact page claim and a minimal ticket-shaped graphic. Do not imply an actual customer lost money or a real backpack failed a water test.

## Visual specification

- Canvas: 1920×1080, 30 fps. Keep all critical text inside 96 px horizontal / 70 px vertical safe margins. Reframe for the 4K captured sources without stretching them.
- Color: background `#080D0A`, primary text `#E9F1EB`, secondary `#A7BBAE`, evidence/confirmation `#34D399`, missing/outdated `#E8B45F`, unsupported claim `#EF8F76`.
- Type: Manrope 700 for titles, DM Sans 400 for narration captions. Font files and licenses included. On-screen title 72–100 px; captions 38–44 px; at most two caption lines and approximately 42 characters per line. The concept SVGs use fallback Arial for portability; replace that with packaged Manrope in the final film.
- Product UI retains its own typography and proportions. Use real screen capture at 100% zoom and magnify a crop in post. Do not manufacture prettier result text.
- Motion: fast editorial reveals 8–12 frames; focus changes 12–18 frames; major pushes 30–45 frames; result holds at least 90–150 frames. Easing `(0.22, 1, 0.36, 1)` for the outer film composition. The filmed UI keeps its own timing.
- Opening: a shallow 3D page plane, maximum 8° rotation; no spinning laptops. The stamp exits in the first 2 seconds, but the claim remains. By 13 seconds the product fills the frame.
- Evidence: one 2 px connection line from quoted source to changed statement. Line movement follows source selection, not imaginary reasoning inside Gemini.
- Invalidation: a single green connection becomes amber and breaks after the actual evidence update. Hold the real outdated state. Do not invent a “100% safe” seal.
- Publish: match the location of the old sentence to the new sentence across the cut. Keep refresh and version number visible. Restore shows a new recorded version, never a reverse transition suggesting history was erased.
- Numbers: five independent duration bars, not a “100% success” doughnut. Show the sample size. Earlier failures receive a readable line.
- End: actual product name, accepted tagline, live demo/repository destination. Render a QR only from the verified canonical link and test it on a phone. QR is optional; readable title and URL matter more.

## Five-second hook, frame by frame

| Frames at 30 fps | Picture | Sound |
|---|---|---|
| 0–17 | Dark page plane already in frame, claim faintly legible; no empty logo intro | Dry low pulse |
| 18–35 | Minimal ticket with `Resolved` lands in foreground | Short stamp cue |
| 36–59 | Ticket flicks away; `100% waterproof` is still lit | Reverb cuts sharply |
| 60–104 | The ticket is closed. Small line at top; old claim stays underneath | Quiet air, narrator close |
| 105–149 | The mistake is still live. Accent becomes coral; 4-frame movement then stable | One controlled bass impact |

The first spoken line must fit naturally, not be sped up. The product scenario disclosure can remain in a readable lower corner for the entire opening.

## Audio

Use an original or properly licensed 112 BPM restrained electronic bed. Suggested palette: a warm sub pulse, a dry clock-like tick and a thin glass harmonic. No cinematic trailer braaams, famous-song imitation, or synthetic “AI voice” chatter. The included three 48 kHz cue sketches are original signal synthesis, not a finished soundtrack.

Voice should be confident and conversational. Approximately 333 words over 195 seconds leaves room for UI inspection. Use no celebrity or founder voice imitation without authorization. Final voice choice depends on available authorized recording/TTS; do not buy services silently.

Target final mix: about -16 LUFS integrated, true peak no higher than -1 dBTP. Duck music by roughly 5–8 dB under speech and check by listening on laptop speakers. These are production targets, not measurements of supplied files. Avoid adding “success” sounds before the real system has confirmed the operation.

## Short cut

Create 3:15 first for the current submission field. The alternate cut removes twenty seconds as listed in `timeline.json`; rewrite the corresponding spoken sentences and retime captions. Do not simply delete the last twenty seconds or accelerate all speech. The factual disclosure, human approval and served-page verification must survive both cuts.
