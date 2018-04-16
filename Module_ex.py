# /* atexit */
"""
The atexit module provides a simple interface to register functions to be called when a program closes down normally.
The sys module also provides a hook, sys.exitfunc, but only one function can be registered there.
"""

import atexit
import os


def my_cleanup(name):
    print('My_cleaUp {}'.format(name))
    # print(abc)


atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')
# If os._exit() instead of exiting normally, the callback is not invoked.
# os._exit(0)

# /* bisect */
"""
Maintains a list in sorted order without having to call sort each time an item is added to the list.
"""

# /* Calendar */
"""
The calendar module implements classes for working with dates to manage year/month/week oriented values.
"""

import calendar


c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2018, 4)


# /* fnmatch */
"""
The fnmatch module is used to compare filenames against glob-style patterns such as used by Unix shells.
"""
import fnmatch
import pprint

pattern = 'fnmatch_*.py'

print(fnmatch.fnmatch('hello.py', pattern))  # False
fnmatch.fnmatchcase('hello.py', pattern)  # Case insensitive
files = ['fnmatch_filter.py',
         'fnmatch_fnmatch.py',
         'fnmatch_fnmatchcase.py',
         'fnmatch_translate.py',
         'index.rst']
"""
filter() returns the list of names of the example source files associated with this section.
"""
pprint.pprint(fnmatch.filter(files, pattern))

# Translating Patterns
"""
fnmatch converts the glob pattern to a regular expression and uses the re module to compare the name and pattern.
The translate() function is the public API for converting glob patterns to regular expressions.
"""

print("Pattern: {}".format(pattern))
print("regex: {}".format(fnmatch.translate(pattern)))

# /* glob: Filename Pattern matching */
"""
Use Unix shell rules to find filenames matching a pattern.
"""
# glob.glob('dir/subdir/*')

# glob.glob('dir/*[0-9].*')

