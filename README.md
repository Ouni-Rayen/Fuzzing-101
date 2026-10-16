# SEC Club — Beginner Web CTF (Fuzzing)

## Theme
Club colors: deep navy background, soft lavender, cyan glow.

## Challenge Flow
1. Visit the homepage
2. Check `/robots.txt` → hint about a colors file
3. Find and download `/colors.txt` (list of ~100 color names)
4. Fuzz the color names as paths (e.g. `/red`, `/navy`, `/cyan` …)
5. The correct one (`/cyan`) reveals the flag

## Flag
`Securinets{F4di_Y4_b000000h4}`

## Quick Start with Docker

```bash
# Build
docker build -t sec-club-ctf .

# Run
docker run -d -p 5000:5000 --name sec-ctf sec-club-ctf

# Open http://localhost:5000
```

Stop & remove:
```bash
docker stop sec-ctf && docker rm sec-ctf
```

## Local (without Docker)
```bash
pip install -r requirements.txt
python app.py
```

## Notes for organizers
- Pure path fuzzing — no parameters, no auth, no XSS.
- All non-cyan color paths return a friendly 404 that still stays on-theme.
- The homepage, robots.txt and colors.txt are intentionally designed to push players toward fuzzing the color list.
