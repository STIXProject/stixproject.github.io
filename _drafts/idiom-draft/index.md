---
layout: idiom
title: C2 Indicator
---

One of the most common forms of [indicator](/idioms/indicator) seen describes a pattern for TCP traffic beaconing to a specific command and control (C2, C&C) server. This idiom describes creating such an indicator in STIX.

## Scenario

This scenario consists of the description of a simple indicator that represents a test for a single IP address and the context that if that IP address is seen it means that there might be C2 traffic.

## Data model

As with all indicators, the data model consists of two primary components: the "test" portion describing some pattern of cyber observables to look for, and the "context" portion describing what it means if that observable is actually sighted.

In this case, the "test" portion will be a simple cyber observable for an IP address. The "context" portion will be a TTP indicating that it represents malware beaconing.

![IP Address Indicator Diagram](diagram.png)

In the diagram above, the Indicator component contains the test: a CybOX [Address Object](/documentation/AddressObj/AddressObjectType/) with an `Address Value` of the IP to check for (10.0.0.0). The `Indicated TTP` then uses a [STIX Relationship](idioms/relationships) to link to a TTP that describes the indicator. Note that, besides the TTP, the indicator `Type` field is also used to give the indicator some context.

## XML

{% highlight xml linenos %}
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-33fe3b22-0201-47cf-85d0-97c02164528d" timestamp="2014-02-20T09:00:00.000000Z">
    <indicator:Title>IP Address for known C2 channel</indicator:Title>
    <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
    <indicator:Observable  id="example:Observable-1c798262-a4cd-434d-a958-884d6980c459">
        <cybox:Object id="example:Object-1980ce43-8e03-490b-863a-ea404d12242e">
            <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
                <AddressObject:Address_Value condition="Equals">10.0.0.0</AddressObject:Address_Value>
            </cybox:Properties>
        </cybox:Object>
    </indicator:Observable>
    <indicator:Indicated_TTP>
        <stixCommon:TTP idref="example:TTP-bc66360d-a7d1-4d8c-ad1a-ea3a13d62da9" />
    </indicator:Indicated_TTP>
</stix:Indicator>
<!-- SNIP -->
<stix:TTP xsi:type="ttp:TTPType" id="example:TTP-bc66360d-a7d1-4d8c-ad1a-ea3a13d62da9" timestamp="2014-02-20T09:00:00.000000Z">
    <ttp:Title>C2 Behavior</ttp:Title>
</stix:TTP>
{% endhighlight %}

[Full XML](ip-indicator.xml)

## Further Reading

* [Indicator Type](/documentation/indicator/IndicatorType)
* [CybOX Address Object](/documentation/AddressObj/AddressObjectType)