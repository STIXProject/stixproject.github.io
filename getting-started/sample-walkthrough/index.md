---
layout: getting_started
title: Sample Walkthrough
---

# Building a STIX document

Our goal is to capture three IP addresses in a `IP Watchlist` object, which will look [something like this](IP_Watchlist-1.1.1.xml).  

It demonstrates an `Indicator` which captures CybOX observables for each IP address combined with a STIX context around those values. 

## Define Namespaces and Schema Locations
First we declare the scope of the document, including a pointer to the sceham location.

```xml
<stix:STIX_Package
  xmlns:stix="http://stix.mitre.org/stix-1"
  xsi:schemaLocation="
  http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd"
    <!-- snip -->
  >
```

The following are commonly defined:

|Prefix|Description|
|---|---|
|`xsi`|Standard XML Schema Instance namespace|
|`stix`|Core STIX schema for root elements|
|`indicator`|The STIX Indicator component|
|`cybox`|The CybOX Observable structure |
|`AddressObject`|CybOX representation of an IP Address |
|`cyboxVocabs` and `stixVocabs`|Define accepted vocabularies|
|`example`|namespace for the content producer|



## Describe STIX Package

The `STIX_Package` contains metadata about the document, such as the creation time and a globally unique `ID` value.

The `version` attribute is optional but suggested when creating content  - defining the supported STIX schema version.
```xml
<stix:STIX_Package
  ...
  id="example:STIXPackage-33fe3b22-0201-47cf-85d0-97c02164528d"
  timestamp="2014-02-20T09:00:00.000000Z"
  version="1.1.1">

  xmlns:example="http://example.com/"
```

 `timestamp`  indicates when this version of the file was created. Suggested practice is to always include a timestamp with an ID, to allow for seamless updates of values with the same ID.

## Provide a header
`STIX_Header` describes the purpose and usage hints for the package. Typical fields include the package `Title`, a `Description` short summary of the content, its `Intent` and `Source`.  

```
<stix:STIX_Header>
  <stix:Title>Example watchlist that contains IP information.</stix:Title>
  <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Watchlist</stix:Package_Intent>
</stix:STIX_Header>
```

*Note:* xsi:type is used in STIX to handle inheritance and type hierarchies (. This allows abstract types such as Package_Intent to be overloaded with a particular vocabulary as an "extension". 

For instance, usage of `PackageIntentVocab` here will limit the range of valid input for `Intent`. Defaults are listed under [stix_default_vocab
ularies.xsd](https://github.com/STIXProject/schemas/blob/master/stix_default_vocabularies.xsd)

Any data markings such as classification or sharing restrictions will also be noted in this section. These can be implemented as `xsi:type` extensions to the `Handling` object of a given indicator - the DHS "Traffic Light Protocol" is included as a sane default. [For an example, see here](http://stix.mitre.org/about/example_datamarkings.html)


## Including an Indicator

Our `Indicator` is extended using `xsi:type` to cast it to the generic `IndicatorType` . Several can be included under the same `Indicators` tag.

```xml
<stix:Indicators>
  <stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-33fe3b22-0201-47cf-85d0-97c02164528d" timestamp="2014-02-20T09:00:00.000000Z">
<indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
<indicator:Description>IP addresses that are super malicious.</indicator:Description>
    <!-- snip -->
  </stix:Indicator>
</stix:Indicators>
```

The `Type` field denotes this as an `IP Watchlist`, selected from a controlled vocabulary, while the `Description` is a prose summary meant to be human readable.


## Creating an Observable

```xml
<indicator:Observable  id="example:Observable-1c798262-a4cd-434d-a958-884d6980c459">
<cybox:Object id="example:Object-1980ce43-8e03-490b-863a-ea404d12242e">
<cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
  <AddressObject:Address_Value condition="Equals" apply_condition="ANY">10.0.0.0##comma##10.0.0.1##comma##10.0.0.2</AddressObject:Address_Value>
</cybox:Object>
  <!-- snip -->
</indicator:Observable>
```

A CybOX observable wraps the properties of a given type of object, which is specified by its `xsi:type`. These are inherited from `cyboxCommon:ObjectPropertiesType` which provides `Properties` that are specific to each object type.

In this case the `Address_Value` field stores the IP addresses as a list. Note that '##comma##' is used instead of a literal comma to avoid special character conflicts.

# Setting a Condition

For the purpose of taking action on a STIX document, a `condition` defines how to match the given data against observations.

In this case, each IP address is seen as malicious if observed individually.

This modifier also supports data ranges and numerical comparisons, as well as ANY or NONE logical comparisons.

