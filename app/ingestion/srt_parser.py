import pysrt


def parse_srt(file_path: str):
    subs = pysrt.open(file_path, encoding="utf-8")
    lines = []

    for sub in subs:
        lines.append({
            "start_time": sub.start.ordinal / 1000,
            "end_time": sub.end.ordinal / 1000,
            "raw_text": sub.text.replace("\n", "")
        })

    return lines

