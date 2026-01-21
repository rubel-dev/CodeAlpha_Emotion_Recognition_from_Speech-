from pathlib import Path

def load_audio(path:str):

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Audio file not found: {path}")
    
    return None, None


def extract_mfcc(path:str):

    return None