---
layout: idiom
title: "Extension Points and xsi:type"
---

STIX makes heavy use of extension points for various reasons.

The first, and most obvious, is to allow several implementations for a given field. For example, data markings are implemented using an extension point to allow users to choose which type of data markings they want to use (if any). Some users might want TLP, others might want just a simple marking statement, and others might have something specific to their organization or industry. STIX recognizes that for many situations a single implementation will not work for everyone, so simply provides an extension point so that users can use whichever they want (assuming all parties in the sharing arrangement agree on this of course).

A second reason STIX uses xsi:type is to loosely couple separate components from the core schema. Each of the STIX components (with the exception of CybOX) is implemented as an "extension point". In this case, the assumption is that except for extraordinary circumstances the "extension point" will be implemented using the standard STIX component. The [IndicatorBaseType](/documentation/stixCommon/IndicatorBaseType) extension point (in STIX Package/Indicators) should be implemented with [IndicatorType](/documentation/indicator/IndicatorType) from the indicators schema, for example (you will see this when we get farther in the document).

A third reason (well, really just a variety of the first) is to implement controlled vocabularies. While controlled vocabularies in some ways are simply a specific use of extension mechanisms, in other ways they have their own goals and purposes so we think about them separately from normal extension points.

## XML Implementation

`xsi:type` is a standard XML and XML schema mechanism for enabling type hierarchies (inheritance, if you're an object-oriented programmer). Essentially, STIX uses this to create abstract placeholders for concrete implementations. The abstract placeholders are the extension point and the concrete implementations are the extension implementation.

As an example, STIX uses extensions to allow marking data with different marking models (see the [data markings idiom](/idioms/features/data-markings)). The *extension point* is the `Marking_Structure` field in [MarkingType](/documentation/marking/MarkingType), which is directly typed as [MarkingStructureType](/documentation/marking/MarkingStructureType). The use of the `xsi:type` attribute, however, allows the producer to override that type with anything that extends from it. The various data marking extensions all define types that extend from MarkingStructureType and add fields appropriate to that marking model: for example, [TLPMarkingStructureType](/documentation/tlpMarking/TLPMarkingStructureType) extends from MarkingStructureType to add an attribute to indicate the TLP color.

The same mechanism is used to abstract away the specific implementation of STIX components [TTPType](/documentation/ttp/TTPType), [CourseOfActionType](/documentation/coa/CourseOfActionType), etc. from the places they are used. The places a TTP is used are typed as [TTPBaseType](/documentation/stixCommon/TTPBaseType) in the STIX Common schemas, which means that they don't need to import the TTP schema in order to reference TTPs. This allows the schemas to avoid importing each other unnecessarily and therefore makes it easier to use them in isolation.

As a variation on the first use case, the STIX controlled vocabulary implementation uses an extension point off of any field implemented as [ControlledVocabularyStringType](/documentation/stixCommon/ControlledVocabularyStringType). Each controlled vocabulary defined in the controlled vocabularies schema extends from that type and can therefore be used for those controlled vocabulary fields.

## Using xsi:type for components

As explained above, all STIX components are extended from a base type defined in the STIX common schema. That type is then used throughout the other schemas as a placeholder for the actual component type.

Because of this, it's often confusing to new users of STIX who wonder why the type directly used in the schemas has so few fields defined. For example, in the `Indicators` list in `STIX Package`, the type for the list of indicators is [IndicatorBaseType](/documentation/stixCommon/IndicatorBaseType), not [IndicatorType](/documentation/indicator/IndicatorType). IndicatorBaseType only defines the ID and timestamp fields, not the full indicator structure. Therefore, it can seem like something is missing, and in fact it is. Simply set the `xsi:type` correctly to IndicatorType and you can use all of the expected fields.

In the Python APIs this is automatically handled for you when you assign a full indicator to an IndicatorBaseType extension point. The libraries will allow you to do this and set the `xsi:type` automatically so you don't have to worry about it. JAXB bindings in Java will do the same.

## Using xsi:type for extension points

Similar to using xsi:type for components, using it for extension points requires understanding that certain fields in STIX aren't "complete" unless they have an extension implementing it. The MarkingStructureType mentioned above is one instance of this. In other cases, like [MalwareInstanceType](/documentation/ttp/MalwareInstanceType), the extension point has fields itself and may be used as a baseline implementation without an extension. The extension, however, adds additional capabilities: in this case, the [MAEC4.1InstanceType](/documentation/stix-maec/MAEC4.1InstanceType/) extension allows you to represent a full MAEC characterization of a piece of malware in addition to the fields given by MalwareInstanceType.

In order to make identifying these places easier, the STIX schema annotations and documentation will indicate which types define an extension point and list any extensions provided by STIX. Extensions provided by third parties or defined by producers will need to be communicated and understood out of band. Though STIX extensions can be a powerful way to exchange information, consumers and producers must agree ahead of time which extensions will be used, particularly when they are not a part of the STIX distribution.

## Using xsi:type for controlled vocabularies

STIX controlled vocabularies are implemented via [ControlledVocabularyStringType](/documentation/stixCommon/ControlledVocabularyStringType). When used without `xsi:type`, that field allows any value in the field. For example, [ConfidenceType](/documentation/stixCommon/ConfidenceType)'s `Value` field is a controlled vocabulary. If the field doesn't have an `xsi:type` it is not bound to any particular controlled vocabulary and arbitrary string values can be used. You could set the confidence value to "Extra Confident!", for example. Without the type, however, consumers may not know what the field value really means: is "Extra Confident!" more or less confident than "Very Very Confident!"? Similarly, without the controlled vocabulary inconsistencies may arise between instances (e.g. one time "Extra Confident!" may be used but another time it may be "Extra Confident" which is similar but not the same).

Using a defined vocabulary allows producers and consumers to agree on a defined set of values that have a shared meaning. [HighMediumLowVocab-1.0](/documentation/stixVocabs/HighMediumLowVocab-1.0) defines confidence as either high, medium, or low. While not a precise definition, at least the relative values are known: high is the highest value, medium is in the middle, and low is the lowest. To indicate a field uses the HighMediumLow vocabulary, as with the extension points, the `xsi:type` attribute should be set to `HighMediumLowVocab-1.0`.

For further reading on this topic, see the [Controlled Vocabularies](../controlled-vocabularies) idiom.

## Further Reading

Use of `xsi:type` from a consumer's perspective is explained in the [sample walkthrough](/getting-started/sample-walkthrough) and from a producer's perspective in the [authoring tutorial](/getting-started/authoring-tutorial).