# BECAUSE OF THE UNIVERSITY

"for the: `SCRIPT LANG` : python-django"

---

That was a plan I will not update this repo, but found a typo, and after that I made some changes too. Not just in this README file.

This version is still very static. I made some changes in the other, but it is not committed here....

Maybe I will upload some modifications later....

[no longer available online, because salesforce killed heroku's free tier](https://#)

---

## usage | test

### remember: I'm using Linux! some of your commands may vary

- open a terminal
  - keep it in your mind: **Linux users are not afraid to use terminal**
- navigate into your working directory
- if you wish: create a new directory and `cd` in it, but the following command will make you a `script_lang` directory
- `git clone https://github.com/dabzse/script_lang.git`
  - or use the GitHub cli: `gh repo clone dabzse/script_lang`
  - or user SSH: `git clone ssh://git@github.com/dabzse/script_lang.git`
  - or use a GUI
  - or download a zip and extract it
- `cd script_lang`
- `python -m venv` + [virtual_environment_name]
  - for example: *CV-env*
- `source` + [virtual_environment_name] + `/bin/activate`
  - if you made *CV-env*, then the command is: *`source CV-env/bin/activate`*
- first: upgrade pip
  - `pip install --upgrade pip`
- `pip install -r requirements.txt`
  - this will install the versions which I have used
  - be very careful with the updates!
- run it: `python manage.py runserver`
- the given link: `http://localhost:8000` or `http://127.0.0.1:8000` open in a browser

---

#### Initial release: Django 3.2.9

#### Updated release: Django 3.2.12

#### Updated release: Django 3.2.19 (latest version at the moment in django3, LTS)

---

<center>{{ MNY : @dabzse }}</center>
