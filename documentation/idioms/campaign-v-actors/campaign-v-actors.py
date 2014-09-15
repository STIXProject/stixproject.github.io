#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.1 or greater installed.
For installation instructions, please refer to https://stix.readthedocs.org.
'''

def main():
    from stix.campaign import Campaign, Attribution
    from stix.threat_actor import ThreatActor
    from stix.incident import Incident
    from stix.core import STIXPackage
    from stix.ttp import TTP, VictimTargeting

    ttp = TTP()
    ttp.title = "Victim Targeting: Customer PII and Financial Data"
    ttp.victim_targeting = VictimTargeting()
    ttp.victim_targeting.add_targeted_information("Information Assets - Financial Data")

    actor = ThreatActor()
    actor.title = "People behind the intrusion"
    attrib = Attribution()
    attrib.append(actor)

    c = Campaign()
    c.attribution = []
    c.attribution.append(attrib)
    c.title = "Compromise of ATM Machines"
    c.related_ttps.append(ttp)

    c.related_incidents.append(Incident(idref="example:incident-229ab6ba-0eb2-415b-bdf2-079e6b42f51e"))
    c.related_incidents.append(Incident(idref="example:incident-517cf274-038d-4ed4-a3ec-3ac18ad9db8a"))
    c.related_incidents.append(Incident(idref="example:incident-7d8cf96f-91cb-42d0-a1e0-bfa38ea08621"))

    pkg = STIXPackage()
    pkg.add_campaign(c)

    print pkg.to_xml()

if __name__ == '__main__':
    main()
