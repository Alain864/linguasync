from pydantic import BaseModel


class SubtitleLine(BaseModel):
    episode_id: str
    start_time: float
    end_time: float
    raw_text: str


class CleanSentence(BaseModel):
    sentence_id: str
    episode_id: str
    text: str

