---
layout: flat
title: Indicator for Malicious URL
constructs:
  - Indicator
summary: This idiom is an example of a malicious URL indicator that represents a URL and indicates that it's a delivery mechanism for a piece of malware.
---

{% include awesome-indicator.html %}

A very common method for delivering malware to potential targets is to host it at a particular URL. Targets are then directed to that URL via a phishing e-mail or a link from another site and, when they reach it, are exploited. Sharing lists of malicious URLs can be an effective and cheap way to limit exposure to malicious code.


## Scenario

This scenario consists of an indicator for the URL `http://x4z9arb.cn/4712/`, which is known to be malicious. Unlike the [C2 beaconing](../c2-indicator) and [Malware hash](../malware-hash) idioms, in this scenario the organization creating the indicator does not have any specific context and so chooses to just represent the indicator without additional context. Though it's suggested that some context always be given with an indicator if possible, in this case the organization does not have enough additional context to add anything.

## Data model

Because this indicator doesn't include any context (see scenario above), the indicator itself is the only top-level component. Within the indicator, the URL is represented as a [URI Object](/data-model/{{site.current_version}}/URIObj/URIObjectType) with the `Type` set to "URL" and the `Value` set to the malicious URL itself (`http://x4z9arb.cn/4712/`).

![URL Indicator Diagram](diagram.png)



## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="malicious-url" %}{% highlight xml linenos %}
<stix:Indicator id="example:Indicator-d81f86b9-975b-bc0b-775e-810c5ad45a4f" xsi:type='indicator:IndicatorType'>
    <indicator:Title>Malicious site hosting downloader</indicator:Title>
    <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.0">URL Watchlist</indicator:Type>
    <indicator:Observable id="example:Observable-ee59c28e-d922-480e-9b7b-a79502696505">
        <cybox:Object id="example:URI-b13ae3fc-80af-49c2-9de9-f713abc070ba">
            <cybox:Properties xsi:type="URIObj:URIObjectType" type="URL">
                <URIObj:Value condition="Equals">http://x4z9arb.cn/4712</URIObj:Value>
            </cybox:Properties>
        </cybox:Object>
    </indicator:Observable>
</stix:Indicator>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

indicator = Indicator()
indicator.id_ = "example:package-382ded87-52c9-4644-bab0-ad3168cbad50"
indicator.title = "Malicious site hosting downloader"
indicator.add_indicator_type("URL Watchlist")

url = URI()
url.value = "http://x4z9arb.cn/4712"
url.type_ =  URI.TYPE_URL
url.condition = "Equals"

indicator.add_observable(url)
print(indicator.to_xml())

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

print("== MALWARE ==")
for ind in pkg.indicators:
    print("---")
    print("Title : " + ind.title)
    print("ID : " + ind.id_)
    for ind_type in ind.indicator_types:
        print("Type: " + str(ind_type))

    for obs in ind.observables:
        print("URL : " + str(obs.object_.properties.value))

{% endhighlight %}{% include end_tabs.html %}

[Full XML](indicator-for-malicious-url.xml) | [Python Producer](indicator-for-malicious-url_producer.py) | [Python Consumer](indicator-for-malicious-url_consumer.py)


## Further Reading

* [Indicator Type](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [CybOX URI Object](/data-model/{{site.current_version}}/URIObj/URIObjectType)
