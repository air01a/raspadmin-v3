#---------------------------------------------------------------------------------------------
#-
#- ConfigReader.py
#- ---------------
#-
#- Read config files
#-
#- Author : Erwan Niquet
#- Date : Jan 2014
#- Part of raspadmin project, an Admin interface for raspberry pi
#-
#--------------------------------------------------------------------------------------------

# -------------
# Import lib
# -------------

import configparser
import sys

# Items required
webconffield=['httpport','usessl','certfile','keyfile','staticfiledir','templatesdir','logfile']
modulefield=['moduledir','login_allowusers','login_pammodule']

# Read config section
def ConfigSectionMap(Config,section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1

Config = configparser.ConfigParser()
Config.read('/etc/raspadmin/raspadmin.conf')
webconf=ConfigSectionMap(Config,'webadmin')

webconfkeys=list(webconf.keys())
for field in webconffield:
	if field not in webconfkeys:
		print("--- Error : Missing field %s in section webadmin" % (field))
		sys.exit(1)

moduleconf=ConfigSectionMap(Config,'module')
moduleconfkeys=list(moduleconf.keys())
for field in modulefield:
        if field not in moduleconfkeys:
                print("--- Error : Missing field %s in section module" % (field))
                sys.exit(1)

globalconf=dict(list(moduleconf.items()) + list(webconf.items()))
