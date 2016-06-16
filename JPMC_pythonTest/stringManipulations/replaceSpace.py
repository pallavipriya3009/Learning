__author__ = 'pallavipriya'


def replaceSpace(astring):
    return "%20".join(astring.split(" "))

print(replaceSpace("python is cool"))