import sys
import time
from datetime import datetime, timedelta, timezone

from libqtile.log_utils import logger
from libqtile.widget import base

try:
    import pytz
except ImportError:
    pass

try:
    import dateutil.tz
except ImportError:
    pass


class CustomClock(base.InLoopPollText):
    """A simple but flexible text-based clock"""
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('format', '%H:%M', 'A Python datetime format string'),
        ('update_interval', 1., 'Update interval for the clock'),
        ('timezone', None, 'The timezone to use for this clock, either as'
         ' string if pytz or dateutil is installed (e.g. "US/Central" or'
         ' anything in /usr/share/zoneinfo), or as tzinfo (e.g.'
         ' datetime.timezone.utc). None means the system local timezone and is'
         ' the default.')
    ]
    DELTA = timedelta(seconds=0.5)

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Clock.defaults)
        if isinstance(self.timezone, str):
            if "pytz" in sys.modules:
                self.timezone = pytz.timezone(self.timezone)
            elif "dateutil" in sys.modules:
                self.timezone = dateutil.tz.gettz(self.timezone)
            else:
                logger.warning('Clock widget can not infer its timezone from a'
                               ' string without pytz or dateutil. Install one'
                               ' of these libraries, or give it a'
                               ' datetime.tzinfo instance.')
        if self.timezone is None:
            logger.debug('Defaulting to the system local timezone.')

    def tick(self):
        self.update(self.poll())
        return self.update_interval - time.time() % self.update_interval

    # adding .5 to get a proper seconds value because glib could
    # theoreticaly call our method too early and we could get something
    # like (x-1).999 instead of x.000
    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format)
