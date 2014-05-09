**Status**: Accepted  
**Comment Period Closes**: 12/6/2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/25

#### Background Information
The STIX Indicator component has a mechanism for capturing sightings of that indicator using ```SightingType```. In STIX 1.0.1, ```SightingType``` allows you to capture:
* A timestamp indicating when the sighting was observed
* A Source, indicating the information source of the sighting
* A Confidence, indicating confidence in the sighting
* A Reference, indicating a formal reference to the sighting

#### Proposal
This proposal suggests adding a field to ```SightingType``` to capture the actual observable instances that were observed. For example, if the indicator pattern is for IP addresses matching ```192.168.x.x``` the related sighting might indicate that it saw the specific IP address ```192.168.123.123```. Note that the object type in the sighting might also be different from the object type in the indicator: in response to the above indicator, a sighting might reference instead actual netflow data or connection information rather than just the IP.

> This proposal does not suggest any mechanisms for indicating which sightings types are expected in an indicator. It simply adds a field allowing any type of observable that was captured as a sighting to be represented for any type of indicator. That capability is not in-scope for STIX 1.1 and is tracked in [issue #72](https://github.com/STIXProject/schemas/issues/72).

As an example of this capability:
```
<stix:Indicator xsi:type="indicator:IndicatorType" id="example-1">
    <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.0">Domain Watchlist</indicator:Type>
    <indicator:Description>Sample domain Indicator for this watchlist</indicator:Description>
    <indicator:Observable id="example-2">
        <cybox:Object id="example-3">
            <cybox:Properties xsi:type="URIObject:URIObjectType">
                <URIObject:Value condition="Equals" apply_condition="ANY">malicious1.example.com##comma##malicious2.example.com##comma##malicious3.example.com</URIObject:Value>
            </cybox:Properties>
        </cybox:Object>
    </indicator:Observable>
    <indicator:Sightings>
        <indicator:Sighting timestamp="2012-11-28T11:35:15Z">
            <indicator:Source>Acme</indicator:Source>
            <indicator:Related_Observable>
                <cybox:Object id="example-4">
                    <cybox:Properties xsi:type="URIObject:URIObjectType">
                       <URIObject:Value>malicious1.example.com</URIObject:Value>
                    </cybox:Properties>
                </cybox:Object>
            </indicator:Related_Observable>
        </indicator:Sighting>
    </indicator:Sightings>
</stix:Indicator>
```

#### Impact
There is no expected compatibility impact. Producers will have the option to use this new field and consumers can choose to handle or not handle them as with any other field in STIX.

#### Requested Feedback

1. Should this capability be added to STIX?
1. Is the manner in which the proposal suggests adding it correct?