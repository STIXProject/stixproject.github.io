---
layout: idiom
title: Victim Targeting by Sector
---

A key usage of the [TTP](/documentation/ttp/TTPType) component is to characterize the types of victims that a particular threat targets, known as victim targeting. This idiom describes how to use the victim targeting structures in STIX to characterize a threat that targets particular industry sectors, such as the Energy Sector and the Banking and Finance Sector.

TTP Victim Targeting, including by industry sector, is commonly used within a larger STIX document by relating it to a threat actor or a campaign via a Related TTP. For example, the [Campaign Victim Targeting](/idioms/campaign/victim-targeting) idiom describes linking a campaign to the victims that campaign targets: when combined with this idiom, you could describe a campaign that targets victims by industry sector.

## Scenario

In this scenario, the STIX document describes a very simple victim targeting structure that denotes that the threat targets organizations in the energy sector and in the banking and finance sector.

## Data model

The portion of the TTP data model that is used to represent victim targeting is [VictimTargetingType](/documentation/ttp/VictimTargetingType) within [BehaviorType](/documentation/ttp/BehaviorType). That type contains a field called `Identity` that is used to express facts about victim identity that are targeted, including industry sector.

The `Identity` field is an extension point represented by [IdentityType](/documentation/stixCommon/IdentityType). The default extension provided by STIX for use in expressing identity is the [CIQIdentity3.0InstanceType](/documentation/stixCiqIdentity/CIQIdentity3.0InstanceType), which leverages the external [CIQ](TODO) (Customer Information Quality) standard published by OASIS. Though it's possible to use a different extension, in most cases producers will be using CIQ.

Within CIQ, the specific field used is `@IndustryType` within `OrganisationInfo`. That field is an XML attribute and, therefore, the [suggested practice](/suggested-practices/ciq/commas) is to use comma separated values.

![TTP Targeting Sector Diagram](diagram.png)

## XML

{% highlight xml linenos %}
<stix:TTPs>
    <stix:TTP timestamp="2014-02-20T09:00:00.000000Z" id="example:ttp-030d3edf-da7c-4d1f-a0b9-6c38a8af73db" xsi:type="ttp:TTPType">
        <ttp:Title>Victim Targeting: Electricity Sector and Industrial Control System Sector</ttp:Title>
        <ttp:Victim_Targeting>
            <ttp:Identity id="example:ciqidentity3.0instance-f8cd0af8-6534-496e-bf53-f6a9aa11e5ce" xsi:type="stixCIQIdentity:CIQIdentity3.0InstanceType">
                <stixCIQIdentity:Specification>
                    <xpil:OrganisationInfo xpil:IndustryType="Electricity Sector, Industrial Control System Sector"/>
                </stixCIQIdentity:Specification>
            </ttp:Identity>
        </ttp:Victim_Targeting>
    </stix:TTP>
</stix:TTPs>
{% endhighlight %}

[Full XML](victim-targeting-sector.xml)

## Further Reading

* [TTP](/documentation/ttp/TTPType)
* [Victim Targeting](/documentation/ttp/VictimTargetingType)
* [OASIS CIQ](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=ciq)