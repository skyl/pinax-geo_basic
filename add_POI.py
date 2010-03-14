#!/usr/bin/env python
import sys

from os.path import abspath, dirname, join
import os

try:
    import pinax
except ImportError:
    sys.stderr.write("Error: Can't import Pinax. Make sure you are in a virtual environment that has Pinax installed or create one with pinax-boot.py.\n")
    sys.exit(1)

from django.conf import settings
from django.core.management import setup_environ, execute_from_command_line

try:
    import settings as settings_mod # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings_mod)

sys.path.insert(0, join(settings.PINAX_ROOT, "apps"))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))


def run():
    from geonames.models import POI
    f = file('data/US.txt')
    for l in f:
        li = l.split('\t')
        try:
            p = POI()
            p.geonameid = li[0]
            p.name = li[1]
            p.asciiname = li[2]
            p.alternatenames = li[3]
            p.point = "POINT(%s %s)" % (li[5], li[4])
            p.feature_class = li[6]
            p.feature_code = li[7]
            p.country_code = li[8]
            p.ccs2 = li[9]
            p.admin1_code = li[10]
            p.admin2_code = li[11]
            p.admin3_code = li[12]
            p.admin4_code = li[13]
            p.population = li[14]
            p.elevation = li[15]
            p.gtopo30 = li[16]
            p.timezone = li[17]
            p.modification_date = li[18]
            p.save()
        except IndexError:
            pass

if __name__ == "__main__":
    run()

