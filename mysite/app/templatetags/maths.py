from django import template
from app.models import ToDoList,Item

register = template.Library()

@register.filter(name="percent_complete")
def percent_complete(to_do:ToDoList):
    completed_items = to_do.item_set.filter(complete=True).count()
    all_items = to_do.item_set.all().count()
    result =  completed_items / all_items *100 if all_items != 0 else 0
    return round(result,2)