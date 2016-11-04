#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.indicator.test_mechanism import TestMechanisms
from stix.ttp import TTP
from stix.exploit_target import ExploitTarget, Vulnerability
from stix.extensions.test_mechanism.snort_test_mechanism import SnortTestMechanism
from stix.common import Confidence, InformationSource, Identity


def main():
    stix_package = STIXPackage()

    # Build the Exploit Target
    vuln = Vulnerability()
    vuln.cve_id = "CVE-2014-0160"
    vuln.add_reference("http://heartbleed.com/")

    et = ExploitTarget(title="Heartbleed")
    et.add_vulnerability(vuln)

    stix_package.add_exploit_target(et)

    # Build the TTP
    ttp = TTP(title="Generic Heartbleed Exploits")
    ttp.exploit_targets.append(ExploitTarget(idref=et.id_))

    stix_package.add_ttp(ttp)

    # Build the indicator
    indicator = Indicator(title="Snort Signature for Heartbleed")
    indicator.confidence = Confidence("High")

    tm = SnortTestMechanism()
    tm.rules = [
        """alert tcp any any -> any any (msg:"FOX-SRT - Flowbit - TLS-SSL Client Hello"; flow:established; dsize:< 500; content:"|16 03|"; depth:2; byte_test:1, <=, 2, 3; byte_test:1, !=, 2, 1; content:"|01|"; offset:5; depth:1; content:"|03|"; offset:9; byte_test:1, <=, 3, 10; byte_test:1, !=, 2, 9; content:"|00 0f 00|"; flowbits:set,foxsslsession; flowbits:noalert; threshold:type limit, track by_src, count 1, seconds 60; reference:cve,2014-0160; classtype:bad-unknown; sid: 21001130; rev:9;)""",
        """alert tcp any any -> any any (msg:"FOX-SRT - Suspicious - TLS-SSL Large Heartbeat Response"; flow:established; flowbits:isset,foxsslsession; content:"|18 03|"; depth: 2; byte_test:1, <=, 3, 2; byte_test:1, !=, 2, 1; byte_test:2, >, 200, 3; threshold:type limit, track by_src, count 1, seconds 600; reference:cve,2014-0160; classtype:bad-unknown; sid: 21001131; rev:5;)"""
    ]
    tm.efficacy = "Low"
    tm.producer = InformationSource(identity=Identity(name="FOX IT"))
    tm.producer.references = ["http://blog.fox-it.com/2014/04/08/openssl-heartbleed-bug-live-blog/"]
    indicator.test_mechanisms = TestMechanisms([tm])
    indicator.add_indicated_ttp(TTP(idref=ttp.id_))

    stix_package.add_indicator(indicator)

    print(stix_package.to_xml())

if __name__ == '__main__':
    main()
