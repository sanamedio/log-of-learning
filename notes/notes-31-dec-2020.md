# 31-dec-2020

### 1 - github actions are amazing

- https://lab.github.com/githubtraining/github-actions:-hello-world
- Just one .github/workflows/actions.yml file and magic. the followign one is to update readme of this repo!

```
name: learn-github-actions
on: [push]
jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
     - name: checkout repo content
       uses: actions/checkout@v2 # checkout the repository content to github runner.
     - name: setup python
       uses: actions/setup-python@v2
       with:
         python-version: 3.8
     - name: execute  
       run: |
          python readme_generator.py
     - name: commit back 
       uses: stefanzweifel/git-auto-commit-action@v4
```
