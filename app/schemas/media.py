from pydantic import BaseModel


class Episode(BaseModel):
    episode_id: str
    title: str
    season_number: int
    episode_number: int
    language: str = "ja"

