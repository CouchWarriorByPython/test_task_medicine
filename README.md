# Doctors and Line of actions
test project for potential job

## Contents
1. Preparing to start the project
2. Launch and familiarize yourself with the features
3. Api endpoints and auto-documentation


### Preparing to start the project
1. Create a folder (the place of creation does not matter)</br>
2. Copy the project from GitHub and navigate to the folder:</br>
   git clone https://github.com/CouchWarriorByPython/test_task_medicine.git </br>
   cd test_task_medicine
3. Installing and creating venv (virtual environment)
   1. Install:</br>
   sudo apt install python3-venv -- for Linux</br>
   Windos and MacOS have included this module
   2. Functional testing (only for Linux):</br>
   python3 -m venv --help</br>
   usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] 
   [--upgrade] [--without-pip] [--prompt PROMPT] ENV_DIR [ENV_DIR ...]
   3. Creating the name of env:</br>
   python3 -m venv name_of_space
   4. Activating:</br>
   source name_of_space/bin/activate -- for Linux and Mac</br>
   C:\> first_venv\Scripts\activate.bat -- for Windows</br>
   Note that in Windows, the subdirectory with the executable files is not called **bin**, but **Scripts**!
4. Installing all dependencies:</br>
   pip install -r requirements.txt
### Launch and familiarize yourself with the features
1. Project Launch:</br>
   python manage.py migrate</br>
   python manage.py createsuperuser</br>
   python manage.py runserver</br>
2. You can open in your browser the following ip address:</br>
   **http:127.0.0.1/admin/** - and fill in all the fields (data for the fields you created after command _python manage.py createsuperuser_)
