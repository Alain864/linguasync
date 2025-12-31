from fastapi import FastAPI
from app.ingestion.pipeline import ingest_episode
import boto3
import tempfile

app = FastAPI()

s3 = boto3.client("s3")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest/episode")
def ingest_episode_from_s3(
    bucket: str,
    key: str,
    episode_id: str
):
    with tempfile.NamedTemporaryFile(suffix=".srt") as tmp:
        s3.download_file(bucket, key, tmp.name)

        subtitles, sentences = ingest_episode(
            episode_id=episode_id,
            srt_path=tmp.name
        )

    return {
        "episode_id": episode_id,
        "subtitle_lines": len(subtitles),
        "sentences": len(sentences)
    }

