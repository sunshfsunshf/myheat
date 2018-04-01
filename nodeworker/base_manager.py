#!/usr/bin/env python
import tecs_manager
import baremetal_manager
import preset_manager


class baseManager(object):
    def __init__(self):
        pass

    def get_manager_class(self, **kwargs):
        return tecs_manager.TecsResourceManager

    def create_nodepool(self, nodepool_info):
        mgr_cls = self.get_manager_class()
        mgr = mgr_cls()
        mgr.create_nodepool(nodepool_info)

    def update_nodepool(self, nodepool_id, info):
        pass
            
    def delete_nodepool(self, nodepool_id):
        pass
    
    def create_node(self, node, nodepool_id):
        pass
    
    def delete_node(self, node, nodepool_id):
        pass
    
    def create_volume(self):
        pass
    
    def delete_volume(self):
        pass

    def periodic_polling_node(self):
        nodepools = [1,2,3,4]
        for pool in nodepools:
            "if nodepool node less than minium"
            print "rpc api create node %s" % pool
            np_mgr = self.get_manager_class(nodepool=pool)
            np_mgr.apply_nodes()
    
    def periodic_sync_node_status(self):
        pass

    def periodic_sync_volume_status(self):
        pass
