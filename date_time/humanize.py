# coding=utf-8

"""humanize dates and times
"""
import datetime


def get_humanize_datetime(d):
    now = datetime.datetime.now()

    delta = now - d
    if delta < datetime.timedelta(minutes=5):
        return u'刚刚'
    elif delta < datetime.timedelta(hours=1):
        return u'{}分钟前'.format(delta.seconds / 60)
    elif delta < datetime.timedelta(days=1):
        return u'{}小时前'.format(delta.seconds / (60 * 60))
    elif delta < datetime.timedelta(days=30):
        return u'{}天前'.format(delta.days)
    elif d.year == now.year:
        return d.strftime('%m-%d')
    else:
        return d.strftime('%Y-%m-%d')


if __name__ == '__main__':
    assert get_humanize_datetime(datetime.datetime(2013, 9, 15)) == '2013-09-15'