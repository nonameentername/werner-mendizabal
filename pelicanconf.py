#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'werner m'
SITENAME = u'werner mendizabal'
SITEURL = 'https://wernermendizabal.com'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
if 'RELATIVE_URLS' in os.environ:
    RELATIVE_URLS = True

THEME = 'html5up-future-imperfect'
FEED_ALL_RSS = 'rss'

DEFAULT_DATE_FORMAT = ('%B %d, %Y')

#DISQUS_SITENAME = 'tecunhuman'

SITE_SUMMMARY = 'Artist, Musician, Programmer and Game Developer'

ABOUT_TEXT = SITE_SUMMMARY
#ABOUT_LINK = 'http://google.com'

TWITTER_USER = 'nonameentername'
FACEBOOK_USER = 'werner.io'
INSTAGRAM_USER = 'nonameentername'
MAIL = 'nonameentername@gmail.com'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
