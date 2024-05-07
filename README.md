# automation-to-add-all-repos-to-a-github-teams
GitHub automation to add all repos to a specific team across GitHub org

# use case
* Security team may need to monitor all repos 
* core team need to be added as a reviewer for PP's, so they need to add the teams to repos

# How code works

* This repository contains code to add all repositories in a github organization to a specific github teams

* Uses Github REST API along with python.

* This will add all repos in organization to the team thats specfied returning 204 status code.


## GitHub API Calls
The program makes several API calls to the GitHub API using the requests module to list repositories, list teams, and add repositories to teams. It uses the Authorization header with a GitHub token (os.getenv('GH_TOKEN')) for authentication.

# Program Inputs

The program requires 3 Inputs which are passed as inputs

* organization --> GitHub Organization name
* github_team_name --> GithHub team name
* permission --> Permissions for Github teams across repository `admin`,`push`,`pull`,`maintain`,`triage`

# dot env file

```markdown
GH_TOKEN="<your github token here>"
```

# Run code in local
1. clone the repository to your local
2. Change directory to the cloned repository
3. set up the .env file and pass the auth token there.
4. Run `python3 add_repos_to_gh_teams.py --organization <organization name> --github_team_name <github team name> --permission <permission required>`


>[!NOTE]
> This Program uses Personal Access token for GitHub authentication 
> On local testing python-dotenv with .env file is used
> On GitHub Workflow, passed as a environment variable in from GitHub Secrets.