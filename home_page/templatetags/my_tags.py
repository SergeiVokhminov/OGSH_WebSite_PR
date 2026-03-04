from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.simple_tag(takes_context=True)
def get_bg_class(context):
    request = context.get("request")
    if not request:
        return "bg-default"

    # Получаем имя текущего url-пути из объекта request
    url_name = request.resolver_match.url_name

    mapping = {
        "home": "bg-default",
        "register": "bg-registration",
        "login": "bg-login",
    }

    return mapping.get(url_name, "bg-default")
