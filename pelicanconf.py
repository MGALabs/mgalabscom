AUTHOR = 'MGAadmin'
SITENAME = 'MGALabs'
HIDE_SITENAME = True
SITELOGO = 'images/logo_MGALABS.png'
# SITEURL = 'https://www.mgalabs.com/' # prod url is specified in publishconf.py
SITEURL = '' # de-comment to work in local

STATIC_PATHS = [
    'images',
    'extra', 
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/academy/': {'path': 'academy/'},
    'extra/.well-known/security.txt': {'path': '.well-known/security.txt'},
}

FAVICON = 'images/favicon.png'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'Italian'

THEME = 'themes/bootstrap-next'
# BOOTSTRAP_THEME = 'darkly'
BOOTSTRAP_FLUID = True
BOOTSTRAP_NAVBAR_INVERSE = True
CUSTOM_CSS = 'theme/css/custom.css'
HIDE_SIDEBAR = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_ORDER_BY = 'menu_order'
PAGES_SORT_ATTRIBUTE = 'menu_order'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = ['i18n_subsites', 'jinja2content']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False