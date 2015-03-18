#!/usr/bin/env python

from stix.ttp import TTP
from stix.indicator import Indicator
from stix.core import STIXPackage, STIXHeader
from stix.common import (InformationSource, Identity, RelatedObservable,
                         VocabString)
                         
from stix.common.kill_chains import KillChain,KillChainPhase, KillChainPhaseReference

def main():
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

if __name__ == "__main__":
    main()
