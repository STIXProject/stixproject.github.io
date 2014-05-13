---
layout: getting_started
title: Authoring Tutorial
---

This authoring tutorial will walk you through how to create a simple indicator that looks for a file hash and, if that file hash is found, points to a piece of malware that might be present. You can think of it as a correlary to the [sample walkthrough](/getting-started/sample-walkthrough): while that takes an existing piece of content and explains what it means, this will walk through how to actually author content. This guide will show how to author content by hand, so when using the bindings and APIs some of this might be done for you. The general concepts, though, might be helpful regardless of how you're creating content.

## Prerequisites

Prior to going through this walkthrough, you should understand the general concept of what STIX is, what problems it is designed to solve, and how it is used to solve those problems. The best place to do that is by going to the Getting Started page and reading through the whitepaper and other materials linked from there.

You also should have good XML tools in order to work with STIX. Most of the STIX team uses either Oxygen or XMLSpy, which are both commercial products. Eclipse is an open-source option that is somewhat less fully-featured but should get the job done.

This tutorial does assume intermediate knowledge of XML. You should know what elements are, what attributes are, what validation means, and other basic concepts. If you don't, it's suggested that you either use higher-level tooling when working with STIX or read up on XML before looking into STIX.

Finally, it's best if you have some idea of how STIX works at the XML level, so at minimum you should go through the [sample walkthrough](/getting-started/sample-walkthrough) first.

## Get Started

The first step is to get the STIX schemas (so you can easily reference them) and create a new file. Although we'll use the online schema locations to actually perform validation, it's helpful to have an offline copy so you can refer to them when creating content.

## Creating the package

As a general rule, all STIX content should be enclosed in a STIX_Package. This allows you to represent metadata about the content, such as the intent, title, and information source. So, let's start off with that:

```xml
<stix:STIX_Package>

</stix:STIX_Package>
```

### Define namespace prefixes

You'll notice two things: one is that `STIX_Package` uses the `stix` namespace prefix and the second is that this obviously isn't valid yet. In order to make this valid, we need to declare the relevant namespace prefixes and map them to the full namespaces. Since we might not know what all of these are from the start, I like to add a couple commonly used ones at first and then expand on that as I use things. So, let's define some basic namespaces used in most STIX documents first. `xsi` is required to use `xsi:type` (the STIX extension mechanism), `stix` is the top-level STIX namespace (that STIX_Package is in), `stixVocabs` is the namespace for the default vocabularies, `stixCommon` and `cyboxCommon` are library namespaces that are used throughout STIX, and `example` is the namespace we'll use when creating IDs (it denotes the producer of the content, so feel free to use your company name here). We'll be adding more throughout this tutorial, but in general the namespaces below are a good place to start.

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:example="http://example.com">
</stix:STIX_Package>
```

### Add schemaLocation

Next, let's set the schemaLocation attribute, which is a space-separated list of namespaces mapped to schemas. In this case, we say the `http://stix.mitre.org/stix-1` namespace can be found in the `http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd` schema. You can find these locations by going to the [current release](http://stix.mitre.org/language/version1.1.1/) page and copying the XSD URL for the correct link (STIX Core, in this case). If you're offline or behind a firewall and can't access the schema locations above, you can also use a relative or absolute path to a local copy of the schema that you've downloaded.

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:example="http://example.com"
  xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd
    http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
    http://cybox.mitre.org/common-1 http://cybox.mitre.org/XMLSchema/common/2.1/stix_common.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
  ">
</stix:STIX_Package>
```

Note that we don't need a schema location for xsi (because editors always know what it means) or for example (because it's only used for IDs, not schema constructs).

### Set the version and ID fields

```xml
<stix:STIX_Package
  ...
  version="1.1.1"
  id="example:package-382ded87-52c9-4644-bab0-ad3168cbad59"
  timestamp="2014-05-08T09:00:00.000000Z"
  >
</stix:STIX_Package>
```

The version attribute is set to the version of STIX that you're targeting, which in almost all cases will be the same as the version of the schemas that you're using. In this case, we're using STIX 1.1.1 so we set the `version` attribute to "1.1.1".

The `id` attribute is set to a globally-unique identifier for this content, and in general the best way to achieve that goal is to follow our [suggested practice](https://github.com/STIXProject/schemas/wiki/Suggested-Practices-%281.1%29#formatting-ids) for creating IDs: a producer namespace prefix, followed by a ":" (required by the field to separate the namespace from the ID), followed by the type of construct the ID is for ("package"), followed by a GUID. You can use an [online GUID generator](https://www.google.com/search?q=guid+generator) to generate the GUID. In this case the producer namespace prefix is "example" (note that this prefix must also be declared in the head of the document), the construct type is "package", and the GUID itself is "382ded87-52c9-4644-bab0-ad3168cbad59".

Finally, the `timestamp` attribute is set to the time (with fractional seconds if possible) that this version of the construct was published. Later versions of the construct can then re-use the same ID but update the timestamp to reflect the new version.

### Validate the document

Try to validate the document in your XML tool. With the schemaLocation set and the namespaces defined, the document should now validate against the schemas and we can move on. In many tools, the editor will now automatically validate the document against the schemas and even autocomplete element and attribute names for you (both Oxygen and XML Spy do this).

## Add the STIX_Header

Next, we need to add a STIX_Header element in order to represent metadata. It should be added inside STIX_Package:

```xml
<stix:STIX_Package
  ... >
  <stix:STIX_Header>
  </stix:STIX_Header>
</stix:STIX_Package>
```

Per the [suggested practices](https://github.com/STIXProject/schemas/wiki/Suggested-Practices-%281.1%29#stix-header) for STIX_Header, we should include a:

* Title
* Package_Intent
* Information_Source

Always check the suggested practices to see if an element is recommended. We recommend you add certain elements because we find they're useful to consumers of STIX content, and so by following these recommendations whenever possible you'll create content that's most useful to the people using your content.

### Add Title
Moving along, let's add the title, that's easy:

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
</stix:STIX_Header>
```

### Add Package Intent

After that comes the package intent. The package intent tells consumers what type of threat intelligence you're intending to convey. In this case, we'll be conveying indicators of a malicious piece of software.

If you followed the sample walkthrough, or have been checking the documentation, you'll know that this field is a controlled vocabulary. To figure out which vocabulary you should use by default, check the [schema annotations](http://stix.mitre.org/language/version1.1.1/xsddocs/core/1.1.1/stix_core_xsd.html#STIXHeaderType_Package_Intent) for the field. You can do this either in the online docs (linked from the release page) or by looking directly at the schemas. In this case, they tell us to use "PackageIntentVocab-1.0", so we set that in the `xsi:type` field (see the section on xsi:type in the sample walkthrough for more info on this).

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
  <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0"></stix:Package_Intent>
</stix:STIX_Header>
```

In many editors, the possible types you can use for `xsi:type` will autocomplete for you. Additionally, the element value itself will autocomplete once you put in the `xsi:type`. Either way, we take a look through the values that are acceptable for that vocabulary (looking in the schemas, in the documentation, or in the editor autocomplete) and choose "Indicators - Malware Artifacts".

```xml
<stix:STIX_Header>
  <stix:Title>Example File Hash Watchlist for Fake Malware XYZ</stix:Title>
  <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Malware Artifacts</stix:Package_Intent>
</stix:STIX_Header>
```

### Add the Information Source

The information source field contains information about, naturally, the source of the watchlist. We'll fill in the author (us) and the time it was created:

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
1. Notice the "Z" at the end of the time. It is strongly suggested that all times in STIX and CybOX include a specification of the timezone if it is know, so in this case we set it to UTC by appending a Z. You can also use UTC offsets (-1:00), etc.

## Add the Indicator

Now that we've finished the header, let's move on to adding the indicator itself. First, we create the wrapper element and a stub indicator.

```xml
<stix:STIX_Package ...>
  <stix:STIX_Header><!-- snip --></stix:STIX_Header>
  <stix:Indicators>
    <stix:Indicator></stix:Indicator>
  </stix:Indicators>
</stix:STIX_Package>
```

Now, if you go to autocomplete new elements in the indicator you'll find that not many are available. This is because the core STIX components also use the `xsi:type` abstraction mechanism. This allows STIX Core to be used without requiring it to import each of the components. It does mean, however that we need to add the indicators schema to our document. We add the prefix mapping to the head of the document with the other namespaces and update the schemaLocation attribute to add the mapping to the actual schema:

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:indicator="http://stix.mitre.org/Indicator-2"
  xmlns:example="http://example.com"
  xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd
    http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd
    http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
    http://cybox.mitre.org/common-1 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
  ">
```

Next, we need to set the xsi:type to `indicator:IndicatorType`. After that's done, we should be able to autocomplete elements. The same pattern will apply to any component.

```xml
<stix:Indicator xsi:type="indicator:IndicatorType">
```

Before we add content though, we should set an ID and timestamp. Following the suggesting practice, we set the prefix to our producer prefix, use "indicator-" as the basis for the ID portion, and generate a new GUID to fill in the rest:

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
```

Like we did with STIX_Header, we also look at the suggested practices for STIX indicators to see what elements we should add. They are:

* Either Observable, Observable Composition, or Indicator Composition to represent the detectable pattern
* Title
* Type
* Valid_Time_Position
* Indicated_TTP, even if pointing to a very simple TTP with just a title
* A confidence assertion

### Set the Indicator Title and Type

That looks like a lot, but a couple are easy: `Title` and `Type` are very similar to the `Title` and `Package_Intent` fields on `STIX_Header`: title is just a title for the indicator, and type indicates what general type of indicator it is (using a controlled vocabulary).

It might be worth seeing if you can add these yourself before looking to see how I did it. Specifically, make sure you can identify the fact that `Type` is a controlled vocabulary field and, from there, figure out which vocabulary to use.

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975">
  <indicator:Title>Malware XYZ Hashes</indicator:Title>
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
</stix:Indicator>
```

### Set the Observable Pattern using CybOX

Alright, this is going to get a little more complicated. Since STIX uses CybOX to represent cyber observable patterns in indicators, we need to move on to CybOX. Basically, we're filling out the "what to look for" portion of an indicator using CybOX.

Essentially we need to identify the correct CybOX object to use for file hashes and then create a static pattern observable in CybOX that represents the hash. What does that mean? First, we need an observable wrapper to contain the CybOX pattern. Then, we need an Object element to indicate that we're creating a static (stateful measure) observable instead of a dynamic (event-based) observable. Lastly, we add a CybOX object, using the Properties field, and give it the properties we want the indicator to look for.

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

Notice that we've assigned IDs for the Observable and Object. CybOX IDs are recommended on major components and follow the same format as STIX IDs. You'll also see that we've started using the "cybox" namespace, which has not been defined yet. If you're using an XML tool, it probably complained at you. The fix, as usual, is to import this schema.

#### Object Properties

Next, we need to identify the correct CybOX object type to use to represent file hashes. Looking through the list on the [CybOX release page](http://cybox.mitre.org/language/version2.1/), the best choice seems to be the FileObject. Opening the documentation for that object, we can see that it does include a Hashes element that we can use to represent file hashes. As we did when we added the Indicator component, we'll need to add this schema to our instance document by defining the namespace prefix in the head of the document and adding the mapping to the schema in the `schemaLocation` attribute.

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:stixCommon="http://stix.mitre.org/common-1"
  xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
  xmlns:cybox="http://cybox.mitre.org/cybox-2"
  xmlns:indicator="http://stix.mitre.org/Indicator-2"
  xmlns:FileObj="http://cybox.mitre.org/objects#FileObject-2"
  xmlns:example="http://example.com"
  xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd
    http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd
    http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
    http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd
    http://cybox.mitre.org/common-1 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd
    http://cybox.mitre.org/objects#FileObject-2 http://cybox.mitre.org/XMLSchema/objects/File/2.1/File_Object.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
  ">
```

You'll need to do this every time you use a type from a new schema (generally when you use xsi:type) unless it has already been added.

Next, we'll create the `Properties` element and fill in the `xsi:type`:

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
      <cyboxCommon:Simple_Hash_Value condition="Equals" apply_condition="ANY">01234567890abcdef01234567890abcdef##comma##abcdef1234567890abcdef1234567890##comma##00112233445566778899aabbccddeeff</cyboxCommon:Simple_Hash_Value>
    </cyboxCommon:Hash>
  </FileObj:Hashes>
</cybox:Properties>
```

This looks a little bit complicated, but you should be able to see the logic behind it now that you understand how STIX and CybOX work. We have a couple wrapper elements around the hashes, then a controlled vocabulary describing the type of hash and a `Simple_Hash_Value` field with the hashes to look for. Of course, you'll also seem some extra stuff there: the `condition` attributes, the `apply_condition`, and the `##comma##` separators.

#### CybOX Pattern Fields

Here's how it works: all of the lowest-level fields in CybOX representing cyber observables data extend from a field that implements CybOX patterning capability called `BaseObjectPropertyType`. That type adds fields and defines behavior for CybOX patterning. There are two fields you will see used very frequently in indicators:

* `condition`, which specifies how to match the target (data you're applying the indicator against) to the pattern
* `apply_condition`, which specifies how multiple items should be matched

As you probably guessed, `##comma##` is used to separate multiple list items. So, how do you use these fields?

First, decide on an appropriate condition. For this hash match, we use "Equals" because we want to test whether file hashes equal each other. When using observables in an indicator (or really any time you use observables for patterns) you need to have the condition attribute set. Omitting it implies the CybOX observable was an instance.

As another example, if we were testing for IP Addresses in a range we might use "Starts_With" and supply a partial IP address, or if we were searching for keywords in an e-mail we could use "Contains" and supply the keywords. The various CybOX conditions and how they work are described in the schema annotations.

Next, if you have a single item to test against (single hash, single IP, whatever) you can move on, you don't need to use `@apply_condition`. If you do have multiple values, it's likely that you want the pattern to match if any of them match, in which case you should use `@apply_condition="ANY"`. This is essentially a blacklist. An alternative is to use `@apply_condition="NONE"` and provide good values instead of bad values, which is essentially a whitelist. Finally, you can test that the tested values matches ALL of the items in the list using `@apply_condition="ALL"`.

That's basically how to use CybOX patterns. Remember that to create a CybOX pattern you always need to use the `condition` attribute, even if you just set it to "Equals".

### Add the Confidence and Valid_Time_Position

It's generally a good idea to include a confidence in your indicators so you can let consumers know how confident in it you are and a valid time position to let them know when the indicator is valid for. Note that these are not required, it's just a suggested practice. In particular, in a lot of cases you won't have a defined time window for indicators. When this happens, it's fine to omit the time position.

These fields are fairly standard STIX, so I'll just show you the end result. It might be a good exercise to try adding them yourself first, though.

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

The `Valid_Time_Position` is added above Observable (most STIX elements are ordered) and the `Confidence` structure is added below it. Did you catch the controlled vocabulary for Confidence/Value and remember to add the timezone for the `Valid_Time_Position`? We also started using a new vocabulary in the CybOX vocabularies namespace, so you would have needed to import the CybOX vocabularies namespace/schema as we did for the STIX vocab schema earlier.

## Add the TTP

Stepping back from the indicator, the next step is to represent the TTP that the indicator indicates. In STIX, TTPs are used to represent three primary concepts:

* Resources (infrastructure and tools)
* Behavior (attack patterns, malware, exploits)
* Victim Targeting

In this case, we want to represent a piece of malware. For this example we'll just give it a name, but you could also represent more complicated information about it using something like MAEC.

First, we need to import the TTP schema by defining the namespace and adding it to the schemaLocation. I won't show what this looks like for space reasons, but just replace what we did for indicator with TTP (making sure to copy the namespace and XSD location correctly).

Next, we add the TTPs element with an xsi:type, id, and timestamp:

```xml
<stix:TTPs>
  <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd" timestamp="2014-05-08T09:00:00.000000Z">
  </stix:TTP>
</stix:TTPs>
```

### Setting the malware information

Next, we'll give it a title appropriate to the malware we want to represent and a Behavior/Malware instance to identify the malware:

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

## Bringing it all together

Alright, now we've got an indicator with file hashes for a piece of malware and a representation of the malware itself in a TTP. How do we say that when we see the indicator, it might indicate you're seeing malware activity? Just having them in the same package is not enough.

This is where STIX relationships come in. Essentially, we want to relate the Indicator to the TTP using the "Indicated_TTP" field on the indicator:

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975" timestamp="2014-05-08T09:00:00.000000Z">
  <!-- snip -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP idref="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd"/>
  </indicator:Indicated_TTP>
</stix:Indicator>
```

As you can see, a relationship is fairly straightforward to add. All you have to do is add the wrapper element, create a new TTP (no need for the `xsi:type` in this case, since `@idref` is on the base type), and set the `@idref` to the ID of the TTP that you want to point to. That TTP can be in the same document, a document you send alongside it, or even in a document that was sent at another time. Essentially, relationships in STIX are considered global, not local.

One other note about relationships is that, if we wanted, we could reference a specific version of the TTP by including the timestamp field. For example:

```xml
<indicator:Indicated_TTP>
  <stixCommon:TTP idref="example:ttp-f3eb3e3f-fb53-427e-9171-ff5bc0b1e6cd" timestamp="2014-05-08T09:00:00.000000Z"/>
</indicator:Indicated_TTP>
```

That will reference the specific version of the TTP that was published with the timestamp "2014-05-08T09:00:00.000000Z". In this case though, we want to reference the "latest" version of that TTP as it evolves so leave off the timestamp field.

An alternative to the reference-based approach using @idref is embedding the TTP inside the indicator. For the most part, STIX relationships allow either approach. The [suggested practices](https://github.com/STIXProject/schemas/wiki/Suggested-Practices-(1.1)#wiki-referencing-vs-embedding) page has some guidelines for when to use each. As an example of embedding, we can just copy the TTP itself into the indicator where previously we had the TTP with an `idref`:

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:indicator-3c3885fe-a350-4a5c-aae3-6f014df36975">
  <!-- snip -->
  <indicator:Indicated_TTP>
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
  </indicator:Indicated_TTP>
  <!--snip-->
</stix:Indicator>
```

Note that the TTP looks essentially the same regardless of whether it's embedded or referenced. You do need the `xsi:type` in this case, by the way.

# Summary

Congratulations, you just wrote a STIX document. It might be a simple one, but you've learned STIX concepts that will let you compose much more complicated documents once you learn the rest of the data model.

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
                <cyboxCommon:Simple_Hash_Value condition="Equals" apply_condition="ANY">01234567890abcdef01234567890abcdef##comma##abcdef1234567890abcdef1234567890##comma##00112233445566778899aabbccddeeff</cyboxCommon:Simple_Hash_Value>
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

If this were a class, I'd say you just graduated from "basic" STIX. The next steps are really going to depend on what you want to use STIX for. You could start looking at [Tools](https://github.com/STIXProject/schemas/wiki/Tools) 
 to understand how to build STIX programmatically (or to visualize STIX documents), look at the full report samples on our [samples page](http://stix.mitre.org/language/version1.1.1/samples.html), or study the documentation more in-depth. If you're not quite sure, feel free to contact us at stix@mitre.org and maybe we can help guide you.