try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-sentry').version
except Exception as e:
    VERSION = 'unknown'
