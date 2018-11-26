# How to write rules

Please follow the DATA model user guide present [here](https://www.juniper.net/documentation/en_US/healthbot/help/information-products/pathway-pages/topic-131332.html).
Submit only the .conf files

# How to contribute

### Juniper Employees
- Subscribe to 'jfit-rules-official' alias on jam.juniper.net
- Create a personal fork of the project on Github
- Clone the fork on your local machine. Your remote repo on Github is called origin
- Add the original repository as a remote called upstream
- If you created your fork a while ago be sure to pull upstream changes into your local repository. Your fork needs to be in sync with upstream for pull request to get merged
- Your latest commit on the pull request must be a verified commit. Follow the following steps for signing a commit.
  - Follow the steps from [here](https://help.github.com/articles/generating-a-new-gpg-key/) to generate and add gpg key to your github user account. Use your internal juniper email address for the key. 
  - Follow the steps from [here](https://help.github.com/articles/adding-an-email-address-to-your-github-account/) to add and verify the internal juniper email address to your github account 
  - Set your local repo to use the key generated above for making signed commits
    - Use the `gpg --list-secret-keys --keyid-format LONG` command to list GPG keys and copy the short key
      ```
      $ gpg --list-secret-keys --keyid-format LONG
      /Users/hubot/.gnupg/secring.gpg
      ------------------------------------
      sec   4096R/<COPY_SHORT_KEY> 2016-03-10 [expires: 2017-03-10]
      uid                          Hubot 
      ssb   4096R/42B317FD4BA89E7A 2016-03-10
      ```
    - Set git to use commit signing using `git config commit.gpgsign true`
    - Set git to use the key generated above using `git config user.signingKey <PASTE_SHORT_KEY_HERE>`
    - Use '-S' flag while making a commit e.g. `git commit -S -m your commit message`
- From your fork open a pull request to the development branch
- NOTE - You need to set the juniper email id in your git configuration
    
### Others
- All others can only contribute to the 'Community_Supplied' folder. Steps to follow are as follows
  - Create a personal fork of the project on Github
  - Clone the fork on your local machine. Your remote repo on Github is called origin
  - Add the original repository as a remote called upstream
  - If you created your fork a while ago be sure to pull upstream changes into your local repository. Your fork needs to be in sync with upstream for pull request to get merged
  - Make changes 
  - From your fork open a pull request to the development branch

**NOTE** 
Pull request will be closed automatically if you contributed to the 'Juniper_Official' folder. Please refrain from doing that if you are not a employee

# Automated Testing

- CI pipeline is run for every submitted and updated pull request. Reviewer will only review the rules after it passes the automated syntax testing.
- Any syntax error occured on all the changed files will be reported back as a review comment.
- CI pipeline can also be triggered by commenting 'Jenkins please retry a build' on the pull request
