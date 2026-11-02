"""Factual article draft. Not published."""

from __future__ import annotations

from tools.statements import AUDITION, ON_PICTURE, PREVIEW_LINE, PROGRAM, PUBLICATION, WARNING

TITLE = "90s R&B is a note-only MIDI construction kit"
SUBTITLE = "Four kits, 32-bar arrangements, and an 8-bar simple-synth preview that is not a master"
TAGS = ["midi", "rnb", "music-production", "composition", "construction-kit"]
TAG_LINE = "Tags: " + ", ".join(TAGS)

PARAGRAPHS = [
    "DRAFT. " + PUBLICATION,
    TAG_LINE,
    "The pack is four construction kits in 4/4. Tempos are 74, 88, 68, and 96 BPM. Those integers sit in the project range 65 to 105. They are a creative direction, not a claim that the files are authentic 90s productions. Every core part is 8 bars. Every kit has one 32-bar arrangement. Lengths were chosen before the notes were written.",
    "Each kit has two variations of five core roles: drums, bass, keys, motif, and pad. That is 40 core files. There are no reference-only files. Variation B changes the phrase. It is not a velocity edit and not a uniform transpose of variation A. The four motifs use different rhythms and different interval lists. Late Ninth is A natural minor at 74. Keys hold Am7, Dm7, Em7, then Cmaj7, two bars each, and the hook waits until a three-note pickup. Offbeat Shell is F major at 88. The keys enter on the and of 1: Fmaj7, Am7, Dm7, Bbmaj7. Held Third is D dorian at 68. Chords arrive on beat 3: Dm7, G7, Cmaj7, Am7. Chorus Snap is Bb major at 96, one chord a bar: Bbmaj7, Ebmaj7, Gm7, F7, Bbmaj7, Cm7, Ebmaj7, Bbmaj7.",
    "The brief asks for vocal-friendly harmony and does not name a MIDI number. This pack keeps every pitched note at or below E5, MIDI 76, so the notes above that stay empty. Keys allow four notes from MIDI 48 to 76. The pad allows three notes from MIDI 48 to 72. The motif is monophonic from MIDI 60 to 76. Bass is monophonic from MIDI 28 to 52. C4 is 60. The resolution is 960 ticks per quarter note. Offsets are 0. No pitched note is flagged as a departure. Drums use channel 10 only: kick 36, snare 38, closed hat 42, open hat 46, crash 49. Closed and open hats do not overlap.",
    "Section contrast is in the 32-bar arrangement, not only in a label. Each kit places variation A in different role groups. Late Ninth bars 1-8 are bass and keys. Bars 9-16 add drums, the motif, and the pad. Bars 17-24 leave the pad out. Bars 25-32 keep bass, motif, and pad, and leave drums and keys out. Offbeat Shell, Held Third, and Chorus Snap use three other orders. The piano roll of the arrangement shows the empty lanes.",
    PROGRAM,
    "The preview synth plays bass and pad as sines, the motif as a triangle, and the keys as a quieter sine. Drums are a falling sine for the kick and short noise for the snare, hats, and crash. Those voices are not in the MIDI. Nothing in the file is a sample or a program change.",
    "The primary preview is bars 9-16 of Late Ninth at 74 BPM, variation A, all five roles. The motif in that window is silent until the pickup, then the hook answers over Am7, Dm7, Em7, and Cmaj7. The encoded duration is written from ffprobe to three decimal places. The 32-bar arrangement remains in the MIDI and is not the MP3. "
    + PREVIEW_LINE
    + ". The film takes its audio from that preview and shows the words "
    + ON_PICTURE
    + " on the picture and in the WebVTT captions.",
    AUDITION
    + " The validator reopened the MIDI bytes and compared them with the canonical score. That is a structural check. Chord names were checked against the pitch classes of the keys notes in each window. The sample peak written beside the preview is the peak of the integer mix. It is not a loudness measurement. Nothing in this build is claimed as a master.",
    "The stills are procedural illustrations: a wine field, an empty cream band for the register above the written notes, and five lanes. They are not photographs of a session or of performers.",
    "When you use the files, use either the combined arrangement or the separate parts. " + WARNING,
    "Call to action: keep the MIDI, the matched report, and the preview together. Do not publish this draft to Medium, Instagram, or X from the draft files alone.",
]


def markdown() -> str:
    body = "\n\n".join(PARAGRAPHS)
    return f"# {TITLE}\n\n{SUBTITLE}\n\n{body}\n"


def plain_text() -> str:
    lines = [TITLE, "", SUBTITLE, "", *PARAGRAPHS, ""]
    return "\n".join(lines) + "\n"
