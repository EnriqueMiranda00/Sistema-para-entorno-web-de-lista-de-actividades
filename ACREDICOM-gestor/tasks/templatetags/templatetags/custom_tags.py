from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    """
    Retorna True si el usuario pertenece al grupo cuyo nombre es group_name.
    """
    return user.groups.filter(name=group_name).exists()
4
