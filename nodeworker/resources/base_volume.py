#!/usr/bin/env python

class base_volume(object):
    def __init__(self):
        print "base volume"

    def create(self):
        print "volume create"

    def delete(self, volume_id):
        print "volume delete"
    
    def update(self, volume_id, volume_info):
        print "volume %s update" % volume_id