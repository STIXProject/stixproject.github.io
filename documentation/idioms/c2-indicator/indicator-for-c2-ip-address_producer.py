#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP
from cybox.core import Observable
from cybox.objects.address_object import Address


def main():
    stix_package = STIXPackage()
    ttp = TTP(title="C2 Behavior")

    indicator = Indicator(title="IP Address for known C2 Channel")
    indicator.add_indicator_type("IP Watchlist")

    addr = Address(address_value="10.0.0.0", category=Address.CAT_IPV4)
    addr.condition = "Equals"
    indicator.add_observable(addr)
    indicator.add_indicated_ttp(TTP(idref=ttp.id_))

    stix_package.add_indicator(indicator)
    stix_package.add_ttp(ttp)

    print (stix_package.to_xml())

if __name__ == '__main__':
    main()
