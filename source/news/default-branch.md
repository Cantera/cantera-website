---
title: Renaming Cantera's default branch
date: 2020-07-10 17:33
slug: default-branch
tags: git
description: Renaming Cantera's default branch
type: text
author: Raymond Speth
---

There has been a growing awareness that the use of the name `master` for the
default branch in Git repositories perpetuates the use of the language of
oppression. It has also [been shown](https://mail.gnome.org/archives/desktop-devel-list/2019-May/msg00066.html)
that the use of the term `master` in Git likely does stem from the harmful
master/slave metaphor, which it inherited from an earlier piece of software.

With the aim of upholding our commitment to fostering an open and welcoming
environment as outlined in our [Code of Conduct](https://github.com/Cantera/cantera/blob/main/CODE_OF_CONDUCT.md),
specifically the standard of using welcoming and inclusive language, we have
changed the default branch name in Cantera to `main`, and recommend this
change to others for their forks and local repositories as well.

Adapting to this change will require a few small changes for anyone who has
already checked out a copy of the Cantera source code using Git, and
instructions which should help in most cases are provided below.

## Updating your local repository and GitHub fork

To change the name of Cantera's default branch open a shell, navigate to the
Cantera source directory, and run the following commands:

```shell
$ git fetch --all
$ git checkout master
$ git branch -m master main
$ git status
On branch main
Your branch is up to date with 'origin/master'.
```

If your `master` branch isn't up to date with its upstream, you will want to fix
that first using your preferred workflow to synchronize the two branches. *If
you have made any local changes to the `master` branch, you should create a
feature branch to avoid losing any changes.*

Next, we want to update the link between your `main` branch and the remote
repository (here, `origin`). You can check whether this remote is the main
Cantera repository or your fork on GitHub (or a different source) by running the
command:

```shell
$ git remote --verbose
origin  git@github.com:cantera/cantera.git (fetch)
origin  git@github.com:cantera/cantera.git (push)
myfork  git@github.com:your_username/cantera.git (fetch)
myfork  git@github.com:your_username/cantera.git (push)
```

#### Case 1: tracked remote is `Cantera/cantera`
If the remote being tracked (in this example, `origin`) is the main Cantera
repository, that is, `Cantera/cantera.git`, then you can set the `main` branch
of `Cantera/cantera` as the upstream for your `main` branch:

```shell
$ git branch --unset-upstream
$ git branch -u origin/main
$ git fetch
$ git rebase origin/main
```

Then, you can push the updated main branch to your fork (in this example,
`myfork`) as well:

```shell
$ git push main myfork
```

#### Case 2: tracked remote is your fork

If the remote listed is your fork of Cantera, then you may want to rename the
branch on your fork as well. If the remote name for your fork is `myfork`, this
can be changed by running:

```shell
$ git push -u myfork main
```

### Deleting the old branch from your fork

Once you have pushed the new `main` branch to your fork, visit the GitHub
website for your fork, go to **Settings**, then **Branches**, then
**Default Branch**, and set the default branch to `main`.

Once you make sure that the `main` branch shows any recent commits that you
expect to see, you can delete the old branch from your fork:

```shell
$ git push origin --delete master
```

If you get an error message that says
```
! [remote rejected]     master (refusing to delete the current branch: refs/heads/master)`
```
this suggests that you haven't successfully changed the default branch on GitHub.
