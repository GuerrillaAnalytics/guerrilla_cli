import click


@click.group()
@click.pass_context
def wp(ctx):
    pass

@wp.group('zone')
def wp_zone():
    pass


@wp_zone.command('add')
@click.option('--jumpstart', '-j', default=True)
@click.option('--organization', '-o', default='')
@click.argument('url')
@click.pass_obj
# @__cf_error_handler
def wp_zone_add(ctx, url, jumpstart, organization):
    pass


@wp.group('record')
def wp_record():
    pass


@wp_record.command('add')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
# @__cf_error_handler
def wp_record_add(ctx, domain, name, type, content, ttl):
    pass


@wp_record.command('edit')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
# @__cf_error_handler
def wp_record_edit(ctx, domain):
    pass