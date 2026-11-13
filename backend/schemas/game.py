from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class GameSessionCreate(BaseModel):
    user_id: int | str | None = None
    firebase_uid: str | None = Field(default=None, max_length=128)
    user_name: str | None = Field(default=None, max_length=100)
    game_id: int | None = None
    lesson_id: int | None = None
    game_key: str | None = Field(default=None, max_length=100)
    game_type: str | None = Field(default=None, max_length=100)


class GameSessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    game_id: int
    started_at: datetime
    score: int | None


class GameEventCreate(BaseModel):
    action: str = Field(min_length=1, max_length=100)
    event_data: str | None = Field(default=None, max_length=4000)