import requests
import ipaddress
import json

class bcpRequestController(object):
    def __init__(self, base_url=''):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = "https://api.bgpview.io"

    def query(self, entrypoint, method=requests.get, params=None):
        headers = {'Content-Type':'application/json'}

        get_request = method(self.base_url + entrypoint, params=params, headers=headers)

        if get_request.status_code == 200:
            req_response = json.loads(get_request.text)

            return(req_response['data'])

        else:
            print(get_request)

class bgpviewController(object):
    def __init__(self, bgpview=None):
        if bgpview:
            self.bgpview = bgpview
        else:
            self.bgpview = bcpRequestController()

    def get_asn_details(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn/view-asn-details

        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_asn_prefixes(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn-prefixes/view-asn-prefixes
        
        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}/prefixes'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_asn_peers(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn-peers/view-asn-peers
        
        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}/peers'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_asn_upstreams(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn-upstreams/view-asn-upstreams
        
        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}/upstreams'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_asn_downstreams(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn-downstreams/view-asn-downstreams
        
        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}/downstreams'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_asn_ixs(self, asn):
        #https://bgpview.docs.apiary.io/#reference/0/asn-ixs/view-asn-ixs
        
        if bcp_utilities.validate_asn(asn):
            entrypoint = '/asn/{}/ixs'.format(asn)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_ip_prefix(self, prefix):
        #https://bgpview.docs.apiary.io/#reference/0/prefix/view-prefix-details
        
        check_prefix = bcp_utilities.validate_cidr(prefix)

        if check_prefix:
            entrypoint = '/prefix/{}/{}'.format(check_prefix['prefix'], check_prefix['cidr'])
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_ip(self, ip):
        #https://bgpview.docs.apiary.io/#reference/0/ip/view-ip-address-details
        
        if bcp_utilities.validate_ip(ip):
            entrypoint = '/ip/{}'.format(ip)
            req = self.bgpview.query(entrypoint)
            return(req)

    def get_ix_by_id(self, ix_id):
        #https://bgpview.docs.apiary.io/#reference/0/ix/view-ix-details-and-members
        entrypoint = '/ix/{}'.format(ix_id)
        req = self.bgpview.query(entrypoint)
        return(req)

class bcp_utilities():
    def validate_asn(asn):
        #Just checks ASN is an integer, I've left the bgpview API to determine in the ASN is not actually valid since it's quicker instead of running through all the RFC ranges in a python script
        #If the ASN is reserved, it will return information regarding it being reserved with the related RFC (eg. 'description_full': 'Reserved for Private Use [RFC6996]' or 'name': 'IANA-RESERVED')
        if isinstance(asn, int):
            return(True)
        else:
            return(False)

    def validate_ip(ip):
        #Simple check with the ipaddress module, works with both ipv4 and ipv6
        try:
            ipAddr = ipaddress.ip_address(ip)
        
            if ipAddr:
                return(str(ipAddr))
            else:
                return(False)
        except:
            return(False)

    def validate_cidr(prefix):
        #Prefix needs to be in to format with CIDR, not subnet mask... Works both with IPv4 and IPv6 instead of having 2 functions...
        try:
            network = ipaddress.ip_network(prefix)
        
            if network:
                return({'prefix': str(network.network_address), 'cidr': str(network.prefixlen)})
            else:
                return(False)
        except:
            return(False)
