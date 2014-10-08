---
layout: flat
title: Defining a Kill Chain
constructs:
  - TTP
summary: Learn how to represent the phases of an intrusion in a chain of actions.
---

## Scenario
Network intrusions can be seen as a series of actions taken in sequence, each relying on the success of the last. These can be seen as stages of the intrusion - starting with initial reconaissance and ending in compromise of sensitive data.
These concepts are useful in coordinating defensive measures and defining malicious actors in how they perform intrusions.
For instance, a financially motivated intruder may appear similar to an espionage-motivated one, until the final stage where they execute actions to steal their preferred type of information from the target. 
Lockheed Martin published a version of their "kill chain" concept which became the de facto standard for this purpose.

## Data model
Kill chains are captured under the [TTP object](https://stixproject.github.io/data-model/{{site.current_version}}/ttp/TTPType/) and contain a [number of phases[(https://stixproject.github.io/data-model/{{site.current_version}}/stixCommon/KillChainPhaseType/)

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="identity-group" %}{% highlight xml linenos %}
<stix:STIX_Package >
	<stix:STIX_Header>
        <stix:Title>Kill Chain Definition</stix:Title>
    </stix:STIX_Header>
    <stix:TTPs>
        <stix:Kill_Chains>
            <stixCommon:Kill_Chain id="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff" definer="LMCO" name="LM Cyber Kill Chain">
                <stixCommon:Kill_Chain_Phase ordinality="1" name="Reconnaissance" phase_id="stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a"/>
                <stixCommon:Kill_Chain_Phase ordinality="2" name="Weaponization" phase_id="stix:TTP-445b4827-3cca-42bd-8421-f2e947133c16"/>
                <stixCommon:Kill_Chain_Phase ordinality="3" name="Delivery" phase_id="stix:TTP-79a0e041-9d5f-49bb-ada4-8322622b162d"/>
                <stixCommon:Kill_Chain_Phase ordinality="4" name="Exploitation" phase_id="stix:TTP-f706e4e7-53d8-44ef-967f-81535c9db7d0"/>
                <stixCommon:Kill_Chain_Phase ordinality="5" name="Installation" phase_id="stix:TTP-e1e4e3f7-be3b-4b39-b80a-a593cfd99a4f"/>
                <stixCommon:Kill_Chain_Phase ordinality="6" name="Command and Control" phase_id="stix:TTP-d6dc32b9-2538-4951-8733-3cb9ef1daae2"/>
                <stixCommon:Kill_Chain_Phase ordinality="7" name="Actions on Objectives" phase_id="stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6"/>
            </stixCommon:Kill_Chain>
        </stix:Kill_Chains>
    </stix:TTPs>
</stix:STIX_Package>


{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_pkg = STIXPackage()
stix_header = STIXHeader()
stix_header.title = "Kill Chain Definition"
stix_pkg.stix_header = stix_header


# create LM-style kill chain 
# REF: http://stix.mitre.org/language/version1.1.1/stix_v1.1.1_lmco_killchain.xml

recon = KillChainPhase(phase_id="stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a", name="Reconnaissance", ordinality="1")
weapon = KillChainPhase(phase_id="stix:TTP-445b4827-3cca-42bd-8421-f2e947133c16", name="Weaponization", ordinality="2")
deliver = KillChainPhase(phase_id="stix:TTP-79a0e041-9d5f-49bb-ada4-8322622b162d", name="Delivery", ordinality="3")
exploit = KillChainPhase(phase_id="stix:TTP-f706e4e7-53d8-44ef-967f-81535c9db7d0", name="Exploitation", ordinality="4")
install = KillChainPhase(phase_id="stix:TTP-e1e4e3f7-be3b-4b39-b80a-a593cfd99a4f", name="Installation", ordinality="5")
control = KillChainPhase(phase_id="stix:TTP-d6dc32b9-2538-4951-8733-3cb9ef1daae2", name="Command and Control", ordinality="6")
action = KillChainPhase(phase_id="stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6", name="Actions on Objectives", ordinality="7")

chain = KillChain(id_="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff", name="LM Cyber Kill Chain")
chain.definer = "LMCO"

chain.kill_chain_phases = [recon,weapon,deliver,exploit,install,control,action]
stix_pkg.ttps.kill_chains.append(chain)

print stix_pkg.to_xml() 

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
print "== TTP =="
for chain in pkg.ttps.kill_chains:
    print "Name: " + chain.name
    print "Definer: " + chain.definer
    
    for phase in chain.kill_chain_phases: 
        print "Phase: " + str(phase.name)
    
{% endhighlight %}{% include end_tabs.html %}

[Full XML](kill-chain.xml) | [Python Producer](kill-chain_producer.py) | [Python Consumer](kill-chain_consumer.py)
## Further Reading

* [Kill Chain Definition](/data-model/{{site.current_version}}/stixCommon/KillChainType/)
