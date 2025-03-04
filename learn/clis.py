import click
from learn import db
from learn import models


def _init_database(with_data=False):
    try:
        db.create_all()
        if with_data:
            fake_users = [
                {'username': 'xiedandan', 'password': 'hC(E6L#nDe', 'email': 'dan07@example.com'},
                {'username': 'zhaishuzhen', 'password': '(7jIOCxnwz', 'email': 'qkong@example.org'},
                {'username': 'libo', 'password': '05sZSVnQ*K', 'email': 'pingfeng@example.org'},
                {'username': 'shigang', 'password': '5BHL)xfx#S', 'email': 'na29@example.org'},
                {'username': 'wulihua', 'password': 'PM2P6PXh(5', 'email': 'guiying10@example.net'},
                {'username': 'mahongxia', 'password': 'mn4HJb#&K!', 'email': 'xiazhao@example.org'}
            ]
            # 批量插入
            db.session.bulk_insert_mappings(models.User, fake_users)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error encountered while initializing database: {e}")


# click.command() 可以传递 name 参数自定义命令，如果不传递，默认命令为函数名
@click.command()
@click.option("--with_data", default=False, help="Generate fake data. default: False")
def initdb(with_data):
    """Created all tables of database."""
    _init_database(with_data)
    click.echo("Initialized database.")


@click.command()
def cleandb():
    """Drop all tables."""
    db.drop_all()
    click.echo("Cleaned database.")


@click.command("lsj_reset")
@click.option("--regen_data", default=False, help="Regenerate fake data. default: False")
def resetdb(regen_data):
    """Reset database."""
    db.drop_all()
    _init_database(with_data=regen_data)
    click.echo("Reset database.")
