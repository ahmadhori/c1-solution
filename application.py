import logging
from typing import List, Optional

import requests
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from github import Github

logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/navigator", response_class=HTMLResponse)
def search_github(request: Request, search_term: Optional[str] = None):
    github = Github()
    try:
        repos = github.find_repo(query=search_term, sort_key="created_at", reverse=True)[:5]
        for repo in repos:
            repo.last_commit = github.get_last_commit(repo)
    except requests.exceptions.HTTPError as err:
        return templates.TemplateResponse("error.html", {"request": request})

    return templates.TemplateResponse("template.html",
                                      {"request": request,
                                       "search_term": search_term,
                                       "repository_list": repos})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9876)
