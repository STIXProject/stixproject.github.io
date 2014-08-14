#!/usr/bin/env python

from stix.core import STIXPackage, STIXHeader
from datetime import datetime
from cybox.common import Time

from stix.incident import Incident,ImpactAssessment, AffectedAsset
from stix.incident import Time as incidentTime # different type than common:Time

from stix.common import InformationSource
from stix.common import Confidence
from stix.common import Identity

from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.simple_marking import SimpleMarkingStructure

def build_stix( ):
    # setup stix document
    stix_package = STIXPackage()
    stix_header = STIXHeader()

    stix_header.description = "Sample breach report" 
    stix_header.add_package_intent ("Incident")

    # stamp with creator
    stix_header.information_source = InformationSource()
    stix_header.information_source.description = "The person who reported it"

    stix_header.information_source.time = Time()
    stix_header.information_source.time.produced_time = datetime.strptime("2014-03-11","%Y-%m-%d") # when they submitted it

    stix_header.information_source.identity = Identity()
    stix_header.information_source.identity.name = "Sample Investigations, LLC"

    stix_package.stix_header = stix_header

    # add incident and confidence
    breach = Incident()
    breach.description = "Intrusion into enterprise network"
    breach.confidence = "High"

    # incident time is a complex object with support for a bunch of different "when stuff happened" items
    breach.time = incidentTime()
    breach.title = "Breach of Canary Corp"
    breach.time.incident_discovery = datetime.strptime("2013-01-13", "%Y-%m-%d") # when they submitted it

    # add the impact
    impact = ImpactAssessment()
    impact.add_effect("Financial Loss")
    breach.impact_assessment = impact

    # add the victim
    breach.add_victim ("Canary Corp")

    stix_package.add_incident(breach)

    return stix_package

if __name__ == '__main__':
    # emit STIX
    pkg = build_stix()
    print pkg.to_xml() 
