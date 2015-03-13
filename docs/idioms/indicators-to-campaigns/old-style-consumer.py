import sys
from stix.core import STIXPackage

def parse_stix(pkg):
  # Collect indicators by ID
  indicators = {}
  for indicator in pkg.indicators:
    indicators[indicator.id_] = indicator

  # Walk all campaigns
  for campaign in pkg.campaigns:
    print "Campaign: " + campaign.title
    # And list relationships to indicators
    for indicator in campaign.related_indicators:
      print "  - Related To: " + indicators[indicator.item.idref].title

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)