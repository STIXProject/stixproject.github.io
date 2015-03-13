#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for orcomplete terms.

from stix.core import STIXPackage
from stix.indicator import Indicator, CompositeIndicatorExpression
from stix.ttp import TTP
from cybox.core import Observable,ObservableComposition
from cybox.objects.address_object import Address

from cybox.objects.email_message_object import EmailMessage,Attachments,AttachmentReference
from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.port_object import Port
from cybox.objects.domain_name_object import DomainName
from cybox.objects.file_object import File
from cybox.objects.mutex_object import Mutex

from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.network_connection_object import NetworkConnection

def main():
    # NOTE: ID values will differ due to being regenerated on each script execution
    pkg = STIXPackage()
    pkg.title="Examples of Observable Composition"


    
    # USE CASE: single obj with single condition
    obs = File()
    obs.file_name = "foo.exe"
    obs.file_name.condition = "Contains"
    pkg.add_observable(obs)
    
    # USE CASE: single obj with multiple conditions
    obs = File()
    obs.file_name = "foo"
    obs.file_name.condition = "Contains"
    obs.size_in_bytes = '1896000'
    obs.size_in_bytes.condition = "Equals"
    pkg.add_observable(obs)

    # USE CASE: multiple obj with individual conditions
    obs = EmailMessage()

    obs.subject = "Syria strategic plans leaked"
    obs.subject.condition= "Equals"
    file_obj = File()
    file_obj.file_name = "bombISIS.pdf"
    file_obj.file_name.condition = "Equals"
    obs.add_related(file_obj, "Contains")
    
    pkg.add_observable(obs)

    
    # USE CASE: multiple objects  with complex condition like (A OR B) AND C
    
    # orcomp = either of a mutex or file are present
    
    orcomp = ObservableComposition()
    orcomp.operator = "OR"
    obs = Mutex()
    obs.name = 'foo'
    obs.name.condition= "Contains"
    
    orcomp.add(obs)
    
    obs = File()
    obs.file_name = "barfoobar"
    obs.file_name.condition = "Equals"
    
    orcomp.add(obs)
    
    # andcomp = the above is true AND a network connection is present
    andcomp = ObservableComposition()
    andcomp.operator = "AND"
    
    andcomp.add(orcomp)
    
    obs = NetworkConnection()
    sock = SocketAddress()
    sock.ip_address = "46.123.99.25"
    sock.ip_address.category = "ipv4-addr"
    sock.ip_address.condition = "Equals"
    obs.destination_socket_address = sock
    andcomp.add (obs)
    
    pkg.add_observable(andcomp) 
    
    # USE CASE:  single object, one property with multiple values 
    obs = SocketAddress()
    obs.ip_address = ['10.0.0.0','10.0.0.1','10.0.0.2'] # comma delimiter automagically added
    obs.ip_address.condition = "Equals"
    obs.ip_address.apply_condition = "ANY"
    
    pkg.add_observable(obs)

    print pkg.to_xml() 
   

if __name__ == '__main__':
    main()
