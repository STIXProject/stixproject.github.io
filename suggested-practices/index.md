---
layout: flat
---

## STIX Header
Metadata about a STIX package is optional, but highly recommended

    Title
    Package_Intent
    Information_Source


Timestamps should include time zones

## Indicator Metadata

	Title
	Type
    	Timestamp
	Observed TTP
	Confidence
	Observable, Observable Composition, or Indicator Composition 


## Creating pattern observables for indicators
When creating observables for use as patterns within indicators, you should always set the condition attribute on all possible fields to an appropriate value, even if that value is equals. Leaving off the condition attribute implies that the observable is an instance rather than a pattern.


## Controlled Structure XPaths

The XPath specified in a data marking controlled structure field must select all fields (elements and attributes) that the marking will be applied to. It is not sufficient to select only the root element using the `/` character. Instead, you should use the `node()` function to select relevant nodes. For example, to select the entire document you should use `//node()` while to select a parent construct (Indicator, for example), you could use `ancestor-or-self::stix:Indicator//node()`.

As noted in the annotations, prefixes are valid if they are declared in scope of the Controlled_Structure element.
## Formatting IDs

STIX IDs are [XML QNames](http://en.wikipedia.org/wiki/QName). Each ID includes both a namespace portion (optional) and an ID portion (required) separated by a colon (:). The recommend approach to creating STIX IDs is to define a producer namespace and namespace prefix, then use the form:

`[ns prefix]:[construct type]-[GUID]`

The "ns prefix" should be a namespace prefix bound to a namespace owned/controlled by the producer of the content.

Some examples:
```xml
acme:package-ce431003-ad07-4c96-bd7a-a50a3196e2a0
acme:indicator-bf8bc5d5-c7e6-46b0-8d22-7500fea77196
acme:campaign-79090715-8d6a-46b7-943b-c0bb9e063788
```

In order to use this approach, you will need to define that namespace prefix in the head of your XML document:

```xml
<stix:STIX_Package xmlns:acme="http://acme.example.com" ...
```

This format provides high assurance that IDs will be both unique and meaningful, because the producer namespace denotes who's producing it, the construct name denotes what it is, and the overall ID including the GUID lends a high degree of confidence in its uniqueness.

## Referencing vs. Embedding

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

## Versioning and the timestamp attribute

8 major STIX constructs are versioned:

* Packages (STIXType, STIX_Package)
* Campaigns
* Courses of Action
* Exploit Targets
* Indicators
* Incidents
* Threat Actors
* TTPs

These versioned constructs include a `@timestamp` attribute at the top level in addition to the `@id`. To create versioned content (which is always suggested), the suggested approach is to always include the `@timestamp` attribute whenever you include an `@id` and set that timestamp to the exact time the construct was last modified (or was created if it's new). The `@id` is then re-used for the initial creation and all modifications. For example, when creating a new indicator set the timestamp to the time it was created:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-20T09:00:00.000000" xsi:type="indicator:IndicatorType" />
```

When it's updated, update that timestamp but keep the id:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-21T12:32:13.234234" xsi:type="indicator:IndicatorType" />
```

Note that because you should only publish content in your own ID namespace, you should not version content created by someone else using this mechanism. To create content derived off of content published by someone else, use a relationship to the original content and set the relationship field to "Derived From":

```xml
<stix:Indicator id="example2:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-22T16:23:37.456332" xsi:type="indicator:IndicatorType">
  <indicator:Related_Indicators>
    <indicator:Related_Indicator>
      <stixCommon:Relationship>Derived From</stixCommon:Relationship>
      <stixCommon:Indicator idref="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" />
    </indicator:Related_Indicator>
  </indicator:Related_Indicators>
</stix:Indicator>
```

You can create that with or without the timestamp reference as appropriate, but if you use the timestamp attribute consumers will know which specific version your derived content was created from.


## Creating References

There are two primary ways to create references in STIX 1.1: you can either create a reference to a specific version of a construct or you can create a reference to the latest version of a construct.

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

## Creating documents for human consumption

These suggestions only apply when you're creating documents you intend to be human-readable. They simply make the document more readable and easy to validate by XML editors but are not important for automated processing.

For best readability:
* Only include necessary namespaces
* Use the namespace prefixes as defined in the schemas
* Affinity-group or alphabetize namespaces
* Do not include attributes that have default attributes if you're simply setting the attribute to the default (i.e. @negate on indicators).

To ease validation in XML editors:
* Include schemaLocation attributes to the hosted versions of the STIX schemas
* If you include any non-standard extension or marking schemas, include them with the bundle and include that reference in the schemaLocation attribute

## Using Vocabularies

Many places in STIX use controlled vocabularies to represent data. When possible, you should use the vocabularies included in the STIX defaults. If necessary you can use your own vocabulary or even use strings outside of any vocabularies.

If you do this to add values that you think might be useful for other STIX users, you should [let us know](https://github.com/STIXProject/schemas/wiki#feedback) so we can consider adding it to the default vocabulary.

