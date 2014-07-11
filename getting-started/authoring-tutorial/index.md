---
layout: getting_started
title: Authoring Tutorial
---

This authoring tutorial will walk you through how to create a simple STIX indicator that looks for a file hash and, if that file hash is found, points to a piece of malware that might be present. You can think of it as a correlary to the [sample walkthrough](/getting-started/sample-walkthrough): while that takes an existing piece of content and explains what it means, this will walk through how to actually author content.

<p class="alert alert-info">This guide covers authoring content by hand or with languages/tools other than the <a href="http://stix.readthedocs.org">python-stix API</a>. If you're using the Python API, the <a href="http://stix.readthedocs.org/en/latest/getting_started.html#your-first-stix-application">Your First STIX Application</a> guide in the API docs is recommended.</p>

## Prerequisites

1. Understand the general concept of what STIX is and what problems it's designed to solve. Get this by reading the [whitepaper](http://stix.mitre.org/about/documents/STIX_Whitepaper_v1.1.pdf).

1. Understand how STIX is structured and interpreted. Get this by going through the [sample walkthrough](/getting-started/sample-walkthrough)

1. Beginner/intermediate knowledge of XML is suggested. You should know what elements and attributes are, how namespaces work, what validation means, and other basic concepts.

1. A XML IDE is recommended in order to auto-complete and validate content. [Oxygen](http://www.oxygenxml.com/), [XMLSpy](http://www.altova.com/simpledownload2c.html), and [Eclipse](http://www.eclipse.org) are all good options.

## Scenario

As explained above, in this walkthrough we'll create a STIX report that describes an indicator for (fake) Malware XYZ. The information is:

* File hash = 01234567890abcdef01234567890abcdef
* Malware name = Malware XYZ

## Creating the Document

The root element for all STIX content is `STIX_Package` ([STIXType](/data-model/{{site.current_version}}/stix/STIXType)). This type contains all STIX content (indicators, campaigns, incidents, etc.) as well as metadata that applies to the content it bundles such as who produced it and how it can be shared. `STIX_Package` is defined in the STIX Core namespace and therefore is represent as `stix:STIX_Package`.

```xml
<stix:STIX_Package>

</stix:STIX_Package>
```

### XML Namespaces and Schema Locations

STIX takes advantage of XML namespaces to separate types and fields by purpose as well as XML Schema to allow for validation.

The `xmlns:*` attributes on `STIX_Package` map namespace prefixes/aliases to full namespaces. These mappings are required for any namespaces you use (STIX and CybOX Core/Common/Vocabs, STIX Components, CybOX Objects, Extensions).

`xsi:schemaLocation` is an optional hint (not required for validation) used by some tools to indicate which schemas should be used to validate the content. The format is `[namespace] [schema location] [namespace 2] [schema location 2] etc` and, if you use it, the mapping must be present for every namespace.

In this case, we've looked and figured out which namespaces/schemas we'll be using ahead of time and added the mappings for those. Alternatively, you can either start with the [template](http://stix.mitre.org/language/version1.1.1/stix_v1.1.1_template.xml) and delete the ones you don't need when you're done or just start with none and add them as necessary.

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cybox="http://cybox.mitre.org/cybox-2"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:indicator="http://stix.mitre.org/Indicator-2"
  xmlns:ttp="http://stix.mitre.org/TTP-1"
  xmlns:FileObj="http://cybox.mitre.org/objects#FileObject-2"
  xmlns:example="http://example.com"
  xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd
    http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd
    http://stix.mitre.org/TTP-1 http://stix.mitre.org/XMLSchema/ttp/1.1.1/ttp.xsd
    http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
    http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd
    http://cybox.mitre.org/common-1 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd
    http://cybox.mitre.org/objects#FileObject-2 http://cybox.mitre.org/XMLSchema/objects/File/2.1/File_Object.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
    http://cybox.mitre.org/default_vocabularies-2 http://cybox.mitre.org/XMLSchema/default_vocabularies/2.1/cybox_default_vocabularies.xsd
  ">
</stix:STIX_Package>
```

### Version, ID, and Timestamp

```xml
<stix:STIX_Package
  ...
  version="1.1.1"
  id="example:package-382ded87-52c9-4644-bab0-ad3168cbad59"
  timestamp="2014-05-08T09:00:00.000000Z"
  >
</stix:STIX_Package>
```

The `@version` attribute is set to the version of STIX that you're targeting, which in almost all cases will be the same as the version of the schemas that you're using.

The `@id` attribute is set to a globally-unique identifier for this content, and in general the best way to achieve that goal is to follow our [suggested practice](/suggested-practices/#toc_1) for creating IDs: a producer namespace prefix, followed by a ":" (required by the field to separate the namespace from the ID), followed by the type of construct the ID is for ("package"), followed by a GUID. You can use an [online GUID generator](https://www.google.com/search?q=guid+generator) to generate the GUID. In this case the producer namespace prefix is "example" (note that this prefix must also be declared in the head of the document), the construct type is "package", and the GUID itself is "382ded87-52c9-4644-bab0-ad3168cbad59".

Finally, the `@timestamp` attribute is used for [versioning](/idioms/features/versioning/) and should be set to the time (with fractional seconds if possible) that this version of the construct was published. To avoid ambiguity, this time should include a timezone if at all possible.

## STIX Header

The `STIX_Header` element ([STIXHeaderType](/data-model/{{site.current_version}}/stix/STIXHeaderType)) is used to represent metadata about the content contained in the containing `STIX_Package`. It is added as a child of the `STIX_Package`:

```xml
<stix:STIX_Package
  ... >
  <stix:STIX_Header>
  </stix:STIX_Header>
</stix:STIX_Package>
```

In this case, we'll set a title, package intent, and information source for this package. More generally, you can check the data model documentation and suggested practices for information on what you can and should populate for the element you're creating.

### Report Title

The `Title` field gives the package (report) a basic title. Because this report talks about a file hash for fake malware, we'll indicate that in the report title.

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
</stix:STIX_Header>
```

### Package Intent

The `Package_Intent` field tells consumers what type of threat intelligence you're intending to convey. In this case, we'll be conveying indicators of a malicious piece of software.

If you followed the sample walkthrough or checked the documentation, you'll know that this field is a [controlled vocabulary](/idioms/features/controlled-vocabularies/). In this case we'll set the intent to a value in the default vocabulary by setting the `xsi:type` to the type for the default vocabulary for package intent. You can find the default vocabulary listed in the [documentation](/data-model/{{site.current_version}}/stix/STIXHeaderType) for the field.

For this scenario we'll set that field to "Indicators - Malware Artifacts".

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
  <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Malware Artifacts</stix:Package_Intent>
</stix:STIX_Header>
```

### Information Source

The information source field contains information about the who/what/when/where/how of report production. In this case we'll fill in the author (ourselves) and the time it was produced:

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
  <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Malware Artifacts</stix:Package_Intent>
  <stix:Information_Source>
    <stixCommon:Identity>
      <stixCommon:Name>John Smith</stixCommon:Name>
    </stixCommon:Identity>
    <stixCommon:Time>
      <cyboxCommon:Produced_Time>2013-12-20T12:48:50Z</cyboxCommon:Produced_Time>
    </stixCommon:Time>
  </stix:Information_Source>
</stix:STIX_Header>
```

There are a few things we did here:

1. The `Information_Source` element is still in the STIX namespace, but the `Identity` and `Time` children are in the `stixCommon` namespace. You can see what namespace a node is in either through autocomplete (it will automatically add the correct one) or by looking at the schema.
1. You see we also use `cyboxCommon` for the `Time` element. Some places in STIX use elements from the CybOX common namespace.
1. Note that in most cases the `Produced_Time` will be identical to the `@timestamp` attribute on the STIX_Package element.

## Adding Content

Now that we've finished the header, let's move on to adding the indicator itself. First, we create the wrapper element and a stub indicator.

```xml
<stix:STIX_Package ...>
  <stix:STIX_Header><!-- snip --></stix:STIX_Header>
  <stix:Indicators>
    <stix:Indicator></stix:Indicator>
  </stix:Indicators>
</stix:STIX_Package>
```

Now, if you go to autocomplete new elements in the indicator you'll find that not many are available. This is because, like controlled vocabularies, the core STIX components also use the [xsi:type abstraction mechanism](/idioms/features/xsi-type). In nearly all cases, you'll want to set the `@xsi:type` attribute to the appropriate STIX schema type (`indicator:IndicatorType` in this case). If you work off the template, you'll notice that the xsi:type is already set for you.

```xml
<stix:Indicator xsi:type="indicator:IndicatorType">
```

Before we add content though, we should set an ID and timestamp. Following the suggesting practice, we set the prefix to our producer prefix, use "indicator-" as the basis for the ID portion, and generate a new GUID to fill in the rest:

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
```

As with STIX_Header, we'll also check suggested practices to see also look at the suggested practices for STIX indicators to see what elements we should add.

### Set the Indicator Title and Type

Basic indicator data includes a human-readable `Title` and the indicator's `Type` (similar to `Title` and `Package_Intent` on `STIX_Package`).

<p class="alert alert-warning">If you're following along, at this point it might be worth seeing if you can add these yourself before looking to see how I did it. Specifically, make sure you can identify the fact that <pre>Type</pre> is a controlled vocabulary field and, from there, figure out which vocabulary to use.</p>

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975">
  <indicator:Title>Malware XYZ Hashes</indicator:Title>
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
</stix:Indicator>
```

### Set the Observable Pattern using CybOX

As explained in the [indicator idioms](/idioms/indicator), indicators consist of two key pieces of information: a pattern for what to look for, and a description of what it means if that pattern is seen. The pattern portion is captured either via CybOX in the `Observable` field or via a native signature in the `Test_Mechanism` field. The indicator idioms give several examples of both approaches.

In this case, we'll use CybOX.

The first step is to identify the correct CybOX object to use for the data we want to represent (a file hash) and then create a pattern observable in CybOX that represents the hash. What does that mean? First, we need an [Observable](/data-model/{{site.current_version}}/cybox/ObservableType) wrapper to contain the CybOX pattern. Then, we need an [Object](/data-model/{{site.current_version}}/cybox/ObjectType) element to indicate that we're creating a static (stateful measure) observable instead of a dynamic (event-based) observable. Lastly, we add a CybOX object, using the `Properties` field, and give it the properties we want the indicator to look for.

So to start, we just need to create the CybOX observable and object wrappers:

#### Observable and Object

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
  <indicator:Title>Malware XYZ Hashes</indicator:Title>
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
  <indicator:Observable id="example:observable-3d7b08aa-88bf-4f9c-bb34-939b7548b636">
    <cybox:Object id="example:observable-5a5a0a2d-3b75-4ba6-932f-9d5f596c3c5b">
    </cybox:Object>
  </indicator:Observable>
</stix:Indicator>
```

Notice that we've assigned IDs for the Observable and Object. CybOX IDs are recommended on major components and follow the same format as STIX IDs. CybOX content is not versioned and therefore does not have the `@timestamp` attribute.

#### Object Properties

Next, we need to identify the correct CybOX object type to use to represent file hashes. Looking through the list on the [CybOX release page](http://cybox.mitre.org/language/version2.1/), the best choice seems to be the [FileObject](/data-model/{{site.current_version}}/FileObj/FileObjectType/). Opening the documentation for that object, we can see that it does include a `Hashes` element that we can use to represent file hashes.

So, we'll create the `Properties` element and fill in the `xsi:type` to indicate that we're using the file object:

```xml
<indicator:Object id="example:observable-5a5a0a2d-3b75-4ba6-932f-9d5f596c3c5b">
  <cybox:Properties xsi:type="FileObj:FileObjectType">
  </cybox:Properties>
</indicator:Object>
```

Finally, we add in the fields to represent the hash. This will vary greatly depending on what type of indicator you want to create: IP indicators, domain indicators, e-mail indicators, file indicators, etc. will all use different fields. Essentially, search through the objects and the object fields to see what you want the indicator to trigger on and add those fields.

```xml
<cybox:Properties xsi:type="FileObj:FileObjectType">
  <FileObj:Hashes>
    <cyboxCommon:Hash>
      <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0" condition="Equals">MD5</cyboxCommon:Type>
      <cyboxCommon:Simple_Hash_Value condition="Equals">01234567890abcdef01234567890abcdef</cyboxCommon:Simple_Hash_Value>
    </cyboxCommon:Hash>
  </FileObj:Hashes>
</cybox:Properties>
```

This looks a little bit complicated, but you should be able to see the logic behind it now that you understand how STIX and CybOX work. We have a couple wrapper elements around the hashes, then a controlled vocabulary describing the type of hash and a `Simple_Hash_Value` field with the hashes to look for. The question you might be having is about the `@condition` attribute, which is related to CybOX patterning.

#### CybOX Pattern Fields

All of the lowest-level fields in CybOX representing cyber observables data extend from a field that implements CybOX patterning capability called [BaseObjectPropertyType](/data-model/{{site.current_version}}/cyboxCommon/BaseObjectPropertyType). That type adds fields and defines behaviors for CybOX patterning. The most common field you'll need to set is `@condition`, which indicates how the value in the field should be matched against target data.

For this hash match, the condition is set to "Equals" because we want to test whether file hashes equal each other. When using observables in an indicator (or any other time you use observables for patterns) you MUST have the condition attribute set. Omitting it implies the CybOX observable is an instance and therefore matching content against it does not make sense.

A few other examples of `@condition`: if we were testing for IP Addresses in a range we might use "Starts_With" and supply a partial IP address, or if we were searching for keywords in an e-mail we could use "Contains" and supply the keywords. The various CybOX conditions and how they work are described in the schema annotations.

### Add the Confidence and Valid_Time_Position

It's generally a good idea to let consumers know how confident in the indicator you are via the `Confidence` field and how long the indicator is valid for via the `Valid_Time_Position` field. If this information isn't known then it isn't required, but it does help consumers understand how to implement the indicator in their infrastructure.

These fields are fairly standard STIX, so let's just look at the end result. Alternatively, you could try adding them yourself and then quiz yourself.

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
  <indicator:Title>Malware XYZ Hashes</indicator:Title>
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
  <indicator:Valid_Time_Position>
    <indicator:Start_Time>2014-01-01T12:48:50Z</indicator:Start_Time>
    <indicator:End_Time>2014-01-31T12:48:50Z</indicator:End_Time>
  </indicator:Valid_Time_Position>
  <indicator:Observable id="example:observable-3d7b08aa-88bf-4f9c-bb34-939b7548b636">
    <cybox:Object id="example:observable-5a5a0a2d-3b75-4ba6-932f-9d5f596c3c5b">
      <cybox:Properties xsi:type="FileObj:FileObjectType">
        <FileObj:Hashes>
          <cyboxCommon:Hash>
            <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0" condition="Equals">MD5</cyboxCommon:Type>
            <cyboxCommon:Simple_Hash_Value condition="Equals" apply_condition="ANY">01234567890abcdef01234567890abcdef##comma##abcdef1234567890abcdef1234567890##comma##00112233445566778899aabbccddeeff</cyboxCommon:Simple_Hash_Value>
          </cyboxCommon:Hash>
        </FileObj:Hashes>
      </cybox:Properties>
    </cybox:Object>
  </indicator:Observable>
  <indicator:Confidence>
    <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Medium</stixCommon:Value>
  </indicator:Confidence>
</stix:Indicator>
```

<p class="alert alert-info"><strong>Quiz:</strong> If you tried this yourself, did you catch the controlled vocabulary for Confidence/Value and remember to add the timezone for the valid time position?</p>

## Add the TTP

Once again, an indicator consists of a pattern for something to look for and then the context for what that means. The STIX [TTP](/data-model/{{site.current_version}}/ttp/TTPType) construct is often used to describe the latter, including:

* Resources (infrastructure and tools)
* Behavior (attack patterns, malware, exploits)
* Victim Targeting

In this case, we want to represent a piece of malware. For this example we'll just give it a name, but you could also represent more complicated information about it using something like MAEC.

So, we'll first add the TTPs element with a single TTP that has the correct xsi:type and an id and timestamp:

```xml
<stix:TTPs>
  <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd" timestamp="2014-05-08T09:00:00.000000Z">
  </stix:TTP>
</stix:TTPs>
```

### Setting the malware information

Next, we'll give it a title appropriate to the malware we want to represent and a Behavior/Malware instance to identify the malware. Although it looks a little duplicitous to have the malware name in both the `TTP` `Title` and the `Malware_Instance` `Name`, having it in both places ensures both high and low level tools understand what the TTP is saying.

```xml
<stix:TTP xsi:type="ttp:TTPType" id="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd">
  <ttp:Title>Malware XYZ</ttp:Title>
  <ttp:Behavior>
    <ttp:Malware>
      <ttp:Malware_Instance>
        <ttp:Name>Malware XYZ</ttp:Name>
      </ttp:Malware_Instance>
    </ttp:Malware>
  </ttp:Behavior>
</stix:TTP>
```

## Linking it all together

Alright, now we've got an indicator with file hashes for a piece of malware and a representation of the malware itself in a TTP. How do we say that when we see the indicator, it might indicate you're seeing malware activity? Just having them in the same package is not enough.

This is where STIX relationships come in. We'll need to relate the Indicator to the TTP using the `Indicated_TTP` field on the indicator:

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
  <!-- snip -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP idref="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd"/>
  </indicator:Indicated_TTP>
</stix:Indicator>
```

As you can see, a relationship is fairly straightforward to add. All you have to do is add the wrapper element, create a new TTP (no need for the `xsi:type` in this case, since `@idref` is on the base type), and set the `@idref` to the ID of the TTP that you want to point to. That TTP can be in the same document, a document you send alongside it, or even in a document that was sent at another time. Essentially, relationships in STIX are considered global, not local.

## Validating your document

One very important step in creating STIX content is to ensure that it's valid. This can be done in a few ways:

* Programatically, by calling the appropriate schema validation methods against the instance document
* In an XML IDE
* Using [stix-validator](https://github.com/STIXProject/stix-validator)

# Summary

Congratulations, you just wrote a STIX document! It might be a simple one, but you've learned STIX concepts that will let you compose much more complicated documents once you learn the rest of the data model.

The entire document, by the way, should look something like this:

{% highlight xml linenos %}
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cybox="http://cybox.mitre.org/cybox-2"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:indicator="http://stix.mitre.org/Indicator-2"
  xmlns:ttp="http://stix.mitre.org/TTP-1"
  xmlns:FileObj="http://cybox.mitre.org/objects#FileObject-2"
  xmlns:example="http://example.com"
  xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd
    http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd
    http://stix.mitre.org/TTP-1 http://stix.mitre.org/XMLSchema/ttp/1.1.1/ttp.xsd
    http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
    http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd
    http://cybox.mitre.org/common-1 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd
    http://cybox.mitre.org/objects#FileObject-2 http://cybox.mitre.org/XMLSchema/objects/File/2.1/File_Object.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
    http://cybox.mitre.org/default_vocabularies-2 http://cybox.mitre.org/XMLSchema/default_vocabularies/2.1/cybox_default_vocabularies.xsd
  "
  version="1.1.1"
  id="example:package-382ded87-52c9-4644-bab0-ad3168cbad59"
  timestamp="2014-05-08T09:00:00.000000Z">
  <stix:STIX_Header>
    <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Malware Artifacts</stix:Package_Intent>
    <stix:Information_Source>
      <stixCommon:Identity>
        <stixCommon:Name>John Smith</stixCommon:Name>
      </stixCommon:Identity>
      <stixCommon:Time>
        <cyboxCommon:Produced_Time>2013-12-20T12:48:50Z</cyboxCommon:Produced_Time>
      </stixCommon:Time>
    </stix:Information_Source>
  </stix:STIX_Header>
  <stix:Indicators>
    <stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
      <indicator:Title>Malware XYZ Hashes</indicator:Title>
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
      <indicator:Valid_Time_Position>
        <indicator:Start_Time>2014-01-01T12:48:50Z</indicator:Start_Time>
        <indicator:End_Time>2014-01-31T12:48:50Z</indicator:End_Time>
      </indicator:Valid_Time_Position>
      <indicator:Observable id="example:observable-3d7b08aa-88bf-4f9c-bb34-939b7548b636">
        <cybox:Object id="example:observable-5a5a0a2d-3b75-4ba6-932f-9d5f596c3c5b">
          <cybox:Properties xsi:type="FileObj:FileObjectType">
            <FileObj:Hashes>
              <cyboxCommon:Hash>
                <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0" condition="Equals">MD5</cyboxCommon:Type>
                <cyboxCommon:Simple_Hash_Value condition="Equals" apply_condition="ANY">01234567890abcdef01234567890abcdef</cyboxCommon:Simple_Hash_Value>
              </cyboxCommon:Hash>
            </FileObj:Hashes>
          </cybox:Properties>
        </cybox:Object>
      </indicator:Observable>
      <indicator:Indicated_TTP>
        <stixCommon:TTP idref="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd"/>
      </indicator:Indicated_TTP>
      <indicator:Confidence>
        <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Medium</stixCommon:Value>
      </indicator:Confidence>
    </stix:Indicator>
  </stix:Indicators>
  <stix:TTPs>
    <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd" timestamp="2014-05-08T09:00:00.000000Z">
      <ttp:Title>Malware XYZ</ttp:Title>
      <ttp:Behavior>
        <ttp:Malware>
          <ttp:Malware_Instance>
            <ttp:Name>Malware XYZ</ttp:Name>
          </ttp:Malware_Instance>
        </ttp:Malware>
      </ttp:Behavior>
    </stix:TTP>
  </stix:TTPs>
</stix:STIX_Package>
{% endhighlight %}

# Where to go from here

1. Read up on the [idioms](/idioms) to learn more about how STIX can help with specific use cases and to see many more examples
1. Take a look at the data model documentation for the types you're interested in
1. Try your own! Make sure to validate your documents when you're finished.