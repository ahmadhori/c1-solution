from typing import List

import requests
from pydantic import parse_obj_as

from schema import Commit, Repository


class Github:
    """[summary]
    This class is reposnsible to communicate with Github API and to return the results
    """

    search_url = 'https://api.github.com/search/repositories'
    commits_url = 'https://api.github.com/repos/{owner}/{repo}/commits'

    def find_repo(self, query: str, sort_key=None, reverse=True) -> List[Repository]:
        """[summary]

        Parameters
        ----------
        query : str
            Search query
        sort_key : [type], optional
            you can provide attribute name to sort by it, by default None
        reverse : bool, optional
            order of sorting, by default True which means desc order

        Returns
        -------
        List[Repository]
            list of repositories based on search term
        """
        response = requests.get(Github.search_url, params={'q': query})
        response.raise_for_status()
        repos = parse_obj_as(List[Repository], response.json()['items'])
        if sort_key:
            repos.sort(key=lambda x: getattr(x, sort_key), reverse=reverse)
        return repos

    def get_last_commit(self, repo: Repository) -> Commit:
        """[summary]

        Parameters
        ----------
        repo : Repository
            repository which you want to fetch the commits for it

        Returns
        -------
        Commit
            returns a commit object according to the schema
        """
        response = requests.get(Github.commits_url.format(owner=repo.owner.login, repo=repo.repository_name), params={"per_page": 1})
        response.raise_for_status()
        if len(response.json()) > 0:
            commit = parse_obj_as(Commit, response.json()[0])
            return commit
        else:
            return None
