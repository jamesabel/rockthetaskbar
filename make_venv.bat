REM stay on 3.5 until pip bug in embedded 3.6 fixed
\Users\james\AppData\Local\Programs\Python\Python35\python.exe -m venv --clear venv
venv\Scripts\pip3 install -U pip
venv\Scripts\pip3 install -U setuptools
venv\Scripts\pip3 install -r requirements.txt
