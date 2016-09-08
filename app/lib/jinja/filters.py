import datetime
import time


__epoch = datetime.datetime.utcfromtimestamp(0)


def datetime_filter(dt, sep='T'):
    """
    Prints the datetime object according to the ISO format with the specified
    separator.

    :param datetime: A datetime object.
    """
    return dt.isoformat(sep)


def datetime_to_unix_timestamp(dt):
    if dt.tzinfo is not None:  # Cannot mix aware and naive datetime objects.
        dt = dt.replace(tzinfo=None)
    return (dt - __epoch).total_seconds() * 1000