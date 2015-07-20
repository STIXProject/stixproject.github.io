---
layout: flat
title: File Hash Reputation
use_cases:
  - Reputation
constructs:
  - Indicator
  - TTP
summary: This idiom describes how reputation services (using file hash as an example) can be represented in STIX
---

Although there are variations, reputation services generally present information about a single data point (IP address, file by hash, e-mail, or URL) and how likely it is that that data point is "malicious". As you might expect, that's the perfect use case for a STIX [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType) and so that will be the focus of this idiom. If you're not already familiar with basic STIX indicators, read the [Indicator for C2 IP Address](/documentation/idioms/c2-indicator) for some background on creating indicators in general.

This idiom will cover some specific cases that many reputation services have to deal with:

- Where the reputation score itself goes
- How custom scoring systems or vocabularies are represented

Keep in mind that many reputation services are request/response: the consumer asks for information about a single hash and the producer creates a response specific to that hash. This idiom only describes the "response" part of that cycle. To see a more transport-oriented view of this idiom that incorporates TAXII, take a look at their [TAXII Service Profile for IP Reputation](http://taxiiproject.github.io/documentation/service-profiles/file-hash-rep/). This STIX idiom is a subset of that that goes into more detail on the STIX side.

**Shortcut: Already very comfortable creating or parsing indicators? Reputation services are just an indicator with a "Confidence" field that indicates the score itself (use a custom vocabulary if you need to).**

## Data model

The basic data model is the same as for most indicators:

- A top-level indicator to bring together:
  - A CybOX object to represent the data point
  - If possible, an indicated TTP on the indicator to describe how the object is malicious
  - A confidence to indicate the reputation score (the likelihood that the object is malicious)

{% include start_tabs.html tabs="Diagram|XML|Python Producer|Python Consumer" name="indicator" %}
<img src="diagram.png" alt="File hash reputation" />
{% include tab_separator.html %}{% highlight xml %}
<stix:Indicator id="example:indicator-340493c6-5bef-41a7-95da-04dde6dc132c" timestamp="2015-07-20T18:30:25.438755+00:00" xsi:type='indicator:IndicatorType'>
    <indicator:Title>File Reputation for SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</indicator:Title>
    <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
</stix:Indicator>
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
indicator = Indicator(title="File Reputation for SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
indicator.add_indicator_type("File Hash Watchlist")
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
indicator = stix_package.indicators[0]
{% endhighlight %}{% include end_tabs.html %}

### The object itself

This is essentially just a normal indicator, so for more background see the [Indicator for C2 IP Address idiom](/documentation/idioms/c2-indicator/).

In particular, because this is an indicator keep in mind that all of the fields on the CybOX object MUST have a `@condition` explicitly set. In most cases (such as for single IP addresses, file hashes, and URLs) the condition can just be "Equals".

In this example, the SHA256 hash for the file is given along with the notation that the match should (of course, because it's a hash) be an equality match:

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="observable" %}{% highlight xml %}
<indicator:Observable id="example:Observable-4101d261-e4d5-4d56-b293-4354b9826a13">
    <cybox:Object id="example:File-eaec587e-3b47-41fd-aad6-ed71fa85526b">
        <cybox:Properties xsi:type="FileObj:FileObjectType">
            <FileObj:Hashes>
                <cyboxCommon:Hash>
                    <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0" condition="Equals">SHA256</cyboxCommon:Type>
                    <cyboxCommon:Simple_Hash_Value condition="Equals">e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</cyboxCommon:Simple_Hash_Value>
                </cyboxCommon:Hash>
            </FileObj:Hashes>
        </cybox:Properties>
    </cybox:Object>
</indicator:Observable>
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
file_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
file_object = File()
file_object.add_hash(Hash(file_hash))
file_object.hashes[0].simple_hash_value.condition = "Equals"
file_object.hashes[0].type_.condition = "Equals"
indicator.add_observable(file_object)
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
print "Hash: " + indicator.observable.object_.properties.hashes[0].simple_hash_value.value
{% endhighlight %}{% include end_tabs.html %}

### Indicated TTP

To make indicators more useful it's a good idea to include an `Indicated_TTP` on the indicator. This is a relationship that points to the [TTP](/data-model/{{site.current_version}}/ttp/TTPType) construct to describe what about the object is bad: maybe it's a piece of malware, maybe it's an IP used for C2, maybe it's an e-mail address used for spear phishing. In many cases, reputation services don't include this data at all and can completely omit it while in other cases they may use a basic TTP with a human-readable title and nothing else.

In this example we'll skip the indicated TTP, but you can look at the idiom for [C2 IP address](/documentation/idioms/c2-indicator/) to see what it looks like.

### Reputation score

For almost all reputation services, the reputation score isn't _how bad_ the indicated object is but _how likely it is_ that the object is bad. In the indicator context, this data is represented on the `Confidence` field (which can in some ways be thought of as a synonym for `Indicated_TTP/Confidence`). This field can either use the default vocabulary ([HighMediumLow](/data-model/{{site.current_version}}/stixVocabs/HighMediumLowVocab-1.0/)) or a custom vocabulary to represent a different scoring system.

When using a custom vocabulary, the `@vocab_name` field represents the name of the scoring system and the `@vocab_reference` field represents a URL to something that defines the scoring system. In this example, we just use a placeholder link to Wikipedia but in a real service it should be set to the documentation for the scoring system so that consumers can understand the score that they get.

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="confidence" %}{% highlight xml %}
<indicator:Confidence timestamp="2015-07-20T18:30:25.439498+00:00">
    <stixCommon:Value vocab_reference="https://en.wikipedia.org/wiki/Percentage" vocab_name="Percentage">75</stixCommon:Value>
</indicator:Confidence>
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
indicator.confidence = Confidence(value=VocabString('75'))
indicator.confidence.value.vocab_name = "Percentage"
indicator.confidence.value.vocab_reference = "https://en.wikipedia.org/wiki/Percentage"
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
print "Reputation: " + indicator.confidence.value.value
{% endhighlight %}{% include end_tabs.html %}

## Putting it all together

Here's the whole thing in one big chunk:

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="everything" %}{% highlight xml %}
<stix:Indicator id="example:indicator-340493c6-5bef-41a7-95da-04dde6dc132c" timestamp="2015-07-20T18:30:25.438755+00:00" xsi:type='indicator:IndicatorType'>
    <indicator:Title>File Reputation for SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</indicator:Title>
    <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">File Hash Watchlist</indicator:Type>
    <indicator:Observable id="example:Observable-4101d261-e4d5-4d56-b293-4354b9826a13">
        <cybox:Object id="example:File-eaec587e-3b47-41fd-aad6-ed71fa85526b">
            <cybox:Properties xsi:type="FileObj:FileObjectType">
                <FileObj:Hashes>
                    <cyboxCommon:Hash>
                        <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">SHA256</cyboxCommon:Type>
                        <cyboxCommon:Simple_Hash_Value condition="Equals">e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</cyboxCommon:Simple_Hash_Value>
                    </cyboxCommon:Hash>
                </FileObj:Hashes>
            </cybox:Properties>
        </cybox:Object>
    </indicator:Observable>
    <indicator:Confidence timestamp="2015-07-20T18:30:25.439498+00:00">
        <stixCommon:Value vocab_reference="https://en.wikipedia.org/wiki/Percentage" vocab_name="Percentage">75</stixCommon:Value>
    </indicator:Confidence>
</stix:Indicator>
{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
file_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

indicator = Indicator(title="File Reputation for SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
indicator.add_indicator_type("File Hash Watchlist")

file_object = File()
file_object.add_hash(Hash(file_hash))
file_object.hashes[0].simple_hash_value.condition = "Equals"
file_object.hashes[0].type_.condition = "Equals"
indicator.add_observable(file_object)

indicator.confidence = Confidence(value=VocabString('75'))
indicator.confidence.value.vocab_name = "Percentage"
indicator.confidence.value.vocab_reference = "https://en.wikipedia.org/wiki/Percentage"

{% endhighlight %}{% include tab_separator.html %}{% highlight python %}
stix_package = STIXPackage.from_xml('file-hash-reputation.xml')
for indicator in stix_package.indicators:
  print "Hash: " + indicator.observable.object_.properties.hashes[0].simple_hash_value.value
  print "Reputation: " + indicator.confidence.value.value
{% endhighlight %}{% include end_tabs.html %}


## Further Reading

* [Indicator Type](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Indicator for C2 IP Address](/documentation/idioms/c2-indicator)
