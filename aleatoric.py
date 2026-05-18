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
