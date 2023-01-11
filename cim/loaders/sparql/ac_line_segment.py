from typing import List
from dataclasses import dataclass, field

import cim.data_profile as cim

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?length ?bch ?r ?x ?gch ?b0ch ?r0 ?x0 ?g0ch 
        ?PerLengthImpedance ?WireSpacingInfo
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        (group_concat(distinct ?ACLineSegmentPhase; separator=';') as ?ACLineSegmentPhases)  
        WHERE {          
          ?eq r:type cim:ACLineSegment.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        ?eq cim:ConductingEquipment.BaseVoltage ?bv.
        ?bv cim:IdentifiedObject.mRID ?BaseVoltage.

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:IdentifiedObject.mRID ?Terminal

        OPTIONAL {?meas cim:Measurement.Terminal ?t.
          ?meas cim:IdentifiedObject.mRID ?Measurement}

        OPTIONAL {?eq cim:Conductor.length ?length.}
        
        OPTIONAL {?eq cim:ACLineSegment.bch ?bch.}
        OPTIONAL {?eq cim:ACLineSegment.r ?r0.}
        OPTIONAL {?eq cim:ACLineSegment.x ?x0.}
        OPTIONAL {?eq cim:ACLineSegment.g ?r0.}
        OPTIONAL {?eq cim:ACLineSegment.b0ch ?b0.}
        OPTIONAL {?eq cim:ACLineSegment.r0 ?r0.}
        OPTIONAL {?eq cim:ACLineSegment.x0 ?x0.}
        OPTIONAL {?eq cim:ACLineSegment.g0ch ?b0.}

        OPTIONAL {?eq cim:ACLineSegment.PerLengthImpedance ?pli.
                  ?pli cim:IdentifiedObject.mRID ?PerLengthImpedance.}
        OPTIONAL {?eq cim:ACLineSegment.WireSpacingInfo ?wsi.
                  ?wsi cim:IdentifiedObject.mRID ?WireSpacingInfo.}
        OPTIONAL {?aclsp cim:ACLineSegmentPhase.ACLineSegment ?eq.
                  ?aclsp cim:IdentifiedObject.mRID ?ACLineSegmentPhase.}

        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?length ?bch ?r ?x ?gch ?b0ch ?r0 ?x0 ?g0ch 
                ?PerLengthImpedance ?WireSpacingInfo 
        ORDER by  ?name
        """
    return query_message