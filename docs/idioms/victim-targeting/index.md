---
layout: flat
title: Victim Targeting for a Campaign
use_cases:
  - Victim Targeting
constructs:
  - Campaign
  - TTP
summary:  A cyber campaign may be defined based on the fact that it targets a consistent set of victims, as defined by their nationality or industry sector (as an example). This idiom demonstrates how to express that in STIX, accomplished through the use of a related TTP.
---

<img src="/images/Victim Targeting.png" class="component-img" alt="Victim Targeting Icon" />

One common method by which cyber threat campaigns are defined and tracked is based on the types of victims they target, whether victims are defined by the victim themselves (where they are located, the types of work they do), or by the fact that they have certain types of information or systems (customer PII, Industrial Control Systems, etc), or by the fact that they target specific technical configurations (a certain browser or OS for example).

This idiom describes the representation of a cyber threat campaign characterized by the fact that it targets customer PII and financial information.

## Data model

<img src="diagram.png" alt="Campaign victim targeting" class="aside-text" />

There are two main pieces of information that need to be communicated in this idiom: the campaign construct itself (using [CampaignType](/data-model/{{site.current_version}}/campaign/CampaignType)) and the victim targeting (using [VictimTargetingType](/data-model/{{site.current_version}}/ttp/VictimTargetingType)) in TTP. These are related together using the Campaign=>Related_TTP relationship.

The campaign is represented with just a title and a related TTP with a relationship name of "Targets". The TTP leverages the victim targeting constructs to represent the types of information that are targeted. For targeting of a specific type of information, the `Targeted Information` field is used, leveraging the controlled vocabulary for information types, [InformationTypeVocab-1.0](/data-model/{{site.current_version}}/stixVocabs/InformationTypeVocab-1.0/).

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="victim-targeting" %}{% highlight xml linenos %}
<stix:TTPs>
    <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-4fde045a-b25f-f035-e8d0-29c9d5130cd9" timestamp="2014-02-20T09:00:00.000000Z">
        <ttp:Title>Victim Targeting: Customer PII and Financial Data</ttp:Title>
        <ttp:Victim_Targeting xsi:type="ttp:VictimTargetingType">
            <ttp:Targeted_Information xsi:type="stixVocabs:InformationTypeVocab-1.0">Information Assets - Customer PII</ttp:Targeted_Information>
            <ttp:Targeted_Information xsi:type="stixVocabs:InformationTypeVocab-1.0">Information Assets - Financial Data</ttp:Targeted_Information>
        </ttp:Victim_Targeting>
    </stix:TTP>
</stix:TTPs>
<stix:Campaigns>
    <stix:Campaign xsi:type="campaign:CampaignType" id="example:campaign-c831ab93-ff84-9cda-2bd8-b094004da969" timestamp="2014-02-20T09:00:00.000000Z">
        <campaign:Title>Operation Alpha</campaign:Title> 
        <campaign:Related_TTPs>
            <campaign:Related_TTP>
                <stixCommon:Relationship>Targets</stixCommon:Relationship>
                <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-4fde045a-b25f-f035-e8d0-29c9d5130cd9"/>    
            </campaign:Related_TTP>
        </campaign:Related_TTPs>
    </stix:Campaign>
</stix:Campaigns>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

ttp = TTP()
ttp.title = "Victim Targeting: Customer PII and Financial Data"
ttp.victim_targeting = VictimTargeting()
ttp.victim_targeting.add_targeted_information("Information Assets - Customer PII")
ttp.victim_targeting.add_targeted_information("Information Assets - Financial Data")

ttp_ref = TTP()
ttp_ref.idref = ttp.id_
related_ttp = RelatedTTP(ttp_ref)
related_ttp.relationship = "Targets"

c = Campaign()
c.title = "Operation Alpha"
c.related_ttps.append(related_ttp)

pkg = STIXPackage()
pkg.add_campaign(c)
pkg.add_ttp(ttp)

print pkg.to_xml()

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

print "== Campaign =="
for camp in pkg.campaigns:
    print "---"
    print "Campaign: " + str(camp.title)
    
    for tactic in camp.related_ttps:
        ttp = pkg.find(tactic.item.idref)
        print "RelatedTTP: " + str(ttp.title)
        print "Relationship: " + str(tactic.relationship)
        for target in ttp.victim_targeting.targeted_information:
            print "Target: " + str(target)
{% endhighlight %}{% include end_tabs.html %}
[Full XML](victim-targeting.xml) | [Python Producer](victim-targeting_producer.py) | [Python Consumer](victim-targeting_consumer.py)

## Further Reading

You can build on this idiom by representing other types of victim targeting in the TTP:

* [Targeting by Industry Sector](../industry-sector)

See the full documentation for the relevant types for further information that may be provided:

* [CampaignType](/data-model/{{site.current_version}}/campaign/CampaignType)
* [TTPType](/data-model/{{site.current_version}}/ttp/TTPType)
* [VictimTargetingType](/data-model/{{site.current_version}}/ttp/VictimTargetingType)
