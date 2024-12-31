# Student-Result-Management-System-Final-Project-

STEP - 1: clone the repository to your local machine  
https://github.com/SouravChowdhury569/Student-Result-Management-System-Final-Project-.git

STEP - 2: Now create a virtual machine:  
Name : Virtualenv venv  
.\venv\Scripts\Activate.ps1

STEP - 3: Install the requirements  
pip install -r requirments.txt

STEP - 4: Install extra requirements if "no module found" pop up.  
pip install module_name

STEP - 5: Apply the migrations  
python manage.py makemigrations  
python manage.py migrate

STEP - 6: Run the Django development server  
python manage.py runserver
