---
layout: flat
title: Indicator for C2 IP Address
use_cases:
  - Command and Control
constructs:
  - Indicator
  - TTP
summary: This idiom walks through the very common use case where you have an indicator where the "test" is a simple IP address and the context is that the IP is being used to host a C2 server. This is often implemented via a network block to that IP address as the external firewall.
---

One of the most common forms of [indicator](../#indicator) seen describes a pattern for TCP traffic beaconing to a specific command and control (C2, C&C) server. This idiom describes creating such an indicator in STIX.

## Scenario

This scenario consists of the description of a simple indicator that represents a test for a single IP address and the context that if that IP address is seen it means that there might be C2 traffic. Unlike many real-world use cases, it does not state that the C2 channel is for any particular piece of malware and does not give much context beyond simply that it's C2 Behavior.

## Data model

As with all indicators, the data model consists of two primary components: the "test" portion describing some pattern of cyber observables to look for, and the "context" portion describing what it means if that observable is actually sighted.

In this case, the "test" portion will be a simple cyber observable for an IP address. The "context" portion will be a TTP indicating that it represents malware beaconing.

![IP Address Indicator Diagram](diagram.png)

In the diagram above, the Indicator component contains the test: a CybOX [Address Object](/data-model/{{site.current_version}}/AddressObj/AddressObjectType/) with an `Address Value` of the IP to check for (10.0.0.0). The `Indicated TTP` then uses a [STIX Relationship](/documentation/concepts/relationships) to link to a TTP that gives context as to why the test is relevant. In this case, that context is that the indicator indicates "C2 Behavior". Note that, besides the TTP, the indicator `Type` field is also used to give the indicator some context.

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

[Full XML](indicator-for-c2-ip-address.xml)

## Python

{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP
from cybox.core import Observable
from cybox.objects.address_object import Address

stix_package = STIXPackage()
ttp = TTP(title="C2 Behavior")
   
indicator = Indicator(title="IP Address for known C2 Channel")
indicator.add_indicator_type("IP Watchlist")
  
addr = Address(address_value="10.0.0.0", category=Address.CAT_IPV4)
indicator.add_observable(addr)
indicator.add_indicated_ttp(TTP(idref=ttp.id_))
    
stix_package.add_indicator(indicator)
stix_package.add_ttp(ttp)
    
print stix_package.to_xml()
{% endhighlight %}

[Full Python](indicator-for-c2-ip-address.py)

## Further Reading

* [Indicator Type](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [CybOX Address Object](/data-model/{{site.current_version}}/AddressObj/AddressObjectType)
