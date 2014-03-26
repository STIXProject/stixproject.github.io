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

{% endhighlight %}

## Python

{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.tlp import TLPMarkingStructure

alpha_package = STIXPackage()
alpha_package.stix_header = STIXHeader()
alpha_package.stix_header.title = "Report on Adversary Alpha"
alpha_package.stix_header.handling = Marking()

alpha_marking = MarkingSpecification()
alpha_marking.controlled_structure = "../../../../node()"
alpha_tlp_marking = TLPMarkingStructure()
alpha_tlp_marking.color = "AMBER"
alpha_marking.marking_structure.append(alpha_tlp_marking)
alpha_package.stix_header.handling.add_marking(alpha_marking)

bravo_package = STIXPackage()
bravo_package.stix_header = STIXHeader()
bravo_package.stix_header.title = "Report on Adversary Bravo"
bravo_package.stix_header.handling = Marking()

bravo_marking = MarkingSpecification()
bravo_marking.controlled_structure = "../../../../node()"
bravo_tlp_marking = TLPMarkingStructure()
bravo_tlp_marking.color = "RED"
alpha_marking.marking_structure.append(bravo_tlp_marking)
bravo_package.stix_header.handling.add_marking(bravo_marking)
    
stix_package = STIXPackage()
stix_package.related_packages.append(alpha_package)
stix_package.related_packages.append(bravo_package)

print stix_package.to_xml()
{% endhighlight %}

[Full Python](plain-wrapper-around-multiple-packages.py)

## Further Reading

* [STIX Package](/documentation/stix/STIXType)