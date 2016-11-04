#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for orcomplete terms.

from stix.core import STIXPackage
from stix.indicator import Indicator, CompositeIndicatorExpression
from stix.ttp import TTP, Resource, Behavior
from stix.ttp.malware_instance import MalwareInstance
from stix.ttp.infrastructure import Infrastructure
from stix.ttp.behavior import Behavior

from stix.common.related import RelatedTTP
from cybox.core import Observable, ObservableComposition
from cybox.objects.address_object import Address

from stix.campaign import Campaign
from stix.common.vocabs import VocabString

from stix.threat_actor import ThreatActor

from cybox.objects.email_message_object import EmailMessage, Attachments, AttachmentReference
from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.port_object import Port
from cybox.objects.domain_name_object import DomainName
from cybox.objects.file_object import File
from cybox.objects.mutex_object import Mutex

from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.network_connection_object import NetworkConnection

from stix.common import Identity


def main():
    # NOTE: ID values will differ due to being regenerated on each script execution
    pkg1 = STIXPackage()
    pkg1.title = "Example of Indicator Composition for an aggregate indicator composition"

    # USE CASE: Indicator with aggregate pattern

    # Add TTP for malware usage
    malware_ttp = TTP()
    malware_ttp.behavior = Behavior()

    malware = MalwareInstance()
    malware.title = "foobar malware"
    malware.add_type("Remote Access Trojan")
    malware_ttp.behavior.add_malware_instance(malware)

    c2_ttp = TTP()
    c2_ttp.resources = Resource()
    c2_ttp.resources.infrastructure = Infrastructure()
    c2_ttp.resources.infrastructure.add_type(VocabString("Malware C2"))

    pkg1.add_ttp(c2_ttp)
    pkg1.add_ttp(malware_ttp)

    nw_ind = Indicator()
    nw_ind.description = "Indicator for a particular C2 infstructure IP address."
    # add network network connection to this indicator
    obs = NetworkConnection()
    sock = SocketAddress()
    sock.ip_address = "46.123.99.25"
    sock.ip_address.category = "ipv4-addr"
    sock.ip_address.condition = "Equals"
    obs.destination_socket_address = sock
    nw_ind.add_observable(obs)

    nw_ind.add_indicated_ttp(TTP(idref=c2_ttp.id_))

    # create File Hash indicator w/ embedded Observable
    file_ind = Indicator()

    file_ind.description = "Indicator for the hash of the foobar malware."
    file_ind.add_indicator_type("File Hash Watchlist")

    file_obs = File()
    file_obs.add_hash("01234567890abcdef01234567890abcdef")
    file_obs.hashes[0].type_ = "MD5"
    file_obs.hashes[0].type_.condition = "Equals"
    file_ind.add_observable(file_obs)

    # create references
    file_ind.add_indicated_ttp(TTP(idref=malware_ttp.id_))

    # create container indicator
    ind = Indicator()
    ind.add_indicator_type(VocabString("Campaign Characteristics"))
    ind.description = "Indicator for a composite of characteristics for the use of specific malware and C2 infrastructure within a Campaign."

    # Add campaign with related
    camp = Campaign()
    camp.title = "holy grail"
    pkg1.add_campaign(camp)
    camp.related_ttps.append(TTP(idref=c2_ttp.id_))
    camp.related_ttps.append(TTP(idref=malware_ttp.id_))

    # Add threat actor
    ta = ThreatActor()
    ta.identity = Identity()
    ta.identity.name = "boobear"
    ta.observed_ttps.append(TTP(idref=malware_ttp.id_))
    pkg1.add_threat_actor(ta)

    # Create composite expression

    ind.composite_indicator_expression = CompositeIndicatorExpression()
    ind.composite_indicator_expression.operator = "AND"

    ind.composite_indicator_expression.append(file_ind)
    ind.composite_indicator_expression.append(nw_ind)

    pkg1.add_indicator(ind)

    print pkg1.to_xml()

#  USE CASE: Indicator with partial matching

    pkg2 = STIXPackage()
    pkg2.title = "Example of Indicator Composition for a one of many indicator composition"

    # create container indicator
    watchlistind = Indicator()
    watchlistind.add_indicator_type("IP Watchlist")
    watchlistind.description = "This Indicator specifies a pattern where any one or more of a set of three IP addresses are observed."

    watchlistind.add_indicated_ttp(TTP(idref=c2_ttp.id_))

    # Create composite expression
    watchlistind.composite_indicator_expression = CompositeIndicatorExpression()
    watchlistind.composite_indicator_expression.operator = "OR"

    ips = ['23.5.111.68', '23.5.111.99', '46.123.99.25']
    for ip in ips:
        new_ind = Indicator()
        new_ind.description = "This Indicator specifies a pattern where one specific IP address is observed"
        # add network network connection to this indicator
        obs = Address()
        obs.address_value = ip
        obs.address_value.condition = "Equals"
        new_ind.add_observable(obs)

        new_ind.add_indicated_ttp(TTP(idref=c2_ttp.id_))

        watchlistind.composite_indicator_expression.append(new_ind)

    pkg2.add_indicator(watchlistind)

    print pkg2.to_xml()

    #  USE CASE: Indicator with compound detection

    pkg3 = STIXPackage()
    pkg3.title = "Example of Indicator Composition for compound detection"

    # create container indicator
    watchlistind2 = Indicator()
    watchlistind2.add_indicator_type("IP Watchlist")
    watchlistind2.description = "This Indicator specifies a composite condition of two preexisting Indicators (each identifying a particular TTP with low confidence) that in aggregate identify the particular TTP with high confidence."
    # Create composite expression
    watchlistind2.composite_indicator_expression = CompositeIndicatorExpression()
    watchlistind2.composite_indicator_expression.operator = "OR"

    watchlistind2.add_indicated_ttp(TTP(idref=c2_ttp.id_))
    watchlistind2.confidence = "High"

    nw_ind.description = "Indicator for a particular C2 IP address used by a malware variant."
    nw_ind.confidence = "Low"
    nw_ind.indicator_types = ["C2"]
    file_ind.description = "Indicator that contains malicious file hashes for a particular malware variant."
    file_ind.confidence = "Low"
    watchlistind2.composite_indicator_expression.append(nw_ind)
    watchlistind2.composite_indicator_expression.append(file_ind)

    pkg3.add_indicator(watchlistind2)

    print pkg3.to_xml()


if __name__ == '__main__':
    main()
