---
layout: idiom
title: Marking Data
---

In STIX, data markings are used to mark specific pieces of the STIX document with some sort of information. In many cases that information is handling instructions, classifications, or terms of use but in reality the data markings structure can be used to mark the data with anything. For example, data markings could be used to indicate that the STIX document is part of an exercise and is not actual production data.

Markings in STIX are applied at the field level, meaning that marking statements can apply as atomically as individual fields up to all fields in the document (essentially marking the whole document). Thus a copyright may be applied across the entire document while specific terms of use might apply to certain fields in indicator test mechanisms or courses of action (as an example).

## Using Markings

Before talking about how markings are defined and represented it's useful to understand how and where markings are used. The most common place to see data markings is in the `Handling` field of the `STIX Header`. Markings placed in this field are often used to apply markings globally either to the entire document or to specific types of information regardless of where it appears in the document.

For example, a copyright that applies to the entire STIX package would be best placed in the handling field of the header. Similarly, the indication that all indicator courses of action are TLP:RED would also be best placed in the header.

Here's a simplified look at a marking placed in the STIX header. The actual marking content is omitted (see below for a discussion on how to create marking statements) in order to focus on where the marking appears.

<ul class="nav nav-tabs">
  <li class="active"><a href="#header-markings-xml" data-toggle="tab">XML</a></li>
  <li><a href="#header-markings-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="header-markings-xml">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:STIX_Header>
    <stix:Handling>
      <marking:Marking><!-- Marking content here --></marking:Marking>
    </stix:Handling>
  </stix:STIX_Header>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="header-markings-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification

handling = Marking()
handling.add_marking(MarkingSpecification())

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.handling = handling

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

The document header is not the only place data markings can be used, however. Individual STIX components (Indicators, Courses of Action, etc.) all each have their own `Handling` field. As you might expect, the `Handling` field within a component restricts the marking applicability to just fields within that component. That allows consumers to safely preserve markings within a component and move it between documents or into a datastore without worrying that the markings will change in meaning. Note, however, that this is not enforced in the data model: it's up to consumers to enforce this and ensure that markings applied within components do not "break out" of those components.

<ul class="nav nav-tabs">
  <li class="active"><a href="#component-markings-xml" data-toggle="tab">XML</a></li>
  <li><a href="#component-markings-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="component-markings-xml">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:Indicators>
    <stix:Indicator>
      <indicator:Handling>
        <marking:Marking><!-- Marking content here --></marking:Marking>
      </indicator:Handling>
    </stix:Indicator>
  </stix:Indicators>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="component-markings-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.data_marking import Marking, MarkingSpecification

indicator = Indicator()
indicator.handling = Marking()
indicator.handling.add_marking(MarkingSpecification())

stix_package = STIXPackage()
stix_package.add_indicator(indicator)

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

Notice that, although the handling field is placed directly in an indicator, the field itself is the same. Markings use a common structure regardless of where they are used. That said, it's important to understand where the marking structure is placed because the controlled structure may use relative document locations in order to mark specific fields (especially when used within components).

<div class="well well-sm">
<h4>Aside: Marking Precedence</h4>
<p>The STIX handling structures do allow documents to be marked with multiple markings, both of the same type and of different types. For example, an indicator could be marked both "Copyright Acme, Inc." and TLP:GREEN as well as both "TLP:GREEN" and "TLP:RED".</p>
<p>The behavior when an item is marked twice is undefined when multiple markings are applied (it's up to the consumers and producers to agree on what it means, though in many cases that will be obvious). Marking extensions themselves (TLP, for example) should define what to do when an item has multiple markings of that type applied. TLP says that the higher marking applies (so an item marked GREEN and RED would be considered marked RED) but other extensions might make it invalid to mark a construct twice or might define different rules.</p>
</div>

### Deciding where to place markings

For obvious reasons (given the scope for field-level markings) the only place to put markings that apply to a complete STIX document are in the `Handling` field of the STIX header. Generally, copyright statements and terms of use will apply at this level, though there will be exceptions.

Similarly, when applying markings to specific types of information wherever they occur (all indicator titles, all threat actor identities, etc.) it's usually best to place these markings in the header. That way they can consistently apply to everything in the package no matter which specific constructs they appear in.

On the other hand, it's usually better to apply markings to specific constructs in the handling structure for the component itself. For example, if only one indicator out of 10 is TLP:RED, it would be best to apply that marking in the indicator's handling field so it travels with the indicator.

One common use case, at least in TLP, is that most of the document is marked at a lower level (TLP:GREEN) while a few constructs are higher (TLP:AMBER). One strategy for approaching this is to use the global handling field to mark the entire document GREEN and then use more specific markings to override that and mark those constructs higher.

## Defining Markings

STIX data markings are implemented via [MarkingType](/documentation/marking/MarkingType), which has two primary fields: the `Controlled Structure` field indicates which part of the STIX document is being marked, while the `Marking Structure` field, which contains the marking itself. Besides these two primary fields are an `id` and `idref` pair to enable re-using markings, a `version` to indicate which version the data markings schema is being used, and an `Information Source` to indicate who is marking the data and when it was marked.

Let's dive into each piece of STIX data markings in turn.

### Controlled Structure

As explained above, the `Controlled Structure` field indicates which part of the document the markings apply to. Currently, this is implemented using [XPath 1.0](http://www.w3.org/TR/xpath/), a language for selecting portions of XML documents. As you would imagine, this means that the data markings structure is currently tied to XML, though notionally this controlled structure field simply indicates which part of the STIX document is being marked and so could be implemented in other document selection languages.

Note that the controlled structure must EXPLICITLY select ALL nodes that the marking applies to. It's not enough to select the parent and assume it applies to all children. So a selector for just an Indicator element will only select that element itself, it does not select the indicator content. To select that indicator and its children, make sure to use a selector like 'node()' or 'descendant-or-self()' that selects all fields. Note that in XPath, '*' only selects elements, not attributes, and so is not sufficient.

As an example, here's a small snippet that shows the controlled structure field in a handling construct:

<ul class="nav nav-tabs">
  <li class="active"><a href="#cs-xml" data-toggle="tab">XML</a></li>
  <li><a href="#cs-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="cs-xml">
{% highlight xml linenos %}
<stix:Handling>
  <marking:Marking>
    <marking:Controlled_Structure>//node()</marking:Controlled_Structure>
    <!-- Marking statement would go here, indicating the marking statement applies to all nodes selected by the Controlled_Structure -->
  </marking:Marking>
</stix:Handling>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="cs-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification

marking_specification = MarkingSpecification()
marking_specification.controlled_structure = "//node()"

handling = Marking()
handling.add_marking(marking_specification)

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.handling = handling

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

#### Relative Paths

Because XPath allows relative paths, the location of the `Controlled Structure` field in the document may be important. All relative paths should be applied from the location of the `Controlled Structure` field. That means that an XPath '..' would select the `Marking` parent of the `Controlled Structure`.

#### Namespace Prefixes

XPath selectors can make use of namespace prefixes. For example, "stix:Indicator" uses the `stix` prefix which, in most STIX documents, is defined to the STIX Core namespace. For the purpose of data marking XPaths, prefixes defined at the point of the `Controlled Structure` are considered valid for the XPath statement. In most cases, this means that the prefixes you define at the top of the document (in STIX_Package) can be used in the controlled structure. To make your documents easier to use it's probably best to stick with the common namespace prefixes used in the STIX schemas and examples.

#### Examples

A couple examples of some controlled structure statements are below:

<table class="table">
  <thead>
    <tr>
      <th>Location</th>
      <th>Controlled Structure Statement</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Header</td>
      <td>//node()</td>
      <td>Entire Document</td>
    </tr>
    <tr>
      <td>Individual Component</td>
      <td>../../../descendant-or-self()</td>
      <td>Entire Component</td>
    </tr>
    <tr>
      <td>Header</td>
      <td>//stix:Indicator</td>
      <td>All top-level indicators</td>
    </tr>
    <tr>
      <td>Individual Component</td>
      <td>../../../ta:Title</td>
      <td>Threat actor title</td>
    </tr>
  </tbody>
</table>

### Marking Structures and Default Extensions

Marking structures, as mentioned above, are an [extension point](/idioms/features/xsi-type) in STIX. This means that any marking structure in use by the community can be used within STIX documents. Note, however, that producers and consumers should agree on which types of extensions are used (perhaps through profiles) in order to make sure that all parties understand and will respect the particular marking structures used.

STIX itself defines three marking structure extensions, however others in the community may define additional structures. For example, the Information Sharing Architecture community has defined an extension to mark STIX documents with their extensions to the U.S. Government's Enterprise Data Headers.

#### Simple Marking

The simple marking extension allows users to make a text statement to mark the content. For example, copyright information can easily be communicated via a simple text statement "Copyright 2014, Acme Inc.". As an example:

<ul class="nav nav-tabs">
  <li class="active"><a href="#simple-marking-xml" data-toggle="tab">XML</a></li>
  <li><a href="#simple-marking-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="simple-marking-xml">
{% highlight xml linenos %}
<stix:Handling>
  <marking:Marking>
    <marking:Controlled_Structure>//node()</marking:Controlled_Structure>
    <marking:Marking_Structure xsi:type="simpleMarking:SimpleMarkingStructureType">
      <simpleMarking:Statement>Copyright 2014, Acme Inc.</simpleMarking:Statement>
    </marking:Marking_Structure>
  </marking:Marking>
</stix:Handling>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="simple-marking-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.simple_marking import SimpleMarkingStructure

marking_specification = MarkingSpecification()
marking_specification.controlled_structure = "//node()"

simple = SimpleMarkingStructure()
simple.statement = "Copyright 2014, Acme Inc."
marking_specification.marking_structure.append(simple)

handling = Marking()
handling.add_marking(marking_specification)

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.handling = handling

print stix_package.to_xml()

{% endhighlight %}
  </div>
</div>

#### Terms of Use

The terms of use marking extension allows users to make a text statement to mark the terms of use of the marked content. For example, terms of use can easily be communicated via a simple text statement "Acme Inc. is not responsible for the content of this file". In that sense it is very similar to the SimpleMarking extension but has a stronger semantic meaning.

As an example:

<ul class="nav nav-tabs">
  <li class="active"><a href="#tou-marking-xml" data-toggle="tab">XML</a></li>
  <li><a href="#tou-marking-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="tou-marking-xml">
{% highlight xml linenos %}
<stix:Handling>
  <marking:Marking>
    <marking:Controlled_Structure>//node()</marking:Controlled_Structure>
    <marking:Marking_Structure xsi:type="terms:TermsOfUseMarkingStructureType">
      <terms:Terms_Of_Use>Acme Inc. is not responsible for the content of this file</terms:Terms_Of_Use>
    </marking:Marking_Structure>
  </marking:Marking>
</stix:Handling>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="tou-marking-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.terms_of_use_marking import TermsOfUseMarkingStructure

marking_specification = MarkingSpecification()
marking_specification.controlled_structure = "//node()"

tou = TermsOfUseMarkingStructure()
tou.terms_of_use = "Acme Inc. is not responsible for the content of this file."
marking_specification.marking_structure.append(tou)

handling = Marking()
handling.add_marking(marking_specification)

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.handling = handling

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

#### TLP

[Traffic Light Protocol](http://www.us-cert.gov/tlp) is a mechanism created by US-CERT and used throughout the cyber threat sharing industry to indicate how content may be shared. STIX provides a TLP extension that allows content to be marked with the colors from the TLP matrix.

As an example:

<ul class="nav nav-tabs">
  <li class="active"><a href="#tlp-marking-xml" data-toggle="tab">XML</a></li>
  <li><a href="#tlp-marking-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="tlp-marking-xml">
{% highlight xml linenos %}
<stix:Handling>
  <marking:Marking>
    <marking:Controlled_Structure>//node()</marking:Controlled_Structure>
    <marking:Marking_Structure xsi:type="tlp:TLPMarkingStructureType" tlp:color="AMBER" />
  </marking:Marking>
</stix:Handling>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="tlp-marking-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.tlp import TLPMarkingStructure

marking_specification = MarkingSpecification()
marking_specification.controlled_structure = "//node()"

tlp = TLPMarkingStructure()
tlp.color = "AMBER"
marking_specification.marking_structure.append(tlp)

handling = Marking()
handling.add_marking(marking_specification)

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.handling = handling

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>


## Further Reading

* [xsi:type](/idioms/features/xsi-type) - The STIX xsi:type-based extension mechanism is used to implement marking structures.
* [MarkingType](/documentation/marking/MarkingType)