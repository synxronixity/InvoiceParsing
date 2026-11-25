# GitHub + VS Code: Quick Start, Best Practices & Cheat Sheet

A practical guide to working with Git and GitHub from Visual Studio
Code.

## 1. Understand the tools

-   **Git** tracks changes to your code locally.
-   **GitHub** hosts Git repositories online and supports collaboration.
-   **VS Code** is your development environment, with built-in Git
    integration.

You can do most everyday Git operations from VS Code, but knowing the
terminal commands makes you more effective when troubleshooting.

## 2. Initial setup

### Install the essentials

-   [Visual Studio Code](https://code.visualstudio.com/)
-   [Git](https://git-scm.com/downloads)
-   [GitHub](https://github.com/)

### Configure Git

Open the VS Code terminal with `` Ctrl + ` `` (or use **Terminal → New
Terminal**).

Check that Git is installed:

``` bash
git --version
```

Set the name and email that will be associated with your commits:

``` bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Set `main` as the default branch for new repositories:

``` bash
git config --global init.defaultBranch main
```

Review your configuration:

``` bash
git config --list
```

### Connect VS Code to GitHub

1.  Open VS Code.
2.  Select the Accounts icon.
3.  Choose **Sign in with GitHub**.
4.  Complete authentication in your browser.
5.  Authorize VS Code.

## 3. Create or download a repository

### Option A: Start a new project locally

1.  Create a project folder.
2.  Open that folder in VS Code.
3.  Open the integrated terminal.
4.  Initialize Git and make your first commit:

``` bash
git init
git add .
git commit -m "Initial commit"
```

5.  Open Source Control (`Ctrl + Shift + G`).
6.  Select **Publish Branch** or **Publish to GitHub**.
7.  Choose whether the repository should be public or private.

### Option B: Clone an existing GitHub repository

On GitHub, open the repository and copy its URL. In VS Code:

1.  Press `Ctrl + Shift + P`.
2.  Search for **Git: Clone**.
3.  Paste the repository URL.
4.  Choose a local folder.
5.  Open the cloned repository.

Equivalent terminal command:

``` bash
git clone https://github.com/username/repository.git
```

**Best practice:** Clone a repository rather than downloading its ZIP
file. Cloning preserves the Git history and connection to the remote
repository.

## 4. The everyday Git workflow

The basic cycle is:

1.  **Pull** --- get the latest changes from GitHub.
2.  **Code** --- make changes locally in VS Code.
3.  **Review** --- inspect modified files and their differences.
4.  **Stage** --- select which changes belong in the next commit.
5.  **Commit** --- save a snapshot locally.
6.  **Push** --- upload your commits to GitHub.

``` bash
git pull
# Make and save your code changes
git status
git diff
git add .
git commit -m "Describe the changes"
git push
```

Remember: **commit** and **push** are different. A commit saves changes
in your local repository; a push uploads those commits to GitHub.

### Using the VS Code interface

Open Source Control with `Ctrl + Shift + G`.

  Action              VS Code interface
  ------------------- -----------------------------------------------
  View changes        Source Control panel
  Stage a file        Click the `+` beside the file
  Stage all changes   Click the `+` beside Changes
  Unstage a file      Click the `-` beside the staged file
  Commit              Enter a message and select Commit
  Push                Push or Sync Changes
  Pull                Pull or Sync Changes
  View history        Source Control Graph or Git history extension

## 5. Branches: work without breaking your project

A branch lets you work on a feature or experiment separately from your
stable code. Think of `main` as the stable version and a feature branch
as an isolated workspace.

Example:

``` bash
# Start from the latest main branch
git switch main
git pull

# Create and switch to a new branch
git switch -c feature/new-calculator

# Make changes, then commit
git add .
git commit -m "Add calculator functionality"

# Publish the branch to GitHub
git push -u origin feature/new-calculator
```

Then create a **Pull Request (PR)** on GitHub to merge the branch into
`main`.

### Branch naming conventions

  Purpose         Example
  --------------- -----------------------------
  New feature     `feature/user-login`
  Bug fix         `bugfix/fix-calculation`
  Documentation   `docs/update-readme`
  Experiment      `experiment/new-model`
  Maintenance     `chore/update-dependencies`

Use branches for new features, major refactoring, and experiments. For a
small personal project, working directly on `main` can be perfectly
reasonable.

## 6. Best practices

### A. Commit frequently, but meaningfully

Avoid vague messages:

``` bash
git commit -m "updates"
git commit -m "stuff"
```

Prefer messages that explain the change:

``` bash
git commit -m "Add input validation"
git commit -m "Fix CSV export formatting"
git commit -m "Update heat exchanger calculations"
```

A commit should represent one logical unit of work.

### B. Create a `.gitignore`

A `.gitignore` file tells Git which untracked files it should ignore.
For a Python project, a starting point could be:

``` gitignore
# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Environment variables and secrets
.env
.env.*

# Operating system
.DS_Store
Thumbs.db

# Temporary files
*.log
```

For MATLAB projects, you may also want:

``` gitignore
*.asv
*.mex*
```

Do not blindly ignore `.vscode/`: some projects intentionally share
workspace settings and recommended extensions.

Never commit API keys, passwords, private credentials, or personal data.
If a secret is accidentally committed, revoke or rotate it immediately.
Deleting it in a later commit does not remove it from Git history.

### C. Include a README

A README explains what the project does and how to run it. A useful
starting structure:

``` markdown
# Project Name

## Overview
What does this project accomplish?

## Features
- Feature 1
- Feature 2

## Requirements
- Python 3.12
- NumPy
- SciPy

## Installation
pip install -r requirements.txt

## Usage
python main.py

## Project Structure
Describe important folders and files.

## License
MIT
```

Adapt the requirements and commands to your actual project.

### D. Pull before starting work

If you work across multiple computers or collaborate with someone,
synchronize before editing:

``` bash
git pull
```

This reduces the chance of conflicts, although it cannot prevent every
conflict.

### E. Review before staging and committing

``` bash
git status
git diff
```

Stage individual files when appropriate:

``` bash
git add src/main.py
```

This is safer than staging everything when your project contains
generated files, datasets, or sensitive configuration.

### F. Tag important milestones

Tags mark significant versions:

``` bash
git tag v1.0.0
git push origin v1.0.0
```

## 7. Git command cheat sheet

### Basic commands

  Command                     Function
  --------------------------- -------------------------------------------------
  `git init`                  Initialize a repository
  `git clone URL`             Clone a repository
  `git status`                Show current changes and repository state
  `git add .`                 Stage all changes in the current directory tree
  `git add FILE`              Stage a specific file
  `git commit -m "message"`   Create a commit
  `git log --oneline`         View compact commit history
  `git diff`                  View unstaged changes
  `git diff --staged`         View staged changes

### Synchronization

  Command                       Function
  ----------------------------- --------------------------------------------------
  `git fetch`                   Download remote updates without integrating them
  `git pull`                    Fetch and integrate remote updates
  `git push`                    Upload local commits
  `git push -u origin BRANCH`   Publish a branch and set its upstream
  `git remote -v`               List remote repositories

### Branch management

  Command                Function
  ---------------------- ----------------------------------------------
  `git branch`           List local branches
  `git branch -a`        List local and remote-tracking branches
  `git switch main`      Switch to `main`
  `git switch -c NAME`   Create and switch to a branch
  `git merge NAME`       Merge another branch into the current branch
  `git branch -d NAME`   Delete a merged local branch

### Undo and recovery

  -----------------------------------------------------------------------
  Command                             Function
  ----------------------------------- -----------------------------------
  `git restore FILE`                  Discard unstaged changes to a file

  `git restore --staged FILE`         Unstage a file without deleting its
                                      changes

  `git stash`                         Temporarily save uncommitted
                                      changes

  `git stash pop`                     Reapply the latest stash and remove
                                      it from the stash list if
                                      successful

  `git revert HASH`                   Create a new commit that reverses
                                      another commit

  `git reset --soft HEAD~1`           Undo the latest commit while
                                      keeping its changes staged
  -----------------------------------------------------------------------

**Caution:** `git reset --hard` discards uncommitted changes.
`git clean -fd` deletes untracked files and folders. Avoid these unless
you understand exactly what will be removed.

## 8. Common problems and solutions

  -----------------------------------------------------------------------
  Problem                             Possible solution
  ----------------------------------- -----------------------------------
  `git` is not recognized             Install Git, then restart VS Code
                                      or its terminal

  Authentication failed               Sign in again through VS Code or
                                      check your GitHub authentication

  Push rejected                       Fetch/pull remote changes and
                                      resolve any conflicts

  Merge conflict                      Resolve the conflicting sections,
                                      then stage and commit

  Wrong branch                        Use `git switch BRANCH_NAME`

  Accidentally staged a file          Use `git restore --staged FILE`

  Repository not detected             Open the actual repository folder
                                      in VS Code
  -----------------------------------------------------------------------

### Understanding merge conflicts

A conflict occurs when Git cannot automatically reconcile competing
changes. A conflicted file may contain markers like:

``` text
<<<<<<< HEAD
temperature = 300
=======
temperature = 350
>>>>>>> feature/update-temperature
```

Choose the correct result, remove the conflict markers, and save the
file. Then:

``` bash
git add .
git commit -m "Resolve temperature calculation conflict"
```

VS Code offers actions such as **Accept Current**, **Accept Incoming**,
and **Accept Both**. Review the resulting code instead of blindly
accepting one.

## 9. Useful VS Code shortcuts

  Shortcut (Windows)   Action
  -------------------- ---------------------------------
  `Ctrl + Shift + G`   Open Source Control
  `Ctrl + Shift + P`   Open Command Palette
  ``` Ctrl + `` ```    Open integrated terminal
  `Ctrl + P`           Quick file navigation
  `Ctrl + Shift + F`   Search across the project
  `Ctrl + /`           Toggle line comment
  `Alt + Up/Down`      Move line
  `Ctrl + D`           Select next matching occurrence
  `F2`                 Rename symbol

Useful Command Palette commands include:

-   `Git: Clone`
-   `Git: Create Branch`
-   `Git: Checkout to...`
-   `Git: Pull`
-   `Git: Push`
-   `Git: Fetch`

## 10. Recommended VS Code extensions

These are optional; VS Code already includes core Git integration.

-   **[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)**
    --- inspect line history, authorship, commits, and changes.
-   **[GitHub Pull
    Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)**
    --- create and review pull requests in VS Code.
-   **[Git
    Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)**
    --- visualize branches, commits, and merges.

## 11. The workflow to memorize

For a feature branch, this is a compact routine:

``` bash
# 1. Get the latest changes
git pull

# 2. Create a working branch
git switch -c feature/my-feature

# 3. Check and review changes
git status
git diff

# 4. Stage and commit
git add .
git commit -m "Describe my changes"

# 5. Push the branch
git push -u origin feature/my-feature
```

Then create a Pull Request on GitHub.

For a solo project, you can simplify this by working directly on `main`
and pushing after committing.

## 12. Practice exercise

Use a small test repository to practice:

-   [ ] Install Git and authenticate VS Code with GitHub.
-   [ ] Create a new local repository.
-   [ ] Create a `README.md`.
-   [ ] Make your first commit.
-   [ ] Publish the repository to GitHub.
-   [ ] Create a feature branch.
-   [ ] Modify a file and commit the changes.
-   [ ] Push the branch to GitHub.
-   [ ] Create and merge a Pull Request.
-   [ ] Return to `main` and pull the latest changes.

## 13. Official references

-   [VS Code --- Git
    Quickstart](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)
-   [VS Code --- Working with
    GitHub](https://code.visualstudio.com/docs/sourcecontrol/github)
-   [VS Code --- Source
    Control](https://code.visualstudio.com/docs/sourcecontrol/overview)
-   [GitHub Docs --- Getting
    started](https://docs.github.com/en/get-started)
-   [Git documentation](https://git-scm.com/doc)

------------------------------------------------------------------------

**Final recommendation:** Learn both the VS Code Source Control
interface and the terminal. The interface is convenient for reviewing
changes; the terminal helps you understand what Git is doing and
troubleshoot problems. You do not need to memorize every Git command.
