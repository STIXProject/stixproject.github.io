import sys
from stix.core import STIXPackage


def parse_stix(pkg):
    # Collect campaigns by ID
    campaigns = {}
    for campaign in pkg.campaigns:
        campaigns[campaign.id_] = campaign

    # Walk all campaigns
    for indicator in pkg.indicators:
        print("Indicator: " + indicator.title)
        # And list relationships to campaigns
        # Broken, see #192
        # for campaign in indicator.related_campaigns:
        #   print "  - Related To: " + campaigns[campaign.item.idref].title

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except:
        exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
