"""Define features that can be used throughout the code.
"""
def split_host_port(uri, default_port):
    """Return a tuple with host and port.

    If a port is not found in the uri, the default port is returned.
    """
    if uri.find(":") >= 0:
        host, port = uri.split(":")
    else:
        host, port = (uri, default_port)
    return host, port

def combine_host_port(host, port, default_port):
    """Return a string with the parameters host and port.
        
    :return: String host:port.
    """ 
    if host:
        host_info = host
    else:
        host_info = "unknown host"

    if port:
        port_info = port
    else:
        port_info = default_port
    
    return "%s:%s" % (host_info, port_info)


class SingletonMeta(type):
    """Define a Singleton.
    This Singleton class can be used as follows::

      class MyClass(object):
        __metaclass__ = SingletonMeta
      ...
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(object):
    """Define a Singleton.
    This Singleton class can be used as follows::

      class MyClass(Singleton):
      ...
    """
    __metaclass__ = SingletonMeta