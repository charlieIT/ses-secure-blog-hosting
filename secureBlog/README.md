# secure-blog-hosting-poc
Software Security Project for Master's in Information Security @ FCUP


# Installation

Ensure python3 is installed:

```
python3 --version
```

Ensure pip is installed
```bash
python3 -m pip install --upgrade pip
python3 -m pip --version
```

Install venv
```bash
python3 -m pip install virtualenv
```

For Kali:
```
sudo apt install pip
sudo apt install virtualenv
```

Clone the repo
```bash
git clone [https://path/to/repo] [dir_name]
cd [dir_name]
```

Activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

**Note**: dependency backports.zoneinfo may need and clause for python version pre-condition in order to install correctly.
In requirements.txt file, add the clause:
```
backports.zoneinfo==0.2.1;python_version<"3.9"
```

if not using docker, these additional packages may require installation (same package available in the Dockerfile):
```
sudo apt install -y libcairo2-dev pkg-config 
sudo apt install -y gcc libpcre3-dev zlib1g-dev libluajit-5.1-dev
sudo apt install -y libcairo2-dev pkg-config 
```

Create your .env file, example available @ [.env example](/.env.example)
```
SECRET_KEY='your-key'
DEBUG=False

## Super-User Credentials
SUPER_USER_NAME = 'your super user'
SUPER_USER_PASSWORD = 'your super secret password'
SUPER_USER_EMAIL = 'to blame'

## Database
POSTGRES_NAME='<db name>'
POSTGRES_USER='<db user>'
POSTGRES_PASSWORD='<db credential>'
```

Move to secureblog directory
```
cd secureblog
```

Run migrations and create superuser
```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

Run the application
```
python manage.py runserver
```

Login available @ `/admin`
