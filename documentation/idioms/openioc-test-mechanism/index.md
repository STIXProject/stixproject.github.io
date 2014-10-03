---
layout: flat
title: OpenIOC Test Mechanism
constructs:
  - Indicator
  - TTP
summary: Represent how to detect an indicator using OpenIOC.
---

While one option when sharing indicator signatures is to use the `Observable` field in the indicator using CybOX, another option is to share indicators with signatures in a non-CybOX language via the `Test_Mechanisms` field. The advantage of this is that you can share signatures that work natively in existing tools but can still integrate with the rest of the STIX architecture.

This idiom describes using the OpenIOC test mechanism to share IOCs for the Zeus malware as used in the OpenIOC [example](http://openioc.org/iocs/6d2a1b03-b216-4cd8-9a9e-8827af6ebf93.ioc).

## Scenario

The hypothetical producer of this information could want to use OpenIOC because it's a popular language for sharing IOCs that work in existing tools. At the same time, it's helpful to have the rest of the STIX architecture available to relate the discovered IOCs to what they mean. In this scenario, IOCs that detect some variants of the Zeus malware family are provided along with the indicate that they detect that Zeus malware.

## Data Model

The information that the producer provides is simply the OpenIOC signature and the fact that it indicates Zeus malware. The [Malware Hash](../malware-hash/) idiom describes, we can use the [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType) and [TTP](/data-model/{{site.current_version}}/ttp/TTPType) components to describe this type of relationship. Unlike in that idiom however, in this case we'll provide the OpenIOC test mechanism in the indicator rather than a CybOX pattern.

Because OpenIOC is also an XML language, we're able to use XML schema features to ensure that both the STIX and the OpenIOC are valid. This is in contrast to the Snort and Yara test mechanisms, which merely embed those text rules and therefore their format cannot be validated during STIX validation. The other advantage of both languages being XML is that XML parsers are the only ones required to understand the full contents.

<img src="diagram.png" alt="OpenIOC Test Mechanism" />

## Implementation

Notice in both the production code and the consumption code that the OpenIOC itself is accessed via an lxml ElementTree. That way you can work with it as normal XML...though if you need to extract it in order to send it off to a tool that can process it you can always use the `tostring` method to do so.

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="openioc" %}{% highlight xml linenos %}
<stix:Indicator id="example:indicator-b92194e0-da61-4a32-9034-1148123b0f7a" timestamp="2014-06-20T20:53:08.440812+00:00" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1">
    <indicator:Title>Zeus</indicator:Title>
    <indicator:Description>Finds Zeus variants, twexts, sdra64, ntos</indicator:Description>
    <indicator:Indicated_TTP>
        <stixCommon:TTP idref="example:ttp-27884a06-e75c-4f35-b58d-f8cf2722f7d3" xsi:type='ttp:TTPType' version="1.1.1"/>
    </indicator:Indicated_TTP>
    <indicator:Test_Mechanisms>
        <indicator:Test_Mechanism id="example:testmechanism-c7f7dad4-4835-4105-8a53-72149f721ec0" xmlns:stix-openioc='http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1' xsi:type='stix-openioc:OpenIOC2010TestMechanismType'>
          <indicator:Producer>
            <!-- snip -->      
          </indicator:Producer>
          <stix-openioc:ioc xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.mandiant.com/2010/ioc" xmlns:stix-openioc="http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1" id="6d2a1b03-b216-4cd8-9a9e-8827af6ebf93" last-modified="2011-10-28T19:28:20">
              <short_description>Zeus</short_description>
              <description>Finds Zeus variants, twexts, sdra64, ntos</description>
              <keywords/>
              <authored_by>Mandiant</authored_by>
              <authored_date>0001-01-01T00:00:00</authored_date>
              <links/>
            <definition>
              <!-- snip - full IOC content would go here - snip -->
            </definition>
          </stix-openioc:ioc>
        </indicator:Test_Mechanism>
    </indicator:Test_Mechanisms>
</stix:Indicator>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
ioc = etree.parse('6d2a1b03-b216-4cd8-9a9e-8827af6ebf93.ioc.xml')

indicator = Indicator(title="Zeus", description="Finds Zeus variants, twexts, sdra64, ntos")

tm = OpenIOCTestMechanism()
tm.ioc = ioc
tm.producer = InformationSource(identity=Identity(name="Yara"))
time = Time()
time.produced_time = "0001-01-01T00:00:00"
tm.producer.time = time
tm.producer.references = ["http://openioc.org/iocs/6d2a1b03-b216-4cd8-9a9e-8827af6ebf93.ioc"]
indicator.test_mechanisms = [tm]
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_package = STIXPackage.from_xml('openioc-test-mechanism.xml')

ttps = {}
for ttp in stix_package.ttps.ttps:
    ttps[ttp.id_] = ttp

for indicator in stix_package.indicators:
    print "== INDICATOR =="
    print "Title: " + indicator.title
    print "Description: " + indicator.description.value

    for indicated_ttp in indicator.indicated_ttps:
        ttp = ttps[indicated_ttp.item.idref] # Resolve the TTP by idref
        print "Indicated TTP: " + ttp.title

    for tm in indicator.test_mechanisms:
        print "Producer: " + tm.producer.identity.name
        print "== IOC =="
        print etree.tostring(tm.ioc)
        print "== ENDIOC =="
{% endhighlight %}{% include end_tabs.html %}

[Full XML](openioc-test-mechanism.xml) | [Python Producer](openioc-test-mechanism-producer.py) | [Python Consumer](openioc-test-mechanism-consumer.py)

## Further Reading

* The [TTP idioms](../#ttp) describe other usage of [TTP](/data-model/{{site.current_version}}/ttp/TTPType), which may be helpful when giving OpenIOC indicators context.
* The [OpenIOC2010TestMechanism](/data-model/{{site.current_version}}/stix-openioc/OpenIOC2010TestMechanismType/) data model documentation has more information on other fields that are available.
* Other test mechanisms are [Snort](../snort-test-mechanism), [Yara](../yara-test-mechanism), and OVAL.
* The [OpenIOC homepage](http://openioc.org/) has more information and examples on OpenIOC
