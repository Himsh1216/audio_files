from pydub import AudioSegment


def isolate_background(src_path: str, dst_path: str) -> None:
    """Extract background music by subtracting stereo channels."""
    song = AudioSegment.from_file(src_path)
    if song.channels == 2:
        left, right = song.split_to_mono()
        background = left.overlay(right.invert_phase())
    else:
        background = song
    background.export(dst_path, format='wav')
