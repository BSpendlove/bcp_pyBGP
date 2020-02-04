# bcp_pyBGP
Brandon's Cisco Project - Python BGP Viewer

This project is a quick and dirty Python API to interact with the bgpview's API (https://bgpview.io/)

API documentation can be found here: https://bgpview.docs.apiary.io/

"BGPView is a simple API allowing consumers to view all sort of analytics data about the current state and structure of the internet."


bgpview_controller contains all the classes/functions needed to perform the Query. You just need to initiate the bgpviewController() class with no required variables.

```python
from bgpview_controller import bgpviewController

controller = bgpviewController()
print(controller.get_asn_details(65132))
print(controller.get_ip_prefix('8.8.8.0/24'))
```

I've left most of the error handling to BGPView such as invalid AS numbers, ip addresses/networks, etc... The module is actually fairly simple and just perform http get requests to the BGPView API and returns the JSON data.