---
layout: flat
title: Barebones Incident Description
constructs:
  - Incident
summary: "Just the facts, ma'am"
---


## Scenario

In this example we will cover the basic information needed to capture a computer intrusion incident using STIX.

Imagine that in early 2012 a company named "Canary Corp" had their network compromised and reported that information as a financial loss in SEC filings. The breach was disclosed by "Sample Investigations, LLC" and included substantial details with third-party verification.

## Data model

Historical incidents (breaches) are describing using the [Incident](/data-model/{{site.current_version}}/incident/IncidentType) structure. The bare minimum to describe an Incident is **who** was affected, **what** type of damage was sustained, and **when** it was detected (and later reported).

**WHO:** The organization affected (Canary Corp) is listed as the `Victim` using [IdentityType](/data-model/{{site.current_version}}/stixCommon/IdentityType/). In this case just the name is used but you could also characterize more detailed information (addresses, organizational hierarchies, etc.) via the [CIQ extension](/data-model/{{site.current_version}}/stix-ciqidentity/CIQIdentity3.0InstanceType/). The person or organization who reported it is captured under `Reporter`. As with Victim, the Reporter field can use either a simple name or the CIQ extension.

**WHAT:** The `Impact_Assessment` field is used to convey a list of impacts that the incident caused using the [IncidentEffectVocab](/data-model/{{site.current_version}}/stixVocabs/IncidentEffectVocab-1.0/). In this case, a single effect is added corresponding to financial impact. Additionally, since the investigators were able to thoroughly validate the incident the `Confidence` field is set to "High". If the incident were unsubstantiated or in early stages of investigation, this value would instead be `Low`.

**WHEN:** Timestamps related to the incident itself are all represented in the `Time` field using [TimeType](data-model/{{site.current_version}/incident/TimeType/). In this case, only the discovery time is known so the `Incident_Discovery` field is populated with that time. One gotcha with incident timestamps is that time fields related to the incident itself all go in `Time` while timestamps related to the STIX data construct go into `Information_Source/Time`.

## XML

{% highlight xml linenos  %}
<stix:STIX_Package 
	xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
	xmlns:example="http://example.com"
	xmlns:incident="http://stix.mitre.org/Incident-1"
	xmlns:stixCommon="http://stix.mitre.org/common-1"
	xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
	xmlns:stix="http://stix.mitre.org/stix-1"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="
	http://cybox.mitre.org/common-2 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd
	http://stix.mitre.org/Incident-1 http://stix.mitre.org/XMLSchema/incident/1.1.1/incident.xsd
	http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
	http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
	http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd" id="example:Package-fba447a0-7c5b-4329-98a3-1324080101d4" version="1.1.1" timestamp="2014-08-28T16:42:52.859307+00:00">
    <stix:STIX_Header>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Incident</stix:Package_Intent>
        <stix:Description>Sample breach report</stix:Description>
    </stix:STIX_Header>
    <stix:Incidents>
        <stix:Incident id="example:incident-fd56fb34-af59-47b3-95cf-7baaaa53fe93" timestamp="2014-08-28T16:42:52.859547+00:00" xsi:type='incident:IncidentType' version="1.1.1">
            <incident:Title>Breach of Canary Corp</incident:Title>
            <incident:Time>
                <incident:Incident_Discovery precision="second">2013-01-13T00:00:00</incident:Incident_Discovery>
            </incident:Time>
            <incident:Description>Intrusion into enterprise network</incident:Description>
            <incident:Reporter>
                <stixCommon:Description>The person who reported it</stixCommon:Description>
                <stixCommon:Identity id="example:Identity-5db269cf-e603-4df9-ae8c-51ff295abfaa">
                    <stixCommon:Name>Sample Investigations, LLC</stixCommon:Name>
                </stixCommon:Identity>
                <stixCommon:Time>
                    <cyboxCommon:Produced_Time>2014-03-11T00:00:00</cyboxCommon:Produced_Time>
                </stixCommon:Time>
            </incident:Reporter>
            <incident:Victim id="example:Identity-c85082f3-bc04-43c8-a000-e0c1d0f2c045">
                <stixCommon:Name>Canary Corp</stixCommon:Name>
            </incident:Victim>
            <incident:Impact_Assessment>
                <incident:Effects>
                    <incident:Effect xsi:type="stixVocabs:IncidentEffectVocab-1.0">Financial Loss</incident:Effect>
                </incident:Effects>
            </incident:Impact_Assessment>
            <incident:Confidence timestamp="2014-08-28T16:42:52.859570+00:00">
                <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
            </incident:Confidence>
        </stix:Incident>
    </stix:Incidents>
</stix:STIX_Package>


{% endhighlight %}

[Full XML](sample.xml)

## Python

{% highlight python linenos %}
#!/usr/bin/env python

from stix.core import STIXPackage, STIXHeader
from datetime import datetime
from cybox.common import Time

from stix.incident import Incident,ImpactAssessment, AffectedAsset
from stix.incident import Time as incidentTime # different type than common:Time

from stix.common import InformationSource
from stix.common import Confidence
from stix.common import Identity

from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.simple_marking import SimpleMarkingStructure

def build_stix( ):
    # setup stix document
    stix_package = STIXPackage()
    stix_header = STIXHeader()

    stix_header.description = "Sample breach report" 
    stix_header.add_package_intent ("Incident")

    # stamp with creator
    stix_header.information_source = InformationSource()
    stix_header.information_source.description = "The person who reported it"

    stix_header.information_source.time = Time()
    stix_header.information_source.time.produced_time = datetime.strptime("2014-03-11","%Y-%m-%d") # when they submitted it

    stix_header.information_source.identity = Identity()
    stix_header.information_source.identity.name = "Sample Investigations, LLC"

    stix_package.stix_header = stix_header

    # add incident and confidence
    breach = Incident()
    breach.description = "Intrusion into enterprise network"
    breach.confidence = "High"

    # incident time is a complex object with support for a bunch of different "when stuff happened" items
    breach.time = incidentTime()
    breach.title = "Breach of Canary Corp"
    breach.time.incident_discovery = datetime.strptime("2013-01-13", "%Y-%m-%d") # when they submitted it

    # add the impact
    impact = ImpactAssessment()
    impact.add_effect("Financial Loss")
    breach.impact_assessment = impact

    # add the victim
    breach.add_victim ("Canary Corp")

    stix_package.add_incident(breach)

    return stix_package

if __name__ == '__main__':
    # emit STIX
    pkg = build_stix()
    print pkg.to_xml() 
{% endhighlight %}

[Full Python](sample.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
