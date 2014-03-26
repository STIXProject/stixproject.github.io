---
layout: idiom
title: Plain Wrapper Around Multiple Reports
---

Although not always considered as important as the content itself, the packaging of cyber threat intelligence can often be very important. A basic title, intent, and description of the data is of course important, but other metadata can include data handling instructions, information about the source of the data, and information about how the data was generated. This idiom describes representing a bundle of several unrelated reports as a single document.

## Scenario

In this scenario, two unrelated threat reports are distributed in a single document at the same time. This was considered easier from an operational perspective than just distributing them separately, but other than that they are not related at all.

## Data model

<img src="diagram.png" alt="Wrapper around packages" class="aside-text" />

The data model for this scenario is very simple, but leverages several some new features in STIX 1.1 that might be unknown to many people.

The outer package wrapper is, as usual, given the suggested ID value (though it isn't in the diagram, it's also given a timestamp) but other than that does not contain any metadata. Instead, the `Related Package` field is used to embed two full [STIX Package](/documentation/stix/STIXType) constructs inside it. Thus, the entire data model consists of the the wrapper package containing almost no information and the two included reports that independently convey all necessary information.

For example, the first report is marked TLP:AMBER while the second is marked TLP:RED.

## XML

{% highlight xml linenos %}
<stix:Related_Packages>
    <stix:Related_Package>
        <stix:Package id="example:package-ca6e215c-fbb7-4b7a-b678-632562f85e93" timestamp="2014-02-20T09:00:00.000000Z" version="1.1">
            <stix:STIX_Header>
                <stix:Title>Report on Adversary Alpha</stix:Title>
                <stix:Handling>
                    <markings:Marking>
                        <markings:Controlled_Structure>../../../../node()</markings:Controlled_Structure>
                        <markings:Marking_Structure xsi:type="tlpMarking:TLPMarkingStructureType" color="AMBER"/>
                    </markings:Marking>
                 </stix:Handling>
            </stix:STIX_Header>                
        </stix:Package>
    </stix:Related_Package>
    <stix:Related_Package>
        <stix:Package id="example:package-162faaf6-4fa8-47d8-b128-115b392bbb19" timestamp="2014-03-26T02:01:00.000000Z" version="1.1">
            <stix:STIX_Header>
                <stix:Title>Report on Adversary Bravo</stix:Title>
                <stix:Handling>
                    <markings:Marking>
                        <markings:Controlled_Structure>../../../../node()</markings:Controlled_Structure>
                        <markings:Marking_Structure xsi:type="tlpMarking:TLPMarkingStructureType" color="RED"/>
                    </markings:Marking>
                </stix:Handling>
            </stix:STIX_Header>
        </stix:Package>
    </stix:Related_Package>
</stix:Related_Packages>
{% endhighlight %}

[Full XML](multiple-packages.xml) 

## Further Reading

* [STIX Package](/documentation/stix/STIXType)