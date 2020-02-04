from bgpview_controller import *
from pprint import pprint

controller = bgpviewController()
pprint(controller.get_asn_details(65132))
pprint(controller.get_ip_prefix('8.8.8.0/24'))