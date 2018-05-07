#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import os
import sys

def realmain (navpath):
    with open(navpath+'/docker-compose.yml', "r+") as f:
        newdct = yaml.load(f)
        dir = os.getcwd()
        if dir in [m.split(':')[0] for m in newdct['services']['nav']['volumes']]:
            print "Directory {} is already configured as volume".format(dir)
        else:
            print "Adding dir {} to docker volumes".format(dir)
            newdct['services']['nav']['volumes'].append(dir+':/tmsource')
            # print newdct
            f.seek(0)
            yaml.dump(newdct, f)
            f.truncate()

if __name__ == '__main__':
    realmain(sys.argv[1])
        
