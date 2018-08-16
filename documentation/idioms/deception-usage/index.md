---
layout: flat
title: Deception for Defense
constructs:
  - Incident
  - Course of Action
summary: Leverage deception to build shared awareness of threats
---

## Scenario
Network defense teams can leverage deception to mitigate fraud and intrusions, while sharing lessons learned and effective strategies. 

One method of referencing these actions is the "Deception Kill Chain" [described by MITRE ](http://deceptionbook.com)  

An organization might send an Incident report describing their strategy :

- The Purpose of their deception: prevent intruders from unauthorized access to customer accounts 
- Their Collected Intelligence on intruders
- Creation of a Cover Story with false identity and associated accounts
- Their Plan and Preparations to link that identity to the company
- Monitoring of attempts to interact with the false identity 

## Data model
To describe deception techniques, an [Incident can reference ](https://stixproject.github.io/data-model/{{site.current_version}}/indicator/IndicatorType/) one or more [Courses of Action that describe mitigation techniques](https://stixproject.github.io/data-model/{{site.current_version}}/coa/CourseOfActionType/)

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="indicator-w-kill-chain" %}{% highlight xml linenos %}

<stix:Incidents>
    <stix:Incident id="example:incident-b44bc002-4f4c-4dea-ab8b-2dbef815d016" timestamp="2015-06-02T20:21:54.139254+00:00" xsi:type='incident:IncidentType'>
        <incident:Title>Breach of Cyber Tech Dynamics</incident:Title>
        <incident:COA_Requested>
            <incident:Course_Of_Action id="example:coa-9b5c8e6f-c7e4-45dc-812e-098d455bf023" timestamp="2015-06-02T20:21:54.139444+00:00" xsi:type='coa:CourseOfActionType'>
                <coa:Title>Monitor activity related to known compromised accounts</coa:Title>
                <coa:Stage xsi:type="stixVocabs:DeceptionVocab-1.0">Monitor</coa:Stage>
                <coa:Type xsi:type="stixVocabs:CourseOfActionTypeVocab-1.0">Redirection (Honey Pot)</coa:Type>
                <coa:Objective>
                    <coa:Description>Further investigation into intruders re-using compromised accounts</coa:Description>
                </coa:Objective>
            </incident:Course_Of_Action>
        </incident:COA_Requested>
    </stix:Incident>
</stix:Incidents>


{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
pkg = STIXPackage()
incident = Incident(title="Breach of Cyber Tech Dynamics")

coa = CourseOfAction()
coa.title = "Monitor activity related to known compromised accounts"
coa.stage = VocabString("Monitor")
coa.stage.xsi_type = "stixVocabs:DeceptionVocab-1.0"
coa.type_ = "Redirection (Honey Pot)"

obj = Objective()
obj.description = "Further investigation into intruders re-using compromised accounts"

coa.objective = obj

incident.add_coa_requested(coa)

pkg.add_incident(incident)

print pkg.to_xml()

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

print "== INCIDENT =="
for inc in pkg.incidents:
    for coa in inc.coa_requested:
      requested = coa.course_of_action
      print "COA: " + str(requested.title)
      print "Stage: "+ str(requested.stage)
      print "Type: "+ str(requested.type_)
      print "Objective: "+ str(requested.objective.description)
      
        
{% endhighlight %}{% include end_tabs.html %}

[Full XML](sample.xml) | [Python Producer](indicator-w-kill-chain_producer.py) | [Python Consumer](indicator-w-kill-chain_consumer.py)
## Further Reading

* [Kill Chain Definition](/data-model/{{site.current_version}}/stixCommon/KillChainType/)
