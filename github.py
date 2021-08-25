from schema import Commit, Repository, Owner
import requests
from typing import List
from pydantic import parse_obj_as


class Github:

    search_url = 'https://api.github.com/search/repositories'
    commits_url = 'https://api.github.com/repos/{owner}/{repo}/commits'

    def find_repo(self, query: str, sort_key=None, reverse=True) -> List[Repository]:
        response = requests.get(Github.search_url, params={'q': query})
        repos = parse_obj_as(List[Repository], response.json()['items'])
        if sort_key:
            repos.sort(key=lambda x: getattr(x, sort_key), reverse=reverse)
        return repos

    def get_last_commit(self, repo: Repository) -> Commit:
        response = requests.get(Github.commits_url.format(owner=repo.owner.login, repo=repo.repository_name), params={"per_page": 1})
        if len(response.json()) > 0:
            commit = parse_obj_as(Commit, response.json()[0])
            return commit
        else:
            return None