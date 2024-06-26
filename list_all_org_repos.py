import argparse
import os
import requests
from dotenv import load_dotenv

def list_all_github_org_repos(organization:str):
    """
    python program to list all repos in a org
    :param organization:
    :return:
    """
    repo_endpoint = f'https://api.github.com/orgs/{organization}/repos'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {
        'sort':'created',
        'per_page': 30,
        'page': 1
    }

    # List to hold all repositories
    all_repositories = []
    # Paginate through all pages
    while True:
        # Make the GET request with query parameters
        response = requests.get(url=repo_endpoint, headers=headers, params=params)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            repositories = response.json()
            if not repositories:
                break
            all_repositories.extend(repositories)
            params["page"] += 1
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            break

    # response = requests.get(url=repo_endpoint, headers=headers)
    # response_json = response.json()
    repo_names = []
    for repos in all_repositories:
        repo_names.append(repos['name'])

    return repo_names


def main():
    """main function to test the code"""
    parser = argparse.ArgumentParser(description="Add all repos to a github team")
    parser.add_argument("--organization",required=True, type=str, help="Github organization name")
    # parser.add_argument("--github_team_name",required=True, type=str, help="Your GitHub team name")
    # parser.add_argument("--permission", required=True,choices=['admin', 'push', 'pull', 'triage', 'maintain'], help="Permissions for Github teams across repositories" )

    #Processing args
    args = parser.parse_args()

    organization = args.organization
    # github_team_name = args.github_team_name
    # permission = args.permission

    load_dotenv()
    # function call
    repo_names = list_all_github_org_repos(organization=organization)
    print(repo_names)


if __name__ == "__main__":
    main()