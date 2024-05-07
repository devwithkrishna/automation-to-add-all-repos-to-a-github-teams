import argparse
import os
import requests
from dotenv import load_dotenv
from list_all_org_repos import list_all_github_org_repos

def add_repos_to_github_team(organization:str, github_team_name:str,repo_names: list, github_teams_list: list[dict], permission:str):
    """
    Add all repos to a github team
    :param organization:
    :param github_team_name:
    :return:
    """
    slug = None
    for github_team in github_teams_list:
        if github_team_name == github_team['name']:
            slug = github_team['slug']
            print(f'The slug of the team name {github_team_name} - {slug}')
            break
    if slug is not None:
        for repo in repo_names:
            teams_endpoint = f'https://api.github.com/orgs/{organization}/teams/{slug}/repos/{organization}/{repo}'
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
                "X-GitHub-Api-Version": "2022-11-28"
            }
            data = {
                "permission": permission
            }
            response = requests.put(url=teams_endpoint,headers=headers,json=data)
            if response.status_code == 204:
                print(f'{repo} repository on {organization} has been added to {github_team_name} github team.')
            else:
                print(f'unable to complete the operation - adding {repo} repository to {github_team_name} github team.')



def list_all_github_teams_in_organization(organization:str):
    """
    Lists all teams in an organization
    :param organization:
    :return:
    """
    api_endpoint = f'https://api.github.com/orgs/{organization}/teams'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url=api_endpoint, headers=headers)
    response_json = response.json()
    github_teams_list = []
    for team in response_json:
        team_dict = {
            'name' : team['name'],
            'slug' : team['slug']
        }
        github_teams_list.append(team_dict)

    return github_teams_list


def main():
    """main function to test the code"""
    parser = argparse.ArgumentParser(description="Add all repos to a github team")
    parser.add_argument("--organization",required=True, type=str, help="Github organization name")
    parser.add_argument("--github_team_name",required=True, type=str, help="Your GitHub team name")
    parser.add_argument("--permission", required=True,choices=['admin', 'push', 'pull', 'triage', 'maintain'], help="Permissions for Github teams across repositories" )

    #Processing args
    args = parser.parse_args()
    organization = args.organization
    github_team_name = args.github_team_name
    permission = args.permission

    load_dotenv()
    # function call
    repo_names = list_all_github_org_repos(organization=organization)
    print(repo_names)
    github_teams_list = list_all_github_teams_in_organization(organization=organization)
    print(github_teams_list)
    add_repos_to_github_team(organization=organization, github_team_name=github_team_name, repo_names=repo_names, github_teams_list=github_teams_list, permission=permission)


if __name__ == "__main__":
    main()