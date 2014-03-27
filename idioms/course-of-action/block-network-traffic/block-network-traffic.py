from stix.coa import CourseOfAction, Objective
from stix.common import Confidence
from cybox.core import Observables
from cybox.objects.address_object import Address

coa = CourseOfAction()
coa.title = "Block traffic to PIVY C2 Server (10.10.10.10)"
coa.stage = "Response"
coa.type_ = "Perimeter Blocking"

obj = Objective()
obj.description = "Block communication between the PIVY agents and the C2 Server"
obj.applicability_confidence = Confidence("High")

coa.objective = obj
coa.impact = "Low"
coa.impact.description = "This IP address is not used for legitmate hosting so there should be no operational impact."
coa.cost = "Low"
coa.efficacy = "High"

addr = Address(address_value="10.0.0.0", category=Address.CAT_IPV4)
coa.parameter_observables=Observables(addr)

print coa.to_xml()
