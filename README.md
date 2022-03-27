# BECAUSE OF THE UNIVERSITY

"for the: `SCRIPT LANG` : python-django"
-
---
That was a plan I will not update this repo, but found a typo, and after that I made some changes too. Not just in this README file.

This version is still very static. I made some changes in the other, but it is not committed here....

Maybe I will upload some modifications later....

[view it on Heroku](https://dabzse-cv.herokuapp.com)

----------

### usage | test

#### remember: I'm using Linux! some of your commands may vary
- open a terminal
  - keep it in your mind: Linux users are not afraid to use terminal
- navigate into your working directory
- if you wish: create new directory and `cd` in, but the following command will make you a `script_lang` directory
- `git clone https://github.com/dabzse/script_lang.git`
    - or use the GitHub cli: `gh repo clone dabzse/script_lang`
- `cd script_lang`
- `python -m venv` + [virtual_environment_name]
  - for example: *CV-env*
- `source` + [virtual_environment_name] + `/bin/activate`
  - if you made *CV-env*, then the command is: *`source CV-env/bin/activate`*
- first: upgrade pip
  - `pip install --upgrade pip`
- navigate into the project's directory
  - `cd CV__HU-django/src/CV__HU_django/`
    - that's because when I created it first time, I made `CV__HU-django` directory and there I made a venv + src directories.... but used `git init` in the very first directory
- `pip install -r requirements.txt`
    - this will install the versions which I have used
    - be very careful with the updates!
- run it: `python manage.py runserver`
- the given link: `http://localhost:8000` or `http://127.0.0.1:8000` open in a browser

---

### Initial release: Django 3.2.9
### Updated release: Django 3.2.12

---

<center>{{ MNY : @dabzse }}</center>
