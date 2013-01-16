# A [Flask](http://flask.pocoo.org) app skeleton in a Virtualbox VM, built using [Vagrant](http://vagrantup.com), including:

- [Bootstrap](http://twitter.github.com/bootstrap/)
- HTML5 template
- Postgres DB
- [Blueprint](http://flask.pocoo.org/docs/blueprints/) app structure

## Quickstart

After installing [Virtualbox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](http://downloads.vagrantup.com/), create and boot the VM in the cloned repository:

    vagrant up

SSH to the VM:

    vagrant ssh

### From within the VM, you can now  

Run your app:

    fab run_app

Run an [iPython](http://ipython.org) shell with a test request context and imported models:

    fab shell

Run, list, and create [alembic](http://alembic.readthedocs.org/en/latest/) migrations:

    fab upgrade_db:optional revision
    fab downgrade_db:revision
    fab show_migrations
    fab revision:"Revision detail"


## Notes

You should check that the versions of the packages currently present in `requirements.txt` match your requirements, and update / amend them if necessary.

The Bootstrap and Javascript components which are installed are detailed in `assets.yml`, and are present in the `static` directory. Your application's JS should be placed in the `app.js` file. Refer to [the webassets documentation](http://webassets.readthedocs.org/en/latest/) for details of how to use and customise the package.

You can connect to the database using e.g. [PGAdmin](http://www.pgadmin.org) from your local machine by connecting to:

    localhost port 15432
    db: app_db
    user: flask_user
    pass: flask_pass

From within your VM, you can connect using the same credentials on port 5432.

## Todo

- enable [auto-generate](https://alembic.readthedocs.org/en/latest/tutorial.html#auto-generating-migrations) support in Alembic

