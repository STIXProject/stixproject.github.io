---
layout: flat
title: Defining Campaigns vs Threat Actors
constructs:
  - Campaign
  - Threat Actor
  - TTP
summary:  Discussion and examples on when to use the term "Campaign" vs "Actor".
---

In STIX terminology, an individual or group involved in malicious cyber activity is called a `Threat Actor`.  A set of activity (`Incidents`) carried out by `Threat Actors` using specific techniques (`TTP`) for some particular purpose is called a `Campaign`. Such activity might fit along the lines of stealing financial information from banking customers or [targeting a particular business sector](../industry-sector). 

When data is collected on various related intrusion attempts (`Incidents`), it may not initially include enough information for characterizing attribution of the actor causing them. In this case, for cross-incident analysis of the "who" and "why", the preferred method is to begin by defining a `Campaign` for that activity with a placeholder `Threat Actor` identity until additional information comes to light. As more information evolves for characterizing the responsible actors the `Threat Actor` placeholder can be incrementally fleshed out.

As an example, if domains used in an intrusion are owned and registered by a single persona, the persona may be added to the `Threat Actor` placeholder but possibly given "Low" `Confidence` for attribution in relation to the incident.  If the persona is known through other means to be used by a professional intrusion team, the placeholder could be related to that larger group and the associated `Confidence` would likely go up.  Occasionally it is possible to fingerprint an actor by the customizations made in their tools (such as language choice or debug information), which would further flesh out characterization of the `Threat Actor` placeholder and increase `Confidence` in the actor being involved.

Once the `Threat Actor` placeholder reaches a level of characterization to be relevant outside the restricted context of its enclosing `Campaign` (this is largely a subjective decision) it can be split out into a separate entity and be replaced with a reference to it within the `Campaign`. This will allow that actor to be associated with other `Incident` or `TTP`.

When data is collected on various related activity including information characterizing those responsible or an actor is known but cannot be linked to existing activity, this can be defined directly as a `Threat Actor` with the `Identity` or other characterizing information filled out with things like their handles, location, known tools and network infrastructure. If those markers are observed in a new `Incident` or correlated with historical data, the `Actor` can be related according to its `Confidence` rating.

It is tempting to name a given `Campaign` or `Threat Actor` after the malware involved or to name a `Campaign` after the apparent group involved, however these methods are not very precise and prone to conflicts in naming between information sources. Imagine a situation where one organization declares that the "Netcat" malware had targeted their network, or the "Poison Ivy" actors were involved in a given intrusion.

Overall, a Campaign is some time-bounded set of activity that uses particular techniques against a set of targets, while a Threat Actor is the entity performing such behavior.

## Data model

We use the [CampaignType](/data-model/{{site.current_version}}/campaign/CampaignType) to render the campaign and [ThreatActorType](/data-model/{{site.current_version}}/campaign/ThreatActorType) for the actor.

In this case, a `Campaign` has an identified `ThreatActor` and constrained victim targeting. Since the actor was likely involved in other incidents, it may be related to other campaigns as well.

The example below shows a VERY simple initial `Campaign` defined to correlate a specific set of activity (three referenced `Incidents`) with a particular victim targeting profile believed to be carried out by the same unknown actor (characterized initially by a placeholder `Threat Actor` entry). 

## XML
{% highlight xml linenos %}
<stix:Campaign id="example:Campaign-e5268b6e-4931-42f1-b379-87f48eb41b1e" timestamp="2014-08-08T15:50:10.983728+00:00" xsi:type='campaign:CampaignType' version="1.1.1">
    <campaign:Title>Compromise of ATM Machines</campaign:Title>
    <campaign:Related_TTPs>
        <campaign:Related_TTP>
            <stixCommon:TTP id="example:ttp-2d1c6ab3-5e4e-48ac-a32b-f0c01c2836a8" timestamp="2014-08-08T15:50:10.983464+00:00" xsi:type='ttp:TTPType' version="1.1.1">
                <ttp:Title>Victim Targeting: Customer PII and Financial Data</ttp:Title>
                <ttp:Victim_Targeting>
                    <ttp:Targeted_Information xsi:type="stixVocabs:InformationTypeVocab-1.0">Information Assets - Financial Data</ttp:Targeted_Information>
                </ttp:Victim_Targeting>
            </stixCommon:TTP>
        </campaign:Related_TTP>
    </campaign:Related_TTPs>
    <campaign:Related_Incidents>
		<campaign:Related_Incident><stixCommon:Incident idref="example:incident-229ab6ba-0eb2-415b-bdf2-079e6b42f51e"/></campaign:Related_Incident>
		<campaign:Related_Incident><stixCommon:Incident idref="example:incident-517cf274-038d-4ed4-a3ec-3ac18ad9db8a"/></campaign:Related_Incident>
		<campaign:Related_Incident><stixCommon:Incident idref="example:incident-7d8cf96f-91cb-42d0-a1e0-bfa38ea08621"/></campaign:Related_Incident>
	</campaign:Related_Incidents>
    <campaign:Attribution>
		<campaign:Attributed_Threat_Actor>
			<stixCommon:Threat_Actor id="example:threatactor-56f3f0db-b5d5-431c-ae56-c18f02caf500" timestamp="2014-08-08T15:50:10.983629+00:00" xsi:type='ta:ThreatActorType' version="1.1.1">
            <ta:Title>People behind the intrusion</ta:Title>
        </stixCommon:Threat_Actor>
		</campaign:Attributed_Threat_Actor>
    </campaign:Attribution>
</stix:Campaign>
{% endhighlight %}


[Full XML](campaign-v-actors.xml)

## Python

{% highlight python linenos %}
#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

def main():
    from stix.campaign import Campaign, Attribution
    from stix.threat_actor import ThreatActor
    from stix.core import STIXPackage
    from stix.ttp import TTP, VictimTargeting

    ttp = TTP()
    ttp.title = "Victim Targeting: Customer PII and Financial Data"
    ttp.victim_targeting = VictimTargeting()
    ttp.victim_targeting.add_targeted_information("Information Assets - Financial Data")

    actor = ThreatActor()
    actor.title = "People behind the intrusion"

    c = Campaign()
    c.attribution.append(actor)
    c.title = "Compromise of ATM Machines"
    c.related_ttps.append(ttp)

    pkg = STIXPackage()
    pkg.add_campaign(c)

    print pkg.to_xml()

if __name__ == '__main__':
    main()
{% endhighlight %}

[Full Python](campaign-v-actors.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [CampaignType](/data-model/{{site.current_version}}/campaign/CampaignType)
* [TTPType](/data-model/{{site.current_version}}/ttp/TTPType)
* [VictimTargetingType](/data-model/{{site.current_version}}/ttp/VictimTargetingType)
