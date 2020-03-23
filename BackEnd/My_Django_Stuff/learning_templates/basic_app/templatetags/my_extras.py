#create your own filter
from django import template

register = template.Library()

# use python decorators to register
@register.filter(name='cut')
#custome template filter
def cut(value,arg):
    # this cuts out all values of "arg" from the string!
    return value.replace(arg,'')

#regist the custome filter: 'cut' is the name you want, and cut is the function
# register.filter('cut',cut)