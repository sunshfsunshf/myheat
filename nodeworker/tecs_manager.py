#!/usr/bin/env python
from nodeworker.resources.tecs import nodepool
from nodeworker.resources.tecs import node
from nodeworker.resources.tecs import volume


class TecsResourceManager(object):
    def __init__(self):
        print "tecs res mgr"
        self.nodepool_mgr = nodepool.nodepool()
        self.node_mgr = node.node()
        self.volume_mgr = volume.volume()
    
    def create_nodepool(self, nodepool_info):
        self.nodepool_mgr.create(nodepool_info)

    def update_nodepool(self, nodepool_id, info):
        self.nodepool_mgr.update(nodepool_id, info)
            
    def delete_nodepool(self, nodepool_id):
        self.nodepool_mgr.delete(nodepool_id)
    
    def create_node(self, node):
        self.node_mgr.create(node)
        
    
    def delete_node(self, node_id):
        self.node_mgr.delete(node_id)
    
    def create_volume(self):
        self.volume_mgr.create()
        "do create volume action"
        "get next step:: create port"
        "api: create port"

    def create_port(self):
        print "create port"
        "do create port"
        "get next step: create node"
        "api: create node"

    
    def delete_volume(self, volume_id):
        self.volume_mgr.delete(volume_id)
        

    def apply_nodes(self):
        nodepool_min_size = 5
        for i in range(nodepool_min_size):
            self._async_apply_node()

    def _async_apply_node(self):
        steps = ["create volume",  "create_port", "create_node"]
        print "get first step"
        print "rpcapi first step:: create volume"
            