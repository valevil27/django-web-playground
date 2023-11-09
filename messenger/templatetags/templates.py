from django.template import Library


register = Library()

@register.filter
def exclude(queryset, user):
    return queryset.exclude(username=user.username).first()