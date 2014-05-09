**Status**: Open  
**Comment Period Closes**: 1/31/2014  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/93

#### Background Information
Several members of the STIX community have recently encountered a few cases where it would be useful to be able to represent which “personas” a threat was leveraging for masquerading as other parties. For example, a phishing campaign might purport to be sending e-mails from Target, a malicious website may be setup to look identical to a particular bank,or a piece of malware might masquerade as being from Acme, Inc.

STIX 1.0.1 does not have an existing mechanism to represent this.

#### Proposal
This proposal suggests add a field to TTP's `ResourcesType` called "Personas" that uses `IdentityType` to allow you to capture this type of information.

```xml
<ttp:TTP id="guid-1234">
  <ttp:Resources>
    <ttp:Personas>
      <ttp:Persona xsi:type="STIXCIQIdentityType">
        <ttp:Name>ACME, Inc.</ttp:Name>
        <!-- Other information ....... -->
      </ttp:Persona>
    </ttp:Personas>
  </ttp:Resources>
</ttp:TTP>
```

In the example above, the TTP represents a persona for ACME, Inc. As a few examples of how this could be used, the TTP could then be related to a threat actor to show that the actor uses that persona, another TTP to show that a particular TTP uses that persona, or an Incident to show that the persona was leveraged in an incident.

The implementation for this would essentially be to add the `Personas` element to the TTP's `ResourcesType`, because a persona is, in reality, a resource leveraged by a threat. That `Personas` element would then contain 1 to many `Persona` elements that use the existing STIX `IdentityType`, which allows you to either extend the type and use CIQ or some other identity structure or just represent a simple name. The schema snippet is below:

```xml
<!-- Type used by TTP/Resources element -->
<xs:complexType name="ResourceType">
  <xs:sequence>
    <xs:element name="Tools" type="ttp:ToolsType" minOccurs="0"><!-- snip --></xs:element>
    <xs:element name="Infrastructure" type="ttp:InfrastructureType" minOccurs="0"><!-- snip --></xs:element>
    <xs:element name="Personas" type="ttp:PersonasType" minOccurs="0">
      <xs:annotation>
        <xs:documentation>The Personas field characterizes specific classes or instances of personas (identities) leveraged by a threat to masquerade as other parties.</xs:documentation>
      </xs:annotation>
    </xs:element>
  </xs:sequence>
</xs:complexType>

<!-- Type definition -->
<xs:complexType name="PersonasType">
  <xs:sequence>
    <xs:element name="Persona" type="stixCommon:IdentityType" maxOccurs="unbounded">
      <xs:annotation>
        <xs:documentation>The persona field characterizes a single persona (identity) leveraged by a threat to masquerade as another party.</xs:documentation>
      </xs:annotation>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

The changeset can also be viewed in the associated pull request: https://github.com/STIXProject/schemas/pull/122

#### Impact
There is no expected compatibility impact. Producers will have the option to use the new field and consumers can support it or not as with any other STIX field.

#### Requested Feedback

1. Should this capability be added to STIX?
1. If added, does it make sense to use the IdentityType to represent it?
1. Should any other information about personas beyond that in IdentityType be captured?