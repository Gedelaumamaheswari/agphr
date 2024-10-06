from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name):
    request = context['request']
    current_url = request.resolver_match.url_name
    return 'active' if current_url == url_name else ''
