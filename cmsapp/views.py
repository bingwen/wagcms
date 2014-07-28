from django.http import HttpResponse
from wagtail.wagtailcore.models import Page, Q


def sub_nav_html(nodes):
    html = ''
    for page in nodes:
        children = page.get_children()
        if children:
            html += '<li "has-children">'
            html += '<a href="' + str(page.url) + '" class="icon icon-folder-open-inverse">' + page.title + '</a>'
            html += '<div class="children icon icon-arrow-right"></div>'
            html += '<ul class="dl-submenu">'
            html += sub_nav_html(children)
            html += '</ul>'
            html += '</li>'
        else:
            html += '<li>'
            html += '<a href="' + page.url + '" class="icon icon-folder-open-inverse">' + page.title + '</a>'
            html += '</li>'
    return html


def nav_html(nodes):
    return '<ul class="dl-menu">' + sub_nav_html(nodes) + '</ul>'


def explorer_nav(request):
    return HttpResponse(nav_html(Page.objects.filter(Q(depth=2))))
