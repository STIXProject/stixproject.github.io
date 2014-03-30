---
layout: idiom
title: Campaign Idioms
---

<img src="/images/Campaign.png" class="component-img" alt="Campaign Icon" />

A STIX [Campaign](/documentation/campaign/CampaignType) represents a set of TTPs, incidents, or threat actors that together express a common intent or desired effect. For example, an adversary using a particular set of TTPs (malware and tools) to target an industry sector with a specific intent may constitute a campaign. In the STIX data model, campaigns represent both that intent itself and, perhaps more importantly, act as a meta-construct to relate the associated TTPs, incidents, and threat actors that are part of that campaign together.

The campaign idioms documented here can be divided into how to express data about the campaign itself (such as expressing multiple aliases for the same campaign) and how to use the campaign construct to tie together related TTPs, incidents, and threat actors.

<hr class="separator" />

{% comment %}
### Campaign Aliases

Often, a cyber threat campaign will be known by several different aliases (names). This idiom shows an example of how this can be done using the Campaign Names field.

[View this idiom »](aliases)

### Attribution

It is often very useful to express "attribution" for a given campaign, whereby one or more threat actors are said to be responsible for the campaign. This idiom shows an example of expressing campaign attribution in STIX, accomplished through the Attribution field on a campaign.

[View this idiom »](attribution)
{% endcomment %}

### Victim Targeting

A cyber campaign may be defined based on the fact that it targets a consistent set of victims, as defined by their nationality or industry sector (as an example). This idiom demonstrates how to express that in STIX, accomplished through the use of a related TTP.

[View this idiom »](victim-targeting)