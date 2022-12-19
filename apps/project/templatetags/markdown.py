from django.template import Library
import markdown


register = Library()


@register.filter()
def md2html(text):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']
    html = markdown.markdown(text, extensions=exts)
    return html
