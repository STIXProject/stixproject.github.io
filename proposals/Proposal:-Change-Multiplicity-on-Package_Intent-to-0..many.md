**Status**: Accepted  
**Comment Period Closes**: November 22, 2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/24

#### Background Information
This proposal concerns the ```Package_Intent``` field in the ```STIX_Header```. In STIX 1.0.1, this construct has a multiplicity of 0...1. An example of its usage is:

```
<stix:STIX_Header>
    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Watchlist</stix:Package_Intent>
</stix:STIX_Header>
```

#### Proposal
Change the multiplicity of this field (```Package_Intent```) from ```0...1``` to ```0...many```. This would allow for the STIX_Header element to effectively capture cases where a given STIX_Package has multiple intents. As an example, a package might contain both a description of TTP Infrastructure and the corresponding Indicators in a watchlist. That package could be represented in the package intent as:

```
<stix:STIX_Header>
    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Watchlist</stix:Package_Intent>
    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">TTP - Infrastructure</stix:Package_Intent>
</stix:STIX_Header>
```

Note the addition of the second ```Package_Intent``` element, which is not legal in STIX 1.0.1. The specific schema change is to add the @maxOccurs attribute to the definition for ```STIXHeaderType/Package_Intent``` and set it to "unbounded" (the default is 1):

**Old**
```
<xs:element name="Package_Intent" type="stixCommon:ControlledVocabularyStringType" minOccurs="0">
<!-- snip -->
</xs:element>
```

**New**
```
<xs:element name="Package_Intent" type="stixCommon:ControlledVocabularyStringType" minOccurs="0" maxOccurs="unbounded">
<!-- snip -->
</xs:element>
```

#### Impact
The drawback of this change is that, while it is technically backwards compatible at the schema level, the bindings and APIs will need to be updated to support lists of package intents and therefore this will require changes to existing code using package intent. API code that current sets the value of package intent will be required to set it to a list:

**Old:** ```header.package_intent = "IP Watchlist"```  
**New:** ```header.package_intent = ['IP Watchlist']```  

#### Requested Feedback

1. Should we make this change in STIX 1.1?
1. If not, should we consider it for STIX 2.0?

#### Resolution

This proposal was accepted for STIX 1.1 and will be implemented as described above.