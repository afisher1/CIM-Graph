from __future__ import annotations
import uuid
import json
import logging
import importlib


from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cimgraph.models.graph_model import GraphModel
from cimgraph.models.distributed_area import DistributedArea
from cimgraph.databases import ConnectionInterface
from cimgraph.topology_processor.linknet import LinkNet
from cimgraph.topology_processor.distributed_feeder_areas import DistributedFeederTopology


_log = logging.getLogger(__name__)

@dataclass
class FeederModel(GraphModel):
    """ 
    Knowledge graph class for distribution feeder objects
    Args:
        container: a CIM Feeder object with specified mRID
        connection: a ConnectionInterface object, such as BlazegraphConnection
        distributed: a boolean to indicate if the graph is distributed
    Optional Args:
        distributed_hierarchy: Custom inheritance structure for defining distributed areas
        topology_message: JSON message from GridAPPS-D Topology Proccessor Service
    Returns:
        none
    Methods:
        add_to_graph(object): adds a new CIM object to the knowledge graph
        get_all_edges(cim.ClassName): universal database query to expand graph by one edge
        graph[cim.ClassName]: access to graph dictionary sorted by class and mRID
        pprint(cim.ClassName): pretty-print method for showing graph of a class type
        get_edges_query(cim.ClassName): returns query text for debugging
    """
    topology_message: dict = field(default_factory=dict)
    distributed_hierarchy: list[type] = field(default_factory=list)

    
    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)

        if self.distributed:
            self.initialize_distributed_model(self.container)
        else:
            self.initialize_centralized_model(self.container)

    def initialize_centralized_model(self, container) -> None:
        self.graph = self.connection.create_new_graph(container)

        
    def initialize_distributed_model(self, container) -> None:
        centralized_graph = self.connection.create_new_graph(container) # Initialize centralized graph model
        
        # Use output from GridAPPS-D Topology Processor if given
        if self.topology_message is not None: 
            self.switch_areas = []
            topo = self.topology_message["feeders"]
            # for feeder in self.distributed_topology["feeders"]:
                # if feeder["feeder_id"] == self.container.mRID:

            self.FeederArea = DistributedArea(self.connection, self.cim_profile)
            self.FeederArea.build_from_topo_message(topo, centralized_graph)
            self.graph = self.FeederArea.graph

            for switch_topo in topo["switch_areas"]:
                switch_container = self.cim.EquipmentContainer(mRID=str(uuid.uuid4()))
                SwitchArea = DistributedArea(connection=self.connection, container=switch_container)
                SwitchArea.build_from_topo_message(switch_topo, centralized_graph)
                self.switch_areas.append(SwitchArea)
                for secondary_topo in switch_topo["secondary_areas"]:
                    SwitchArea.secondary_areas = []
                    secondary_container = self.cim.EquipmentContainer(mRID=str(uuid.uuid4()))
                    SecondaryArea = DistributedArea(connection=self.connection, container=secondary_container)
                    SecondaryArea.build_from_topo_message(secondary_topo, centralized_graph)

        # If GridAPPS-D Topology Processor output is not provided, build new topology:
        else:
        
            if len(self.distributed_hierarchy) > 0:
                for container_class in self.distributed_hierarchy:
                    container_type = container_class.__class__.__name__
                    setattr(self, container_type + 's', []) 
                    #TODO: create subclasses based on pre-defined topology        
            else:
                self.get_all_edges(self.cim.PowerTransformer, centralized_graph)
                self.get_all_edges(self.cim.TransformerTank, centralized_graph)
                self.get_all_edges(self.cim.BaseVoltage, centralized_graph)
                
                DistTopo = DistributedFeederTopology(self.connection, self.cim_profile, centralized_graph)
                self.switch_areas, self.graph = DistTopo.create_distributed_graph()
    #             self.linknet = LinkNet(self.cim_profile, centralized_graph)
    #             self.linknet.build_linknet([self.cim.ACLineSegment])
            

        
            