# Copyright 2023 ROOIGETY, all rights reserved.
#
# Written by rooigety <flanker_sheen.Of@icloud.com> and originally
# created on 2023-03-13.

from typing import List, Tuple

import numpy as np
import plotly.express as px
import streamlit as st

CHORDS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRINGS = ["E", "A", "D", "G", "B", "E"]


def main():
    st.title("Chord Finder")

    chord = st.sidebar.selectbox("Chord", CHORDS)

    mode = st.sidebar.radio("Mode", ["Major", "Minor"])

    if chord:
        # Find triads from the selected chord.
        triads = find_triads(chord, mode)

        st.subheader(f"Triads: {triads}")
        open_chord, open_places = find_open_chord(triads)
        colors = {chord: 0}
        for note in open_chord:
            if not note in colors and note != "x":
                colors[note] = len(colors)

        color_setting = []
        for note in open_chord:
            rgb = [0, 0, 0]
            if note in colors:
                rgb[colors[note]] = 255
            rgb = f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"
            color_setting.append(rgb)

        fig = px.scatter(
            y=range(1, 7),
            x=open_places,
        )
        start = max(0, min(open_places))
        offset = 0
        if start == 0:
            offset = 1
            fig.add_vline(x=0, line_width=5, line_color="gray")
        for i in range(start + offset, max(open_places) + 1):
            fig.add_vline(x=i, line_width=1, line_dash="dash", line_color="gray")

        fig.update_layout(
            xaxis={"categoryorder": "category ascending"},
            # xaxis_type="category",
            xaxis_title="Fret",
            xaxis_tickvals=list(range(max(open_places) + 1)),
            xaxis_ticktext=list(range(max(open_places) + 1)),
            yaxis_title="String",
            xaxis_range=[max(0, min(open_places)) - 0.5, max(open_places) + 1],
        )
        fig.update_traces(marker_size=20, marker_color=color_setting)

        st.plotly_chart(fig)


def make_tones(chord: str) -> list:
    """Make tones from the selected chord."""
    index = CHORDS.index(chord)
    return CHORDS[index:] + CHORDS[:index]


def find_triads(chord: str, mode: str) -> list:
    """Find triads from the selected chord."""
    tones = make_tones(chord)
    if mode == "Major":
        return [tones[i] for i in [0, 4, 7]]
    else:
        return [tones[i] for i in [0, 3, 7]]


def find_open_chord(triads: List[str]) -> Tuple[List[str]]:
    """Find open chord from the selected triads."""
    chord = []
    places = []
    for string in STRINGS:
        tones = make_tones(string)
        for note in tones:
            if note in triads:
                chord.append(note)
                places.append(tones.index(note))
                break

    # # Makes sure fingering is okay.
    # chord.reverse()
    # places.reverse()
    # _strings = STRINGS.copy()
    # _strings.reverse()

    # anchor = places[0]
    # for i in range(1, len(places)):
    #     tones = make_tones(_strings[i])

    #     # Find the next note from the triad in this string.
    #     for fret in range(places[i] + 1, 12):
    #         if tones[fret] in triads:
    #             if abs(fret - anchor) < abs(places[i] - anchor):
    #                 chord[i] = tones[fret]
    #                 places[i] = fret
    #             else:
    #                 fret = places[i]

    #             anchor = fret
    #             break

    # places.reverse()
    # chord.reverse()

    if places[0] == 0 and chord[0] != triads[0]:
        chord[0] = "x"
        places[0] = -1

    return chord, places
