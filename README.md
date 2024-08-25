### **Installation (Linux, Mac):**
```
git clone https://github.com/usrbad/ga-ro.git
cd ga-ro
```
#### Create .env file with variables like:
```
TEST_EMAIL=
TEST_PASSWORD=
TEST_URL=
```
#### If you prefer to use venv:
```
python -m venv venv
source venv/bin/activate
```

#### Install requirements:
```
pip install -r requirements.txt
```
#### Collecting tests:
```
python -m pytest --co
```

#### Run specified test:
```
python -m pytest -k <test_name>
```

#### Example:
```
python -m pytest -k test_folder_created_smoke
```

#### Run all tests:
```
python -m pytest
```
<p></p>
#### Not necessary actions:
#### May need to reload env (Linux):
```
source ~/.bash_profile
```
#### on Mac:
```
source ~/.zshrc
```
##### or if you use venv:
```
deactivate
source venv/bin/activate
```