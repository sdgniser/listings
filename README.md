# Listings

A place for trading things you do not need.

### Running a local instance

 * Install `python` and `postgresql`
 * Clone the repo
 * Configure `postgresql` on your machine and create a new database for this
   project.
 * Rename `listings/local_settings_example.py` to `listings/local_settings.py`.
   Put the details of your newly created database in `local_settings.py`
 * Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
   and do `pip install -r requirements.txt`
 * `cd` to the cloned repo (while still in virtualenv) and run: `python manage.py makemigrations main`, `python manage.py migrate`
 * Run `python populate.py` to populate the database with some "categories",
   "locations", etc
 * Start the development server: `python manage.py runserver`
 * Let me know if you're unable to get it running
