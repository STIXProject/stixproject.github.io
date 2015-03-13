---
layout: flat
title: Kill Chains in STIX
constructs:
  - TTP
summary: Learn how to represent the phases of an intrusion as a chain of actions.
---

Network intrusions can be seen as a series of actions taken in sequence, each relying on the success of the last. Stages of the intrusion progress linearly - starting with initial reconaissance and ending in compromise of sensitive data.
These concepts are useful in coordinating defensive measures and defining the behavior of malicious actors.

For instance, the behavior of a financially motivated intruder may appear similar to an espionage-motivated one until the final stage where they execute actions to steal their preferred type of information from the target.

This concept is often called a "kill chain" or a "cyber attack lifecycle".

## Defining A Kill Chain

STIX represents kill chains using the [KillChainType](data-model/{{site.current_version}}/stixCommon/KillChainType). Each kill chain contains a name, information about the definer, and a set of phases (represented using [KillChainPhaseType](data-model/{{site.current_version}}/stixCommon/KillChainPhaseType). Phases can be unordered or follow each other using the `ordinality` attribute.

The example below defines a two-phase model from scratch. Additionally, Lockheed Martin published one of the first papers on kill chains and their own kill chain has become a de facto standard for this purpose. As such, STIX has defined static IDs to use for this phase. The example below also demonstrates how to create that kill chain definition using the existing static IDs.

## Referencing A Kill Chain Phase

Kill chains are referenced by phase and kill chain ID from either indicators or TTPs using [KillChainPhaseReferenceType](/data-model/{{site.current_version}}/stixCommon/KillChainPhaseReferenceType). A kill chain reference in an indicator indicates that the indicator detects malicious behavior at that phase of the kill chain. A kill chain reference or definition in a TTP indicates that the TTP is used (malware, infrastructure, etc.) at that phase of the kill chain.

The example below demonstrates how to reference the kill chains (defined as explained above) on an indicator. The indicator contents are empty to focus on the kill chain reference.

## Example

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="kill-chain" %}{% highlight xml linenos %}
<stix:Indicators>
    <stix:Indicator id="example:indicator-f33c2b75-aa60-4ffb-9829-3746ef233311" timestamp="2014-10-21T21:10:09.423000+00:00" xsi:type='indicator:IndicatorType'>
        <indicator:Kill_Chain_Phases>
            <stixCommon:Kill_Chain_Phase/>
            <stixCommon:Kill_Chain_Phase phase_id="stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6" kill_chain_id="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff"/>
        </indicator:Kill_Chain_Phases>
    </stix:Indicator>
</stix:Indicators>
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
        <stixCommon:Kill_Chain definer="Myself" name="Organization-specific Kill Chain">
            <stixCommon:Kill_Chain_Phase name="Infect Machine"/>
            <stixCommon:Kill_Chain_Phase name="Exfiltrate Data"/>
        </stixCommon:Kill_Chain>
    </stix:Kill_Chains>
</stix:TTPs>
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

lmchain = KillChain(id_="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff", name="LM Cyber Kill Chain")
lmchain.definer = "LMCO"

lmchain.kill_chain_phases = [recon,weapon,deliver,exploit,install,control,action]
stix_pkg.ttps.kill_chains.append(lmchain)

infect = KillChainPhase(name="Infect Machine")
exfil = KillChainPhase(name="Exfiltrate Data")

mychain = KillChain(name="Organization-specific Kill Chain")
mychain.definer = "Myself"

mychain.kill_chain_phases = [infect, exfil]
stix_pkg.ttps.kill_chains.append(mychain)

indicator = Indicator()
indicator.kill_chain_phases = KillChainPhasesReference([
    KillChainPhaseReference(phase_id=exfil.phase_id,kill_chain_id=mychain.id_),
    KillChainPhaseReference(phase_id=action.phase_id,kill_chain_id=lmchain.id_)
])
stix_pkg.add_indicator(indicator)

print stix_pkg.to_xml() 

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
kill_chains = {}
kill_chain_phases = {}
print "== TTP =="
for chain in pkg.ttps.kill_chains:
    kill_chains[chain.id_] = chain.name
    print "--"
    print "Name: " + chain.name
    print "Definer: " + chain.definer
    
    for phase in chain.kill_chain_phases: 
        kill_chain_phases[phase.phase_id] = str(phase.name)
        print "Phase: " + str(phase.name)

print "== Indicator =="
for indicator in pkg.indicators:
    print "ID: " + indicator.id_
    for phase in indicator.kill_chain_phases:
        print "  == Kill Chain Reference =="
        print "  Name: " + kill_chains[phase.kill_chain_id]
        print "  Phase: " + kill_chain_phases[phase.phase_id]    
{% endhighlight %}{% include end_tabs.html %}

[Full XML](kill-chain.xml) | [Python Producer](kill-chain_producer.py) | [Python Consumer](kill-chain_consumer.py)

## Further Reading

* [Kill Chain Definition](/data-model/{{site.current_version}}/stixCommon/KillChainType/)
* [Kill Chain Phase Definition](/data-model/{{site.current_version}}/stixCommon/KillChainPhaseType/)
* [Kill Chain Phase Reference](/data-model/{{site.current_version}}/stixCommon/KillChainPhaseReferenceType)
