---
layout: flat
title: Incident Essentials - Who, What, When
constructs:
  - Incident
summary: Example of a basic incident
---

## Scenario

STIX can represent computer intrusions along with details on the victim, reporter, and timeline using the [Incident](/data-model/{{site.current_version}}/incident/IncidentType) construct. This example outlines a basic incident report - data in the wild may include or omit these fields and others.

Suppose a company named  "CyberTech Dynamics" had their network compromised in early 2012, discovered by security staff in May of the same year, later cleaned up and reported by security company "Sample Investigations, LLC".  Their investigation would have produced:

* Multiple timestamps, such as "when did the initial breach happen?" and "when did we clean it up?"
* An estimate of the cost to the victim, calculated based on the damage caused by information theft, outages, or other effects.
* Demographic information about the victim

## Data model

The [Incident](/data-model/{{site.current_version}}/incident/IncidentType) structure is used to describe this type of event. The minimum amount of data that is usually considered useful to describe an Incident is **who** was affected, **what** type of damage was sustained, and **when** it was detected (and later reported).

Note that in addition to confirmed incidents, many users of the STIX data model use the Incident construct to represent unconfirmed events and other analysis activities. As such, use of the incident construct it itself does not necessariliy mean that any particular legal or reporting barriers have been met.

**WHO:** The organization affected is listed as the `Victim` using [IdentityType](/data-model/{{site.current_version}}/stixCommon/IdentityType/). In this case just the name is used but you could also characterize more detailed information (addresses, organizational hierarchies, etc.) via the [CIQ extension](/data-model/{{site.current_version}}/stix-ciqidentity/CIQIdentity3.0InstanceType/). The person or organization who reported it is captured under `Reporter`. As with Victim, the Reporter field can use either a simple name or the CIQ extension.

**WHAT:** The `Impact_Assessment` field is used to convey a list of impacts that the incident caused using the [IncidentEffectVocab](/data-model/{{site.current_version}}/stixVocabs/IncidentEffectVocab-1.0/). In this case, a single effect is added corresponding to financial impact. Additionally, since the investigators were able to thoroughly validate the incident the `Confidence` field is set to "High". If the incident were unsubstantiated or in early stages of investigation, this value would instead be `Low`.

**WHEN:** Timestamps related to the incident itself are all represented in the `Time` field using [TimeType](data-model/{{site.current_version}}/incident/TimeType/). In this case, only the discovery time is known so the `Incident_Discovery` field is populated with that time. One gotcha with incident timestamps is that time fields related to the incident itself all go in `Time` while timestamps related to the STIX data construct go into `Information_Source/Time`. STIX uses a [rich model of time for incidents](/data-model/{{site.current_version}}/incident/TimeType) which allows an organization to represent the times that various events occurred during the course of the incident. 

To represent this (notional) breach, we first describe the breach as having been discovered internally, with the organization listed as the `Victim` and the internal team who reported it is captured under `Information Source`.

The time when the machine was infected is represented in the `Initial Compromise Time` field. The time they found the infected computer is the `Incident Discovery Time` and when they cleaned and rebuilt it is `Restoration Achieved Time`. Finally, `Incident Reported Time` is when the company disclosed the breach.

Note that timestamps describing the incident should be represented under `incident:Time`, as these are data directly related to the breach in question. `Information_Source/Time` also allows you to represent timestamps, but rather than data about the incident they represent metadata about the incident report. For example, `Information_Source/Time/Produced_Time` represents the time the incident record was produced. Similarly, the `@timestamp` field is used to version the construct and should not be used to represent any time related to the incident itself.


## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="simple-incident" %}{% highlight xml linenos  %}
<stix:STIX_Package >
    <stix:STIX_Header>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Incident</stix:Package_Intent>
        <stix:Description>Sample breach report</stix:Description>
    </stix:STIX_Header>
    <stix:Incidents>
        <stix:Incident id="example:incident-8236b4a2-abe0-4b56-9347-288005c4bb92" timestamp="2014-11-18T23:40:08.061362+00:00" xsi:type='incident:IncidentType' version="1.1.1">
            <incident:Title>Breach of Cyber Tech Dynamics</incident:Title>
            <incident:Time>
                <incident:Initial_Compromise precision="second">2012-01-30T00:00:00</incident:Initial_Compromise>
                <incident:Incident_Discovery precision="second">2012-05-10T00:00:00</incident:Incident_Discovery>
                <incident:Restoration_Achieved precision="second">2012-08-10T00:00:00</incident:Restoration_Achieved>
                <incident:Incident_Reported precision="second">2012-12-10T00:00:00</incident:Incident_Reported>
            </incident:Time>
            <incident:Description>Intrusion into enterprise network</incident:Description>
            <incident:Reporter>
                <stixCommon:Description>The person who reported it</stixCommon:Description>
                <stixCommon:Identity id="example:Identity-cd64aaa6-b1c0-4026-8ea1-14ff5a19e5fb">
                    <stixCommon:Name>Sample Investigations, LLC</stixCommon:Name>
                </stixCommon:Identity>
                <stixCommon:Time>
                    <cyboxCommon:Produced_Time>2014-03-11T00:00:00</cyboxCommon:Produced_Time>
                </stixCommon:Time>
            </incident:Reporter>
            <incident:Victim id="example:Identity-dd8637b7-51b4-48f0-9e3c-a2b23b3a2dd7">
                <stixCommon:Name>Cyber Tech Dynamics</stixCommon:Name>
            </incident:Victim>
            <incident:Impact_Assessment>
                <incident:Effects>
                    <incident:Effect xsi:type="stixVocabs:IncidentEffectVocab-1.0">Financial Loss</incident:Effect>
                </incident:Effects>
            </incident:Impact_Assessment>
            <incident:Confidence timestamp="2014-11-18T23:40:08.061379+00:00">
                <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
            </incident:Confidence>
        </stix:Incident>
    </stix:Incidents>
</stix:STIX_Package>

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
# setup stix document
stix_package = STIXPackage()
stix_header = STIXHeader()

stix_header.description = "Sample breach report" 
stix_header.add_package_intent ("Incident")

stix_package.stix_header = stix_header

# add incident and confidence
breach = Incident()
breach.description = "Intrusion into enterprise network"
breach.confidence = "High"

# stamp with reporter
breach.reporter = InformationSource()
breach.reporter.description = "The person who reported it"

breach.reporter.time = Time()
breach.reporter.time.produced_time = datetime.strptime("2014-03-11","%Y-%m-%d") # when they submitted it

breach.reporter.identity = Identity()
breach.reporter.identity.name = "Sample Investigations, LLC"

# set incident-specific timestamps
breach.time = incidentTime()
breach.title = "Breach of CyberTech Dynamics"
breach.time.initial_compromise = datetime.strptime("2012-01-30", "%Y-%m-%d") 
breach.time.incident_discovery = datetime.strptime("2012-05-10", "%Y-%m-%d") 
breach.time.restoration_achieved = datetime.strptime("2012-08-10", "%Y-%m-%d") 
breach.time.incident_reported = datetime.strptime("2012-12-10", "%Y-%m-%d") 

# add the impact
impact = ImpactAssessment()
impact.add_effect("Unintended Access")
breach.impact_assessment = impact

# add the victim
breach.add_victim ("CyberTech Dynamics")

# add the impact
impact = ImpactAssessment()
impact.add_effect("Financial Loss")
breach.impact_assessment = impact

stix_package.add_incident(breach)

print stix_package

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
print "== INCIDENT =="
print "Package: " + str(pkg.stix_header.description)
for inc in pkg.incidents:
    print "---"
    print "Reporter: " + inc.reporter.identity.name
    print "Title: "+ inc.title
    print "Description: "+ str(inc.description)
    print "Confidence: "+ str(inc.confidence.value)
    for impact in inc.impact_assessment.effects:
        print "Impact: "+ str(impact)
    
    print "Initial Compromise: "+ str(inc.time.initial_compromise.value)
    print "Incident Discovery: "+ str(inc.time.incident_discovery.value)
    print "Restoration Achieved: "+ str(inc.time.restoration_achieved.value)
    print "Incident Reported: "+ str(inc.time.incident_reported.value)

    for victim in inc.victims:
        print "Victim: "+ str(victim.name)
{% endhighlight %}{% include end_tabs.html %}

[Full XML](sample.xml) | [Python Producer](simple-incident_producer.py) | [Python Consumer](simple-incident_consumer.py) 

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
