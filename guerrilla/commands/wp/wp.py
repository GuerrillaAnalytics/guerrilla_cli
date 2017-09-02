import click


@click.group()
@click.pass_context
def wp(ctx):
    pass


@wp.command('add')
@click.argument('id', '-i', default="wp")
@click.argument('label', '-l', default='')
@click.pass_obj

def wp_add(ctx, url, jumpstart, organization):
    pass
