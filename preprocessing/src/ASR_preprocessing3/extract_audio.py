from pathlib import Path
import tarfile
from tqdm import tqdm

# Paths and constants
ARCHIVE_PATH = Path("cv-corpus-9.0-2022-04-27-sw.tar.gz")  # Path to the dataset archive
EXTRACT_DIR  = Path("common_voice_sw")                     # Directory to extract files to
 
EXTRACT_DIR.mkdir(exist_ok=True)

# Extract only the validated.tsv and all .mp3 files from the archive
with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
    members = []
    for m in tqdm(tar.getmembers(), desc="Retrieving files"):
        if m.name.endswith("sw/validated.tsv") or m.name.endswith(".mp3"):
            members.append(m)
    print("Extracting", len(members), "files")
    tar.extractall(path=EXTRACT_DIR, members=members)