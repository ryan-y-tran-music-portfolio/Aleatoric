from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd
import argparse

aleatoric_parser = argparse.ArgumentParser(description="Aleatoric Music Generator")
aleatoric_parser.add_argument(
    "--output", "-o", type=str, help="Output to WAV instead of Playing Directly"
)
args = aleatoric_parser.parse_args()

STRUCTURES = ["AABB/CC", "ABAB/CD", "AB/CDDD"]
CHORDS = [
    "I-IV-ii-V",
    "I-vi-ii-V",
    "I-iii-IV-iv",
    "I-V-ii-V",
    "I-vi-IV-V",
    "IV-I-vi-IV",
    "I-V-vi-I",
    "I-IV-iv-I",
    "IV-V-I-I",
    "vi-IV-I-V",
]

BASE_SCALE_NOTES = {
    "A3": 220.0000,
    "ASHARP3": 233.0819,
    "B3": 246.9417,
    "C4": 261.6526,
    "CSHARP4": 277.1826,
    "D4": 293.5548,
    "DSHARP4": 311.1270,
    "E4": 329.6276,
    "F4": 349.2282,
    "FSHARP4": 369.9944,
    "G4": 391.9954,
    "GSHARP4": 415.3047,
    "A4": 440.0000,
}


def generate_song() -> np.ndarray:
    """With specific parameters.

    Returns: np.ndarray of generated song.
    """


if __name__ == "__main__":
    generated_song = generate_song()
    if args.output:
        print(
            f"When done, this song will be turned into a WAV file called {args.output}"
        )
    else:
        print("When done, this song will be played directly.")
