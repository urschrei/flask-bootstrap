A Flask app skeleton in a Virtualbox VM, built using Vagrant, including:

- Bootstrap
- HTML5 template
- Postgres DB
- Blueprints

## Quickstart

After installing [Virtualbox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](http://vagrantup.com/), create and boot the VM in the cloned repository:

    vagrant up

SSH to the VM:

    vagrant ssh

Run your app:

    fab run_app

Run an iPython shell with a test request context and imported models:

    fab shell

Run or list alembic migrations:

    fab upgrade_db
    fab_downgrade_db
    fab show_migrations

You may also specify optional revisions:

    fab upgrade_db:b2343d67
    fab downgrade_db:a34e876

## Notes

You should check that the versions of the packages currently present in `requirements.txt` match your requirements, and update them if necessary.

The Bootstrap and Javascript components to be installed are detailed in `assets.yml`, and are present in the `static` directory. Your application's JS should be placed in the `app.js` file. Refer to http://webassets.readthedocs.org/en/latest/ for details of how to use and customise Webassets.

You can connect to the DB using e.g. PGAdmin from your local machine by connecting to:

    localhost port 15432
    db: app_db
    user: flask_user
    pass: flask_pass

From within your VM, you can connect using the same credentials on port 5432

Alembic database revisions are created with the command `alembic revision -m "Migration detail"`. For details of how to use Alembic, refer to http://alembic.readthedocs.org/en/latest/

