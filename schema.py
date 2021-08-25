from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Commit(BaseModel):
    sha: str
    author_name: str
    message: str

    def __init__(self, **kwargs):
        kwargs["author_name"] = kwargs["commit"]["author"]["name"]
        kwargs["message"] = kwargs["commit"]["message"]
        super().__init__(**kwargs)


class Owner(BaseModel):
    html_url: str
    avatar_url: str
    login: str


class Repository(BaseModel):
    repo_id: int = Field(alias='id')
    repository_name: str = Field(alias='name')
    created_at: datetime
    owner: Owner
    last_commit: Optional[Commit] = None
