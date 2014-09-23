---
layout: flat
title: Suggested Practices
---

This page contains suggested practices (sometimes called best practices) for producing and consuming STIX content. Following these practices will ensure the best conformance with the design goals of STIX and the best compatibility with other STIX tools. These are not requirements, however: in some cases, technical or business requirements will mean you can't comply with them and that's fine. Think of them as "do it this way unless you have a good reason not to".

## General Practices

General practices apply across STIX (and sometimes CybOX).

### Formatting IDs

STIX IDs are [XML QNames](http://en.wikipedia.org/wiki/QName). Each ID includes both a namespace portion (optional) and an ID portion (required) separated by a colon (:). The recommend approach to creating STIX IDs is to define a producer namespace and namespace prefix, then use the form:

`[ns prefix]:[construct type]-[GUID]`

The "ns prefix" should be a namespace prefix bound to a namespace owned/controlled by the producer of the content.

Some examples:

    acme:package-ce431003-ad07-4c96-bd7a-a50a3196e2a0
    acme:indicator-bf8bc5d5-c7e6-46b0-8d22-7500fea77196
    acme:campaign-79090715-8d6a-46b7-943b-c0bb9e063788

In order to use this approach, you will need to define that namespace prefix in the head of your XML document:

```xml
<stix:STIX_Package xmlns:acme="http://acme.example.com" ...
```

This format provides high assurance that IDs will be both unique and meaningful, because the producer namespace denotes who's producing it, the construct name denotes what it is, and the overall ID including the GUID lends a high degree of confidence in its uniqueness.

### Assigning IDs

STIX has several constructs with the potential to assign IDs to them such that they can be unambiguously referenced from elsewhere.

Technically the decision to specify an ID on a given construct is optional based on the specifics of the usage context.

As a simple general rule specifying IDs on particular instances of constructs enables clear referencing, relating and pivoting.

This supports several very common STIX use cases such as:

* enabling individual portions of content to be externally referenced unambiguously (e.g. a report talking about a specific Campaign or Threat Actor)
* enabling the sharing/resharing of portions of STIX content (e.g. PartyB resharing 2 of a set of 100 Indicators received from PartyA)
* enabling versioning of content
* enabling the specification of potentially complex webs of interconnection and correlation between portions of STIX content (e.g. connecting particular TTPs and Indicators to specific Campaigns over time)
* enabling analysis pivoting on content with multiple contexts (e.g. the same IP Address seen in multiple Incidents and with connections to multiple TTPs and Indicators)


For these reasons, it is suggested that IDs be specified for the following commonly referenced and/or reused constructs unless there is clear reason not to:

* [Package](/data-model/{{site.current_version}}/stix/STIXType)
* [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
* [TTP](/data-model/{{site.current_version}}/ttp/TTPType)
* [Threat_Actor](/data-model/{{site.current_version}}/ta/ThreatActorType)
* [Campaign](/data-model/{{site.current_version}}/campaign/CampaignType)
* [Exploit_Target](/data-model/{{site.current_version}}/et/ExploitTargetType)
* [Course_Of_Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)
* [Observable](/data-model/{{site.current_version}}/cybox/ObservableType)
* [Object](/data-model/{{site.current_version}}/cybox/ObjectType)
* [Action](/data-model/{{site.current_version}}/cybox/ActionType)
* [Event](/data-model/{{site.current_version}}/cybox/EventType)

As a simple general rule specifying IDs is not suggested for constructs embedded within other constructs (e.g. a CybOX Object containing the embedded specification of another CybOX Related_Object) where the embedded constructs are really only relevant/valid/important within the context of the enclosing construct. In other words they provide contextual characterization for the enclosing construct but would not be of interest on their own. 
The upside of this is slightly less complexity of IDs on everything. The downside is that it would not be possible to reference or pivot on the embedded constructs.

### Referencing vs. Embedding

In many cases, you'll have an option to either include a component within the parent component or to reference the component by ID to a representation in a global location.

For example, an Indicator can include Indicated TTPs. One way of doing this is to include the Indicated_TTP inline in the Indicator:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-20T09:00:00.000000" xsi:type="indicator:IndicatorType">
  <!-- SNIP -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP xsi:type="ttp:TTPType" id="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9">
        <ttp:Title>Malware C2</ttp:Title>
    </stixCommon:TTP>
  </indicator:Indicated_TTP>
</stix:Indicator>
```

The other alternative is to reference that TTP, which would be represented elsewhere:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-20T09:00:00.000000" xsi:type="indicator:IndicatorType">
  <!-- SNIP -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" />
  </indicator:Indicated_TTP>
</stix:Indicator>
```

These situations are a judgment call, but when making that judgment you should consider whether the related construct has value individually or only within the context of the parent? If it only has value in the parent, embedding it may be appropriate. Otherwise it's probably better to reference it. If you're unsure, it's generally safer to reference it.

### Versioning and the timestamp attribute

8 major STIX constructs are versioned:

* [Packages](/data-model/{{site.current_version}}/stix/STIXType) (STIXType, STIX_Package)
* [Campaigns](/data-model/{{site.current_version}}/campaign/CampaignType)
* [Courses of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)
* [Exploit Targets](/data-model/{{site.current_version}}/et/ExploitTargetType)
* [Indicators](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Incidents](/data-model/{{site.current_version}}/incident/IncidentType)
* [Threat Actors](/data-model/{{site.current_version}}/ta/ThreatActorType)
* [TTPs](/data-model/{{site.current_version}}/ttp/TTPType)

It is always suggested that you version these constructs by including a relevant `@id` and `@timestamp` per the [STIX versioning guide](/documentation/concepts/versioning).

Note that many constructs that have a `@timestamp` attribute also have an `Information_Source` field with a `Time` field inside it. The `Time` field has a field called `Produced_Time`, which can easily be confused with `@timestamp`. Though similar, these fields are not used for the same purposes. `@timestamp` is used only for versioning and represents the time that version of the versioned structure was created. `Information_Source/Time/Produced_Time` is not related to versioning and represents the time the record (not that version of the record) was created. In some ways, they can be thought of as created time and modified time but in other ways they are used for completely different purposes.

See the [Versioning](/documentation/concepts/versioning) concept discussion for more information.

#### Versioning and References

There are two primary ways to create references in STIX 1.1.1: you can either create a reference to a specific version of a construct or you can create a reference to the latest version of a construct.

To create a reference to a specific version, set the idref attribute to the ID of the construct you want to reference and set the timestamp attribute to the exact timestamp of the version that you want to reference:

```xml
<stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" timestamp="2014-02-20T09:00:00.000000" />
```

The alternative is to omit the timestamp attribute, which indicates that the reference is to the latest version of that construct:

```xml
<stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" />
```

In general you should use the version-specific reference if you're concerned that the meaning of the referenced construct could change and make the reference invalid, while you should use the version-agnostic reference if you just want to reference the latest version of the construct despite any changes that might occur.

References to non-versioned constructs (anything with an id/idref but not a timestamp) implicitly use the latter form.

### Using Vocabularies

Many places in STIX use controlled vocabularies to represent data. When possible, you should use the vocabularies included in the STIX defaults. If necessary you can use your own vocabulary or even use strings outside of any vocabularies.

If you do this to add values that you think might be useful for other STIX users, you should [let us know](https://github.com/STIXProject/schemas/wiki#feedback) so we can consider adding it to the default vocabulary.

### Creating Timestamps

To remove ambiguity regarding the timezone, all times should include an explicit timezone whenever possible.

### Creating documents for human consumption

These suggestions only apply when you're creating documents you intend to be human-readable. They simply make the document more readable and easy to validate by XML editors but are not important for automated processing.

For best readability:

* Only include necessary namespaces
* Use the namespace prefixes as defined in the schemas
* Affinity-group or alphabetize namespaces
* Do not include attributes that have default attributes if you're simply setting the attribute to the default (i.e. @negate on indicators).

To ease validation in XML editors:

* Include schemaLocation attributes to the hosted versions of the STIX schemas
* If you include any non-standard extension or marking schemas, include them with the bundle and include that reference in the schemaLocation attribute

-----

## STIX Package
{% include sp_package.md %}

## Indicator

<img src="/images/Indicator.png" class="component-img-right" alt="Indicator Icon" />

{% include sp_indicator.md %}

## Observable

<img src="/images/Observable.png" class="component-img-right" alt="Observable Icon" />

{% include sp_observable.md %}

## Handling

<img src="/images/Data Marking.png" class="component-img-right" alt="Data Marking Icon" />

{% include sp_handling.md %}


