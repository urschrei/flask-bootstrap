# A [Flask](http://flask.pocoo.org) app skeleton in a Virtualbox VM, built using [Vagrant](http://vagrantup.com), including:

- [Bootstrap](http://twitter.github.com/bootstrap/)
- HTML5 template
- Postgres DB
- [Blueprint](http://flask.pocoo.org/docs/blueprints/) app structure
- [Flask-Bcrypt](http://packages.python.org/Flask-Bcrypt/)

## Quickstart
- Ensure that [Virtualbox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](http://downloads.vagrantup.com/) are installed
- This setup assumes a 64-bit capable system – it should run on a [precise32](http://www.vagrantbox.es) box instead, but I haven't tried
- Clone this repository (you may wish to clone it without any history — `git clone --depth 1 repo_url`)
- `cd` into the newly-cloned repo, and run `git submodule update --init`
- Create and boot the VM: `vagrant up`
- Wait a while – Vagrant may have to download a precise64 box, and the Python requirements installation will be slow on the initial run – maybe you'd like to go for a quick wander, talk to a cat &c.
- SSH to the VM: `vagrant ssh`

### From within the VM, you can now  

- Run your app, which will then be reachable from localhost on `0.0.0.0:5000`: `fab run_app`
- Run an [iPython](http://ipython.org) shell with a test request context and imported models: `fab shell`
- Run, list, and create [alembic](http://alembic.readthedocs.org/en/latest/) migrations, including auto-generation:

    `fab upgrade_db:optional revision`  
    `fab downgrade_db:revision`  
    `fab show_migrations`  
    `fab revision:"Message"`  
    `fab autogenerate:"Message"`

## Notes

Be aware that auto-generation of migrations has some [limitations](https://alembic.readthedocs.org/en/latest/tutorial.html#auto-generating-migrations).

You should check that the versions of the packages currently present in `requirements.txt` match your requirements, and update / amend them if necessary. Currently, the most recent version of each package is being installed, and I'm not aware of any incompatibilities.

The Bootstrap and Javascript components which are installed are detailed in `assets.yml`, and are present in the `static` directory. Your application's JS should be placed in the `app.js` file. Refer to [the webassets documentation](http://webassets.readthedocs.org/en/latest/) for details of how to use and customise the package.

You can connect to the database using e.g. [PGAdmin](http://www.pgadmin.org) from your local machine by connecting to:

    localhost port 15432
    db: app_db
    user: flask_user
    pass: flask_pass

From within your VM, you can connect using the same credentials on port `5432`.

## Todo
- Fix the zip download submodule problem  
