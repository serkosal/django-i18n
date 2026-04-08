# django-i18n
django i18n &amp; l11n ex6nts 

1.  configure languages in settings.py
2.  mark string in python code via using `gettext` from `from django.utils.translation`
    which by convension often imported as `_`.
3.  create translation files using `makemessages` `manage.py` command.
    ```sh
    python manage.py makemessages -a
    ```
4.  edit .po files
5.  ```sh
    python manage.py compilemessages
    ```
6.  ```sh
    python manage.py runserver
    ```
    and try paths for languages specified in settings.py