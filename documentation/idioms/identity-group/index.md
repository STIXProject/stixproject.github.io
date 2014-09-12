---
layout: flat
title: Identifying a Threat Actor Group
constructs:
  - Threat Actor
summary: This idiom describes how to use the threat actor construct to represent the identity of a threat actor group. An example of this in threat intelligence is the characterization of the APT1 threat actor group by Mandiant in their 2013 APT1 report.
---

Although many smaller threat intelligence programs do not consider threat actor attribution and identification as part of their core mission, multiple threat intelligence providers and other large organizations do practice threat actor attribution and include those characterizations in their threat intelligence. For example, Mandiant released their [report](http://intelreport.mandiant.com/) on the APT1 threat actor which included a characterization of that actor's identity.

## Scenario

In this scenario, the STIX represents a threat actor group named "Disco Team" that operates primarily in Spanish. They use the e-mail alias "disco-team@stealthemail.com" publicly and are known alternatively as "Equipo del Discoteca". Several references indicate that they are based primarily in Southern California.

## Data model

<img src="diagram.png" alt="Threat Actor Group Identification" />

Threat actor identification is, as you would expect, represented using the STIX [Threat Actor](/data-model/{{site.current_version}}/ta/ThreatActorType) component. More specifically, the `Identity` field, which uses the [IdentityType](/data-model/{{site.current_version}}/stixCommon/IdentityType) extension point, is the field that contains information about the identity of the actor. Other fields in threat actor describe what the actor targets, how sophisticated it is, and other information about it.

The STIX default extension for identity is [OASIS CIQ](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=ciq) implemented via the [CIQIdentity3.0InstanceType](/data-model/{{site.current_version}}/stix-ciqidentity/CIQIdentity3.0InstanceType). Using this extension point, the threat actor identity is characterized in CIQ within the `Specification` field.

## XML

{% highlight xml linenos %}
<stix:STIX_Package >
 <stix:Threat_Actors>
        <stix:Threat_Actor id="example:threatactor-e4a839d7-a15f-41c8-b81f-7107f8602437" timestamp="2014-09-12T20:14:27.864337+00:00" xsi:type='ta:ThreatActorType' version="1.1.1">
            <ta:Title>Disco Team Threat Actor Group</ta:Title>
            <ta:Identity id="example:Identity-2b99ccab-c627-4a13-bc86-c35aa7032591" xsi:type='stix-ciqidentity:CIQIdentity3.0InstanceType'>
                <ExtSch:Specification xmlns:ExtSch="http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1">
  <xpil:PartyName xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
    <xnl:OrganisationName xmlns:xnl="urn:oasis:names:tc:ciq:xnl:3" xnl:Type="CommonUse">
      <xnl:NameElement>Disco Tean</xnl:NameElement>
    </xnl:OrganisationName>
    <xnl:OrganisationName xmlns:xnl="urn:oasis:names:tc:ciq:xnl:3" xnl:Type="UnofficialName">
      <xnl:NameElement>Equipo del Discoteca</xnl:NameElement>
    </xnl:OrganisationName>
  </xpil:PartyName>
  <xpil:Addresses xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
    <xpil:Address>
      <xal:Country xmlns:xal="urn:oasis:names:tc:ciq:xal:3">
        <xal:NameElement>United States</xal:NameElement>
      </xal:Country>
      <xal:AdministrativeArea xmlns:xal="urn:oasis:names:tc:ciq:xal:3">
        <xal:NameElement>California</xal:NameElement>
      </xal:AdministrativeArea>
    </xpil:Address>
  </xpil:Addresses>
  <xpil:ElectronicAddressIdentifiers xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
    <xpil:ElectronicAddressIdentifier>disco-team@stealthemail.com</xpil:ElectronicAddressIdentifier>
  </xpil:ElectronicAddressIdentifiers>
  <xpil:Languages xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
    <xpil:Language>Spanish</xpil:Language>
  </xpil:Languages>
</ExtSch:Specification>
            </ta:Identity>
        </stix:Threat_Actor>
    </stix:Threat_Actors>
</stix:STIX_Package>

{% endhighlight %}

[Full XML](identifying-a-threat-actor-group.xml)

## Python

{% highlight python linenos %}

from stix.core import STIXPackage
from stix.threat_actor import ThreatActor
from stix.extensions.identity.ciq_identity_3_0 import (CIQIdentity3_0Instance, PartyName, STIXCIQIdentity3_0, 
                                      Address, Country, Language, AdministrativeArea, OrganisationName)


def main():
    stix_package = STIXPackage()
    ta = ThreatActor()
    ta.title = "Disco Team Threat Actor Group"
    
    ta.identity = CIQIdentity3_0Instance()
    identity_spec = STIXCIQIdentity3_0()
    
    identity_spec.party_name = PartyName()
    identity_spec.party_name.add_organisation_name(OrganisationName("Disco Tean", type_="CommonUse"))
    identity_spec.party_name.add_organisation_name(OrganisationName("Equipo del Discoteca", type_="UnofficialName"))
    
    identity_spec.add_language("Spanish")
    
    address = Address()
    address.country = Country()
    address.country.add_name_element("United States")
    address.administrative_area = AdministrativeArea()
    address.administrative_area.add_name_element("California")    
    identity_spec.add_address(address)
    
    identity_spec.add_electronic_address_identifier("disco-team@stealthemail.com")
    
    ta.identity.specification = identity_spec
    stix_package.add_threat_actor(ta)
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()

[Production Python](identifying-a-threat-actor-group_producer.py)[Consumption Python](identifying-a-threat-actor-group_consumer.py)
## Further Reading

* [Threat Actor Component](/data-model/{{site.current_version}}/ta/ThreatActorType)

Much of this idiom focused on using the OASIS CIQ standard to represent information about a threat actor's identity. For further information and full documentation on CIQ, download the release from OASIS [here](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=ciq#download).
