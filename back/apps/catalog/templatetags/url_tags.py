from django import template

register = template.Library()

@register.simple_tag
def go_to(request, field, value):

    dict_ = request.GET.copy()
    dict_[field] = value

    return dict_.urlencode()