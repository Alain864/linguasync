import uuid
from app.schemas.subtitles import SubtitleLine, CleanSentence
from app.ingestion.srt_parser import parse_srt


def ingest_episode(episode_id: str, srt_path: str):
    raw_lines = parse_srt(srt_path)

    subtitle_objects = []
    sentence_objects = []

    for line in raw_lines:
        subtitle = SubtitleLine(
            episode_id=episode_id,
            start_time=line["start_time"],
            end_time=line["end_time"],
            raw_text=line["raw_text"]
        )
        subtitle_objects.append(subtitle)

        sentence = CleanSentence(
            sentence_id=str(uuid.uuid4()),
            episode_id=episode_id,
            text=line["raw_text"]
        )
        sentence_objects.append(sentence)

    return subtitle_objects, sentence_objects

