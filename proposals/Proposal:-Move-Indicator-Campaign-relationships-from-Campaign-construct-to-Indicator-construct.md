**Status**: Accepted w/ modifications  
**Comment Period Closes**: 1/17/2014  
**Affects Backwards Compatibility**: ***YES***  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/55

#### Background Information
This proposal concerns the ability to characterize relationships between Indicators and Campaigns in a simpler, more consistent, more ontologically coherent and more practical manner. The use of the current approach is considered a bug that needs resolving as soon as possible.

In STIX 1.0, relationships between `Indicators` and `Campaigns` are asserted with the `Related_Indicators` element of the `Campaign` construct. As an example:

```
<stix:Campaign id="example-1">
  <campaign:Title>Disco Foo</campaign:Title>
  <campaign:Names>
    <campaign:Name>Disco Foo</campaign:Name>
  </campaign:Names>
  <campaign:Related_Indicators>
    <campaign:Related_Indicator>
      <stixCommon:Indicator idref="example-2" />
    </campaign:Related_Indicator>
  </campaign:Related_Indicators>
</stix:Campaign>
```

There are several downsides to this approach:

* From an ontology perspective it does not really make sense for related `Indicators` to be a part of `Campaigns` as `Campaigns` are a meta construct tying together various `Incidents` and/or `TTP` with some believed attribution and intent. `Indicators` may indicate `TTP` behaviors used within a `Campaign` but they are not really part of the `Campaign` itself
* If one wishes to specify an `Indicator` and give a simple name label to refer to believed related activity before details are known, they would have to create a separate `Campaign` construct with just a `Name` given and `Related_Indicator` and then pass along both the `Campaign` (mostly empty) and `Indicator` contstructs.
* A very common use case would be to specify one or more Indicators related to a `Campaign`, share these and then over time specify and share more Indicators as more is learned. In this use case, the complete `Campaign` instance would need to be updated and resent with each new `Indicator` even though its core content had not changed.
* If a given `Campaign` was known by multiple different names to different parties (a common occurrence), the current approach would require separate `Campaign` entries for each name with `Related_Indicators` defined within each `Campaign` instance to the set of related `Indicators`. If a single `Indicator` was applicable to several different `Campaigns`, the current approach would not give an easy way to discover this without scanning across all known `Campaigns`.

Based on their predominant use cases, numerous stakeholders in the STIX community have expressed an urgent need for a simple way to add `Campaign` relationships to `Indicators` rather than the other way around.


#### Proposal
This proposal suggests reversing the direction of that relationship: rather than a Campaign having Related_Indicators, an Indicator will have Referenced_Campaigns. This new structure would allow for referencing (but not defining) existing or yet-to-be-defined campaigns through either an `@idref` or a campaign name.

The specific change would be to add a new `Campaign_References` element to `IndicatorType`. That element would consistent of a list of zero or more `Campaign_Reference` elements, each of type `ReferencedCampaignType`. `ReferencedCampaignType` would be similar to the existing `RelatedCampaignType` but instead of allowing a full campaign model it would be limited to referencing a campaign by either `@idref` or the campaign's names.

At a more technical level, `CampaignReferenceType` will extend `stixCommon:GenericRelationshipType` and add a simple `Campaign` element of type `CampaignReferenceType`. That element would allow:

* `@idref` attribute (a STIX ID reference to a separately defined `Campaign`)
* `Names` element, of type `campaign:NamesType` (this type would likely be duplicated or moved from the campaign schema to the stixCommon schema)

Of course, at the Campaign_Reference level you would also have the standard relationship metadata:

* ```Confidence``` element, to characterize the confidence in the relationship
* ```Information_Source``` element, to characterize the information source of the relationship
* ```Relationship``` element, to characterize the nature of the relationship

Essentially, you can think of this relationship as identical to standard STIX relationships except instead of allowing for the inline definition of a campaign or a reference to an externally defined campaign, it only allows a reference to an externally defined campaign by @id or Name.

These new types would be added to the `stix_common.xsd` schema file such that it could be leveraged in several places throughout STIX.

Using this approach you could easily do the following things:
* Add a simple campaign appellation to an `Indicator` where a separate `Campaign` construct for that campaign may not exist:
```
<indicator:Referenced_Campaign>
  <stixCommon:Campaign>
    <stixCommon:Names>
      <stixCommon:Name>Disco Foo</Name>
    </stixCommon:Names>
  </stixCommon:Campaign>
</indicator:Referenced_Campaign>
```
* Add a reference to a separately defined `Campaign` construct using the `@idref` attribute:
```
<indicator:Referenced_Campaign>
  <stixCommon:Campaign idref="example-1" />
</indicator:Referenced_Campaign>
```

* Add a set of simple campaign appellations to an `Indicator` where a given campaign may be known by several names:
```
<indicator:Referenced_Campaign>
  <stixCommon:Campaign>
    <stixCommon:Names>
      <stixCommon:Name>Disco Foo</Name>
      <stixCommon:Name>Sunday Parade</Name>
    </stixCommon:Names>
  </stixCommon:Campaign>
</indicator:Referenced_Campaign>
```

* Add a simple campaign appellation as a newly created name for new activity and then in the future also add an `@idref` to a `Campaign` entry when more is known and that knowledge is formalized.

For STIX 1.1, we propose adding a `Campaign_References` element of `CampaingReferencesType` to `Indicator`.
For STIX 2.0, we see potential applicability to adding a similar element to other constructs such as `Incident`, `TTP`, `Exploit_Target`, `Threat_Actor` and potentially `Observables`.

Once again, it should be noted that this relationship structure is a subset of the standard full extension of `GenericRelationshipListType` and not the full type used in most relationships between STIX top level constructs. This is due to the fact that Campaigns are only applicable as separate constructs related from an Indicator and would never make sense to define inline within an Indicator as an inherent part of the Indicator itself.

It is further proposed that the existing `Related_Indicators` structure within the `Campaign` construct be removed in order to avoid inconsistency and complexity issues with maintaining the same relationships in multiple places. This does have the effect of invalidating any existing 1.0 or 1.0.1 content using that structure, however. This is likely the most significant backwards-incompatible change being proposed for STIX 1.1 so please carefully evaluate any potential impact against your current content.

Upon our review of this proposed approach there do not seem to be any major ontological issues, though we are interested if you see any.

Here is the draft XSD for the proposed solution (in stixCommon).
```xml
<xs:complexType name="CampaignReferencesType">
  <xs:annotation>
    <xs:documentation>The CampaignReferencesType specifies identity for one or more referential campaigns asserted to be related to this component.</xs:documentation>
  </xs:annotation>
  <xs:sequence>
    <xs:element maxOccurs="unbounded" name="Campaign_Reference" type="stixCommon:CampaignReferenceType">
      <xs:annotation>
        <xs:documentation>The Campaign_Reference field specifies identity for one referential campaign asserted to be related to this component.</xs:documentation>
      </xs:annotation>
    </xs:element>
  </xs:sequence>
</xs:complexType>
<xs:complexType name="CampaignReferenceType">
  <xs:complexContent>
    <xs:extension base="stixCommon:GenericRelationshipType">
      <xs:sequence>
        <xs:element name="Campaign" type="stixCommon:ReferencedCampaignType" minOccurs="1">
          <xs:annotation>
            <xs:documentation>A reference to the related campaign.</xs:documentation>
          </xs:annotation>
        </xs:element>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
<xs:complexType name="ReferencedCampaignType">
  <xs:sequence>
    <xs:element name="Names" maxOccurs="unbounded" type="stixCommon:CampaignNamesType">
      <xs:annotation>
        <xs:documentation>The Names field specifies Names used to identify a Campaign. These may be either internal or external names.</xs:documentation>
      </xs:annotation>
    </xs:element>
  </xs:sequence>
  <xs:attribute name="idref" type="xs:QName">
    <xs:annotation>
      <xs:documentation>Specifies a globally unique identifier for a cyber threat Campaign specified elsewhere.</xs:documentation>
    </xs:annotation>
  </xs:attribute>
</xs:complexType>
<xs:complexType name="CampaignNamesType">
  <xs:sequence>
    <xs:element maxOccurs="unbounded" name="Name" type="stixCommon:ControlledVocabularyStringType">
      <xs:annotation>
        <xs:documentation>The Name field specifies a Name used to identify a Campaign. This field can be used to capture various aliases used to identify this Campaign.</xs:documentation>
      </xs:annotation>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

#### Impact
This proposal resolves what is considered a bug in STIX 1.0.1 and is not fully backward compatible. Specifically, it removes the `Related_Indicators` element from `CampaignType`. Any `Campaign` instance content currently containing such relationship specifications would need to be transformed to utilize the proposed `Campaign_References` structure on Incidents in order to be valid for STIX 1.1.


#### Requested Feedback
1. Is there value in the ability to refer to `Campaigns` from `Indicators`?
2. Is the mechanism in which this is implemented, including the set of fields on `ReferencedCampaignType`, correct?
3. Are there any significant issues with removing `Related_Indicators` from `CampaignType`?
4. Are there any ontological issues other than those discussed above?

#### Resolution

This proposal was accepted with the stipulation that the existing mechanism (Campaign -> Indicator) was kept and marked as deprecated rather than removed.