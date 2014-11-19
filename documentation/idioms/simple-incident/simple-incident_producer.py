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

    stix_package.stix_header = stix_header

    # add incident and confidence
    breach = Incident()
    breach.description = "Intrusion into enterprise network"
    breach.confidence = "High"

    # stamp with reporter
    breach.reporter = InformationSource()
    breach.reporter.description = "The person who reported it"

    breach.reporter.time = Time()
    breach.reporter.time.produced_time = datetime.strptime("2014-03-11","%Y-%m-%d") # when they submitted it

    breach.reporter.identity = Identity()
    breach.reporter.identity.name = "Sample Investigations, LLC"

    # set incident-specific timestamps
    breach.time = incidentTime()
    breach.title = "Breach of CyberTech Dynamics"
    breach.time.initial_compromise = datetime.strptime("2012-01-30", "%Y-%m-%d") 
    breach.time.incident_discovery = datetime.strptime("2012-05-10", "%Y-%m-%d") 
    breach.time.restoration_achieved = datetime.strptime("2012-08-10", "%Y-%m-%d") 
    breach.time.incident_reported = datetime.strptime("2012-12-10", "%Y-%m-%d") 

    # add the impact
    impact = ImpactAssessment()
    impact.add_effect("Unintended Access")
    breach.impact_assessment = impact

    # add the victim
    breach.add_victim ("CyberTech Dynamics")

    # add the impact
    impact = ImpactAssessment()
    impact.add_effect("Financial Loss")
    breach.impact_assessment = impact

    stix_package.add_incident(breach)

    return stix_package

if __name__ == '__main__':
    # emit STIX
    pkg = build_stix()
    print pkg.to_xml() 
