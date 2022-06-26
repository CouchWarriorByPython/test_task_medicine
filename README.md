# Doctors and Line of actions
test project for potential job

## Contents
1. Preparing to start the project
2. Launch and familiarize yourself with the features
3. Api endpoints


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
2. You can open the following ip address in your browser:</br>
   **http:127.0.0.1:8000/admin/** - and fill in all the fields (data for the fields you created after command _python manage.py createsuperuser_)
3. In the admin panel you can create several model objects for the doctor and his line of action
4. **http:127.0.0.1:8000/swagger/** - this is all the documentation about my project</br>
   **http:127.0.0.1:8000/redoc/** - also the documentation about my project in different format
### Api endpoints
1. API for Line Of Action:</br>
    1. http://127.0.0.1:8000/line-of-actions/ -- GET-request to get all lines of actions</br>
    $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/line-of-actions/ </br>
    2. http://127.0.0.1:8000/line-of-actions/?page=2 -- GET-request to get next lines of actions (request with pagination parameter)</br>
    $ curl -H 'Accept: application/json; indent=4' -d "page=2" http://127.0.0.1:8000/line-of-actions/ </br>
    3. http://127.0.0.1:8000/line-of-actions/1 -- GET-request to get a concrete line of action</br>
    $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/line-of-actions/{id_line_of_action}/ </br>
    4. http://127.0.0.1:8000/line-of-actions/ -- POST-request to create a new line of action</br>
    $ curl -X POST -H 'Accept: application/json; indent=4' -u admin:password -d "title={something}&slug={something}" http://127.0.0.1:8000/line-of-actions/ </br>
    5. http://127.0.0.1:8000/line-of-actions/{id_line_of_action}/ -- PUT-request to correct a line of action</br>
    $ curl -X PUT -H 'Accept: application/json; indent=4' -u admin:password -d "title={something}&slug={something}" http://127.0.0.1:8000/line-of-actions/{id_line_of_action}/ </br>
    6. http://127.0.0.1:8000/line-of-actions/{id_line_of_action}/ -- DELETE-request to delete a line of action</br>
    $ curl -X DELETE -u admin:password http://127.0.0.1:8000/line-of-actions/{id_line_of_action}/ </br>


2. API for Doctors:</br>
   1. http://127.0.0.1:8000/doctors/ -- GET-request to get all doctors</br>
   $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/doctors/ </br>
   2. http://127.0.0.1:8000/doctors/?page=2 -- GET-request to get next page with doctors (request with pagination parameter)</br>
   $ curl -H 'Accept: application/json; indent=4' -d "page=2" http://127.0.0.1:8000/doctors/ </br>
   You can also specify several parameters to filter the final list:</br>
      1. line_of_action={integer};
      2. work_experience={integer};
      3. ordering={work_experience} or {date_of_birth}.
   3. http://127.0.0.1:8000/doctors/1 -- GET-request to get a concrete doctor</br>
   $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/doctors/{id_doctor}/ </br>
   4. http://127.0.0.1:8000/doctors/ -- POST-request to create a new doctor</br>
   $ curl -X POST -H 'Accept: application/json; indent=4' -u admin:password -d "parameters={something}&parameters={something}" http://127.0.0.1:8000/doctors/ </br>
      Required parameters:
      1. name={string};
      2. surname={string};
      3. patronymic={string};
      4. slug={string}.</br>
   
      Optional parameters:
      1. description={string};
      2. date_of_birth={string};
      3. work_experience={integer};
      4. line_of_action={integer}.
   5. http://127.0.0.1:8000/doctors/{id_doctor}/ -- PUT-request to correct a doctor</br>
   $ curl -X PUT -H 'Accept: application/json; indent=4' -u admin:password -d "parameters={something}&parameters={something}" http://127.0.0.1:8000/doctors/{id_doctor}/ </br>
   6. http://127.0.0.1:8000/doctors/{id_doctor}/ -- DELETE-request to delete a doctor</br>
   $ curl -X DELETE -u admin:password http://127.0.0.1:8000/doctors/{id_doctor}/ </br>