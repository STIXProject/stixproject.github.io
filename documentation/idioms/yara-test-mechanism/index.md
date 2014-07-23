---
layout: flat
title: Yara Test Mechanism
tags:
  - indicator
summary: Represent how to detect an indicator using Yara.
---

While one option when sharing indicator signatures is to use the tool-neutral `Observable` field in the indicator using CybOX, another option is to take a tool-specific approach and share indicators with signatures in the native language of specific tools via the `Test_Mechanisms` field. The advantage of this is that you can share signatures that work natively in existing tools but can still integrate with the rest of the STIX architecture.

This idiom describes using the Yara test mechanism to share the basic Yara rule that is used on the [Yara homepage](http://plusvic.github.io/yara/).

## Scenario

A hypothetical producer of this information might want to use just a plain Yara signature (no CybOX) if they know that all consumers use Yara anyway. The use inside a STIX indicator rather than just raw Yara allows for later usage of the indicator in the STIX data model...relate it to a TTP or campaign once that is discovered, for example.

## Data Model

<img src="diagram.png" alt="Yara Test Mechanism" class="aside-text" />

The information that the producer provides is simply the Yara signature and a Title/Description for the indicator. Given this limited information, only an [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType) is necessary to encode the information.

There are a few other details to note as well:

* The `Producer` field is set to provide a reference back to the original information source (blog entry) from Yara.
* The rule is wrapped in CDATA to ensure that any tags or things like that won't break the XML structure and don't need to be escaped.

## XML

{% highlight xml linenos %}
<stix:Indicator id="example:indicator-567b201c-4fd5-4bde-a5db-42abc340807a" timestamp="2014-06-20T15:16:56.987616+00:00" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1">
    <indicator:Title>silent_banker</indicator:Title>
    <indicator:Description>This is just an example.</indicator:Description>
    <indicator:Test_Mechanisms>
        <indicator:Test_Mechanism id="example:testmechanism-a1475567-50f7-4dae-b0d0-47c7ea8e79e1" xsi:type='yaraTM:YaraTestMechanismType'>
            <indicator:Producer>
                <stixCommon:Identity id="example:Identity-a0740d84-9fcd-44af-9033-94e76a53201e">
                    <stixCommon:Name>Yara</stixCommon:Name>
                </stixCommon:Identity>
                <stixCommon:References>
                    <stixCommon:Reference>http://plusvic.github.io/yara/</stixCommon:Reference>
                </stixCommon:References>
            </indicator:Producer>
            <yaraTM:Rule><![CDATA[
rule silent_banker : banker
{
meta:
description = "This is just an example"
thread_level = 3
in_the_wild = true

strings:
$a = {6A 40 68 00 30 00 00 6A 14 8D 91}
$b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
$c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

condition:
$a or $b or $c
}
]]></yaraTM:Rule>
        </indicator:Test_Mechanism>
    </indicator:Test_Mechanisms>
</stix:Indicator>
{% endhighlight %}

<a href="yara-test-mechanism.xml">Full XML</a>

<h2>Python</h2>

<p class="alert alert-danger"><strong>Notice</strong> The current version of python-stix, 1.1.1.0, does not support the Yara test mechanism, so this code will not work.</p>

<ul class="nav nav-tabs">
  <li class="active"><a href="#produce" data-toggle="tab">Produce</a></li>
  <li><a href="#consume" data-toggle="tab">Consume</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="produce">
{% highlight python linenos %}
rule = """
rule silent_banker : banker
{
    meta:
        description = "This is just an example"
        thread_level = 3
        in_the_wild = true

    strings:
        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
        $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

    condition:
        $a or $b or $c
}
"""

indicator = Indicator(title="silent_banker", description="This is just an example")

tm = YaraTestMechanism()
tm.rules = [rule]
tm.efficacy = "Low"
tm.producer = InformationSource(identity=Identity(name="Yara"))
tm.producer.references = ["http://plusvic.github.io/yara/"]
indicator.test_mechanisms = [tm]
{% endhighlight %}
  </div>
  <div class="tab-pane" id="consume">
{% highlight python linenos %}
stix_package = STIXPackage.from_xml('yara-test-mechanism.xml')

for indicator in stix_package.indicators:
    print "== INDICATOR =="
    print "Title: " + indicator.title
    print "Description: " + indicator.description

    for tm in indicator.test_mechanisms:
        print "Producer: " + tm.producer.identity.name
        print "Efficacy: " + tm.efficacy.value.value
        for rule in tm.rules:
            print "Rule: " + rule.value
{% endhighlight %}
  </div>
</div>

[Production Python](yara-test-mechanism-producer.py) | [Consumption Python](yara-test-mechanism-consumer.py)

## Further Reading

* The [CVE idiom](../../exploit-target/cve) has more description on how to work with the [Exploit Target](/data-model/{{site.current_version}}/et/ExploitTargetType) to describe CVEs.
* The [TTP idioms](../../ttp) describe other usage of [TTP](/data-model/{{site.current_version}}/ttp/TTPType), which may be helpful when giving Yara indicators context.
* The [YaraTestMechanism](/data-model/{{site.current_version}}/yaraTM/YaraTestMechanismType) data model documentation has more information on other fields that are available.
* Other test mechanisms are [Snort](../snort-test-mechanism), [OpenIOC](../openioc-test-mechanism), and OVAL.
