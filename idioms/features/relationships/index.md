---
layout: idiom
title: STIX Relationships
---

Relationships are one of the features of STIX that make it so powerful for expressing cyber threat intelligence when compared to other options. Although each of the major components is valuable on its own and can be used independently of the others in order to express those concepts, the true power of STIX is realized when components are used in conjunction with each other to better enable threat analysis. It's one thing to use STIX to describe an indicator for an IP address without context, it's another to relate that to the relevant TTP that it indicates, the TTP to the threat actor or actors that are known to use it, to the incidents where it was observed, and to courses of action that can help mitigate its impact.

STIX relationships enable all of this by defining these connection points and how to express them:

<img src="/images/stix-architecture.png" alt="STIX relationship diagram" />

## Concept

All relationships in STIX are implemented using a similar structure to ensure consistency and ease of implementation. The structure allows for representation of the relationship itself (of course), a name to further describe the semantics of the relationship, a confidence in the assertion of a relationship, and an information source for the relationship. These fields mean that not only can STIX components be related together, they can be related together in a semantically meaninful way that preserves confidence and providence of the relationship assertion.

While all relationships in STIX allow for the information above, there are two general types of relationships: full relationships, which describes almost all STIX relationships, allow for either embedding the full related component inside the relationship or to reference the other component via an idref. Reference relationships only allow relationship by reference, not by embedding it.

## Data Model

In XML, a basic STIX relationship looks like this (the relationship is "Indicated_TTP", which goes from an indicator to a TTP):

```xml
<indicator:Indicator>
  <indicator:Indicated_TTPs>
    <indicator:Indicated_TTP>
      <stixCommon:Confidence />
      <stixCommon:Information_Source />
      <stixCommon:Relationship />
      <stixCommon:TTP />
    </indicator:Indicated_TTP>
  </indicator:Indicated_TTPs>
</indicator:Indicator>
```

The `Confidence` field uses the STIX confidence mechanism to express confidence in the relationship assertion. For example, if the producer is not certain that a particular TTP is used by a Threat Actor they could use "Low" confidence to denote that.

The `Information Source` field, using [InformationSourceType](/documentation/stixCommon/InformationSourceType), is used to characterize provenance information about the relationship assertion. It can be used to indicate who, when, and how (what tools) the relationship assertion was made.

The `Relationship` field uses a STIX controlled vocabulary to specify what type of relationship is being asserted. Although no default vocabulary has been identified, the STIX community is currently soliciting input on potential vocabularies.

Finally, the `TTP` field: this field contains either a pointer to or a full representation of the related component (assuming it's a full relationship type, if not only the reference might be supported). The field name will always be the name of the component that the relationship is pointing to, which in this case is TTP.

If using that field as a reference, the `idref` field is used to point to the `id` of the construct that the relationship is to. Optionally, the `timestamp` field can also be used to create a reference to a specific version of the construct.

For example:

<ul class="nav nav-tabs">
  <li class="active"><a href="#ms-xml" data-toggle="tab">XML</a></li>
  <li><a href="#ms-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="ms-xml">
{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-8837a4b4-b682-11e3-b0f3-0800271e87d2" xsi:type='indicator:IndicatorType' timestamp="2014-03-31T00:00:00.000000Z">
        <indicator:Indicated_TTP>
            <stixCommon:TTP idref="example:ttp-883730f6-b682-11e3-b0f3-0800271e87d2" />
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-883730f6-b682-11e3-b0f3-0800271e87d2" xsi:type='ttp:TTPType' timestamp="2014-03-31T00:00:00.000000Z"/>
</stix:TTPs>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="ms-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
indicator.add_indicated_ttp(TTP(idref=ttp.id_))

stix_package.add_indicator(indicator)
stix_package.add_ttp(ttp)

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

In the example above, a referenced is created by setting the `idref` of the relationship TTP to the `id` of the TTP itself. Note that while the TTP definition requires the `xsi:type`, the relationship TTP does not because it only uses the `id` field. It could also have added a `timestamp` set to exactly "2014-03-31T00:00:00.000000Z" to indicate that the relationship applies to that specific version of the TTP.

Assuming that you're using a full relationship structure, you can also choose to embed the related component:

<ul class="nav nav-tabs">
  <li class="active"><a href="#ms-xml" data-toggle="tab">XML</a></li>
  <li><a href="#embed-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="ms-xml">
{% highlight xml linenos %}
<stix:Indicators>
  <stix:Indicator id="example:indicator-3cdff264-b682-11e3-ab3e-0800271e87d2" timestamp="2014-03-31T00:00:00.000000Z" xsi:type="indicator:IndicatorType">
    <indicator:Indicated_TTP>
      <stixCommon:TTP id="example:ttp-3cdf6c54-b682-11e3-ab3e-0800271e87d2" timestamp="2014-03-31T00:00:00.000000Z" xsi:type="ttp:TTPType">
        <!-- SNIP -->
      </stixCommon:TTP>
    </indicator:Indicated_TTP>
  </stix:Indicator>
</stix:Indicators>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="embed-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
indicator.add_indicated_ttp(ttp)

stix_package.add_indicator(indicator)
print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

In this case the TTP is not defined separately at the top level, it is included in full inside the Indicated TTP. When embedding another component it does require using the `xsi:type` (because the full TTP model is being used) and allows (but does not require) the use of `id` and `timestamp` to give the construct and ID.

<div class="well well-sm">
<h4>Referencing vs. Embedding</h4>
<p>One of the most common questions that the STIX team gets is about how to decide when to reference a construct and when to embed it. There's not a decisive answer to this question that will make the decision for you, it's to a large extent a judgment call that depends on how you expect the content to be used. That said, there are a few guidelines:</p>
<ul>
  <li>If you expect the content to be referenced by multiple other components, it should not be embedded</li>
  <li>If the content has meaning outside of the relationship, it should not be embedded</li>
  <li>If the content, on the other hand, ONLY has meaning in the context of the single relationship, it can probably be embedded</li>
  <li>If you're not sure, it's probably safer to reference it</li>
</div>

## Examples

### Minimal Embed

<ul class="nav nav-tabs">
  <li class="active"><a href="#e-xml" data-toggle="tab">XML</a></li>
  <li><a href="#e-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="e-xml">
{% highlight xml linenos %}
<stix:Indicators>
  <stix:Indicator id="example:indicator-3cdff264-b682-11e3-ab3e-0800271e87d2" timestamp="2014-03-31T00:00:00.000000Z" xsi:type="indicator:IndicatorType">
    <indicator:Indicated_TTP>
      <stixCommon:TTP id="example:ttp-3cdf6c54-b682-11e3-ab3e-0800271e87d2" timestamp="2014-03-31T00:00:00.000000Z" xsi:type="ttp:TTPType">
        <!-- SNIP -->
      </stixCommon:TTP>
    </indicator:Indicated_TTP>
  </stix:Indicator>
</stix:Indicators>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="e-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
indicator.add_indicated_ttp(ttp)

stix_package.add_indicator(indicator)
print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

### Minimal Reference

<ul class="nav nav-tabs">
  <li class="active"><a href="#r-xml" data-toggle="tab">XML</a></li>
  <li><a href="#r-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="r-xml">
{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-8837a4b4-b682-11e3-b0f3-0800271e87d2" xsi:type='indicator:IndicatorType' timestamp="2014-03-31T00:00:00.000000Z">
        <indicator:Indicated_TTP>
            <stixCommon:TTP idref="example:ttp-883730f6-b682-11e3-b0f3-0800271e87d2" />
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-883730f6-b682-11e3-b0f3-0800271e87d2" xsi:type='ttp:TTPType' timestamp="2014-03-31T00:00:00.000000Z"/>
</stix:TTPs>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="r-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
indicator.add_indicated_ttp(TTP(idref=ttp.id_))

stix_package.add_indicator(indicator)
stix_package.add_ttp(ttp)

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

### Use of Relationship Field

<ul class="nav nav-tabs">
  <li class="active"><a href="#ex-r-xml" data-toggle="tab">XML</a></li>
  <li><a href="#ex-r-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="ex-r-xml">
{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-7f7b073e-b683-11e3-b79d-0800271e87d2" xsi:type='indicator:IndicatorType' timestamp="2014-03-31T00:00:00.000000Z">
        <indicator:Indicated_TTP>
            <stixCommon:Relationship>Indicates Malware</stixCommon:Relationship>
            <stixCommon:TTP idref="example:ttp-7f7a4ede-b683-11e3-b79d-0800271e87d2" />
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-7f7a4ede-b683-11e3-b79d-0800271e87d2" xsi:type='ttp:TTPType' timestamp="2014-03-31T00:00:00.000000Z"/>
</stix:TTPs>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="ex-r-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP
from stix.common.related import RelatedTTP

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
indicator.add_indicated_ttp(RelatedTTP(TTP(idref=ttp.id_), relationship="Indicates Malware"))

stix_package.add_indicator(indicator)
stix_package.add_ttp(ttp)

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

### Use of Confidence and Information Source

<ul class="nav nav-tabs">
  <li class="active"><a href="#ex-c-xml" data-toggle="tab">XML</a></li>
  <li><a href="#ex-c-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="ex-c-xml">
{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-50787664-b684-11e3-9149-0800271e87d2" xsi:type='indicator:IndicatorType' timestamp="2014-03-31T00:00:00.000000Z">
        <indicator:Indicated_TTP>
            <stixCommon:Confidence>
                <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
            </stixCommon:Confidence>
            <stixCommon:Information_Source>
                <stixCommon:Identity id="example:Identity-50790476-b684-11e3-9149-0800271e87d2">
                    <stixCommon:Name>Acme, Inc.</stixCommon:Name>
                </stixCommon:Identity>
            </stixCommon:Information_Source>
            <stixCommon:Relationship>Indicates Malware</stixCommon:Relationship>
            <stixCommon:TTP idref="example:ttp-5077da92-b684-11e3-9149-0800271e87d2"/>
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-5077da92-b684-11e3-9149-0800271e87d2" xsi:type='ttp:TTPType' timestamp="2014-03-31T00:00:00.000000Z"/>
</stix:TTPs>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="ex-c-python">
{% highlight python linenos %}
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP
from stix.common.related import RelatedTTP
from stix.common import Confidence, InformationSource, Identity

stix_package = STIXPackage()
ttp = TTP()

indicator = Indicator()
confidence = Confidence(value="High")
info_src = InformationSource(identity=Identity(name="Acme, Inc."))
indicator.add_indicated_ttp(RelatedTTP(TTP(idref=ttp.id_), relationship="Indicates Malware", information_source=info_src, confidence=confidence))

stix_package.add_indicator(indicator)
stix_package.add_ttp(ttp)

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

## Further Reading

Many (even most) of the use-case driven idioms show specific examples of STIX relationships:

* [Campaign Victim Targeting](/idioms/campaign/victim-targeting)
* [Malware used in an Incident](/idioms/incident/incident-malware)
* [C2 Indicator](/idioms/indicator/c2-indicator)
* [Malicious E-mail Attachment](/idioms/indicator/malicious-email-attachment)
* [TTP Leveraged by a Threat Actor](/idioms/threat-actor/leveraged-ttp)