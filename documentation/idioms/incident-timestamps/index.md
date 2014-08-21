---
layout: flat
title: Life and Times of an Incident
constructs:
  - Incident
summary: STIX supports a rich set of timestamps for incidents, learn about them here.
---


## Scenario

An incident will often include several timestamps in the course of investigation, such as "when did the initial breach happen?" and "when did we finally clean it up?"

Take for instance an intrusion into "Cyber Tech Dynamics", comprising a malicious webpage which infected an endpoint in January of 2012, discovered by security staff in May of the same year, later cleaned up and reported to law enforcement by end of year.  

## Data model

STIX uses a [rich model of time for incidents](/data-model/{{site.current_version}}/incident/TimeType) which allows an organization to represent the times that various events occurred during the course of the incident. 

To represent this (notional) breach, we first describe the breach as having been discovered internally, with the organization listed as the `Victim` and the internal team who reported it is captured under `Information Source`.

The time when the machine was infected is represented in the `Initial Compromise Time` field. The time they found the infected computer is the `Incident Discovery Time` and when they cleaned and rebuilt it is `Restoration Achieved Time`. Finally, `Incident Reported Time` is when the company disclosed the breach.

Note that timestamps describing the incident should be represented under `incident:Time`, as these are data directly related to the breach in question. `Information_Source/Time` also allows you to represent timestamps, but rather than data about the incident they represent metadata about the incident report. For example, `Information_Source/Time/Produced_Time` represents the time the incident record was produced. Similarly, the `@timestamp` field is used to version the construct and should not be used to represent any time related to the incident itself.

{% highlight xml linenos %}
<stix:STIX_Package 
	xmlns:example="http://example.com"
	xmlns:incident="http://stix.mitre.org/Incident-1"
	xmlns:stixCommon="http://stix.mitre.org/common-1"
	xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
	xmlns:stix="http://stix.mitre.org/stix-1"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="
	http://stix.mitre.org/Incident-1 http://stix.mitre.org/XMLSchema/incident/1.1.1/incident.xsd
	http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
	http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
	http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd" id="example:Package-069c859b-b9ab-48b5-ab24-e026f8dfb499" version="1.1.1" timestamp="2014-08-18T20:27:39.238685+00:00">
    <stix:STIX_Header>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Incident</stix:Package_Intent>
        <stix:Description>Sample breach report</stix:Description>
        <stix:Information_Source>
            <stixCommon:Description>The person who reported it</stixCommon:Description>
            <stixCommon:Identity id="example:Identity-41df7111-0a2d-4b7f-9cb4-5c04fdfe5697">
                <stixCommon:Name>Infosec Operations Team</stixCommon:Name>
            </stixCommon:Identity>
        </stix:Information_Source>
    </stix:STIX_Header>
    <stix:Incidents>
        <stix:Incident id="example:incident-b967f419-6452-42ae-8c92-87b0706752c5" timestamp="2014-08-18T20:27:39.239048+00:00" xsi:type='incident:IncidentType' version="1.1.1">
            <incident:Title>Breach of Cyber Tech Dynamics</incident:Title>
            <incident:Time>
                <incident:Initial_Compromise precision="second">2012-01-30T00:00:00</incident:Initial_Compromise>
                <incident:Incident_Discovery precision="second">2012-05-10T00:00:00</incident:Incident_Discovery>
                <incident:Restoration_Achieved precision="second">2012-08-10T00:00:00</incident:Restoration_Achieved>
                <incident:Incident_Reported precision="second">2012-12-10T00:00:00</incident:Incident_Reported>
            </incident:Time>
            <incident:Description>Intrusion into enterprise network</incident:Description>
            <incident:Victim id="example:Identity-8f644c2f-0057-442d-b2ef-b4782c253e04">
                <stixCommon:Name>Cyber Tech Dynamics</stixCommon:Name>
            </incident:Victim>
            <incident:Impact_Assessment>
                <incident:Effects>
                    <incident:Effect xsi:type="stixVocabs:IncidentEffectVocab-1.0">Unintended Access</incident:Effect>
                </incident:Effects>
            </incident:Impact_Assessment>
            <incident:Confidence timestamp="2014-08-18T20:27:39.239072+00:00">
                <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
            </incident:Confidence>
        </stix:Incident>
    </stix:Incidents>
</stix:STIX_Package>


{% endhighlight %}

[Full XML](sample.xml)

## Python

Note that `IncidentTime` is distinct from the builtin `Time` type in the following code:
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from datetime import datetime
from cybox.common import Time

from stix.incident import Incident,ImpactAssessment, AffectedAsset
from stix.incident import Time as incidentTime # different type than common:Time

from stix.common import InformationSource
from stix.common import Confidence
from stix.common import Identity


# setup stix document
stix_package = STIXPackage()
stix_header = STIXHeader()

stix_header.description = "Sample breach report" 
stix_header.add_package_intent ("Incident")

# stamp with creator
stix_header.information_source = InformationSource()
stix_header.information_source.description = "The person who reported it"

stix_header.information_source.identity = Identity()
stix_header.information_source.identity.name = "Infosec Operations Team"

stix_package.stix_header = stix_header

# add incident and confidence
breach = Incident()
breach.description = "Intrusion into enterprise network"
breach.confidence = "High"

# set incident-specific timestamps
breach.time = incidentTime()
breach.title = "Breach of Cyber Tech Dynamics"
breach.time.initial_compromise = datetime.strptime("2012-01-30", "%Y-%m-%d") 
breach.time.incident_discovery = datetime.strptime("2012-05-10", "%Y-%m-%d") 
breach.time.restoration_achieved = datetime.strptime("2012-08-10", "%Y-%m-%d") 
breach.time.incident_reported = datetime.strptime("2012-12-10", "%Y-%m-%d") 

# add the impact
impact = ImpactAssessment()
impact.add_effect("Unintended Access")
breach.impact_assessment = impact

# add the victim
breach.add_victim ("Cyber Tech Dynamics")

stix_package.add_incident(breach)

print pkg.to_xml() 
{% endhighlight %}

[Full Python](sample.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
