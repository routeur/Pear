import requests, socket, json, argparse
from rich.console import Console
from rich.table import Column, Table
from rich.prompt import Prompt
import csv

def pdb_base_info_ASN (ASN, pjson=False):
    url = f'https://peeringdb.com/api/net?asn={ASN}'
    resp = requests.get(url)
    pdb_json_as = json.loads(resp.text)
    #check if it doesn't work :
    if('error' in pdb_json_as['meta']):
        return pdb_json_as['meta']['error']
    id_as = (pdb_json_as['data'][0]['id'])
    info_as_type = (pdb_json_as['data'][0]['info_type'])
    info_as_scope = (pdb_json_as['data'][0]['info_scope'])
    org_as_id = (pdb_json_as['data'][0]['org_id'])
    info_as_traffic = (pdb_json_as['data'][0]['info_traffic'])
    info_as_ratio = (pdb_json_as['data'][0]['info_ratio'])
    if(pjson):
        return {'org_id' : org_as_id , 'as_id' : id_as, 'as_scope' : info_as_scope , 'as_type' : info_as_type, 'as_traffic' : info_as_traffic, 'as_ratio' : info_as_ratio}
    else:
        return (org_as_id ,id_as, info_as_scope , info_as_type, info_as_traffic,info_as_ratio)

def pdb_other_infos (org_as_id, pjson=False):
    url_org = f'https://www.peeringdb.com/api/org?id={org_as_id}'
    resp_org = requests.get(url_org)
    pdb_org_json = json.loads(resp_org.text)
    pdb_org_created = (pdb_org_json['data'][0]['created'])
    pdb_org_updated = (pdb_org_json['data'][0]['updated'])
    pdb_org_website = (pdb_org_json['data'][0]['website'])

    if(pjson):
        return {'created' : pdb_org_created, 'update' : pdb_org_updated, 'website' : pdb_org_website}
    else:
        return (pdb_org_created, pdb_org_updated, pdb_org_website)

#Number of networks present at this facility
def pdbsearch_network_facilities (org_as_id, pjson=False):
    pdb_name_interconnect = [""]
    pdb_notes_interconnect = [""]
    pdb_city_interconnect = [""]
    pdb_orgname_inteconnect = [""]
    pdb_net_count_inteconnect = [""]
    pdb_orgname_inteconnect = [""]
    url_org = f'https://www.peeringdb.com/api/org?id={org_as_id}'
    resp_org = requests.get(url_org)
    pdb_org_json = json.loads(resp_org.text)
    pdb_org_created = (pdb_org_json['data'][0]['created'])
    pdb_org_updated = (pdb_org_json['data'][0]['updated'])
    pdb_org_website = (pdb_org_json['data'][0]['website'])
    url_all_org_info = f'https://www.peeringdb.com/api/org/{org_as_id}'
    resp_all_info_org = requests.get(url_all_org_info)
    pdb_all_org = json.loads(resp_all_info_org.text)
    pdb_liste_fac_set_org = (pdb_all_org['data'][0]['fac_set'])
    pdb_netcount_interconnect = []
    for fac_liste_org in pdb_liste_fac_set_org:
        fac_pdb_name = fac_liste_org['name']
        fac_pdb_orgname = fac_liste_org['org_name']
        fac_pdb_notes = fac_liste_org['notes']
        fac_pdb_city = fac_liste_org['city']
        fac_pdb_net_count = fac_liste_org['net_count']
        pdb_name_interconnect.append(fac_pdb_name)
        pdb_notes_interconnect.append(fac_pdb_notes)
        pdb_city_interconnect.append(fac_pdb_city)
        pdb_orgname_inteconnect.append(fac_pdb_orgname)
        pdb_net_count_inteconnect.append(fac_pdb_net_count)

    if(pjson):
        return {'orgname_interco' : pdb_orgname_inteconnect, 'name_interco' : pdb_name_interconnect, 'city_interco' : pdb_city_interconnect, 'net_count_interco' : pdb_net_count_inteconnect, 'note_interco' : pdb_notes_interconnect}
    else:
        return (pdb_orgname_inteconnect, pdb_name_interconnect, pdb_city_interconnect, pdb_net_count_inteconnect, pdb_notes_interconnect)

def pdbsearch_network_NET(org_as_id, pjson=False):
    pdb_net_id_interconect = []
    pdb_net_name_interconect = []
    pdb_net_asn_interconect = []
    pdb_net_info_type_interconect = []
    pdb_net_policy_general_interconect = []
    pdb_net_info_scope_interconect = []
    pdb_net_name_interconect = []
    pdb_net_notes_interconect = []
    pdb_net_policy_contracts_interconect = []
    pdb_net_info_traffic_interconect = []
    pdb_net_irr_as_set_interconect = []
    pdb_net_info_ratio_interconect = []
    pdb_net_website_interconect = []
    url_all_org_info = f'https://www.peeringdb.com/api/org/{org_as_id}'
    resp_all_info_org = requests.get(url_all_org_info)
    pdb_all_org = json.loads(resp_all_info_org.text)
    pdb_liste_fac_set_org = (pdb_all_org['data'][0]['net_set'])
    #c'est un NSP
    for k in range (len(pdb_liste_fac_set_org)):
        pdb_net_id = (pdb_liste_fac_set_org[k]['id'])
        pdb_net_name = (pdb_liste_fac_set_org[k]['name'])
        pdb_net_asn = (pdb_liste_fac_set_org[k]['asn'])
        pdb_net_info_type = (pdb_liste_fac_set_org[k]['info_type'])
        pdb_net_policy_general = (pdb_liste_fac_set_org[k]['policy_general'])
        pdb_net_info_scope = (pdb_liste_fac_set_org[k]['info_scope'])
        pdb_net_notes = (pdb_liste_fac_set_org[k]['notes'])
        pdb_net_policy_contracts = (pdb_liste_fac_set_org[k]['policy_contracts'])
        pdb_net_info_traffic = (pdb_liste_fac_set_org[k]['info_traffic'])
        pdb_net_irr_as_set = (pdb_liste_fac_set_org[k]['irr_as_set'])
        pdb_net_info_ratio = (pdb_liste_fac_set_org[k]['info_ratio'])
        pdb_net_website = (pdb_liste_fac_set_org[k]['website'])
        pdb_net_id_interconect.append(pdb_net_id)
        pdb_net_name_interconect.append(pdb_net_name)
        pdb_net_asn_interconect.append(pdb_net_asn)
        pdb_net_info_type_interconect.append(pdb_net_info_type)
        pdb_net_policy_general_interconect.append(pdb_net_policy_general)
        pdb_net_info_scope_interconect.append(pdb_net_info_scope)
        pdb_net_notes_interconect.append(pdb_net_notes)
        pdb_net_policy_contracts_interconect.append(pdb_net_policy_contracts)
        pdb_net_info_traffic_interconect.append(pdb_net_info_traffic)
        pdb_net_irr_as_set_interconect.append(pdb_net_irr_as_set)
        pdb_net_info_ratio_interconect.append(pdb_net_info_ratio)
        pdb_net_website_interconect.append(pdb_net_website)
    if(pjson):
        return {'net_name' : pdb_net_name_interconect, 'net_id_interco' : pdb_net_id_interconect, 'net_asn_interco' : pdb_net_asn_interconect, 'net_info_traffic_interco' : pdb_net_info_traffic_interconect, 'net_info_type_interco' : pdb_net_info_type_interconect, 'net_info_scope_interco' : pdb_net_info_scope_interconect, 'net_policy_general_interco' : pdb_net_policy_general_interconect, 'net_policy_contracts_interco' : pdb_net_policy_contracts_interconect, 'net_irr_as_set_interco' : pdb_net_irr_as_set_interconect, 'net_info_ratio_interco' : pdb_net_info_ratio_interconect, 'net_notes_interco' : pdb_net_notes_interconect, 'net_website_interco' : pdb_net_website_interconect}
    else:
        return (pdb_net_name_interconect, pdb_net_id_interconect, pdb_net_asn_interconect, pdb_net_info_traffic_interconect, pdb_net_info_type_interconect, pdb_net_info_scope_interconect, pdb_net_policy_general_interconect, pdb_net_policy_contracts_interconect, pdb_net_irr_as_set_interconect, pdb_net_info_ratio_interconect, pdb_net_notes_interconect, pdb_net_website_interconect)

def verification_NET_or_FAC(org_as_id):
    verdict = True
    url_all_org_info = f'https://www.peeringdb.com/api/org/{org_as_id}'
    resp_all_info_org = requests.get(url_all_org_info)
    pdb_all_org = json.loads(resp_all_info_org.text)
    pdb_liste_fac_set_org = (pdb_all_org['data'][0]['fac_set'])
    if pdb_liste_fac_set_org == []:
        verdict = False
    else:
        pass

    return verdict

def caida_search_by_asn (ASN, pjson=False):
    url_all_by_asn_caida = f'https://api.asrank.caida.org/v2/restful/asns/{ASN}'
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
    if(pjson):
        return {'rank' : caida_rank, 'org_id' : caida_org_id, 'source' : caida_source, 'cone_prefixes' : caida_cone_prefixes, 'cone_addresses' : caida_cone_addresses, 'cone_asns' : caida_cone_asns, 'asndegree_total' : caida_asndegree_total, 'asndegree_peer' : caida_asndegree_peer, 'asndegree_customer' : caida_asndegree_customer, 'asndegree_provider' : caida_asndegree_provider}
    else:
        return (caida_rank, caida_org_id, caida_source, caida_cone_prefixes, caida_cone_addresses, caida_cone_asns, caida_asndegree_total, caida_asndegree_peer, caida_asndegree_customer, caida_asndegree_provider)

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

    if(pjson):
        return {'organization_name' : caida_organization_name , 'organization_rank' : caida_organization_rank , 'organization_numberasn' : caida_organization_numberasn, 'organization_numberprefixes' : caida_organization_numberprefixes, 'organization_numberadresses' : caida_organization_numberadresses, 'organization_node_asn' : caida_organization_node_asn}
    else:
        return (caida_organization_name ,caida_organization_rank , caida_organization_numberasn, caida_organization_numberprefixes, caida_organization_numberadresses,caida_organization_node_asn)


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

def initialisation_de_la_table_FAC(couleur):
    ########## initialisation de la table pour les FACILITIES ########
    table_fac = Table(show_header=True, header_style=couleur)
    table_fac.add_column("NOM_ORGANISATION", style="dim", width=28)
    table_fac.add_column("NOM", style="dim", width=40)
    table_fac.add_column("VILLE", style="dim", width=28)
    table_fac.add_column("NET_COUNT", style="dim", width=28)
    table_fac.add_column("NOTES", style="dim", width=28)

    return table_fac

def initialisation_de_la_table_NET_1(couleur):
    ########## initialisation de la table pour les NSP ########
    table_net_1 = Table(show_header=True, header_style=couleur)
    table_net_1.add_column("NOM", style="dim")
    table_net_1.add_column("ID", style="dim")
    table_net_1.add_column("ASN", style="dim")
    table_net_1.add_column("INFO TRAFFIC", style="dim")
    table_net_1.add_column("TYPE", style="dim")
    table_net_1.add_column("SCOPE", style="dim")
    table_net_1.add_column("POLICY GENERALE", style="dim")

    return table_net_1

def initialisation_de_la_table_NET_2(couleur):
    ########## initialisation de la table pour les NSP ########
    table_net_2 = Table(show_header=True, header_style=couleur)
    table_net_2.add_column("POLICY CONTRACT", style="dim")
    table_net_2.add_column("IRR", style="dim")
    table_net_2.add_column("RATIO", style="dim")
    table_net_2.add_column("NOTES", style="dim")
    table_net_2.add_column("WEBSITE", style="dim")

    return table_net_2

def initialisation_de_la_table_CAIDA_orgathering(couleur):
    table_CAIDA_ORG = Table(show_header=True, header_style=couleur)
    table_CAIDA_ORG.add_column("NOM ORGANISATION", style="dim", width=28)
    table_CAIDA_ORG.add_column("CAIDA ORG RANK", style="dim", width=28)
    table_CAIDA_ORG.add_column("NB ASN", style="dim", width=28)
    table_CAIDA_ORG.add_column("NB PREFIXES", width=28)
    table_CAIDA_ORG.add_column("NB ADRESSES", width=28)
    table_CAIDA_ORG.add_column("NODE AS", width=28)

    return table_CAIDA_ORG

def initialisation_de_la_table_CAIDA_ASgathering_1(couleur):
    table_CAIDA_AS_1 = Table(show_header=True, header_style=couleur)
    table_CAIDA_AS_1.add_column("NOM ORGANISATION", style="dim", width=28)
    table_CAIDA_AS_1.add_column("CAIDA AS RANK", style="dim", width=28)
    table_CAIDA_AS_1.add_column("CAIDA ORG ID", style="dim", width=28)
    table_CAIDA_AS_1.add_column("CAIDA SOURCE", width=28)
    table_CAIDA_AS_1.add_column("CONE PREFIX", width=28)
    table_CAIDA_AS_1.add_column("CONE ADRESSES", width=28)
    table_CAIDA_AS_1.add_column("CONE ASNS", width=28)

    return table_CAIDA_AS_1

def initialisation_de_la_table_CAIDA_ASgathering_2(couleur):
    table_CAIDA_AS_2 = Table(show_header=True, header_style=couleur)
    table_CAIDA_AS_2.add_column("ASN DEGREE TOTAL", style="dim", width=28)
    table_CAIDA_AS_2.add_column("ASN DEGREE PEER", style="dim", width=28)
    table_CAIDA_AS_2.add_column("ASN DEGREE CUSTOMER", style="dim", width=28)
    table_CAIDA_AS_2.add_column("ASN DEGREE PROVIDER", width=28)

    return table_CAIDA_AS_2

def get_ASN_global_data(asn):
    pdb_base = pdb_base_info_ASN(asn, pjson=True)
    if(type(pdb_base) is str):
        return {"error" : pdb_base}
    else:
        other = pdb_other_infos(pdb_base['org_id'], pjson=True)
        network_facilities = pdbsearch_network_facilities(pdb_base['org_id'], pjson=True)
        by_asn = caida_search_by_asn(asn, pjson=True)
        org_gathering = caida_organisation_gathering(by_asn['org_id'], pjson=True)
        other_info_pdb = pdb_other_infos(pdb_base['org_id'], pjson=True)
        net_org_gathering = pdbsearch_network_NET(pdb_base['org_id'], pjson=True)
        verification = verification_NET_or_FAC(pdb_base['org_id'])
        total = {
            "base": pdb_base,
            "by_asn" : by_asn,
            "network_facilities" : network_facilities,
            "org" : org_gathering,
            "net_org" : net_org_gathering,
            "other_info" : other_info_pdb,
            "other" : other,
            "verification" : verification,
        }
        return total

if __name__ == "__main__":
    console = Console()

    console.print("MADE BY [bold red]R0uteur / https://github.com/routeur/Pear[/bold red]")
    print("")

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--asn", type=int, help="Numéro d'ASN (exemple 174)")
    parser.add_argument("-e", "--export", type=str, help="File name")
    parser_args = parser.parse_args()

    ASN = parser_args.asn
    File_name_peer_exp = parser_args.export

    pdb_base = pdb_base_info_ASN(ASN)
    if(type(pdb_base) is str):
        console.print("[bold red]ERROR[/bold red] : {}".format(pdb_base))
    else:
        other = pdb_other_infos(pdb_base[0])
        network_facilities = pdbsearch_network_facilities(pdb_base[0])
        by_asn = caida_search_by_asn(ASN)
        org_gathering = caida_organisation_gathering(by_asn[1])
        other_info_pdb = pdb_other_infos(pdb_base[0])
        net_org_gathering = pdbsearch_network_NET(pdb_base[0])

        verification = verification_NET_or_FAC(pdb_base[0])
        if verification == True:
            table_fac = initialisation_de_la_table_FAC("bold green")
            nsporinfra = "NETWORK"
        else:
            table_net_1 = initialisation_de_la_table_NET_1("bold green")
            table_net_2 = initialisation_de_la_table_NET_2("bold green")
            nsporinfra = "ORGANISATION"

        table_CAIDA_ORG = initialisation_de_la_table_CAIDA_orgathering("#E6A52C")
        table_CAIDA_AS_1 = initialisation_de_la_table_CAIDA_ASgathering_1("#29A081")
        table_CAIDA_AS_2 = initialisation_de_la_table_CAIDA_ASgathering_2("#29A081")

        accent = ("'")

        if nsporinfra == "NETWORK" :
            for i in range (0, len(network_facilities)) :
                table_fac.add_row(
                    f'{network_facilities[0][i]}', f'{network_facilities[1][i]}', f'{network_facilities[2][i]}', f'{network_facilities[3][i]}', f'{network_facilities[4][i]}'
                    )
        else:
            for j in range (0, len(net_org_gathering[0])) :
                table_net_1.add_row(
                    f'{net_org_gathering[0][j]}', f'{net_org_gathering[1][j]}', f'{net_org_gathering[2][j]}', f'{net_org_gathering[3][j]}', f'{net_org_gathering[4][j]}', f'{net_org_gathering[5][j]}', f'{net_org_gathering[6][j]}'
                    )
                table_net_2.add_row(
                    f'{net_org_gathering[7][j]}', f'{net_org_gathering[8][j]}', f'{net_org_gathering[9][j]}', f'{net_org_gathering[10][j]}', f'{net_org_gathering[11][j]}'
                    )

        table_CAIDA_ORG.add_row(
            f'{org_gathering[0]}', f'{org_gathering[1]}', f'{org_gathering[2]}', f'{org_gathering[3]}', f'{org_gathering[4]}',f'{org_gathering[5]}'
            )
        table_CAIDA_AS_1.add_row(
            f'{org_gathering[0]}', f'{by_asn[0]}', f'{by_asn[1]}', f'{by_asn[2]}', f'{by_asn[3]}',f'{by_asn[4]}',f'{by_asn[5]}'
            )
        table_CAIDA_AS_2.add_row(
            f'{by_asn[6]}', f'{by_asn[7]}', f'{by_asn[8]}', f'{by_asn[9]}'
            )

        console.print(f'                                                         [bold magenta] {nsporinfra} [/bold magenta]')

        if nsporinfra == "NETWORK" :
            console.print(table_fac)
        else:
            console.print(table_net_1)
            console.print(table_net_2)

        console.print("                                                         [bold magenta] PEERING DB RESULTS [/bold magenta]")
        console.print(table_CAIDA_ORG)
        console.print("                                                         [bold magenta] CAIDA RESULTS [/bold magenta]")
        console.print(table_CAIDA_AS_1)
        console.print(table_CAIDA_AS_2)

    if type(File_name_peer_exp) == str:
        export_CSV_ASN_PEER(ASN,File_name_peer_exp)
    else:
        pass
