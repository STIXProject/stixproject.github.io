---
layout: flat
title: Incident vs. Indicator
use_cases:
  - Watchlist
  - Mapping
constructs:
  - Incident
  - Indicator
summary: You have a list of IP addresses (or hashes, or URLs, etc) and want to convert it to STIX. Should you use incidents, indicators, or both?
---

Many threat intel feeds that are available today and not already formatted as STIX are flat lists of "bad things": IPs that are known to be malware C2, malicious URLs, malware file hashes. When considering how to convert these to STIX (either as the original producer or as an intermediary) a common question that comes up is whether they should be converted to a list of **indicators**, a list of **incidents**, or maybe **both**. This idiom looks at several different examples and explains when to use one approach vs. another.

## Background

In STIX, an [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType) is used to represent detection guidance: it captures how to detect something (i.e. a pattern of what to look for) and what it means if you find it. For example, "If you see 192.168.1.1 in your network traffic it means you might have detected C2 traffic from a ZeuS trojan."

An [Incident](/data-model/{{site.current_version}}/incident/IncidentType), on the other hand, captures information about something that already happened. As an example, "I saw 192.168.1.1 in my network traffic and here's how it affected me".

Notice that those are two different statements and yet both describe the detection of 192.168.1.1 in network traffic. But, the indicator conveys information about something that might happen and how to find it, while the incident conveys a description of something that already happened.

Data providers often do not make this explicit distinction. Many open source intelligence feeds just give a list of IP addresses, potentially with an associated timestamp and maybe some bot name. Often the data is called "IPs of Interest" or "Botnet IPs". It is often not really made clear whether the producer is suggesting that consumers should use the IPs in their detection tools or whether the producer is just indicating that they saw them.

When mapping this to STIX or producing similar content directly to STIX, you're forced to resolve this ambiguity by choosing between an incident and an indicator.

## Considerations

When deciding whether to create indicators or incidents (or both), consider the following question: *Am I conveying what was observed at some point in time, something to look for going forward, or both?*

* Use an **Incident** if you're describing something that was observed at a point in time for use in analysis or to track history over time.
* Use an **Indicator** if you're conveying detection guidance (things to look for and potentially alert on). In some cases, the data will be sourced from something that you observed at a point in time but if your intent in conveying it is to say "look for these things" you should still use an indicator instead of an incident.
* Also note that you could do both: convey both detection guidance and the historical data that is the basis for this detection guidance.

To summarize: use indicators, unless you explicitly want to convey data for analysis rather than detection guidance.

### Example - IP List

Consider a CSV file with the following information:

IP Address|First Seen|Bot Name
---|---|---
192.168.1.1|2014-01-01T09:23:23Z|ZBot
192.168.1.2|2014-01-01T11:21:27Z|iSpy2
192.168.1.3|2014-01-01T17:45:54Z|ZBot

**NOTE**: The XML examples below contain the representation of just the first row in the above table. 

### As Indicators

One option in converting this data to STIX is to convert it to indicators: the **IP address** is the CybOX `Observable` pattern, the **First Seen** time goes into a `Sighting` (which can be ignored if this information is unimportant), and the **Bot Name** is the `Indicated_TTP`. This indicates that you should look for the given IP addresses in your own network traffic and, if you see it, it indicates a potential bot infection.

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="indicator" %}{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-0756a255-6623-4226-8356-015396918b38" timestamp="2014-08-22T20:17:38.959000+00:00" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1">
        <indicator:Title>192.168.1.1</indicator:Title>
        <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">IP Watchlist</indicator:Type>
        <indicator:Observable id="example:Observable-c46356e0-9d93-408b-ad2b-3aa2b561cfe9">
            <cybox:Object id="example:Address-d1482a44-e95b-4ebc-abba-0486e0df7ea9">
                <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
                    <AddressObj:Address_Value condition="Equals">192.168.1.1</AddressObj:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </indicator:Observable>
        <indicator:Indicated_TTP>
            <stixCommon:TTP idref="example:ttp-d6b60324-a1b8-4d51-8c26-3aef6351371d" xsi:type='ttp:TTPType' version="1.1.1"/>
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-d6b60324-a1b8-4d51-8c26-3aef6351371d" timestamp="2014-08-22T20:17:38.959000+00:00" xsi:type='ttp:TTPType' version="1.1.1">
        <ttp:Title>zbot</ttp:Title>
    </stix:TTP>
</stix:TTPs>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
data = json.load(open("data.json"))

stix_package = STIXPackage()

ttps = {}

for info in data['ips']:
  if info['bot'] not in ttps:
    ttps[info['bot']] = TTP(title=info['bot'])
    stix_package.add_ttp(ttps[info['bot']])

  indicator = Indicator(title=info['ip'])
  indicator.add_indicator_type("IP Watchlist")

  addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
  addr.condition = "Equals"
  indicator.add_observable(addr)
  indicator.add_indicated_ttp(TTP(idref=ttps[info['bot']].id_))

  stix_package.add_indicator(indicator)
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_package = STIXPackage.from_xml('sample-indicators.xml')

data = {
  'indicators': {
  }
}

ttps = {}
for ttp in stix_package.ttps:
  ttps[ttp.id_] = ttp
  data['indicators'][ttp.title] = []

for indicator in stix_package.indicators:
  ip = indicator.observable.object_.properties.address_value.value
  ttp = ttps[indicator.indicated_ttps[0].item.idref]
  data['indicators'][ttp.title].append(ip)

print data
{% endhighlight %}{% include end_tabs.html %}

### As Incidents

The other approach would be to convert it to incidents: the **IP Address** is a `Related_Observable`, the **First Seen** time is the incident's `First_Malicious_Action`, and the **Bot Name** is a `Leveraged_TTP`. This conveys that the IP addresses were seen in network traffic at that time and were linked to the bot in the leveraged TTP.

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="incident" %}{% highlight xml linenos %}
<stix:Observables cybox_major_version="2" cybox_minor_version="1" cybox_update_version="0">
    <cybox:Observable id="example:Observable-57501ad9-3b55-44aa-a084-eb55b1a84301">
        <cybox:Object id="example:Address-cbff060f-0010-4f36-9e45-48df756871e1">
            <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
                <AddressObj:Address_Value>192.168.1.1</AddressObj:Address_Value>
            </cybox:Properties>
        </cybox:Object>
    </cybox:Observable>
</stix:Observables>
<stix:TTPs>
    <stix:TTP id="example:ttp-f0c26887-610b-4724-80c6-5bd4e0354df9" timestamp="2014-08-25T13:49:37.079000+00:00" xsi:type='ttp:TTPType' version="1.1.1">
        <ttp:Title>ZBot</ttp:Title>
    </stix:TTP>
</stix:TTPs>
<stix:Incidents>
    <stix:Incident id="example:incident-da4e5808-0159-497a-be65-a65c8974f027" timestamp="2014-08-25T13:49:37.079000+00:00" xsi:type='incident:IncidentType' version="1.1.1">
        <incident:Title>192.168.1.1</incident:Title>
        <incident:Time>
            <incident:First_Malicious_Action precision="second">2014-01-01T09:23:23+00:00</incident:First_Malicious_Action>
        </incident:Time>
        <incident:Related_Observables>
            <incident:Related_Observable>
                <stixCommon:Observable idref="example:Observable-57501ad9-3b55-44aa-a084-eb55b1a84301">
                </stixCommon:Observable>
            </incident:Related_Observable>
        </incident:Related_Observables>
        <incident:Leveraged_TTPs>
            <incident:Leveraged_TTP>
                <stixCommon:Relationship>Used Malware</stixCommon:Relationship>
                <stixCommon:TTP idref="example:ttp-f0c26887-610b-4724-80c6-5bd4e0354df9" xsi:type='ttp:TTPType' version="1.1.1"/>
            </incident:Leveraged_TTP>
        </incident:Leveraged_TTPs>
    </stix:Incident>
</stix:Incidents>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
data = json.load(open("data.json"))

stix_package = STIXPackage()

ttps = {}

for info in data['ips']:
  if info['bot'] not in ttps:
    ttps[info['bot']] = TTP(title=info['bot'])
    stix_package.add_ttp(ttps[info['bot']])

  incident = Incident(title=info['ip'])
  incident.time = Time()
  incident.time.first_malicious_action = info['first_seen']

  addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
  observable = Observable(item=addr)
  stix_package.add_observable(observable)

  related_ttp = RelatedTTP(TTP(idref=ttps[info['bot']].id_), relationship="Used Malware")
  incident.leveraged_ttps.append(related_ttp)

  related_observable = RelatedObservable(Observable(idref=observable.id_))
  incident.related_observables.append(related_observable)

  stix_package.add_incident(incident)
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_package = STIXPackage.from_xml('sample-incidents.xml')

data = {
  
  'incidents': {
  }
}

ttps = {}
for ttp in stix_package.ttps:
  ttps[ttp.id_] = ttp
  data['incidents'][ttp.title] = []

observables = {}
for observable in stix_package.observables.observables:
  observables[observable.id_] = observable

for incident in stix_package.incidents:
  ip = observables[incident.related_observables[0].item.idref].object_.properties.address_value.value
  ttp = ttps[incident.leveraged_ttps[0].item.idref]
  time = incident.time.first_malicious_action.value.isoformat()

  data['incidents'][ttp.title].append({
    'ip': ip,
    'time': time
  })

print data
{% endhighlight %}{% include end_tabs.html %}

### Both Indicators and Incidents

Finally, both an indicator and an incident could be created for each row, and linked together. This would convey both that traffic to the IP address was observed in the producer's environment linked to that bot, and also that the consumer should also look for them in their environment.

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="both" %}{% highlight xml linenos %}
<stix:Observables cybox_major_version="2" cybox_minor_version="1" cybox_update_version="0">
    <cybox:Observable id="example:Observable-6a93879e-58b9-47b0-a44a-77fdb0cf1bb7">
        <cybox:Object id="example:Address-7e4f44b8-a0f9-4940-9de4-da313b6a2827">
            <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
                <AddressObj:Address_Value>192.168.1.1</AddressObj:Address_Value>
            </cybox:Properties>
        </cybox:Object>
    </cybox:Observable>
</stix:Observables>
<stix:Indicators>
    <stix:Indicator id="example:indicator-de988b8f-538b-40d8-b4f3-36378ba18d48" timestamp="2014-08-25T15:55:45.338000+00:00" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1">
        <indicator:Title>192.168.1.1</indicator:Title>
        <indicator:Observable id="example:Observable-c80170c3-64f0-49a7-b16c-be9dc290583f">
            <cybox:Object id="example:Address-85953adb-21ba-447c-8d8b-df8fe4d7e894">
                <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
                    <AddressObj:Address_Value condition="Equals">192.168.1.1</AddressObj:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </indicator:Observable>
        <indicator:Indicated_TTP>
            <stixCommon:TTP idref="example:ttp-e16098ed-8135-43b0-96d1-1d93e52fdab2" xsi:type='ttp:TTPType' version="1.1.1"/>
        </indicator:Indicated_TTP>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:TTP id="example:ttp-e16098ed-8135-43b0-96d1-1d93e52fdab2" timestamp="2014-08-25T15:55:45.338000+00:00" xsi:type='ttp:TTPType' version="1.1.1">
        <ttp:Title>ZBot</ttp:Title>
    </stix:TTP>
</stix:TTPs>
<stix:Incidents>
    <stix:Incident id="example:incident-d6f8f6d6-e9ea-4d8f-b066-20a492ac9561" timestamp="2014-08-25T15:55:45.339000+00:00" xsi:type='incident:IncidentType' version="1.1.1">
        <incident:Title>192.168.1.1</incident:Title>
        <incident:Time>
            <incident:First_Malicious_Action precision="second">2014-01-01T09:23:23+00:00</incident:First_Malicious_Action>
        </incident:Time>
        <incident:Related_Indicators>
            <incident:Related_Indicator>
                <stixCommon:Indicator idref="example:indicator-de988b8f-538b-40d8-b4f3-36378ba18d48" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1"/>
            </incident:Related_Indicator>
        </incident:Related_Indicators>
        <incident:Related_Observables>
            <incident:Related_Observable>
                <stixCommon:Observable idref="example:Observable-6a93879e-58b9-47b0-a44a-77fdb0cf1bb7">
                </stixCommon:Observable>
            </incident:Related_Observable>
        </incident:Related_Observables>
        <incident:Leveraged_TTPs>
            <incident:Leveraged_TTP>
                <stixCommon:Relationship>Used Malware</stixCommon:Relationship>
                <stixCommon:TTP idref="example:ttp-e16098ed-8135-43b0-96d1-1d93e52fdab2" xsi:type='ttp:TTPType' version="1.1.1"/>
            </incident:Leveraged_TTP>
        </incident:Leveraged_TTPs>
    </stix:Incident>
</stix:Incidents>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
data = json.load(open("data.json"))

stix_package = STIXPackage()

ttps = {}

for info in data['ips']:
  # Add TTP, unless it's already been added
  if info['bot'] not in ttps:
    ttps[info['bot']] = TTP(title=info['bot'])
    stix_package.add_ttp(ttps[info['bot']])

  # Add indicator
  indicator = Indicator(title=info['ip'])
  addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
  addr.condition = "Equals"
  indicator.add_observable(addr)
  indicator.add_indicated_ttp(TTP(idref=ttps[info['bot']].id_))

  stix_package.add_indicator(indicator)

  # Add incident
  incident = Incident(title=info['ip'])
  incident.time = Time()
  incident.time.first_malicious_action = info['first_seen']

  addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
  observable = Observable(item=addr)
  stix_package.add_observable(observable)

  related_ttp = RelatedTTP(TTP(idref=ttps[info['bot']].id_), relationship="Used Malware")
  incident.leveraged_ttps.append(related_ttp)

  related_observable = RelatedObservable(Observable(idref=observable.id_))
  incident.related_observables.append(related_observable)

  related_indicator = RelatedIndicator(Indicator(idref=indicator.id_))
  incident.related_indicators.append(related_indicator)

  stix_package.add_incident(incident)
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_package = STIXPackage.from_xml('sample-combined.xml')

data = {
  
  'incidents': {
  }
}

ttps = {}
for ttp in stix_package.ttps:
  ttps[ttp.id_] = ttp
  data['incidents'][ttp.title] = []

observables = {}
for observable in stix_package.observables.observables:
  observables[observable.id_] = observable

indicators = {}
for indicator in stix_package.indicators:
  indicators[indicator.id_] = indicator

for incident in stix_package.incidents:
  ip = observables[incident.related_observables[0].item.idref].object_.properties.address_value.value
  ttp = ttps[incident.leveraged_ttps[0].item.idref]
  time = incident.time.first_malicious_action.value.isoformat()
  address_value = indicators[incident.related_indicators[0].item.idref].observable.object_.properties.address_value

  data['incidents'][ttp.title].append({
    'ip': ip,
    'time': time,
    'pattern': "IP %(condition)s(%(ip)s)" % {'condition': address_value.condition, 'ip': address_value.value}
  })

print data
{% endhighlight %}{% include end_tabs.html %}

## Summary

Note that these options are not different ways to describe the same thing.  Although the underlying data is the same, STIX allows a more expressive context on what the data represents and how consumers should interpret it. The choice between Indicator and Incident is not arbitrary, but depends on what the producer wants to communicate. While in general it's likely that the answer is indicators, this is not a hard and fast rule.

Also, keep in mind that although this example talks about IP addresses the same concepts can be applied to other types of data. Always think "what do I want to describe" instead of "how/where can I fit this data into STIX".

## Further Reading

* The [Indicator C2 idiom](../c2-indicator) describes many of these same concepts but with more of a focus on how to represent the data when you know it's an indicator.
* Similarly, the [Incident Related Observables idiom](../related-observables) describes these concepts in the context of an indicator.
