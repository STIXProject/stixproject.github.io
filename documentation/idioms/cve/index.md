---
layout: flat
title: CVE in an Exploit Target
constructs:
  - Exploit Target
summary: This idiom describes how to represent a disclosed vulnerability identified by a CVE using the Exploit Target construct.
---

Threat intelligence often contains references to the vulnerabilities that threat actors are targeting. When those vulnerabilities have been formally disclosed and identified (i.e., are not 0-day or unknown vulnerabilites) they are almost always identified via a [Common Vulnerabilities and Exposures (CVE®)](http://cve.mitre.org) identifier. This idiom describes how to use the STIX Exploit Target element to represent a disclosed vulnerability via its CVE ID.

## Scenario

In this scenario, we'll describe [CVE-2013-3893](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3893) using the STIX exploit target element.

## Data model

<img src="diagram.png" alt="Representing a CVE in an Exploit Target" class="aside-text" />

The relevant STIX component, [Exploit Target](/data-model/{{site.current_version}}/et/ExploitTargetType), is used to represent potential targets of cyber threat activity. This idiom describes using the exploit target to represent a disclosed vulnerability via its CVE identifier. The advantage of doing this is easier correlation with the large set of existing tools and data sources that already work with CVE.

As you can see, this is a very simple idiom to represent. The `Title` field simply gives the exploit target a human-readable title. Similarly, `Description` and `Short Description` could be used to give it longer human-readable descriptions if desired.

The `Vulnerability` field is used to represent the vulnerability itself. This field is implemented via [VulnerabilityType](/data-model/{{site.current_version}}/et/VulnerabilityType), which can be used to identify vulnerabilities via a CVE ID (as here), OSVDB ID, or even use [Common Vulnerability Reporting Framework (CVRF)](http://www.icasi.org/cvrf-1.1) to characterize an undisclosed vulnerability.

Representing the CVE ID is as easy as filling out the `CVE ID` field with a property-formatted CVE identifier.

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="cve" %}{% highlight xml linenos %}
<stixCommon:Exploit_Target xsi:type="et:ExploitTargetType" id="example:et-48a276f7-a8d7-bba2-3575-e8a63fcd488" timestamp="2014-02-20T09:00:00.000000Z">
    <et:Title>Javascript vulnerability in MSIE 6-11</et:Title>
    <et:Vulnerability>
        <et:CVE_ID>CVE-2013-3893</et:CVE_ID>
    </et:Vulnerability>
</stixCommon:Exploit_Target>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

from stix.core import STIXPackage
from stix.exploit_target import ExploitTarget, Vulnerability

vuln = Vulnerability()
vuln.cve_id = "CVE-2013-3893"
    
et = ExploitTarget(title="Javascript vulnerability in MSIE 6-11")
et.add_vulnerability(vuln)
    
print et.to_xml()
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
print("== VULNERABILITY ==")
for target in pkg.exploit_targets:
    print("---")
    print("Title : " + target.title)
    for vuln in target.vulnerabilities:
        print("CVE: " + vuln.cve_id)

{% endhighlight %}{% include end_tabs.html %}
[Full XML](cve-in-exploit-target.xml) | [Python Producer](cve-in-exploit-target_producer.py) | [Python Consumer](cve-in-exploit-target_consumer.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [ExploitTargetType](/data-model/{{site.current_version}}/et/ExploitTargetType)
