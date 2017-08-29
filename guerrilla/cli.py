import click

@click.group()
@click.version_option()
def cli():
    pass #Entry Point

@cli.group()
@click.pass_context
def cloudflare(ctx):
    pass

@cloudflare.group('zone')
def cloudflare_zone():
    pass

@cloudflare_zone.command('add')
@click.option('--jumpstart', '-j', default=True)
@click.option('--organization', '-o', default='')
@click.argument('url')
@click.pass_obj
#@__cf_error_handler
def cloudflare_zone_add(ctx, url, jumpstart, organization):
    pass

@cloudflare.group('record')
def cloudflare_record():
    pass

@cloudflare_record.command('add')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
#@__cf_error_handler
def cloudflare_record_add(ctx, domain, name, type, content, ttl):
    pass

@cloudflare_record.command('edit')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
#@__cf_error_handler
def cloudflare_record_edit(ctx, domain):
    pass

@cli.group()
@click.pass_context
def uptimerobot(ctx):
    pass

@uptimerobot.command('add')
@click.option('--alert', '-a', default=True)
@click.argument('name')
@click.argument('url')
@click.pass_obj
def uptimerobot_add(ctx, name, url, alert):
    pass

@uptimerobot.command('delete')
@click.argument('names', nargs=-1, required=True)
@click.pass_obj
def uptimerobot_delete(ctx, names):
    pass

if __name__ == '__main__':
    cli()