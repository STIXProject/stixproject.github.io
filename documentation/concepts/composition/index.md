---
layout: flat
title: Composition of Observables and Indicators
---


##Composition of Observables

In the parlance of STIX/CybOX, an observable is one or more events or stateful properties that are observable in the operational cyber domain.

As described in [Concept: Observable Instances vs Observable Patterns](../observable-patterns-vs-instances), there are two different forms of "Observables" possible in STIX: **observable instances** and **observable patterns**. Each form has its own purposes to represent various relevant information in STIX.

Whether you are characterizing instances or patterns, the types of observables you may wish to characterize can vary widely from the very simple to the complex depending on what you are trying to convey.

<button class="btn btn-primary" id="expand-all" data-all-state="collapsed">Show all Examples</button>


###Single Objects
Lets begin with the simplest form of observable, a single property such as a filename. 

Whether you want to convey an instance or a pattern on the property, the mechanism CybOX utilizes to convey this information is the Object. The CybOX Object construct enables the characterization of a given type of object (e.g. File, Email_Message, Network_Connection, Address, etc.). The structure allows the object characterizations to be associated with dynamic actions (which we will ignore for now for simplicity sake) or with other objects but at their core they are focused on characterizing the various properties of any given type of object (CybOX 2.1 provides property schemas for 90+ different cyber objects).

Given this, something simple like a filename can easily be expressed using the File_Name property field on a File Object. An instance can be described directly or a pattern can be conveyed using the CybOX property patterning capabilities on that property. 
{% include expand_link.html text="More detail on mechanism and use >>" section="single-property" %}
{% capture expandable %}

####Observable with single Object and single Property

   * Use for: characterize a single property
   * As an observable instance this very simply characterizes a single property value of a single instance object that was observed (e.g. a file with the name “foo.exe”) {% include expand_link.html section="composition1" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp99" %}{% highlight xml %}
<indicator:Observable id="example:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
  <cybox:Object id="example:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
    <cybox:Properties xsi:type="FileObj:FileObjectType">
      <FileObj:File_Name>foo.exe</FileObj:File_Name>
    </cybox:Properties>
  </cybox:Object>
</indicator:Observable>
{% endhighlight %}

{% include tab_separator.html %}{% highlight python %}
obs = File()
obs.file_name = "foo.exe"
pkg.add_observable(obs)
{% endhighlight %}{% include end_tabs.html %}


{% endcapture %}{% include expander.html section="composition1" %}
   * As an observable pattern this very simply characterizes a condition where any object of the given type has a property value matching the specified pattern. {% include expand_link.html section="composition2" disabledText="Hide Example" %}
{% capture expandable %}


{% include start_tabs.html tabs="XML|Python" name="comp1" %}{% highlight xml %}
<indicator:Observable id="example:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
  <cybox:Object id="example:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
    <cybox:Properties xsi:type="FileObj:FileObjectType">
      <FileObj:File_Name condition="Contains">foo</FileObj:File_Name>
     </cybox:Properties>
  </cybox:Object>
</indicator:Observable>
{% endhighlight %}  
{% include tab_separator.html %}{% highlight python %}
obs = File()
obs.file_name = "foo.exe"
obs.file_name.condition = "Contains"
pkg.add_observable(obs)
{% endhighlight %}{% include end_tabs.html %}

{% endcapture %}{% include expander.html section="composition2" %}
   * Mechanism: specified using the [condition](/data-model/{{site.current_version}}/cyboxCommon/PatternFieldGroup) attribute and field value of a single object property

{% endcapture %}{% include expander.html section="single-property" %}



Unlike some other approaches that treat all object properties as flat fields independent of each other or the particular object instance they apply to, STIX/CybOX associates the set of properties relevant to a given type of object together in that object’s property schema. This allows not only characterization of individual properties as flat fields but also allows **characterization of multiple properties as relevant to a single instance of the given object**. If you wish to characterize multiple properties that were observed (observable instance) for a single object you can simply specify multiple property fields on a single CybOX Object thus characterizing that that one single object had all of those properties. If you wish to specify a pattern for an object (observable pattern) that has a set of specific properties (and potentially specify patterning on each property) you can do this by simply specifying each property pattern using those property fields on a single object. Specifying patterns on multiple properties of an object (e.g. filename and filesize) using a flat field approach leads to ambiguity of whether all of the property patterns apply to the same single object instance or could potentially each map against different object instances. For example, a flat field approach might specify a pattern for filename=“foo.txt” and a pattern for filesize=“1896Kb” which could match against a FileA with both filename=“foo.txt” and filesize=“1896Kb” or it could match against a FileA with filename=“foo.txt” and a FileB with filesize=“1896Kb”. By enabling direct specification of multiple property patterns on a single object, STIX/CyboX allows this ambiguity to be avoided. Specifying a single object with multiple property patterns in STIX/CybOX is equivalent to a logical AND of those patterns but specifically as applied to a single instance of that object. In other words, for the pattern to be true all of the individual property patterns must be true on the same object instance. 
{% include expand_link.html text="More detail on mechanism and use >>" section="multiple-property-single-object" %}
{% capture expandable %}

####Observable with single Object and multiple Properties

   * Use for: characterize multiple properties of a single instance object (e.g. a file with the name “foo.exe” and a size of 1896Kb)
   * As an observable instance this simply characterizes multiple property values of a single instance object that was observed {% include expand_link.html section="composition3" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp98" %}{% highlight xml %}
<indicator:Observable id="example:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
  <cybox:Object id="example:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
     <cybox:Properties xsi:type="FileObj:FileObjectType">
      <FileObj:File_Name>foo.exe</FileObj:File_Name>
      <FileObj:Size_In_Bytes>1896000</FileObj:Size_In_Bytes>
    </cybox:Properties>
  </cybox:Object>
</indicator:Observable>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
obs = File()
obs.file_name = "foo"
obs.size_in_bytes = '1896000'
pkg.add_observable(obs)
{% endhighlight %}
{% include end_tabs.html %}

{% endcapture %}{% include expander.html section="composition3" %}
   * As an observable pattern this characterizes a condition where any object of the given type has property values matching all of the specified property field patterns. In other words, it is defining a logical AND across the set of property value patterns specified on the object. {% include expand_link.html section="composition4" disabledText="Hide Example" %}
{% capture expandable %}


{% include start_tabs.html tabs="XML|Python" name="comp2" %}{% highlight xml %}
<indicator:Observable id="example:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
  <cybox:Object id="example:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
     <cybox:Properties xsi:type="FileObj:FileObjectType">
      <FileObj:File_Name condition="Contains">foo</FileObj:File_Name>
      <FileObj:Size_In_Bytes condition="Equals">1896000</FileObj:Size_In_Bytes>
    </cybox:Properties>
  </cybox:Object>
</indicator:Observable>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
obs = File()
obs.file_name = "foo"
obs.file_name.condition = "Contains"
obs.size_in_bytes = '1896000'
obs.size_in_bytes.condition = "Equals"
pkg.add_observable(obs)
{% endhighlight %}
{% include end_tabs.html %}
{% endcapture %}


{% include expander.html section="composition4" %}
   * Mechanism: specified using the `condition` attribute and field value on each relevant a single object property

{% endcapture %}{% include expander.html section="multiple-property-single-object" %}


###Multiple objects
You may also wish to convey observable information that is not limited to the properties of a single instance object (e.g. an email message with a file attachment). STIX/CybOX enables this through the use of a Related_Objects structure available on any given Object that allows you to assert a relationship to another Object and to characterize the nature of the relationship with a label (e.g. “Contained_Within”). You can specify property patterns on any property fields of any of the related Objects. Similar to the semantics of multiple property patterns on a single Object (described above), property patterns on multiple Objects would evaluate as
equivalent to a logical AND of those patterns but specifically as applied to a single instance of each Object and considering the specified inter-object relationships. In other words, for the pattern to be true all of the individual property patterns and specified relationships must be true.
This approach to composing more complex observables through related objects is often referred to as “**relational composition**”.
{% include expand_link.html text="More detail on mechanism and use >>" section="multiple-objects" %}
{% capture expandable %}

####Observable with multiple related Objects

   * Use for: characterize a more complex situation involving multiple related objects (e.g. an email with a Subject of “Syria strategic plans leaked” and an attached file with File_Name of “bombISIS.pdf”)
   * As an observable instance this characterizes a more complex observation involving a set of related objects each with specific properties {% include expand_link.html section="composition5" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp97" %}{% highlight xml %}
<cybox:Observable id="example:Observable-db066ea1-925b-43df-a341-f513ece3ae94">
  <cybox:Object id="example:Object-e0e87eef-6315-410f-8025-086968129f41">
    <cybox:Properties xsi:type="EmailMessageObj:EmailMessageObjectType">
      <EmailMessageObj:Header>
        <EmailMessageObj:Subject>Syria strategic plans leaked</EmailMessageObj:Subject>
      </EmailMessageObj:Header>
    </cybox:Properties>
    <cybox:Related_Objects>
      <cybox:Related_Object id="example:Object-107a9290-30aa-4059-aa01-b441f6aa0cc6">
        <cybox:Properties xsi:type="FileObject:FileObjectType">
          <FileObject:File_Name>bombISIS.pdf</FileObject:File_Name>
        </cybox:Properties>
        <cybox:Relationship xsi:type="cyboxVocabs:ObjectRelationshipVocab-1.0">Contains</cybox:Relationship>
      </cybox:Related_Object>
    </cybox:Related_Objects>
  </cybox:Object>
</cybox:Observable>
{% endhighlight %}

{% include tab_separator.html %}{% highlight python %}
obs = EmailMessage()
obs.subject = "Syria strategic plans leaked"
file_obj = File()
file_obj.file_name = "bombISIS.pdf"
obs.add_related(file_obj, "Contains")
pkg.add_observable(obs)
{% endhighlight %}
{% include end_tabs.html %}


{% endcapture %}{% include expander.html section="composition5" %}
   * As an observable pattern this characterizes a condition where any full combination exists of the types of objects, the specific relationships and the specific property field patterns. In other words, it is defining a logical AND across not only the set of property value patterns specified on each object but also across the relationships between objects. {% include expand_link.html section="composition6" disabledText="Hide Example" %}
{% capture expandable %}


{% include start_tabs.html tabs="XML|Python" name="comp3" %}{% highlight xml %}

<cybox:Observable id="example:Observable-db066ea1-925b-43df-a341-f513ece3ae94">
  <cybox:Object id="example:Object-e0e87eef-6315-410f-8025-086968129f41">
    <cybox:Properties xsi:type="EmailMessageObj:EmailMessageObjectType">
      <EmailMessageObj:Header>
        <EmailMessageObj:Subject condition="Equals">Syria strategic plans leaked</EmailMessageObj:Subject>
      </EmailMessageObj:Header>
    </cybox:Properties>
    <cybox:Related_Objects>
      <cybox:Related_Object id="example:Object-107a9290-30aa-4059-aa01-b441f6aa0cc6">
        <cybox:Properties xsi:type="FileObject:FileObjectType">
          <FileObject:File_Name condition="Equals">bombISIS.pdf</FileObject:File_Name>
        </cybox:Properties>
        <cybox:Relationship xsi:type="cyboxVocabs:ObjectRelationshipVocab-1.0">Contains</cybox:Relationship>
      </cybox:Related_Object>
    </cybox:Related_Objects>
  </cybox:Object>
</cybox:Observable>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
obs = EmailMessage()
obs.subject = "Syria strategic plans leaked"
obs.subject.condition= "Equals"
file_obj = File()
file_obj.file_name = "bombISIS.pdf"
file_obj.file_name.condition = "Equals"
obs.add_related(file_obj, "Contains")
pkg.add_observable(obs)
{% endhighlight %}
{% include end_tabs.html %}


{% endcapture %}{% include expander.html section="composition6" %} 
   * Mechanism: specified using the [Related_Object](/data-model/{{site.current_version}}/cybox/RelatedObjectType/) structure for relationships from one object to another using and the  `condition` attribute and field value on each relevant a single object property.

{% endcapture %}{% include expander.html section="multiple-objects" %}




###Composition of observable patterns

There are also use cases requiring more complex matching logic that may call for the ability to specify patterns that are logical combinations of other observable patterns. STIX/CybOX support this capability through the [Observable_Composition](/data-model/{{site.current_version}}/cybox/ObservableCompositionType/) structure. Utilizing this structure, you can specify observable patterns that use a logical operator (AND | OR) to compose other observable patterns whether the the component patterns are simple single objects, multiple objects or even other Observable_Compositions themselves (supporting whatever level of composition needed). The evaluation of such patterns follows the explicit operator logic specified and the rules outlined above for object property and relationship patterns. This approach to composing more complex observables through logical combination is often referred to as “**logical composition**”.
   {% include expand_link.html text="More detail on mechanism and use >>" section="observable-composition" %}
{% capture expandable %}

####Observable Composition through explicit use of the Observable_Composition structure
**(often referred to as “logical composition”)**

**NOTE: Observables of this form are only valid as patterns and never as instances.**

   * Use for:  specifying compound observable conditions made up of logical combinations (AND/OR) of other observable conditions (patterns). The components of these compound conditions can be observable patterns of any level of detail including other observable compositions.
   * For example, a condition ((A OR B) AND C) where a system ((contains a mutex=“foo” | contains a file named “barfoobar”) & an outgoing network connection to 46.123.99.25). {% include expand_link.html section="composition7" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp4" %}{% highlight xml %}
<indicator:Observable id="example:Observable-5e7f46ab-5934-4327-aa8c-3a9635b41544">
  <cybox:Observable_Composition operator="AND">
    <cybox:Observable id="example:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
      <cybox:Observable_Composition operator="OR">
        <cybox:Observable id="example:Observable-641f417a-465e-4ebe-b122-7add616e833e">
          <cybox:Object id="example:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
            <cybox:Properties xsi:type="MutexObj:MutexObjectType">
              <MutexObj:Name condition="Contains">foo</MutexObj:Name>
            </cybox:Properties>
          </cybox:Object>
        </cybox:Observable>
        <cybox:Observable id="example:Observable-556fa703-8cee-4f23-a135-22ff4d4c1255">
          <cybox:Object id="example:Object-1efb9f80-b059-4a78-a8d8-9ef9233945e3">
            <cybox:Properties xsi:type="FileObj:FileObjectType">
              <FileObj:File_Name condition="Equals">barfoobar</FileObj:File_Name>
            </cybox:Properties>
          </cybox:Object>
        </cybox:Observable>
      </cybox:Observable_Composition>
    </cybox:Observable>
    <cybox:Observable id="example:Observable-418a3d1d-3eec-4baa-84f3-1fdb6f1a9cad">
      <cybox:Object id="example:Object-e008deda-233a-412d-a7ed-bbb6925e5c06">
        <cybox:Properties xsi:type="NetworkConnectionObj:NetworkConnectionObjectType">
          <NetworkConnectionObj:Destination_Socket_Address>
            <SocketAddressObj:IP_Address category="ipv4-addr">
              <AddressObj:Address_Value condition="Equals">46.123.99.25</AddressObj:Address_Value>
            </SocketAddressObj:IP_Address>
          </NetworkConnectionObj:Destination_Socket_Address>
        </cybox:Properties>
      </cybox:Object>
    </cybox:Observable>
  </cybox:Observable_Composition>
</indicator:Observable>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
orcomp = ObservableComposition()
orcomp.operator = "OR"
obs = Mutex()
obs.name = 'foo'
obs.name.condition= "Contains"
orcomp.add(obs)
obs = File()
obs.file_name = "barfoobar"
obs.file_name.condition = "Equals"
orcomp.add(obs)

andcomp = ObservableComposition()
andcomp.operator = "AND"
andcomp.add(orcomp)

obs = NetworkConnection()
sock = SocketAddress()
sock.ip_address = "46.123.99.25"
sock.ip_address.category = "ipv4-addr"
sock.ip_address.condition = "Equals"
obs.destination_socket_address = sock
andcomp.add (obs)

pkg.add_observable(andcomp) 
{% endhighlight %}
{% include end_tabs.html %}



{% endcapture %}{% include expander.html section="composition7" %}
   * Mechanism: specified using the [Observable_Composition](/data-model/{{site.current_version}}/cybox/ObservableCompositionType/) construct and its `operator` attribute


{% endcapture %}{% include expander.html section="observable-composition" %}
   

There is also a “shorthand” form of composition of observable patterns for the case where each component pattern consists of a single object property pattern all on the same object property (e.g. an IP watchlist of 100 IP addresses). Specifying this sort of composition is possible using the Observable_Composition form described above but is very space inefficient. To address this issue STIX/CybOX also provide the ability to utilize the approach described above for single properties of single objects but with the small twist of providing a list of possible values for the property pattern rather than just a single one. While semantically equivalent to a full logical composition using the Observable_Composition structure, this form is much more concise and is potentially useful for the specific case of composite patterns with a high degree of overlap on a single property field.
 {% include expand_link.html text="More detail on mechanism and use >>" section="observable-composition-list" %}
{% capture expandable %}

####Observable with single Object and single Property with multiple values (list)
**NOTE: Observables of this form are only valid as patterns and never as instances.**

   * Use for: specifying compound observable conditions made up of logical combinations (AND/OR) of patterns on a single object property
   * Mechanism: specified through the use of the `condition` and [apply_condition](/data-model/{{site.current_version}}/cyboxCommon/PatternFieldGroup) attributes on the property field and the inclusion of a delimiter (by default the delimiter is "##comma##” but can be overridden) separated list of values within the property field body. {% include expand_link.html section="composition8" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp5" %}{% highlight xml %}
<indicator:Observable  id="example:Observable-1c798262-a4cd-434d-a958-884d6980c459">
  <cybox:Object id="example:Object-1980ce43-8e03-490b-863a-ea404d12242e">
    <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
      <AddressObject:Address_Value condition="Equals" apply_condition="ANY">10.0.0.0##comma##10.0.0.1##comma##10.0.0.2</AddressObject:Address_Value>
    </cybox:Properties>
  </cybox:Object>
</indicator:Observable>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
obs = SocketAddress()
obs.ip_address = ['10.0.0.0','10.0.0.1','10.0.0.2'] # comma delimiter automagically added
obs.ip_address.condition = "Equals"
obs.ip_address.apply_condition = "ANY"
pkg.add_observable(obs)
{% endhighlight %}
{% include end_tabs.html %}

    
{% endcapture %}{% include expander.html section="composition8" %} 
   * **NOTE: This form of observable composition is semantically identical to use of "Observable Composition through explicit use of the Observable_Composition structure (often referred to as “logical composition”)” where each particular potential field value pattern is represented with its own full observable and all of the field value pattern observables are AND’d or OR’d together as specified by the `apply_condition` attribute. This “list” form of composition can be thought of as a significantly more concise and compact shorthand representation for these semantics. It is especially useful for patterns involving a very large number of potential field values (e.g. an IP watch list).**


{% endcapture %}{% include expander.html section="observable-composition-list" %}



###Composition of Indicators

While the above capabilities exist to specify observable patterns of varying complexity and detail, as “observables” they are all only specifying “factual” patterns without any context for interpretation. This additional context for the observable pattern that gives it meaning (what does it mean if the pattern evaluates “true”?) is provided by the STIX Indicator component. Similar to cases that require the more complex matching logic of composite observable patterns there are also cases that require logical composition of not only observable pattern matching logic but also of the contexts that go with individual observable patterns. To support the need for this sort of composition STIX provides the [Composite_Indicator_Expression](/data-model/{{site.current_version}}/indicator/CompositeIndicatorExpressionType/) structure. It mirrors the same structural approach as the Observable_Composition structure with a logical (AND | OR) operator but enables the specification of composite Indicators such that: 

* each component Indicator has its own defined context
* partial matching is possible on portions of the overall indicator pattern
* new composite Indicators can be specified using other preexisting Indicators


 {% include expand_link.html text="More detail on mechanism and use >>" section="indicator-composition" %}
{% capture expandable %}

Composition of observables directly using CybOX enables the **“factual” specification of arbitrarily complex patterns (independent of usage context)** for detection but in the end each observable only represents a single condition (as complex as it may be) to evaluate against. The evaluation is an all or nothing boolean (true/false) and offers no potential for partial evaluation matches on the pattern.

Indicators are about characterizing the **context for a given potential pattern of observation** and are intentionally abstracted from the technical details of specifying the “facts” of the pattern itself.  Indicators do not duplicate the underlying capabilities of CybOX to characterize/specify observables but rather layer contexts on top of them. Indicator composition in STIX is a composition of detection contexts each of which at its root has its own (potentially complex) “factual” observable pattern.

A mechanism for Indicator composition is provided in STIX to support three primary use cases that cannot be effectively addressed through direct observable composition in CybOX:


   * **The ability to characterize a context for an aggregate pattern where one of more of its parts may have their own relevant contexts that need to be specified.** For example, a single Indicator with an observable pattern for a particular file hash has the context of indicating a particular form of malware in broad use by various threat actors. This context is useful in and of itself and may be desired to be used for detection. Another single Indicator may exist with an observable pattern for network connections to a particular IP address known to be used as C2 infrastructure by a particular threat actor. Again, this context is useful in and of itself and may be desired to be used for detection. However, it may also be useful to detect the combination (AND) of these two patterns at the same time as being indicative of a particular campaign. The entire observable pattern composition could be duplicated in the new aggregate Indicator but that would be far less efficient, effective or consistent than simply allowing a logical composition of the two independent Indicators and specifying a new context for the aggregation. {% include expand_link.html section="composition9" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp6" %}{% highlight xml %}
<stix:STIX_Package  
    id="example:STIXPackage-ac823873-4c51-4dd1-936e-a39d40151cc3"
    timestamp="2014-05-08T09:00:00.000000Z" version="1.1.1">
  <stix:Indicators>
    <stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-e35c5023-0a11-434c-a812-963793b45cec">
      <indicator:Type>Campaign Characteristics</indicator:Type>
      <indicator:Description>Indicator for a composite of characteristics for the use of specific malware and C2 infrastructure within a Campaign.</indicator:Description>
      <indicator:Composite_Indicator_Expression operator="AND">
        <indicator:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-611935aa-4db5-4b63-88ac-ac651634f09b">
          <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
          <indicator:Description>Indicator for the hash of the foobar malware.</indicator:Description>
          <indicator:Observable id="example:Observable-556fa703-8cee-4f23-a135-22ff4d4c1255">
            <cybox:Object id="example:Object-1efb9f80-b059-4a78-a8d8-9ef9233945e3">
              <cybox:Properties xsi:type="FileObj:FileObjectType">
                <FileObj:Hashes>
                  <cyboxCommon:Hash>
                    <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0" condition="Equals">MD5</cyboxCommon:Type>
                    <cyboxCommon:Simple_Hash_Value condition="Equals">01234567890abcdef01234567890abcdef</cyboxCommon:Simple_Hash_Value>
                  </cyboxCommon:Hash>
                </FileObj:Hashes>
              </cybox:Properties>
            </cybox:Object>
          </indicator:Observable>
          <indicator:Indicated_TTP>
            <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-97eecb7a-546d-4e60-ab21-53fdb1a8abec"/>
          </indicator:Indicated_TTP>
        </indicator:Indicator>

        <indicator:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-d83596ff-4700-4698-b8f6-e1ed3f03f0ab">
          <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">C2</indicator:Type>
          <indicator:Description>Indicator for a particular C2 infstructure IP address.</indicator:Description>
          <indicator:Observable id="example:Observable-14a32139-39b1-4b83-897f-7fa3445f937e">
            <cybox:Object id="example:Object-e008deda-233a-412d-a7ed-bbb6925e5c06">
              <cybox:Properties xsi:type="NetworkConnectionObj:NetworkConnectionObjectType">
                <NetworkConnectionObj:Destination_Socket_Address>
                  <SocketAddressObj:IP_Address category="ipv4-addr">
                    <AddressObj:Address_Value condition="Equals">46.123.99.25</AddressObj:Address_Value>
                  </SocketAddressObj:IP_Address>
                </NetworkConnectionObj:Destination_Socket_Address>
              </cybox:Properties>
            </cybox:Object>
          </indicator:Observable>
          <indicator:Indicated_TTP>
            <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
          </indicator:Indicated_TTP>
        </indicator:Indicator>
      </indicator:Composite_Indicator_Expression>
      <indicator:Related_Campaigns>
        <indicator:Related_Campaign>
          <stixCommon:Campaign xsi:type="stixCommon:CampaignReferenceType" idref="example:campaign-d0b31826-d01e-48d1-8af1-5030a32b894a"/>
        </indicator:Related_Campaign>
      </indicator:Related_Campaigns>
    </stix:Indicator>
  </stix:Indicators>

  <stix:TTPs>
    <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-97eecb7a-546d-4e60-ab21-53fdb1a8abec">
      <ttp:Behavior>
        <ttp:Malware>
          <ttp:Malware_Instance>
            <ttp:Type xsi:type="stixVocabs:MalwareTypeVocab-1.0">Remote Access Trojan</ttp:Type>
            <ttp:Title>foobar malware</ttp:Title>
          </ttp:Malware_Instance>
        </ttp:Malware>
      </ttp:Behavior>
    </stix:TTP>
    <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f">
      <ttp:Resources>
        <ttp:Infrastructure>
          <ttp:Type>Malware C2</ttp:Type>
        </ttp:Infrastructure>
      </ttp:Resources>
    </stix:TTP>
  </stix:TTPs>

  <stix:Campaigns>
    <stix:Campaign xsi:type="campaign:CampaignType" id="example:campaign-d0b31826-d01e-48d1-8af1-5030a32b894a">
      <campaign:Title>holy grail</campaign:Title>
      <campaign:Related_TTPs>
        <campaign:Related_TTP>
          <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-97eecb7a-546d-4e60-ab21-53fdb1a8abec"/>
        </campaign:Related_TTP>
        <campaign:Related_TTP>
          <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
        </campaign:Related_TTP>
      </campaign:Related_TTPs>
      <campaign:Attribution>
        <campaign:Attributed_Threat_Actor>
          <stixCommon:Threat_Actor xsi:type="ta:ThreatActorType" idref="example:threatactor-d896f8dd-7dc6-45de-920c-21513c0024be"/>
        </campaign:Attributed_Threat_Actor>
      </campaign:Attribution>
    </stix:Campaign>
  </stix:Campaigns>

  <stix:Threat_Actors>
    <stix:Threat_Actor xsi:type="ta:ThreatActorType" id="example:threatactor-d896f8dd-7dc6-45de-920c-21513c0024be">
      <ta:Identity><stixCommon:Name>boobear</stixCommon:Name></ta:Identity>
      <ta:Observed_TTPs>
        <ta:Observed_TTP>
          <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
        </ta:Observed_TTP>
      </ta:Observed_TTPs>
    </stix:Threat_Actor>
  </stix:Threat_Actors>
</stix:STIX_Package>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
pkg1 = STIXPackage()
pkg1.title="Example of Indicator Composition for an aggregate indicator composition"
malware_ttp = TTP()
malware_ttp.behavior = Behavior()
malware = MalwareInstance()
malware.title = "foobar malware"
malware.add_type("Remote Access Trojan")
malware_ttp.behavior.add_malware_instance (malware)
c2_ttp = TTP()
c2_ttp.resources = Resource()
c2_ttp.resources.infrastructure = Infrastructure()
c2_ttp.resources.infrastructure.add_type( VocabString("Malware C2"))
pkg1.add_ttp(c2_ttp)
pkg1.add_ttp(malware_ttp)
nw_ind = Indicator()
nw_ind.description = "Indicator for a particular C2 infstructure IP address."
# add network network connection to this indicator
obs = NetworkConnection()
sock = SocketAddress()
sock.ip_address = "46.123.99.25"
sock.ip_address.category = "ipv4-addr"
sock.ip_address.condition = "Equals"
obs.destination_socket_address = sock
nw_ind.add_observable(obs)
nw_ind.add_indicated_ttp(TTP(idref=c2_ttp.id_))

# create File Hash indicator w/ embedded Observable
file_ind = Indicator()
file_ind.description = "Indicator for the hash of the foobar malware."
file_ind.add_indicator_type("File Hash Watchlist")
file_obs = File()
file_obs.add_hash("01234567890abcdef01234567890abcdef")
file_obs.hashes[0].type_ = "MD5"
file_obs.hashes[0].type_.condition = "Equals"
file_ind.add_observable(file_obs)
# create references 
file_ind.add_indicated_ttp(TTP(idref=malware_ttp.id_))
# create container indicator
ind = Indicator()
ind.add_indicator_type(VocabString("Campaign Characteristics"))
ind.description = "Indicator for a composite of characteristics for the use of specific malware and C2 infrastructure within a Campaign."
# Add campaign with related
camp = Campaign()
camp.title = "holy grail"
pkg1.add_campaign(camp)
camp.related_ttps.append(TTP(idref=c2_ttp.id_))
camp.related_ttps.append(TTP(idref=malware_ttp.id_))
# Add threat actor
ta = ThreatActor()
ta.identity = Identity()
ta.identity.name = "boobear"
ta.observed_ttps.append(TTP(idref=malware_ttp.id_))
pkg1.add_threat_actor(ta)
# Create composite expression
ind.composite_indicator_expression = CompositeIndicatorExpression()
ind.composite_indicator_expression.operator = "AND"
ind.composite_indicator_expression.append(file_ind)
ind.composite_indicator_expression.append(nw_ind)
pkg1.add_indicator(ind)

{% endhighlight %}{% include end_tabs.html %}

{% endcapture %}{% include expander.html section="composition9" %} 

   * **The ability to do "partial matching” on an aggregate pattern such that you can detect not only that the aggregate is true/false but also potential portions of the aggregate.** For example, a single Indicator with a single observable pattern for an IP watch list of three values would only be able to evaluate whether any one of those values was observed but not whether any particular one of those three were seen. An indicator composition OR’ing three independently defined  indicators (one for each IP value) would be able to evaluate to true/false if ANY of the IPs were seen but each individual Indicator could also be used to evaluate which particular IPs were seen. {% include expand_link.html section="composition10" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp7" %}{% highlight xml %}
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-e35c5023-0a11-434c-a812-963793b45cec">
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
  <indicator:Description>This Indicator specifies a pattern where any one or more of a set of three IP addresses are observed.</indicator:Description>
  <indicator:Composite_Indicator_Expression operator="OR">

    <indicator:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-d83596ff-4700-4698-b8f6-e1ed3f03f0ab">
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
      <indicator:Description>This Indicator specifies a pattern where one specific IP address is observed</indicator:Description>
      <indicator:Observable id="example:Observable-14a32139-39b1-4b83-897f-7fa3445f937e">
        <cybox:Object id="example:Object-e008deda-233a-412d-a7ed-bbb6925e5c06">
          <cybox:Properties xsi:type="AddressObj:AddressObjectType">
            <AddressObj:Address_Value condition="Equals">46.123.99.25</AddressObj:Address_Value>
          </cybox:Properties>
        </cybox:Object>
      </indicator:Observable>
      <indicator:Indicated_TTP>
        <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
      </indicator:Indicated_TTP>
    </indicator:Indicator>

    <indicator:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-90045060-c173-43f3-89f9-1bce3c70d2e9">
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
      <indicator:Description>This Indicator specifies a pattern where one specific IP address is observed</indicator:Description>
      <indicator:Observable id="example:Observable-2bb3f017-06f9-45cc-8f3a-8f22491273bc">
        <cybox:Object id="example:Object-f31d13e1-74fc-4494-a0e6-dad0b0c43570">
          <cybox:Properties xsi:type="AddressObj:AddressObjectType">
            <AddressObj:Address_Value condition="Equals">23.5.111.68</AddressObj:Address_Value>
          </cybox:Properties>
        </cybox:Object>
      </indicator:Observable>
      <indicator:Indicated_TTP>
        <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
      </indicator:Indicated_TTP>
    </indicator:Indicator>

    <indicator:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-ca860234-04b2-4347-a97e-81412f1cd7e3">
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
      <indicator:Description>This Indicator specifies a pattern where one specific IP address is observed</indicator:Description>
      <indicator:Observable id="example:Observable-0b4e8d58-3d9b-41dc-a71d-930e3a343f08">
        <cybox:Object id="example:Object-88aa5ed6-8df8-42e1-b0c5-f6b0f63a839c">
          <cybox:Properties xsi:type="AddressObj:AddressObjectType">
            <AddressObj:Address_Value condition="Equals">23.5.111.99</AddressObj:Address_Value>
          </cybox:Properties>
        </cybox:Object>
      </indicator:Observable>
      <indicator:Indicated_TTP>
        <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
      </indicator:Indicated_TTP>
    </indicator:Indicator>

  </indicator:Composite_Indicator_Expression>
  <indicator:Indicated_TTP>
    <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
  </indicator:Indicated_TTP>
</stix:Indicator>
{% endhighlight %}

{% include tab_separator.html %}{% highlight python %}
pkg2 = STIXPackage()
pkg2.title="Example of Indicator Composition for a one of many indicator composition"

# create container indicator
watchlistind = Indicator()
watchlistind.add_indicator_type("IP Watchlist")
watchlistind.description = "This Indicator specifies a pattern where any one or more of a set of three IP addresses are observed."
watchlistind.add_indicated_ttp(TTP(idref=c2_ttp.id_))
# Create composite expression
watchlistind.composite_indicator_expression = CompositeIndicatorExpression()
watchlistind.composite_indicator_expression.operator = "OR"

ips = ['23.5.111.68','23.5.111.99','46.123.99.25']
for ip in ips:
    new_ind = Indicator()
    new_ind.description = "This Indicator specifies a pattern where one specific IP address is observed"
    # add network network connection to this indicator
    obs = Address()
    obs.address_value = ip
    obs.address_value.condition = "Equals"
    new_ind.add_observable(obs)
    new_ind.add_indicated_ttp(TTP(idref=c2_ttp.id_))
    watchlistind.composite_indicator_expression.append(new_ind)

pkg2.add_indicator(watchlistind)

{% endhighlight %}{% include end_tabs.html %}


{% endcapture %}{% include expander.html section="composition10" %}

   * **The ability to specify new compound detection contexts (Indicators) as appropriate from other preexisting Indicators (potentially created and shared by other players) in a way that yields new levels of contextual understanding but still maintains consistency and practical usefulness with the source Indicators of the composition.** {% include expand_link.html section="composition11" disabledText="Hide Example" %}
{% capture expandable %}
{% include start_tabs.html tabs="XML|Python" name="comp8" %}{% highlight xml %}
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-e35c5023-0a11-434c-a812-963793b45cec"
    timestamp="2014-08-03T011:00:00.000000Z">
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
  <indicator:Description>This Indicator specifies a composite condition of two preexisting Indicators (each identifying a particular TTP with low confidence) that in aggregate identify the particular TTP with high confidence.</indicator:Description>
  <indicator:Composite_Indicator_Expression operator="OR">

    <indicator:Indicator xsi:type="indicator:IndicatorType" id="exampleOrg1:Indicator-d83596ff-4700-4698-b8f6-e1ed3f03f0ab"
        timestamp="2014-06-11T013:00:00.000000Z">
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">C2</indicator:Type>
      <indicator:Description>Indicator for a particular C2 IP address used by a malware variant.</indicator:Description>
      <indicator:Observable id="exampleOrg1:Observable-14a32139-39b1-4b83-897f-7fa3445f937e">
        <cybox:Object id="exampleOrg1:Object-e008deda-233a-412d-a7ed-bbb6925e5c06">
          <cybox:Properties xsi:type="NetworkConnectionObj:NetworkConnectionObjectType">
            <NetworkConnectionObj:Destination_Socket_Address>
              <SocketAddressObj:IP_Address category="ipv4-addr">
                <AddressObj:Address_Value condition="Equals">46.123.99.25</AddressObj:Address_Value>
              </SocketAddressObj:IP_Address>
            </NetworkConnectionObj:Destination_Socket_Address>
          </cybox:Properties>
        </cybox:Object>
      </indicator:Observable>
      <indicator:Indicated_TTP>
        <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
      </indicator:Indicated_TTP>
      <indicator:Confidence>
        <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Low</stixCommon:Value>
      </indicator:Confidence>
    </indicator:Indicator>

    <indicator:Indicator xsi:type="indicator:IndicatorType" id="exampleOrg2:Indicator-611935aa-4db5-4b63-88ac-ac651634f09b"
        timestamp="2014-05-08T09:00:00.000000Z">
      <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
      <indicator:Description>Indicator that contains malicious file hashes for a particular malware variant.</indicator:Description>
      <indicator:Observable id="exampleOrg2:Observable-c9ca84dc-4542-4292-af54-3c5c914ccbbc">
        <cybox:Object id="exampleOrg2:Object-c670b175-bfa3-48e9-a218-aa7c55f1f884">
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
        <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
      </indicator:Indicated_TTP>
      <indicator:Confidence>
        <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Low</stixCommon:Value>
      </indicator:Confidence>
    </indicator:Indicator>

  </indicator:Composite_Indicator_Expression>
  <indicator:Indicated_TTP>
    <stixCommon:TTP xsi:type="ttp:TTPType" idref="example:ttp-c9c82768-8e51-4a8c-b200-5f8d01acda5f"/>
  </indicator:Indicated_TTP>
  <indicator:Confidence>
    <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
  </indicator:Confidence>
</stix:Indicator>
{% endhighlight %}
{% include tab_separator.html %}{% highlight python %}
pkg3 = STIXPackage()
pkg3.title="Example of Indicator Composition for compound detection"
# create container indicator
watchlistind2 = Indicator()
watchlistind2.add_indicator_type("IP Watchlist")
watchlistind2.description = "This Indicator specifies a composite condition of two preexisting Indicators (each identifying a particular TTP with low confidence) that in aggregate identify the particular TTP with high confidence."
# Create composite expression
watchlistind2.composite_indicator_expression = CompositeIndicatorExpression()
watchlistind2.composite_indicator_expression.operator = "OR"
watchlistind2.add_indicated_ttp(TTP(idref=c2_ttp.id_))
watchlistind2.confidence = "High"
nw_ind.description = "Indicator for a particular C2 IP address used by a malware variant."
nw_ind.confidence = "Low"
nw_ind.indicator_types = ["C2"]
file_ind.description = "Indicator that contains malicious file hashes for a particular malware variant."
file_ind.confidence = "Low"
watchlistind2.composite_indicator_expression.append(nw_ind)
watchlistind2.composite_indicator_expression.append(file_ind)
pkg3.add_indicator(watchlistind2)

{% endhighlight %}{% include end_tabs.html %}


{% endcapture %}{% include expander.html section="composition11" %}

{% endcapture %}{% include expander.html section="indicator-composition" %}

**NOTE: At the STIX language level, the complexity of Indicator composition is independent of the complexity of the underlying observable pattern. Each Indicator specifying an observable pattern treats that pattern as a simple boolean condition regardless of complexity.**


##Summary

Composition of Observables directly in CybOX is necessary to enable characterization of complex observations or specification of complex patterns for observation. This function cannot be accomplished at the Indicator composition level as Indicators not only lack the effective structures for complex observable pattern characterization but they are intentionally focused on providing context for the pattern.

Composition of Indicators is necessary to enable characterization of complex composite detection contexts (not just the pattern but also what the pattern means) where the individual sub-contexts of the composition are important and useful. This function cannot be accomplished at the Observable level as Observables are intentionally bound to “factual” characterizations/specifications of observables without contextual meaning to enable their flexible use in a range of differing contexts.

A range of differing levels of detail for composition (as described above) is available in STIX/CybOX and the [appropriate level to use should be determined by the context of use](../../suggested-practices/#selecting-level-of-detail-for-observable-composition/).

[Python code for Observable examples](observable_composition.py)

[Python code for Indicator examples](indicator_composition.py)
