# Task-Manager


## About the Project

To keep track your projects and corresponding tasks

## Installation
1. Clone the repo
```sh
https://github.com/evelynizhang/Task-Manager.git
```
2. Create a new virtual environment
```sh
python -m venv .venv
```
3. Activate a virtual environment
```sh
source ./.venv/bin/activate  # macOS
./.venv/Scripts/Activate.ps1 # Windows
```
4. Update pip
```sh
python -m pip install --upgrade pip
```
5. Instal dependencies from requiremnet.txt
```sh
pip install -r requirements.txt
```
6. Apply the migrations to your database
```sh
python manage.py migrate
```
