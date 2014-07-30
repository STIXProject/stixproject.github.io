---
layout: flat
title: Controlled Vocabularies
---

Many locations in STIX use controlled vocabularies as a mechanism to provide a defined list of values to use by default but also to allow users to define their own vocabularies or even use values outside of any vocabulary.

## Using a value from the default vocabulary

You should use the default STIX vocabulary whenever possible in order to assure the greatest level of compatibility with other STIX users. To do so, simply set the [xsi:type](../xsi-type) to the type for the default vocabulary and use a value as defined in that vocabulary. In the Python APIs, simply setting the value of the field to a value from that vocabulary will accomplish this.

You can find the `xsi:type` to use by looking in the documentation for the field you're working with.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-1" data-toggle="tab">XML</a></li>
  <li><a href="#python-1" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-1">
{% highlight xml linenos %}
<stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators</stix:Package_Intent>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-1">
{% highlight python linenos %}
stix_package.stix_header.package_intents = "Indicators"
{% endhighlight %}
  </div>
</div>

## Using a value without a defined vocabulary

If you want to set the field to custom values and either don't want to or can't define a vocabulary ahead of time you can also set a value outside of any vocabulary. To do this, omit the `xsi:type` and set the text of the field to your custom value. In the Python APIs, create a new instance of `VocabString` from the `stix.common.vocabs` package and set the field to that.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-2" data-toggle="tab">XML</a></li>
  <li><a href="#python-2" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-2">
{% highlight xml linenos %}
<stix:Package_Intent>MyCustomValue</stix:Package_Intent>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-2">
{% highlight python linenos %}
from stix.common.vocabs import VocabString

stix_package.stix_header.package_intents = VocabString("MyCustomValue")
{% endhighlight %}
  </div>
</div>

## Using a value from a custom vocabulary that is not defined as a custom STIX vocabulary

Often a sharing community or product will have a defined vocabulary they want to use but that vocabulary doesn't align completely with the STIX default vocabulary. One way to accomplish this is to set the `vocab_name` and `vocab_reference` fields on the vocabulary field to indicate the vocabulary name and a URL that defines that vocabulary. In the Python APIs, instantiate a new VocabString with the custom value and set these fields on that.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-3" data-toggle="tab">XML</a></li>
  <li><a href="#python-3" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-3">
{% highlight xml linenos %}
<stix:Package_Intent
        vocab_reference="http://myvocabname.example.com/SomeKindOfReferenceInformation"
        vocab_name="MyVocabName"
        >MyCustomValue</stix:Package_Intent>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-3">
{% highlight python linenos %}
from stix.common.vocabs import VocabString

vs = VocabString("MyCustomValue")
vs.vocab_name = "MyVocabName" #Contains a simple name to identify the vocabulary
vs.vocab_reference = "http://myvocabname.example.com/SomeKindOfReferenceInformation" #Contains a reference item for the vocabulary
stix_package.stix_header.package_intents = vs
{% endhighlight %}
  </div>
</div>

## Using a value from a custom vocabulary that is defined as a custom STIX vocabulary

One down side of the above approach is that the values from the vocabulary are not validated. To allow for validation and a more formal description of the vocabulary, you can also define your own vocabulary ahead of time, similar to how the STIX team did so with the default vocabularies. To use this vocabulary, define it in schema and import that schema. Then, set the `xsi:type` to the type for your vocabulary. In the Python APIs, you'll need to create a new class that extends from the ControlledVocabulary class and then at use time import that class and set the value to a new instance.

<ul class="nav nav-tabs">
  <li class="active"><a href="#xml-4" data-toggle="tab">XML</a></li>
  <li><a href="#python-4" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="xml-4">
{% highlight xml linenos %}
<stix:Package_Intent xsi:type="example:MyCustomVocab-1.0">MyCustomValue</stix:Package_Intent>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="python-4">
{% highlight python linenos %}
from example.vocabs import MyCustomVocab

stix_package.stix_header.package_intents = MyCustomVocab("MyCustomValue")
{% endhighlight %}
  </div>
</div>

{% comment %}
## Further Reading

* TODO: Update this with further reading, perhaps when a Package Intent idiom comes around.
* TODO: Also should add a link to the process for defining a new vocabulary via schema.
{% endcomment %}
