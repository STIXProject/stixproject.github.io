#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

def main():
    from stix.campaign import Campaign
    from stix.common.related import RelatedTTP
    from stix.core import STIXPackage
    from stix.ttp import TTP, VictimTargeting

    ttp = TTP()
    ttp.title = "Victim Targeting: Customer PII and Financial Data"
    ttp.victim_targeting = VictimTargeting()
    ttp.victim_targeting.add_targeted_information("Information Assets - Customer PII")
    ttp.victim_targeting.add_targeted_information("Information Assets - Financial Data")

    ttp_ref = TTP()
    ttp_ref.idref = ttp.id_
    related_ttp = RelatedTTP(ttp_ref)
    related_ttp.relationship = "Targets"

    c = Campaign()
    c.title = "Operation Alpha"
    c.related_ttps.append(related_ttp)

    pkg = STIXPackage()
    pkg.add_campaign(c)
    pkg.add_ttp(ttp)

    print pkg.to_xml()

if __name__ == '__main__':
    main()
