#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.2.0.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage, STIXHeader
from stix.report import Report, Header
from stix.common import InformationSource, Identity
from stix.ttp import TTP
from stix.campaign import Campaign

def main():

    campaign = Campaign(title="Campaign against ICS")
    ttp = TTP(title="DrownedRat")

    alpha_report = Report()
    alpha_report.header = Header()
    alpha_report.header.title = "Report on Adversary Alpha's Campaign against the Industrial Control Sector"
    alpha_report.header.descriptions = "Adversary Alpha has a campaign against the ICS sector!"
    alpha_report.header.intents = "Campaign Characterization"
    alpha_report.add_campaign(Campaign(idref=campaign.id_))

    rat_report = Report()
    rat_report.header = Header()
    rat_report.header.title = "Indicators for Malware DrownedRat"
    rat_report.header.intents = "Indicators - Malware Artifacts"
    rat_report.add_ttp(TTP(idref=ttp.id_))

    wrapper = STIXPackage()
    info_src = InformationSource()
    info_src.identity = Identity(name="Government Sharing Program - GSP")
    wrapper.stix_header = STIXHeader(information_source=info_src)
    wrapper.add_report(alpha_report)
    wrapper.add_report(rat_report)
    wrapper.add_campaign(campaign)
    wrapper.add_ttp(ttp)


    print wrapper.to_xml()

if __name__ == '__main__':
    main()
