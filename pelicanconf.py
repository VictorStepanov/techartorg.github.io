#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TAO-community'
SITENAME = 'TAO-wiki'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'themes/tao-wiki-bootstrap-next'

BOOTSTRAP_THEME = 'tao'

PLUGIN_PATHS = ['plugins/pelican-plugins', 'plugins/tao']
PLUGINS = ['i18n_subsites', 'pelican-page-hierarchy', 'data_driven_wiki']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Tech-Artists.Org', 'http://discourse.techart.online'),)

# Social widget
SOCIAL = (('Tech-Artists Slack', 'https://tech-artists.slack.com'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True