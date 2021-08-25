import logging
from typing import Optional

import requests
import uvicorn
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


from github import Github

logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/navigator", response_class=HTMLResponse)
def search_github(request: Request, search_term: str = Query(..., min_length=1)):
    """[summary]
    This endpoint will search for Github repositories using search term
    Parameters
    ----------
    search_term : str
        string that you want to search for (must be a non empty string)

    Returns
    -------
    [type]
        html page which shows to top results according to the task criteria
    """
    github = Github()
    try:
        repos = github.find_repo(query=search_term, sort_key="created_at", reverse=True)[:5]
        for repo in repos:
            repo.last_commit = github.get_last_commit(repo)
    except requests.exceptions.HTTPError as err:
        return templates.TemplateResponse("error.html", {"request": request,
                                                         "message": "Failed to fetch the data from github, please try again later..."})

    return templates.TemplateResponse("template.html",
                                      {"request": request,
                                       "search_term": search_term,
                                       "repository_list": repos})


@app.get("/")
async def redirect_to_docs():
    """[summary]
    Redirect to the documentation page when accessing root
    """
    response = RedirectResponse(url='/docs')
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9876)
