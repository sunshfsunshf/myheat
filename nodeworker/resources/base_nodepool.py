#!/usr/bin/env python

class base_nodepool(object):
    def __init__(self):
        print "base nodepool"

    def create(self):
        print "nodepool create"

    def delete(self, nodepool_id):
        print "nodepool delete"
    
    def update(self, nodepool_id, nodepool_info):
        print "nodepool %s update" % nodepool_id