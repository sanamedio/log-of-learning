git pull
python3 readme_generator.py > README.md
git add notes/* deploy.sh README.md
git commit -m "auto-update"
git push --force
