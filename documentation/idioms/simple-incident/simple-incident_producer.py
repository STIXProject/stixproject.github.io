#!/usr/bin/env python

from stix.core import STIXPackage
from datetime import datetime
from cybox.common import Time

from stix.incident import Incident, ImpactAssessment
from stix.incident.impact_assessment import Effects
from stix.incident import Time as incidentTime  # different type than common:Time

from stix.common import InformationSource
from stix.common import Identity


def build_stix():
    # setup stix document
    stix_package = STIXPackage()

    # add incident and confidence
    breach = Incident()
    breach.description = "Intrusion into enterprise network"
    breach.confidence = "High"

    # stamp with reporter
    breach.reporter = InformationSource()
    breach.reporter.description = "The person who reported it"

    breach.reporter.time = Time()
    breach.reporter.time.produced_time = datetime.strptime("2014-03-11", "%Y-%m-%d")  # when they submitted it

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
    impact.effects = Effects("Unintended Access")
    breach.impact_assessment = impact

    # add the victim
    victim = Identity()
    victim.name = "CyberTech Dynamics"
    breach.add_victim(victim)

    # add the impact
    impact = ImpactAssessment()
    impact.effects = Effects("Financial Loss")
    breach.impact_assessment = impact

    stix_package.add_incident(breach)

    return stix_package

if __name__ == '__main__':
    # emit STIX
    pkg = build_stix()
    print(pkg.to_xml(encoding=None))
