#!/usr/bin/env python

class base_node(object):
    def __init__(self):
        print "base node"

    def create(self):
        print "node create"

    def delete(self, node_id):
        print "node delete"
    
    def update(self, node_id, node_info):
        print "node %s update" % node_id