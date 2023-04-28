import logging
import os
import time

from pelican import signals

logger = logging.getLogger(__name__)


def set_file_utime(path, datetime):
    """Set modified time (mtime) of specified file path to the current time."""
    mtime = time.mktime(datetime.timetuple())
    logger.info("touching %s", path)
    os.utime(path, (mtime, mtime))


def touch_file(path, context):
    """Set modified time (mtime) of Pelican content files that contain dates."""
    content = context.get("article", context.get("page"))
    page = context.get("articles_page")
    dates = context.get("dates")

    if content and hasattr(content, "date"):
        set_file_utime(path, content.date)
    elif page:
        set_file_utime(path, max(x.date for x in page.object_list))
    elif dates:
        set_file_utime(path, max(x.date for x in dates))


def touch_feed(path, context, feed):
    """Set modified time (mtime) of feeds."""
    set_file_utime(path, max(x["pubdate"] for x in feed.items))


def register():
    """Register plugin with specified Pelican signals."""
    signals.content_written.connect(touch_file)
    signals.feed_written.connect(touch_feed)
