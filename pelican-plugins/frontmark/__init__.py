import pelican.plugins.signals

from .__about__ import __version__, __description__  # noqa
from .reader import add_reader


def register():
    pelican.plugins.signals.readers_init.connect(add_reader)
