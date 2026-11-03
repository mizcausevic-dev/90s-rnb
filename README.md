# 90s R&B

**Slow-jam R&B kits: swung sixteenth hats, doubled backbeats, ninth chords and a vocal-range motif at 76 to 96 BPM.** 52 MIDI files (4 kits x 6 roles x 2 variations, plus 4 arrangements), notes only, no samples.

## Status

- Built and checked by script. Validator result: 52 files, 0 errors. See `midi/validation-Claude.json`.
- No human listening audition was performed for this build.
- The audio preview and the film are preview, not a master. They are a simple synthesized render, not a recording and not a mix.
- The GitHub repository is https://github.com/mizcausevic-dev/90s-rnb and it is public. The catalog address is https://mizcausevic-dev.github.io/90s-rnb/ . Treat that address as live only after it responds.
- No license is set in this repository. Add one before you sell or redistribute the files.

## Kits

| Kit | BPM | Key | Mode | Chords |
|---|---|---|---|---|
| k01 Slow Dial | 90 | Ab | ionian | Abmaj9 (2 bars) | Fm9 (2 bars) | Dbmaj7 (2 bars) | Eb7 (2 bars) |
| k02 Late Line | 82 | F | aeolian | Fm9 (2 bars) | Dbmaj9 (2 bars) | Abmaj7 (2 bars) | C7#9 (2 bars) |
| k03 Quiet Storm | 76 | C | dorian | Cm9 (2 bars) | F9 (2 bars) | Bbmaj7 (2 bars) | Gm7b5 | C7 |
| k04 Sunday Tape | 96 | D | ionian | Dmaj9 (2 bars) | Bm9 (2 bars) | Em9 (2 bars) | A13 (2 bars) |

## Roles

Each kit folder `midi/<kit>/` holds `<role>-a.mid` and `<role>-b.mid` (8 bars, 4/4, 960 ticks per quarter note, format 0) and `arrangement.mid` (32 bars, format 1, one tempo track plus six role tracks).

| Role | Channel | What it is | Written range (MIDI note) |
|---|---|---|---|
| drums | 10 | drum pattern on channel 10 (GM drum map) | GM drum map |
| bass | 1 | monophonic bass line | 36 to 52 |
| keys | 2 | chord voicings, up to four notes at once | 48 to 76 |
| motif | 3 | monophonic hook, the part the arrangement restates at the end | 60 to 79 |
| sequence | 4 | monophonic running pattern, used in place of the motif | 52 to 81 |
| pad | 5 | sustained chord layer, up to four notes at once | 48 to 72 |

## Arrangement

| Bars | Section | Parts |
|---|---|---|
| 1-8 | theme | drums A, bass A, keys A, pad A, motif A |
| 9-16 | sequence | drums A, bass A, keys A, pad A, sequence A |
| 17-24 | open | keys B, pad B, sequence B. No drums, bass or motif. |
| 25-32 | return | drums B, bass B, keys A, pad A, motif A |

Use either the combined arrangement or the separate parts. Do not stack the part files on top of the combined file.

No program changes are encoded. A conventional GM player will normally use its default piano program for pitched channels unless configured otherwise; compatible GM channel 10 percussion is treated separately. Player behavior may vary.

## Preview

Preview is Slow Dial bars 21-32 at 90 BPM, 32.026 seconds, not the 32-bar MIDI. Files: `preview/preview.mp3`, `film/preview.mp4`. Both are preview, not a master. No human listening audition was performed for this build.

## Verify

```
python3 generator/build.py 90s-rnb   # rebuilds every file below from the rules
```
MIDI bytes are reproducible from the seeds. The MP3, MP4 and JPEG files depend on the ffmpeg and Pillow versions, so their hashes can differ after a rebuild. Needs Python 3, numpy, scipy, Pillow, mido and ffmpeg.

## Layout

`midi/` the MIDI kits and the validation report. `preview/` the audio preview and its manifest. `film/` the preview film, poster and captions. `art/` the hero and square illustrations. `social/` draft post material, never posted. `articles/` draft article, never published. `catalog/` machine-readable catalog. `checks/` the release checklist. `docs/` the publication plan. `generator/` the code that wrote all of it. `index.html` and `media.html` are the catalog pages.

## Limits

Notes only. No audition by a person has happened. Rule-based generation can sound plain, so audition the parts in your own instrument before you rely on them.
