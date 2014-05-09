**Status**: Accepted  
**Comment Period Closes**: November 22, 2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/58

#### Background Information
This proposal concerns the Type field of the STIX Indicator component. In STIX 1.0.1, this construct has a multiplicity of 0...1. An example of its usage is:

```
<indicator:Indicator xsi:type="indicator:IndicatorType" id="example-1">
  <indicator:Type xsi:type="vocabs:IndicatorTypeVocab-1.0">IP Watchlist</indicator:Type>
  <!-- snip -->
</indicator:Indicator>
```

#### Proposal
Change the multiplicity of the Type field on Indicator from ```0...1``` to ```0...many```. This would allow indicators to have multiple types, a feature that has been requested by the community. An example of an indicator with multiple types could be an indicator for IP addresses in a C2 network:

```
<indicator:Indicator xsi:type="indicator:IndicatorType" id="example-1">
  <indicator:Type xsi:type="vocabs:IndicatorTypeVocab-1.0">IP Watchlist</indicator:Type>
  <indicator:Type xsi:type="vocabs:IndicatorTypeVocab-1.0">C2</indicator:Type>
  <!-- snip -->
</indicator:Indicator>
```

Note the addition of the additional ```Type``` element, which would not have been legal in STIX 1.0.1. The specific schema change is to add the @maxOccurs attribute to the definition for IndicatorType/Type and set it to "unbounded" (the default is 1):

**Old**
```
<xs:element name="Type" type="stixCommon:ControlledVocabularyStringType" minOccurs="0">
<!-- snip -->
</xs:element>
```

**New**
```
<xs:element name="Type" type="stixCommon:ControlledVocabularyStringType" minOccurs="0" maxOccurs="unbounded">
<!-- snip -->
</xs:element>
```

#### Impact
The drawback of this change is that, while it is technically backwards compatible at the schema level, the bindings and APIs will need to be updated to support lists of indicator types and therefore this will require changes to existing code using indicator types. API code that current sets the value of indicator type will be required to set it to a list:

**Old:** ```indicator.type = "IP Watchlist"```  
**New:** ```indicator.type = ['IP Watchlist']```  

#### Requested Feedback

1. Should we make this change in STIX 1.1?
1. If not, should we consider it for STIX 2.0?

#### Resolution

This proposal was accepted for STIX 1.1 and will be implemented as described above.