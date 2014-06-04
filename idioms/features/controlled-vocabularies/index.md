---
layout: idiom
title: Controlled Vocabularies
---

This idiom describes how to use and extend Controlled Vocabularies. Many locations in STIX, like Package Intent, Indicator Type, and more, use Controlled Vocabularies. In each case,
the STIX APIs provide the ability to set any of the default values without any extra work, while using a value outside of the default values (aka a 'custom value') requires a little
additional code. 

## Using a Default Controlled Vocabulary Value

When using a Default Value for a Controlled Vocabulary, simply supply a text string containing one of the Default Values

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-1" data-toggle="tab">XML</a></li>
  <li><a href="#python-1" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-1">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:STIX_Header>
    <stix:Package_Intent>Indicators</stix:Package_Intent>
  </stix:STIX_Header>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-1">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.package_intents = "Indicators"

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

## Using a Custom Controlled Vocabulary Value (Simple Example)

When using a Custom Value for a Controlled Vocabulary, you need to use the VocabString object.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-1" data-toggle="tab">XML</a></li>
  <li><a href="#python-1" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-1">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:STIX_Header>
    <stix:Package_Intent>MyCustomValue</stix:Package_Intent>
  </stix:STIX_Header>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-1">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.common.vocabs import VocabString

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.package_intents = VocabString("MyCustomValue")

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

## Using a Custom Controlled Vocabulary Value (Full Example)

The VocabString object can hold a number of other properties, which are demonstrated in this example.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-2" data-toggle="tab">XML</a></li>
  <li><a href="#python-2" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-2">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:STIX_Header>
    <stix:Package_Intent
            vocab_reference="http://myvocabname.example.com/SomeKindOfReferenceInformation"
            vocab_name="MyVocabName"
            >MyCustomValue</stix:Package_Intent>
  </stix:STIX_Header>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-2">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.common.vocabs import VocabString

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
vs = VocabString("MyCustomValue")
vs.vocab_name = "MyVocabName" #Contains a simple name to identify the vocabulary
vs.vocab_reference = "http://myvocabname.example.com/SomeKindOfReferenceInformation" #Contains a reference item for the vocabulary
stix_package.stix_header.package_intents = vs

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

{% comment %}
## Further Reading

* TODO: Update this with further reading, perhaps when a Package Intent idiom comes around.
{% comment %}