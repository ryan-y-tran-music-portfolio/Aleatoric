# Aleatoric

## What did I do?

I made a program that creates Alaetoric Music. There are several things that are randomized, such as song structure, line structure, base scale note, and eighth note duration. After randomizing these features, the program then randomly generates the melody; it chooses to pick a note from the current chord or major scale (regardless of which, all are within the first octave). Each chord has its notes turned into a sawtooth wave, concatenated based on song structure.

## How did it Go?

It went better than expected. I spent some time brainstorming on the ideal way to structure things such as CHORDS and MAJOR_MINOR_SEMITONES; I needed it to make sense while making the items easy to retrieve (although Python's random library made this somewhat trivial). It wasn't needed, but the extra outputs helped with the debugging process and is probably user-friendly as well. I used my previous projects as a reference when creating WAV Files and outputting songs directly.

## What's next?

While the program only has the --output flag, other flags could make the program fun; and hopefully the way things are set up in my program, it would be easily to account for different arguments. --bass is an example: each measure has the chord root be two octaves lower. --rhythm is interesting: random note patterns instead of eighth notes, although I would probably have to change the generate_sawtooth function.

## How to Build

### Installing uv

Follow the instructions to install the uv package manager [here](https://docs.astral.sh/uv/getting-started/installation/).

### Running the Program

To play the generated song directly, simply run this program via `uv run modem.py`. If you want to output it as a wav file, run this program via `uv run modem.py --output <FILE NAME>.wav`.
