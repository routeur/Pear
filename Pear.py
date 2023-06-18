#!/bin/python3
import requests, json, argparse
from peeringdb import config, resource
from peeringdb.client import Client
from rich.console import Console
from rich.table import Table
import csv

pdb = Client()
net = pdb.tags.net

def pdb_base(as_number):
    asn = net.all().filter(asn=as_number).first()
    id_organisation = asn.org_id
    asn_list = net.all().filter(org_id=id_organisation)
    asn_list = [i.__dict__ for i in asn_list ]
    Facilities = pdb.all(resource.NetworkFacility).filter(local_asn=as_number)
    return asn_list, Facilities

def caida_search_by_asn (as_number,couleur, pjson=False):
    url_all_by_asn_caida = f'https://api.asrank.caida.org/v2/restful/asns/{as_number}'
    all_by_asn_caida = requests.get(url_all_by_asn_caida)
    caida_asn = json.loads(all_by_asn_caida.text)
    caida_rank = (caida_asn['data']['asn']['rank'])
    caida_org_id = (caida_asn['data']['asn']['organization']['orgId'])
    caida_source = (caida_asn['data']['asn']['source'])
    #cone
    caida_cone_prefixes = (caida_asn['data']['asn']['cone']['numberPrefixes'])
    caida_cone_addresses = (caida_asn['data']['asn']['cone']['numberAddresses'])
    caida_cone_asns = (caida_asn['data']['asn']['cone']['numberAsns'])
    #asnDegree
    caida_asndegree_total = (caida_asn['data']['asn']['asnDegree']['total'])
    caida_asndegree_peer = (caida_asn['data']['asn']['asnDegree']['peer'])
    caida_asndegree_customer = (caida_asn['data']['asn']['asnDegree']['customer'])
    caida_asndegree_provider = (caida_asn['data']['asn']['asnDegree']['provider'])
    
    if pjson:
        return {
            'Rank': caida_rank,
            'Organization ID': caida_org_id,
            'Source': caida_source,
            'Cone Prefixes': caida_cone_prefixes,
            'Cone Addresses': caida_cone_addresses,
            'Cone ASNs': caida_cone_asns,
            'ASN Degree Total': caida_asndegree_total,
            'ASN Degree Peer': caida_asndegree_peer,
            'ASN Degree Customer': caida_asndegree_customer,
            'ASN Degree Provider': caida_asndegree_provider
        }
    else:
        table_CAIDA_AS_1 = Table(title='ASN Information', header_style=couleur)
        table_CAIDA_AS_1.add_column('Info')
        table_CAIDA_AS_1.add_column('Valeur')

        table_CAIDA_AS_1.add_row('Rank', str(caida_rank))
        table_CAIDA_AS_1.add_row('Organization ID', str(caida_org_id))
        table_CAIDA_AS_1.add_row('Source', str(caida_source))
        table_CAIDA_AS_1.add_row('Cone Prefixes', str(caida_cone_prefixes))
        table_CAIDA_AS_1.add_row('Cone Addresses', str(caida_cone_addresses))
        table_CAIDA_AS_1.add_row('Cone ASNs', str(caida_cone_asns))
        table_CAIDA_AS_1.add_row('ASN Degree Total', str(caida_asndegree_total))
        table_CAIDA_AS_1.add_row('ASN Degree Peer', str(caida_asndegree_peer))
        table_CAIDA_AS_1.add_row('ASN Degree Customer', str(caida_asndegree_customer))
        table_CAIDA_AS_1.add_row('ASN Degree Provider', str(caida_asndegree_provider))

        console = Console()
        console.print(table_CAIDA_AS_1)
        
        caida_organisation_gathering(caida_org_id)

def caida_organisation_gathering (caida_org_id, pjson=False):
    url_organization_id_caida = f'https://api.asrank.caida.org/v2/restful/organizations/{caida_org_id}'
    organization_id_caida = requests.get(url_organization_id_caida)
    caida_organization_id = json.loads(organization_id_caida.text)
    caida_organization_rank = (caida_organization_id['data']['organization']['rank'])
    caida_organization_name = (caida_organization_id['data']['organization']['orgName'])
    caida_organization_numberasn = (caida_organization_id['data']['organization']['cone']['numberAsns'])
    caida_organization_numberprefixes = (caida_organization_id['data']['organization']['cone']['numberPrefixes'])
    caida_organization_numberadresses = (caida_organization_id['data']['organization']['cone']['numberAddresses'])
    caida_organization_node_asn = (caida_organization_id['data']['organization']['members']['asns']['edges'][0]['node']['asn'])

    if pjson:
        return {
            'Organization Name': caida_organization_name,
            'Organization Rank': caida_organization_rank,
            'Number of ASNs': caida_organization_numberasn,
            'Number of Prefixes': caida_organization_numberprefixes,
            'Number of Addresses': caida_organization_numberadresses,
            'Node ASN': caida_organization_node_asn
        }
    else:
        table_CAIDA_ORG = Table(title='ASN Organization Information', header_style='#E6A52C')
        table_CAIDA_ORG.add_column('Info')
        table_CAIDA_ORG.add_column('Valeur')

        table_CAIDA_ORG.add_row('Organization Name', str(caida_organization_name))
        table_CAIDA_ORG.add_row('Organization Rank', str(caida_organization_rank))
        table_CAIDA_ORG.add_row('Number of ASNs', str(caida_organization_numberasn))
        table_CAIDA_ORG.add_row('Number of Prefixes', str(caida_organization_numberprefixes))
        table_CAIDA_ORG.add_row('Number of Addresses', str(caida_organization_numberadresses))
        table_CAIDA_ORG.add_row('Node ASN', str(caida_organization_node_asn))

        console = Console()
        console.print(table_CAIDA_ORG)

def get_ASN_global_data(asn):
    pdb_base = pdb_base_info_ASN(asn, pjson=True)
    if(type(pdb_base) is str):
        return {"error" : pdb_base}
    else:
        other = pdb_other_infos(pdb_base['org_id'], pjson=True)
        network_facilities = pdbsearch_network_facilities(pdb_base['org_id'], pjson=True)
        by_asn = caida_search_by_asn(asn, pjson=True)
        org_gathering = caida_organisation_gathering(by_asn['org_id'], pjson=True)
        net_org_gathering = pdbsearch_network_NET(pdb_base['org_id'], pjson=True)
        verification = verification_NET_or_FAC(pdb_base['org_id'])
        total = {
            "base": pdb_base,
            "by_asn" : by_asn,
            "network_facilities" : network_facilities,
            "org" : org_gathering,
            "net_org" : net_org_gathering,
            "other" : other,
            "verification" : verification,
        }
        return total

def initialisation_de_la_table_FAC(couleur):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Name")
    table.add_column("AKA")
    table.add_column("IPv6")
    table.add_column("Traffic")
    table.add_column("Prefixes4")
    table.add_column("Prefixes6")
    table.add_column("Notes")
    table.add_column("Website")

    return table

def export_CSV_ASN_PEER (ASN,File_name_peer_exp):
    url = f'https://api.bgpview.io/asn/{ASN}/peers'
    bgp_data_peers = requests.get(url)
    data_peers = json.loads(bgp_data_peers.text)
    with open(f'{File_name_peer_exp}.csv', 'w', newline='',encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(["asn","name","description","country_code","version IP peering"])
        for i in range (0,(len(data_peers['data']['ipv4_peers']))):
            writer.writerow([data_peers['data']['ipv4_peers'][i]['asn'],data_peers['data']['ipv4_peers'][i]['name'] , data_peers['data']['ipv4_peers'][i]['description'],data_peers['data']['ipv4_peers'][i]['country_code'],'ipv4'])
        for i in range (0,(len(data_peers['data']['ipv6_peers']))):
            writer.writerow([data_peers['data']['ipv6_peers'][i]['asn'],data_peers['data']['ipv6_peers'][i]['name'] , data_peers['data']['ipv6_peers'][i]['description'],data_peers['data']['ipv6_peers'][i]['country_code'],'ipv6'])


if __name__ == "__main__":
    
    console = Console()
    console.print("MADE BY [bold red]Routeur / https://github.com/routeur/Pear[/bold red]")
    print("")

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--asn', type=int, help="Numéro d'ASN (exemple 174)")
    parser.add_argument('-e', '--export', type=str, help="File name")
    parser_args = parser.parse_args()

    as_number = parser_args.asn
    File_name_peer_exp = parser_args.export 

    resultat_pdb_base = pdb_base(as_number)
    main_dictonary = {"asn_list": resultat_pdb_base[0], "Network facilities": resultat_pdb_base[1]}
    table_fac = initialisation_de_la_table_FAC("green")

    names = [item['name'] for item in main_dictonary["asn_list"]]
    aka = [item['aka'] for item in main_dictonary["asn_list"]]
    info_ipv6 = [item['info_ipv6'] for item in main_dictonary["asn_list"]]
    info_traffic = [item['info_traffic'] for item in main_dictonary["asn_list"]]
    info_prefixes4 = [item['info_prefixes4'] for item in main_dictonary["asn_list"]]
    info_prefixes6 = [item['info_prefixes6'] for item in main_dictonary["asn_list"]]
    notes = [item['notes'] for item in main_dictonary["asn_list"]]
    website = [item['website'] for item in main_dictonary["asn_list"]]

    json_infos = {
        "names": names,
        "aka": aka,
        "info_ipv6": info_ipv6,
        "info_traffic": info_traffic,
        "info_prefixes4": info_prefixes4,
        "info_prefixes6": info_prefixes6,
        "notes": notes,
        "website": website
    }
    for i in range(len(json_infos["names"])):
        table_fac.add_row(
            json_infos["names"][i],
            json_infos["aka"][i],
            str(json_infos["info_ipv6"][i]),
            str(json_infos["info_traffic"][i]),
            str(json_infos["info_prefixes4"][i]),
            str(json_infos["info_prefixes6"][i]),
            json_infos["notes"][i],
            json_infos["website"][i]
        )

    console.print(table_fac)
    console.print("                                                         [bold magenta] CAIDA RESULTS [/bold magenta]")
    caida_search_by_asn(as_number,'#E6A52C')

    if type(File_name_peer_exp) == str:
        export_CSV_ASN_PEER(as_number,File_name_peer_exp)
    else:
        pass
