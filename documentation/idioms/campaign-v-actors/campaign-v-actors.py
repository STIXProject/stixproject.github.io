#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

def main():
    from stix.campaign import Campaign, Attribution
    from stix.threat_actor import ThreatActor
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

    pkg = STIXPackage()
    pkg.add_campaign(c)

    print pkg.to_xml()

if __name__ == '__main__':
    main()
