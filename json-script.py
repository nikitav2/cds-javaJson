import requests
import json
import argparse

####---------- MAIN ----------####

my_parser = argparse.ArgumentParser('Getting the Github token')
my_parser.add_argument('auth',
                           metavar='<str>',
                           type=str,
                           help='auth token')
my_parser.add_argument('repoName',
                           metavar='<str>',
                           type=str,
                           help='repo_name')

# Eexecute parse_args()
args = my_parser.parse_args()




def main():

    ####---------- REQUESTS ----------####
    # This will probably change. We need:
    #
    # >Read in Master spreadsheet/CSV
    # >Read in Repo List
    # >Read in Artifact ID List
    #
    # 1. GET Request to get all repositories in the org
    # 1a. For repo in repo json, If Repo is new, append repo to an indexed list
    # 1b. Write updated Repo List
    #
    # 2. For repo in Repo List
    # 2a. GET Request for all artifacts json
    # 2b. For artifact in Artifact JSON
    # 2c.   If ID NOT IN existing Artifact List:
    # 2d.       Append ID to Art List (print Art ID to check)
    # 2e.       Download and Unzip Test-Results.json. Emulate the Curl Request we have:
    ###
    ### curl -L -o test-json-output.zip -H 'Authorization: TOKEN' <token ID Here> https://api.github.com/repos/nikitav2/cds-javaJson/actions/artifacts/116050990/zip
    ###
    # 2f.       Add as a new line to the Master Spreadsheet
    #
    # 3. Write new Master Spreadsheet to file with DATE in file name
    from pprint import pprint


    # JSON:  JSON format, read in existing JSON
    artifact_list = []
    repo_name_list = []

    file = open('cds-GithubActionIntegration.json')
    data = json.load(file)
    # Should I check  repoName and TestName? Or just repoName
    for test_repo in data:
        repo_name_list.append(test_repo['repoName'])


    # Step 1
    # setup owner name , access_token, and headers
    owner = "nikitav2"
    access_token = "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"
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', "Authorization": "TOKEN " + access_token}


    for page_number in range(1):
        try:
            # to find all the repo_name_list' names from each page
            url = f"https://api.github.com/users/{owner}/repos?page={page_number}"
            print(headers)
            print(url)
            repo = requests.get(url, headers=headers)
            repo = repo.json()

            for i in range(len(repo)):
                repo_name = repo[i]['name']
                if repo_name not in repo_name_list:
                    repo_name_list.append(repo_name)

        except:
            repo_name_list.append(None)



    # dictionary: (key repo_name, value: whole list returned from specific artifact id
    #Step 2
    for repo_name in repo_name_list:
        # Set Request Parameters
        auth = "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"
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': "TOKEN " + auth}
        url = f"https://api.github.com/repos/nikitav2/{repo_name}/actions/artifacts" #add /zip for download

        ## GET Request with Parameters variable
        r = requests.get(url, headers=headers)
        json_data = r.json()
        if (r.status_code == 404):
            continue
        else:
            #     curl command so that I can access the specific artifact and then append it to JSON
        # not sure what is going on heree
            print('idk')

        # print some log statements to cacth exceptions
        ## Print JSON


    with open('cds-GithubActionIntegration.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    # my_parser = argparse.ArgumentParser('Getting the Github token')
    # my_parser.add_argument('auth',
    #                        metavar='<str>',
    #                        type=str,
    #                        help='auth token')
    # my_parser.add_argument('repoName',
    #                        metavar='<str>',
    #                        type=str,
    #                        help='repo_name')
    #
    # # Execute parse_args()
    # args = my_parser.parse_args()
    #
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': "TOKEN " + args.auth}
    url = f"{args.repoName}/{repo_name}/actions/artifacts"  # add /zip for download
    #do i need two requests? One to get the github token and one to get the actual repository.
    input_path = args.Path


#     python main.py -auth ${{ secrets.AUTH_TOKEN }}


#     github token should be located in git config --global credential.helper manager-core




## Execute main function
main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Next Steps....preffered way to load in tokens without putting them into
# Enter Flags and Paramters(pointing to token), import ARGPARSE --> CLI program
