---
layout: flat
title: Composition of Observables-Indicators
---


##Composition of Observables

As described in [Concept: Observable Instances vs Observable Patterns](../observable-patterns-vs-instances), there are two different forms of "Observables" possible in STIX: **observable instances** and **observable patterns**. Each form has its own purposes to represent various relevant information in STIX.

Whether you are characterizing instances or patterns, the types of observables you may wish to characterize can vary widely from the very simple to the complex depending on what you are trying to convey.

###Observable with single Object and single Property

   * Use for: characterize a single property
   * As an observable instance this very simply characterizes a single property value of a single instance object that was observed (e.g. a file with the name “foo.exe”)
   * As an observable pattern this very simply characterizes a condition where any object of the given type has a property value matching the specified pattern.
   * Mechanism: specified using the [condition](/data-model/{{site.current_version}}/cyboxCommon/PatternFieldGroup) attribute and field value of a single object property


###Observable with single Object and multiple Properties

   * Use for: characterize multiple properties of a single instance object (e.g. a file with the name “foo.exe” and a size of 1896Kb)
   * As an observable instance this simply characterizes multiple property values of a single instance object that was observed 
   * As an observable pattern this characterizes a condition where any object of the given type has property values matching all of the specified property field patterns. In other words, it is defining a logical AND across the set of property value patterns specified on the object.
   * Mechanism: specified using the `condition` attribute and field value on each relevant a single object property


###Observable with multiple related Objects (often referred to as "relational composition")

   * Use for: characterize a more complex situation involving multiple related objects (e.g. an email with a Subject of “Syria strategic plans leaked” and an attached file with File_Name of “bombISIS.pdf”)
   * As an observable instance this characterizes a more complex observation involving a set of related objects each with specific properties 
   * As an observable pattern this characterizes a condition where any full combination exists of the types of objects, the specific relationships and the specific property field patterns. In other words, it is defining a logical AND across not only the set of property value patterns specified on each object but also across the relationships between objects.
   * Mechanism: specified using the [Related_Object](/data-model/{{site.current_version}}/cybox/RelatedObjectType/) structure for relationships from one object to another using and the  `condition` attribute and field value on each relevant a single object property.


###Observable Composition through explicit use of the Observable_Composition structure (often referred to as “logical composition”)
**NOTE: Observables of this form are only valid as patterns and never as instances.**

   * Use for:  specifying compound observable conditions made up of logical combinations (AND/OR) of other observable conditions (patterns). The components of these compound conditions can be observable patterns of any level of detail including other observable compositions.
   * For example, a condition ((A OR B) AND C) where a system ((contains a mutex=“foo” | contains a file named “barfoobar”) & an outgoing network connection to 46.123.99.25).
   * Mechanism: specified using the [Observable_Composition](/data-model/{{site.current_version}}/cybox/ObservableCompositionType/) construct and its `operator` attribute



###Observable with single Object and single Property with multiple values (list)
**NOTE: Observables of this form are only valid as patterns and never as instances.**

   * Use for: specifying compound observable conditions made up of logical combinations (AND/OR) of patterns on a single object property
   * Mechanism: specified through the use of the `condition` and [apply_condition](/data-model/{{site.current_version}}/cyboxCommon/PatternFieldGroup) attributes on the property field and the inclusion of a delimiter (by default the delimiter is "##comma##” but can be overridden) separated list of values within the property field body.
   * **NOTE: This form of observable composition is semantically identical to use of "Observable Composition through explicit use of the Observable_Composition structure (often referred to as “logical composition”)” where each particular potential field value pattern is represented with its own full observable and all of the field value pattern observables are AND’d or OR’d together as specified by the `apply_condition` attribute. This “list” form of composition can be thought of as a significantly more concise and compact shorthand representation for these semantics. It is especially useful for patterns involving a very large number of potential field values (e.g. an IP watch list).**


##Composition of Observable Contexts (Indicators)

Beyond the various levels of detail possible to characterize observables directly using CybOX there is one more relevant level of composition dealing with observables and that is Indicator composition using [Composite_Indicator_Expression](/data-model/{{site.current_version}}/indicator/CompositeIndicatorExpressionType/).

Composition of observables directly using CybOX enables the **“factual” specification of arbitrarily complex patterns (independent of usage context)** for detection but in the end each observable only represents a single condition (as complex as it may be) to evaluate against. The evaluation is an all or nothing boolean (true/false) and offers no potential for partial evaluation matches on the pattern.

Indicators are about characterizing the **context for a given potential pattern of observation** and are intentionally abstracted from the technical details of specifying the “facts” of the pattern itself.  Indicators do not duplicate the underlying capabilities of CybOX to characterize/specify observables but rather layer contexts on top of them. Indicator composition in STIX is a composition of detection contexts each of which at its root has its own (potentially complex) “factual” observable pattern.

A mechanism for Indicator composition is provided in STIX to support three primary use cases that cannot be effectively addressed through direct observable composition in CybOX:


   * **The ability to characterize a context for an aggregate pattern where one of more of its parts may have their own relevant contexts that need to be specified.** For example, a single Indicator with an observable pattern for a particular file hash has the context of indicating a particular form of malware in broad use by various threat actors. This context is useful in and of itself and may be desired to be used for detection. Another single Indicator may exist with an observable pattern for network connections to a particular IP range known to be used as C2 infrastructure by a particular threat actor. Again, this context is useful in and of itself and may be desired to be used for detection. However, it may also be useful to detect the combination (AND) of these two patterns at the same time as being indicative of a particular campaign. The entire observable pattern composition could be duplicated in the new aggregate Indicator but that would be far less efficient, effective or consistent than simply allowing a logical composition of the two independent Indicators and specifying a new context for the aggregation.

   * **The ability to do "partial matching” on an aggregate pattern such that you can detect not only that the aggregate is true/false but also potential portions of the aggregate.** For example, a single Indicator with a single observable pattern for an IP watch list of three values would only be able to evaluate whether any one of those values was observed but not whether any particular one of those three were seen. An indicator composition OR’ing three independently defined  indicators (one for each IP value) would be able to evaluate to true/false if ANY of the IPs were seen but each individual Indicator could also be used to evaluate which particular IPs were seen.

   * **The ability to specify new compound detection contexts (Indicators) as appropriate from other preexisting Indicators (potentially created and shared by other players) in a way that yields new levels of contextual understanding but still maintains consistency and practical usefulness with the source Indicators of the composition.**



**NOTE: At the STIX language level, the complexity of Indicator composition is independent of the complexity of the underlying observable pattern. Each Indicator specifying an observable pattern treats that pattern as a simple boolean condition regardless of complexity.**


##Summary

Composition of Observables directly in CybOX is necessary to enable characterization of complex observations or specification of complex patterns for observation. This function cannot be accomplished at the Indicator composition level as Indicators not only lack the effective structures for complex observable pattern characterization but they are intentionally focused on providing context for the pattern.

Composition of Indicators is necessary to enable characterization of complex composite detection contexts (not just the pattern but also what the pattern means) where the individual sub-contexts of the composition are important and useful. This function cannot be accomplished at the Observable level as Observables are intentionally bound to “factual” characterizations/specifications of observables without contextual meaning to enable their flexible use in a range of differing contexts.

A range of differing levels of detail for composition (as described above) is available in STIX/CybOX and the [appropriate level to use should be determined by the context of use]().
