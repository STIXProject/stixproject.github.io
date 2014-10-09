---
layout: flat
title: Linking an Indicator to Kill Chain Phase
constructs:
  - TTP
summary: Learn how to link malicious activity to a phases of its kill chain.
---

## Scenario
An Indicator may be linked to one or more malicious actions as part of a larger set of behavior called the [kill chain](/documentation/idioms/kill-chain)
STIX supports an optional list of `Related Kill Chain Phases` for each Indicator to represent its relationship to this overall sequence of actions.


In the example below, we define a kill chain and include a reference to one of its phases in an Indicator. Note the use of `phase_id` and `kill_chain_id` in reference creation.

## Data model
[Indicator objects](https://stixproject.github.io/data-model/{{site.current_version}}/indicator/IndicatorType/) can optionally reference  [Kill_Chain_Phases](https://stixproject.github.io/data-model/{{site.current_version}}/stixCommon/KillChainPhaseReferenceType/) that are linked to their usage by malicious actors.

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="indicator-w-kill-chain" %}{% highlight xml linenos %}
<stix:STIX_Package>
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
            <stixCommon:Kill_Chain id="example:killchain-3c868a49-241c-4fb6-9895-76cea4c8cf0b" definer="Myself" name="Organization-specific Kill Chain">
                <stixCommon:Kill_Chain_Phase name="Infect Machine" phase_id="example:killchainphase-86b94dd5-2ece-415e-bff8-861e1ddeab88"/>
                <stixCommon:Kill_Chain_Phase name="Exfiltrate Data" phase_id="example:killchainphase-f959a6c0-540b-4b5a-b44f-8ad6406b2c85"/>
            </stixCommon:Kill_Chain>
        </stix:Kill_Chains>
    </stix:TTPs>
</stix:STIX_Package>

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_pkg = STIXPackage()
stix_header = STIXHeader()
stix_header.title = "Kill Chain Definition"
stix_pkg.stix_header = stix_header

# make indicator 
ind = Indicator()
ind.title = "Malicious executable"
ind.description = "Resident binary which implements infostealing and credit card grabber"

# link to "Installation" phase and kill chain by ID values
infect = KillChainPhase(name="Infect Machine")
exfil = KillChainPhase(name="Exfiltrate Data")
mychain = KillChain(name="Organization-specific Kill Chain")

mychain.kill_chain_phases = [infect, exfil]
stix_pkg.ttps.kill_chains.append(mychain)    
stix_pkg.add_indicator(ind)


# add referenced phase to indicator
ind.kill_chain_phases.append(KillChainPhaseReference(phase_id=infect.phase_id,kill_chain_id = mychain.id_))

print stix_pkg.to_xml() 

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

# load kill chains
phases = {}
for chain in pkg.ttps.kill_chains:
    for phase in chain.kill_chain_phases: 
        phases [phase.phase_id] = phase.name


print "== INDICATOR =="
for ind in pkg.indicators:
    print "--"
    print "Title: " + ind.title
    print "Description: " + str(ind.description)
    for phase in ind.kill_chain_phases:
        # lookup phase by ID
        print "Kill Chain Phase: " + str(phases[phase.phase_id])
        
{% endhighlight %}{% include end_tabs.html %}

[Full XML](indicator-w-kill-chain.xml) | [Python Producer](indicator-w-kill-chain_producer.py) | [Python Consumer](indicator-w-kill-chain_consumer.py)
## Further Reading

* [Kill Chain Definition](/data-model/{{site.current_version}}/stixCommon/KillChainType/)
