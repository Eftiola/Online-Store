# online-store
SDA Albania Python From Scratch Final Project - Online Store

To set this up, 

Clone the code:
    >git clone https://github.com/Eftiola/online-store.git

------------

Enter the directory where the code was cloned and create a virtual environment:
   * >cd online-store
   * >python -m venv venv (name of virtual environment)

-------------
Activate the virtual environment:

* if you are using command prompt
    >venv\Scripts\activate

* if you are on MacOS or Linux
    >venv/bin/activate
------------

Install the required packages:

    >pip install -r requirements.txt

-------------

Apply migrations:

    >python manage.py migrate

--------------

Run the development server:

    >python manage.py runserver

-------------
Deploy to Heroku, PythonAnywhere, or Dokku
