---
layout: idiom
title: Campaign Victim Targeting
---

One common method by which cyber threat campaigns are defined and tracked is based on the types of victims they target, whether victims are defined by the victim themselves (where they are located, the types of work they do), or by the fact that they have certain types of information or systems (customer PII, Industrial Control Systems, etc), or by the fact that they target specific technical configurations (a certain browser or OS for example).

This idiom describes the representation of a cyber threat campaign characterized by the fact that it targets customer PII and financial information.

## Data model

There are two main pieces of information that need to be communicated in this idiom: the campaign construct itself (using [CampaignType](/documentation/campaign/CampaignType)) and the victim targeting (using [VictimTargetingType](/documentation/ttp/VictimTargetingType)) in TTP. These are related together using the Campaign=>Related_TTP relationship.

The campaign is represented with just a title and a related TTP with a relationship name of "Targets". The TTP leverages the victim targeting constructs to represent the types of information that are targeted. For targeting of a specific type of information, the `Targeted_Information` field is used, leveraging the [controlled vocabulary](/idioms/features/controlled-vocabs) for information types, [InformationTypeVocab-1.0](/documentation/stixVocabs/InformationTypeVocab-1.0/).

![Campaign Targeting Diagram](diagram.png)

### XML

{% highlight xml linenos %}

{% endhighlight %}

[Full XML](sample.xml)

## Further Reading

You can build on this idiom by representing other types of victim targeting in the TTP:

* [Targeting by Industry Sector](/idioms/ttp/industry-sector)

See the full documentation for the relevant types for further information that may be provided:

* [CampaignType](/documentation/campaign/CampaignType)
* [TTPType](/documentation/ttp/TTPType)
* [VictimTargetingType](/documentation/ttp/VictimTargetingType)