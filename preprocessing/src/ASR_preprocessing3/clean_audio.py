from pathlib import Path
import pandas as pd
from pydub import AudioSegment, silence
from tqdm import tqdm

# Try multiprocessing for faster processing
from concurrent.futures import ProcessPoolExecutor

# Paths and constants
INPUT_DIR  = Path("common_voice_sw")    # Input directory with the Common Voice dataset
OUTPUT_WAVS  = Path("cleaned_sw_audio") # Directory for cleaned wav files
MANIFEST_CSV = Path("manifest_sw.csv")  # Output manifest CSV file
TARGET_SR    = 16_000                   # Target sample rate for audio
SIL_THRESH   = -40                      # Silence threshold in dB
MIN_MS       = 200                      # Minimum duration (ms) for output clips

# Ensure output directories exist
OUTPUT_WAVS.mkdir(exist_ok=True)

# Find the validated.tsv file
tsv_path = next(INPUT_DIR.rglob("validated.tsv"))
print("tsv:", tsv_path)
df = pd.read_csv(tsv_path, sep="\t")  # Load TSV as DataFrame
print(df)

# Process each row to clean audio and create manifest
def process_row(row):
    mp3_abs = INPUT_DIR / f"cv-corpus-9.0-2022-04-27/sw/clips/{row['path']}"
    if not mp3_abs.exists():
        return None
    try:
        audio = AudioSegment.from_file(mp3_abs, format="mp3")
    except Exception:
        return None
    chunks = silence.split_on_silence(audio, silence_thresh=SIL_THRESH, min_silence_len=150)
    if chunks:
        audio = sum(chunks)
    if len(audio) < MIN_MS:
        return None
    audio = audio.set_frame_rate(TARGET_SR).set_channels(1)
    wav_name = row["path"].replace(".mp3", ".wav")
    wav_out  = OUTPUT_WAVS / wav_name
    wav_out.parent.mkdir(parents=True, exist_ok=True)
    audio.export(wav_out, format="wav")
    return {
        "wav_path"  : str(wav_out.resolve()),
        "duration"  : len(audio) / 1000.0,
        "transcript": row["sentence"]
    }

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_row, [row for _, row in df.iterrows()]), total=len(df)))
    rows = [r for r in results if r]

    # Write manifest CSV with paths, durations, and transcripts
    pd.DataFrame(rows).to_csv(MANIFEST_CSV, index=False)
    print(f"\n kept {len(rows):,} clips.")
    print("   wavs: ", OUTPUT_WAVS.resolve())
    print("   csv: ", MANIFEST_CSV.resolve())
