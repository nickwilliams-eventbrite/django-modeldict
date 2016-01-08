from modeldict.models import ModelDict

try:
    VERSION = __import__('pkg_resources').get_distribution('django-modeldict').version
except Exception, e:
    VERSION = 'unknown'

__all__ = ('VERSION', 'ModelDict')
