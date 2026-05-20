from scipy.io.wavfile import write
from scipy.signal import sawtooth
import numpy as np
import sounddevice as sd
import argparse
import random

aleatoric_parser = argparse.ArgumentParser(description="Aleatoric Music Generator")
aleatoric_parser.add_argument(
    "--output", "-o", type=str, help="Output to WAV instead of Playing Directly"
)
args = aleatoric_parser.parse_args()

STRUCTURES = ["AABB/CC", "ABAB/CD", "AB/CDDD"]
CHORDS = [
    ["I", "IV", "ii", "V"],
    ["I", "vi", "ii", "V"],
    ["I", "iii", "IV", "iv"],
    ["I", "V", "ii", "V"],
    ["I","vi","IV","V"],
    ["IV", "I", "vi", "IV"],
    ["I", "V", "vi", "I"],
    ["I", "IV", "iv", "I"],
    ["IV", "V", "I", "I"],
    ["vi", "IV", "I", "V"],
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

def generate_sawtooth(frequency: float, eighth_note_duration: float, sample_rate: int) -> np.ndarray:
    """For a given frequency, eighth note duration and sample_rate, generate a sawtooth wave.
    
    frequency (float): Frequency in Hz
    eighth_note_duration (float): Duration for each eighth note
    sample_rate (int): Sample Rate

    Returns: Sawtooth wave as Numpy Array
    """
    t = np.linspace(0, eighth_note_duration, int(sample_rate * eighth_note_duration), endpoint=False)
    wave = sawtooth(2.0 * np.pi * 5.0 * t)
    return wave

def generate_song() -> np.ndarray:
    """With specific parameters.

    Returns: np.ndarray of generated song.
    """
    print("Parameters Generated: \n" + "="*20 )

    structure = random.choice(STRUCTURES)
    print(f"Structure: {structure}")

    # For the structure, get each letter. Each letter gets a unique chord.
    all_letters = [character for character in structure if character.isalpha()]
    unique_letters = list(dict.fromkeys(all_letters))
    chords = random.sample(CHORDS, 3)
    unique_chords = dict(zip(unique_letters, chords))
    for letter, chord in unique_chords.items():
        print(f'{letter} Chord: {chord}')
    
    base_scale_notes_as_list = [key for key in BASE_SCALE_NOTES]
    key = random.choice(base_scale_notes_as_list)
    key_frequency = BASE_SCALE_NOTES[key]
    print(f"Key Chosen: {key} || Frequency: {key_frequency}")

    # convert bpm to eighth note duration
    bpm = random.randint(80, 160)
    bps = bpm / 60.0
    eighth_note_duration = 0.5 / bps
    print(f"BPM: {bpm} || BPS: {bps} || Eighth-Note Duration: {eighth_note_duration}")

    print("="*20 )

if __name__ == "__main__":
    generated_song = generate_song()
    if args.output:
        print(
            f"When done, this song will be turned into a WAV file called {args.output}"
        )
    else:
        print("When done, this song will be played directly.")
