---
layout: flat
title: Sample Walkthrough
---

This walkthrough will look at a simple STIX document and look through it piece by piece to help describe basic STIX concepts. Specifically, we'll look at a watchlist for IP addresses to see how STIX can be used to describe indicators of malicious activity.

## Prerequisites

Prior to going through this walkthrough, you should understand the general concept of what STIX is, what problems it is designed to solve, and how it is used to solve those problems. The best place to do that is by going to the [Getting Started](/getting-started) page and reading through the whitepaper and other materials linked from there.

You also should have good XML tools in order to work with STIX. Most of the STIX team uses either Oxygen or XMLSpy, which are both commercial products. Eclipse is an open-source option that is somewhat less fully-featured but should get the job done.

Finally, this tutorial does assume intermediate knowledge of XML. You should know what elements are, what attributes are, what validation means, and other basic concepts. If you don't, it's suggested that you either use higher-level tooling when working with STIX or read up on XML before looking into STIX.

## Get Started

First, download the [IP Watchlist sample](IP_Watchlist-1.2.xml) we'll be working with. It's very similar to the one hosted on the STIX sample page except I've modified the ```schemaLocation``` attribute to use the online schemas so you can validate it without a local copy of the schemas. Open this file up in your XML editor.

The intent of this file (if it were a real file and not an example) would be to provide a list of IP address that are suspected (or known) to be malicious. In STIX, this is done using the Indicator construct, utilizing CybOX observables: the CybOX observable is a pattern that matches data that can be observed (IP addresses in network traffic, for example) while the STIX indicator describes what it means when the CybOX pattern matches.

Let's get started at the very top by looking through the XML Namespace declarations.

## Namespaces and Schema Locations

```xml
<stix:STIX_Package
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:stix="http://stix.mitre.org/stix-1"
  xmlns:indicator="http://stix.mitre.org/Indicator-2"
  xmlns:cybox="http://cybox.mitre.org/cybox-2"
  xmlns:AddressObject="http://cybox.mitre.org/objects#AddressObject-2"
  xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
  xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
  xmlns:example="http://example.com/"
  xsi:schemaLocation="
  http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.2/stix_core.xsd
  http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd
  http://cybox.mitre.org/default_vocabularies-2 http://cybox.mitre.org/XMLSchema/default_vocabularies/2.1/cybox_default_vocabularies.xsd
  http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.2.0/stix_default_vocabularies.xsd
  http://cybox.mitre.org/objects#AddressObject-2 http://cybox.mitre.org/XMLSchema/objects/Address/2.1/Address_Object.xsd"
  ...>
```

If you're used to XML, you might notice that even this short STIX document contains quite a few namespace prefix declarations. This is because of an intentional design decision made by the STIX team to ensure that the schemas were modular and could be used independent of each other. To walk through the various schemas that you'll see being defined:

|Prefix|Description|
|---|---|
|`xsi`|This is a standard XML Schema Instance namespace. You'll see this used later on in the content as part of `xsi:type`.|
|`stix`|This is the core STIX schema, which defines the `STIX_Package` element and the `STIXType` type.|
|`indicator`|This namespace contains the STIX Indicator component. Each of the 7 (8 if you count CybOX) core STIX components are in their own schema and namespace.|
|`cybox`|This namespace contains the CybOX Observable structure (sometimes considered the 8th STIX component). STIX uses CybOX to represent Cyber Observables. This tutorial will walk through how to use both STIX and CybOX, so don't worry if you don't know how to use it.|
|`AddressObject`|This namespace contains a CybOX "Object". CybOX defines 80+ objects that each represent a certain type of Cyber Observable. The Address Object, for example, represents address: IP Address, E-mail Addresses, etc.|
|`cyboxVocabs`, `stixVocabs`|These namespaces define the CybOX and STIX default vocabularies, respectively. We'll walk through what these are and how to use them later.|
|`example`|This is a special namespace in that it's used in instance content and does not have an associated schema. It is used to prefix STIX and CybOX IDs with the conceptual "producer" of the content. In this case, we just use "example" because this is an example. When you consume content, you will probably see various namespaces instead of example to represent whoever is producing the content you're consuming.|

You'll also notice a `schemaLocation` attribute with these schema namespaces mapped to the actual schema (separated by spaces). This is simply a hint to XML editors so that they can automatically find the schemas and validate against them.

## STIX_Package

```xml
<stix:STIX_Package
  ...
  id="example:STIXPackage-33fe3b22-0201-47cf-85d0-97c02164528d"
  version="1.2">
```

At the top level of almost every STIX document will be the `STIX_Package` element. This element is a wrapper around a header, which contains metadata about the information in the package, and the lists of components (indicators in this case) that make up the package. It also contains the namespace prefix declarations and schema location attribute, as described above.

One attribute you'll see on STIX_Package is `version`. This version attribute is strongly suggested when creating content and indicates which version of STIX the package conforms to. In this case, the package conforms to STIX 1.2.

The other important attribute is `@id`. As you might expect, the `@id` is a globally unique ID given to an instance of a construct in STIX. STIX suggests several practices for creating and using IDs that you can see on our [Suggested Practices](/documentation/suggested-practices#formatting-ids) page. (I'll take a timeout to let you read that section). As you can see, in this case we've set the namespace portion of the ID to "example" and the ID portion to "Indicator-33fe3b22-0201-47cf-85d0-97c02164528d" in keeping with STIX suggested practices. You'll also remember that we had defined the example namespace in the head of the document:

```xml
xmlns:example="http://example.com/"
```

It's required to define all prefixes used in the IDs in your document.

## Indicators

```xml
<stix:Indicators>
  <stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-33fe3b22-0201-47cf-85d0-97c02164528d" timestamp="2014-02-20T09:00:00.000000Z">
    <!-- snip -->
  </stix:Indicator>
</stix:Indicators>
```

After the STIX header, the rest of the content consists of lists of components. In this case, the only type of component is Indicator so it's just a list of indicators. If there were TTPs, Incidents, or other components then there would be lists of those as well.

## Indicator

Finally, the meat of the document: a STIX indicator. Once again, STIX indicators are used to give context to what it means when a particular CybOX pattern matches data that was observed in an environment. In many cases the Indicator will contain an Indicated_TTP field that describes the TTP that the pattern indicates, but in this case we just have a simple description.

<div class="well well-sm">The reason this walkthrough focuses on indicators, and the reason we'll go in depth now, is that indicators are one of the most common components used in STIX content today. If you want to see an in-depth walkthrough of another component, e-mail <a href="mailto:{{ site.contact_email }}">{{ site.contact_email }}</a> and let us know.</div>

There's a lot going on up there, so let's take a look at each element one at a time.

### Indicator Element Header

```xml
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-33fe3b22-0201-47cf-85d0-97c02164528d" timestamp="2014-02-20T09:00:00.000000Z">
```

Though we're looking at an indicator now, the two pieces of data we'll look at apply to all STIX components.

The first thing to note is that the xsi:type attribute is used to indicate that we're implementing the `IndicatorBaseType` extension point on the `Indicator` element with a type of `IndicatorType` (see concept note below). For each component you add (except Observable) you will need to do this.

<div class="well well-sm">
<h4>Concept: xsi:type</h4>
<p>xsi:type is a standard XML and XML schema mechanism for enabling type hierarchies (inheritance, if you're an object-oriented programmer). Essentially, STIX uses this to create abstract placeholders (in this case, the Package_Intent element) that can be filled in with specific implementations (in this case, <code>PackageIntentVocab-1.0</code>). Whenever you see an <code>xsi:type</code> attribute in an instance document it means that it's implementing an extension point.</p>
<p>STIX uses extension points for several reasons. The first, and most obvious, is to allow several implementations for a given field. For example, data markings are implemented using an extension point to allow users to choose which type of data markings they want to use (if any). Some users might want TLP, others might want just a simple marking statement, and others might have something specific to their organization or industry. STIX doesn't want to force everyone to use the same implementation, so simply provides an extension point so that users can use whichever they want (assuming all parties in the sharing arrangement agree on this of course).</p>
<p>In many cases, STIX provides extensions to fill these uses: for data markings, it provides both a TLP implementation and a mechanism to make simple statements. That does not mean users are limited to these extensions, however, they are free to use anything they want (again understanding that all parties must understand this marking extension).</p>
<p>A second reason STIX uses xsi:type is to conceptually separate components from the core schema. Each of the STIX components (with the exception of CybOX) is implemented as an "extension point". In this case, the assumption is that except for extraordinary circumstances the "extension point" will be implemented using the standard STIX component. The <code>IndicatorBaseType</code> extension point (in STIX_Package/Indicators) should be implemented with <code>IndicatorType</code> from the indicators schema, for example (you will see this when we get farther in the document).</p>
<p>A third reason (well, really just a variety of the first) is to implement controlled vocabularies.</p>
<p>While controlled vocabularies in some ways are simply a specific use of <code>xsi:type</code> extension mechanisms, in other ways they have their own goals and purposes so we think about them separately from normal extension points.</p>
</div>

Next, notice the ID and timestamp attributes. We suggest giving all top-level components in STIX an ID compliant with our [Suggested Practices](/documentation/suggested-practices#formatting-ids) and, as explained above, whenever you give a versioned construct an ID you should give it a timestamp.

### Indicator Type

```xml
<indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
```

The indicator type field is used to describe, not surprisingly, what type of indicator is being represented. The `indicator:Type` field is an instance of a controlled vocabulary (see concept note below), which is a special usage of `xsi:type` to describe vocabularies.

In this case, we're saying that the type of indicator we're representing is an "IP Watchlist", and the definition for what that means is in `stixVocabs:IndicatorTypeVocab-1.1`.

<div class="well well-sm">
<h4>Concept: Controlled Vocabulary</h4>
<p>The goal for STIX controlled vocabularies is to allow for the expression of an item in a vocabulary (in this case <code>Indicators - Watchlist</code>) as well as an identification of which vocabulary this comes from (in this case, <code>PackageIntentVocab-1.0</code>), if any. You can identify a field that uses a controlled vocabulary in the schema by noticing that its type is <code>ControlledVocabularyStringType</code> (or other controlled vocabulary types in CybOX). In many cases, STIX or CybOX also provide a default vocabulary for a field. If this is the case, it will be noted in the schema annotations and that type will be defined in, as you might guess, <code>stix_default_vocabularies.xsd</code> or <code>cybox_default_vocabularies.xsd</code>. In this case, the author used the STIX default vocabulary for the field by setting the xsi:type to the type noted in the annotations.</p>
<p>In general, if STIX provides a default vocabulary it's best to use that vocabulary unless you have a good reason not to. That way users of STIX can understand what you mean without having to rely on external definitions and the community can standardize on vocabularies.</p>
<p>One note is that in some cases you might need to represent a value without explicitly defining the vocabulary. If that's the case, you can leave the xsi:type off and just enter your value. Understand, however, that by doing this you're relying on consumers to understand your value without having it defined anywhere.</p>
</div>


### Indicator Description

```xml
<indicator:Description>Sample IP Address Indicator for this watchlist. This contains one indicator with a set of three IP addresses in the watchlist.</indicator:Description>
```

Indicator description should be pretty self explanatory. The only note is that there's also a title field (not used here) that is recommended whenever you can give an indicator a human-readable title. Essentially the title and description can allow you to give context to an indicator without having to represent a full TTP using `Indicated_TTP`. For example, the title could say "Known Malicious Traffic from Botnet XYZ" and that means that when the indicator triggers (aka when the CybOX pattern is observed in real data) it might indicate (hence the term indicator) that there is "Known Malicious Traffic from Botnet XYZ". More advanced tutorials can describe better approaches for doing this than simple titles and descriptions, using Indicated_TTP.

<div class="well well-sm">
<h4>Concept: CybOX</h4>
<p>The observable is the first place we've seen actual CybOX in this file. The Observable portion of an indicator describes what, at a technical level, the indicator should trigger on. In this case, because this is an IP Watchlist indicator, we would expect the Observable to describe a list of IP addresses. Continuing on, let's see how CybOX implements this.</p>
</div>

### Observable

```xml
<indicator:Observable  id="example:Observable-1c798262-a4cd-434d-a958-884d6980c459">
  <!-- snip -->
</indicator:Observable>
```

The CybOX observable layer is a wrapper around a CybOX entity, either an object or an event. Objects describe stateful measures (like an IP address or file) while events describe changes that take place (like a file being written). In this case, we'll focus on objects because that's what are most commonly used in indicators. Other than just wrapping the object or event, the Observable layer provides a place to put metadata such as the information source and a title and description. It also provides the capability to do what is called Observable Composition, which is not used in this document but allows for indicators to contain logical combinations of CybOX object patterns at the observable layer. For now, you can just think of it as a wrapper.

You'll probably notice that the header looks quite a bit like the header for indicator, minus the xsi:type and timestamp. We try to use consistent practices across STIX and CybOX so you can easily work with both. In this case, the `@id` is formatted per STIX Suggested Practices for formatting IDs, which are intentionally the same as the [CybOX Suggested Practices](https://github.com/CybOXProject/schemas/wiki/Suggested-Practices#formatting-ids). One important difference is that CybOX observables (and objects and events) are not versioned and so do not support a `@timestamp` at the top level.

### Object

```xml
<cybox:Object id="example:Object-1980ce43-8e03-490b-863a-ea404d12242e">
  <!-- snip -->
</cybox:Object>
```

The object is a representation of a stateful measure in CybOX. It can contain many different things, the most important of which are object properties. They aren't used here, but object relationships, a description of how the object was collected, and other metadata are also part of the object model.

### Object Properties

```xml
<cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
  <AddressObject:Address_Value condition="Equals" apply_condition="ANY">10.0.0.0##comma##10.0.0.1##comma##10.0.0.2</AddressObject:Address_Value>
</cybox:Properties>
```

There's a lot going on in this section so we'll take it one level at a time. At the top level (Properties element) you can see our familiar friend `xsi:type`. Yes, CybOX uses the `xsi:type` extension mechanism too, in this case to allow for representation of any one of the 80+ object types that CybOX defines.

Essentially, each of those objects inherits from a type called `cyboxCommon:ObjectPropertiesType`. The AddressObject, FileObject, WinRegistryKeyObject, and all other object types inherit from this same type. Then, the CybOX Object structure has a field called `Properties` that is that same type, meaning that it can be filled with any type that inherits from `cyboxCommon:ObjectPropertiesType`, or in other words any CybOX object. This means that we can use any object here without having to limit it to a defined set of objects.

When creating a `Properties` element, the author fills in the `xsi:type` attribute with the type of the object that they want to use. They also need to define the prefix in the head of the document and, if using schemaLocation, add that schema to the list. When looking at a document, you can tell what object type is being used just by looking in that same attribute. In this case, we know we're looking at an AddressObject. It's AddressObject, in fact, that adds the `@category` field to the `Properties` element. It's also what defines the list of object property fields that are available. That way the FileObject can have a list of fields applicable to describing files, the AddressObject can have a list of fields applicable to describing addresses, etc.

In this case, we have just one field: `Address_Value`.

### Concept: CybOX Object Property Fields

```xml
<AddressObject:Address_Value condition="Equals" apply_condition="ANY">10.0.0.0##comma##10.0.0.1##comma##10.0.0.2</AddressObject:Address_Value>
```

There's also a lot going on here, so we'll walk through it slowly. The first thing to note is that this field is defined in the AddressObject schema yet contains a general set of attributes applicable to all objects. CybOX has a set of properties called "Object Property Types" that may have a different name (`Address_Value` in this case) but all work the same way. This is done so that regardless of which field of an object you're working with you'll know it has a consistent set of features. In this case, we'll describe these features in the context of an IP address but they're just as applicable to a File's File_Name, a registry key, a user account name, or any other CybOX object property field.

Looking at the first attribute, `condition`, you can probably start to guess what it means. But before going into that, let's talk about a new concept: CybOX Observable Instances vs. Patterns.

<div class="well well-sm">
<h4>Concept: Observable Instance vs. Pattern</h4>
<p>CybOX observables play two related, but different roles: they can represent an instance of an observable (something that was actually seen) or they can represent a pattern (something that might be seen). When used as an instance, they can describe the exact values that were observed while when used as a pattern they use conditional statements to describe the set of things that would or would not match that observable. When used in indicators, you always want to use a CybOX pattern observable. The way to do this is to set the `@condition` attribute: if the condition is set, the Observable is a pattern, while if it isn't set the Observable is an instance.</p>
</div>

In this case, the `@condition` attribute is set to "Equals", which means we're doing a simple equality test. Other options are listed in the documentation and include pattern matching, greater than/less than, contains, and others.

The next attribute is called `@apply_condition`, is used only when providing multiple values to match against. If you were matching a single IP address against any type of condition, you would not need to use apply condition. In this case though, we want to test against a list of IPs, and `@apply_condition` describes how to do that. In this case, the value of "ANY" means that the pattern should match if ANY of the values in the list match the test value. The other values "ALL" and "NONE" match when either all of the list items match the tested value or none of the list items match the tested value.

The delimiter `##comma##` is used to represent a list of values. The reason this is used instead of a literal ',' is that a literal ',' is often found in actual data and we didn't want to worry about having to escape it all the time. So when you see `##comma##` just think of it as a token-separated list of values where the token is `##comma##`. In this case, we have three values: 10.0.0.0, 10.0.0.1, and 10.0.0.2. Taking the list of values in combination with apply_condition and condition, this field essentially states that the observable pattern matches when the target IP address "Equals" "ANY" of 10.0.0.0, 10.0.0.1, or 10.0.0.2. If we had different condition or apply_condition attributes, the indicator would match differently. If necessary you can override the delimiter by specifying the `@delimiter` attribute, but in most cases the default should work fine.

If the observable pattern inside an Indicator matches the data that is being tested against, we say that the Indicator has "triggered". This means that whatever the indicator is indicating (ha) might be present: if there's a title and description, you could look inside that to see what it means. If there's an Indicated_TTP, the indicator triggering indicates (yes there's a lot of indicating going on) that the TTP might be being practiced in your infrastructure.

## Summary

To summarize, there are several main fields in this instance document:

* `STIX_Package` is a wrapper around a bunch of content that gives it a defined meaning (including Package_Intent, data markings, and Title)
* `STIX_Header` is the mechanism to represent the defined meaning for a STIX_Package
* `Indicator` is a way of describing a pattern for something you might observe in cyber (using CybOX) and the context to give it meaning
* CybOX (`Observable`, `Object`, Object Properties) are the way of representing that pattern (when used for indicators, they can also represent instances of things that were actually observed).

## Where to go from here

This tutorial took a look at a very basic indicator. You might be thinking "why should I use STIX when it takes 54 lines of complicated XML just to describe 3 IP addresses?" That's a good point, but it's important to keep in mind that STIX offers a lot of capabilities and when it's used for simple examples (like this one) much of those capabilities are reflected in things that seem redundant. For example, the "Observable" and "Object" layer of CybOX provide many capabilities that were not used, so they look superfluous. As you start to use more advanced capabilities, you'll begin to see that the things that might seem bulky in simple use cases become important.

To start to work towards more advanced indicator matching, some concepts to research are:

* Observable composition, which allows you to combine multiple observables into a logical combination of AND/OR for more complicated matching
* Indicator composition, which allows you to combine multiple indicators into a logical combination of AND/OR for more complicated matching
* Other objects (File, E-mail Message, etc.), which of course can let you create indicators against other types of cyber observables
* Multiple fields in an object, which can let you create patterns against multiple fields on an object (file name and hash, for example)
* Indicated TTP, which can give more structured meaning to an indicator through use of the TTP component
* Suggested Course of Action, which can provide suggested mitigations, remediations, or other responses for when an indicator is observed.
