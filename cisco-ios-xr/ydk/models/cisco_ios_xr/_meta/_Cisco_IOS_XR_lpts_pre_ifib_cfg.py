


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LptsPreIFibPrecedenceNumberEnum' : _MetaInfoEnum('LptsPreIFibPrecedenceNumberEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg',
        {
            'critical':'critical',
            'flash':'flash',
            'flash-override':'flash_override',
            'immediate':'immediate',
            'internet':'internet',
            'network':'network',
            'priority':'priority',
            'routine':'routine',
        }, 'Cisco-IOS-XR-lpts-pre-ifib-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg']),
    'LptsFlowEnum' : _MetaInfoEnum('LptsFlowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg',
        {
            'config-default':'config_default',
            'l2tpv2-fragment':'l2tpv2_fragment',
            'fragment':'fragment',
            'ospf-multicast-known':'ospf_multicast_known',
            'ospf-multicast-default':'ospf_multicast_default',
            'ospf-unicast-known':'ospf_unicast_known',
            'ospf-unicast-default':'ospf_unicast_default',
            'isis-known':'isis_known',
            'isis-default':'isis_default',
            'bfd-known':'bfd_known',
            'bfd-default':'bfd_default',
            'bfd-multipath-known':'bfd_multipath_known',
            'bfd-multipath0':'bfd_multipath0',
            'bfd-blb-known':'bfd_blb_known',
            'bfd-blb0':'bfd_blb0',
            'bfd-sp0':'bfd_sp0',
            'bgp-known':'bgp_known',
            'bgp-config-peer':'bgp_config_peer',
            'bgp-default':'bgp_default',
            'pim-multicast-default':'pim_multicast_default',
            'pim-multicast-known':'pim_multicast_known',
            'pim-unicast':'pim_unicast',
            'igmp':'igmp',
            'icmp-local':'icmp_local',
            'icmp-app':'icmp_app',
            'icmp-control':'icmp_control',
            'icmp-default':'icmp_default',
            'icmp-app-default':'icmp_app_default',
            'ldp-tcp-known':'ldp_tcp_known',
            'ldp-tcp-config-peer':'ldp_tcp_config_peer',
            'ldp-tcp-default':'ldp_tcp_default',
            'ldp-udp':'ldp_udp',
            'all-routers':'all_routers',
            'lmp-tcp-known':'lmp_tcp_known',
            'lmp-tcp-config-peer':'lmp_tcp_config_peer',
            'lmp-tcp-default':'lmp_tcp_default',
            'lmp-udp':'lmp_udp',
            'rsvp-udp':'rsvp_udp',
            'rsvp-default':'rsvp_default',
            'rsvp-known':'rsvp_known',
            'ike':'ike',
            'ipsec-known':'ipsec_known',
            'ipsec-default':'ipsec_default',
            'ipsec-fragment':'ipsec_fragment',
            'msdp-known':'msdp_known',
            'msdp-config-peer':'msdp_config_peer',
            'msdp-default':'msdp_default',
            'snmp':'snmp',
            'ssh-known':'ssh_known',
            'ssh-default':'ssh_default',
            'http-known':'http_known',
            'http-default':'http_default',
            'shttp-known':'shttp_known',
            'shttp-default':'shttp_default',
            'telnet-known':'telnet_known',
            'telnet-default':'telnet_default',
            'css-known':'css_known',
            'css-default':'css_default',
            'rsh-known':'rsh_known',
            'rsh-default':'rsh_default',
            'udp-known':'udp_known',
            'udp-listen':'udp_listen',
            'udp-config-peer':'udp_config_peer',
            'udp-default':'udp_default',
            'tcp-known':'tcp_known',
            'tcp-listen':'tcp_listen',
            'tcp-config-peer':'tcp_config_peer',
            'tcp-default':'tcp_default',
            'multicast-known':'multicast_known',
            'multicast-default':'multicast_default',
            'raw-listen':'raw_listen',
            'raw-default':'raw_default',
            'ipsla':'ipsla',
            'eigrp':'eigrp',
            'rip':'rip',
            'l2tpv3':'l2tpv3',
            'pcep-tcp-default':'pcep_tcp_default',
            'gre':'gre',
            'vrrp':'vrrp',
            'hsrp':'hsrp',
            'mpls-ping':'mpls_ping',
            'l2tpv2-default':'l2tpv2_default',
            'l2tpv2-known':'l2tpv2_known',
            'dns':'dns',
            'radius':'radius',
            'tacacs':'tacacs',
            'ntp-default':'ntp_default',
            'ntp-known':'ntp_known',
            'mobile-ipv6':'mobile_ipv6',
            'amt':'amt',
            'sdac-tcp':'sdac_tcp',
            'radius-coa':'radius_coa',
            'rel-udp':'rel_udp',
            'dhcp4':'dhcp4',
            'dhcp6':'dhcp6',
            'onepk':'onepk',
            'exr':'exr',
        }, 'Cisco-IOS-XR-lpts-pre-ifib-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg']),
}
