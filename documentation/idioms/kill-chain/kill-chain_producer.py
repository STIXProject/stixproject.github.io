#!/usr/bin/env python

from stix.ttp import TTP

from stix.core import STIXPackage, STIXHeader
from stix.common import (InformationSource, Identity, RelatedObservable,
                         VocabString)
from stix.indicator import Indicator
from stix.ttp import TTP
                         
from stix.common.kill_chains import KillChainPhase, KillChain, KillChainPhaseReference, KillChainPhasesReference

def main():
    stix_pkg = STIXPackage()


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

if __name__ == "__main__":
    main()
