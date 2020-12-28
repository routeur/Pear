#  :pear: Pear (Documentation en cours)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

***:fr: Pear est un script qui permet de recuperer des informations sur une AS.***  
:us: Pear is a script for gathering info from an ASNumber.


![image](https://user-images.githubusercontent.com/49996859/103186885-8a88ab80-48c2-11eb-8b64-0b043c40462e.png)

  
***:fr: Comment l'installer ?***  
:us: How to download it ?

via github :

```git clone https://github.com/routeur/Pear```

Then :

```cd Pear```

And :

```pip install -r requirement.txt```

:fr: **Comment le faire run ?**  
:us: **How to run it ?**  

```python3 Pear.py```

# :open_book:	DOCUMENTATION

#### INTRODUCTION

:fr: **Qu'est ce qu'un ASN ?**  
>Un Autonomous System (AS), ou système autonome, est un ensemble de réseaux informatiques IP intégrés à Internet et dont la politique de routage interne est cohérente. Un AS est généralement sous le contrôle d'une entité ou organisation unique. (wikipedia)
Un AS s'engage generalement dans des accords de peering, la plus part des accords d'interconnexion sont tennus secrets mais certainnes de ces informations peuvent être déduites par des dérivés de traceroute et des dataset de topologie BGP.

:us: **What is an ASN ?**
>An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the internet (wikipedia)
An AS engage thmeself to some peering agreement, although most interconnection peering agreements between networks are secret but some information can be inferred from traceroute-derived and BGP-derived Internet topology data sets.

:fr: **Qu'est ce que peeringdb ? :**  
>Peeringdb à été crée pour faciliter le peering entre les réseaux ainsi qu'entre les coordonnateurs de peering mais pas que, dans la base de donnée de peeringdb on peux retrouver des données d'interconnexions sur les réseaux , clouds , services et entreprises.
Peeringdb est une organisation à but non lucrative et gerée par des benevoles.

*:us: **What is peeringdb ? :**  
>PeeringDB was set up to facilitate peering between networks and peering coordinators and that includes all types of interconnection data for networks, clouds, services, and enterprise, as well as interconnection facilities.
Peeringdb is a non-profit organisation and maintained by volunteers.  

:fr: ***MOTS CLÉS :***  
:us: ***KEYWORDS :***

:fr: Network facilities:
>Network Facilities inclus tout ce qui est lié à l'infrastructure réseeau (inclus les cables, conduits, switches et autres équipements) ainsi que les Centres Opérations de réseau terrains et batiments associés

:us: Network facilities:
>Network Facilities means all material network facilities (including cables, wires, conduits, switches etc..) and related material operating support systems, network operations centers land and buildings associated therewith

:fr: NET COUNT
>Nombres de réseaux présent dans cette Facilitie  

:us: NET COUNT
>Number of networks present at this facility

:fr: IRR
>Reference à un AS-SET ou ROUTE-SET d'un Internet Routing Registry  
Le Registre du Routage Internet (Internet Routing Registry ou IRR) décrit les enregistrements maintenus
par de nombreuses organisations réseaux nationales ou internationales

:us: IRR
>Reference to an AS-SET or ROUTE-SET in Internet Routing Registry
The IRR (Internet Routing Registry ou IRR) describe the records maintained by national or international network organizations

:fr: DEGREE  
>Un DEGREE est le nombre de neighbors que possède un node ou un AS
Il y a plusieurs types de DEGREE : global, out, and transit.
***-Entre autre, un global DEGREE est un DEGREE standard dans lequel tout les AS neighbors sont comptés***
-Out et transit DEGREE, toutefois, changent en fonction des chemins observés.
Par exemple, **l'out DEGREE compte uniquement les neighbors qui suivent le chemin de l'AS** et le **transit degree compte uniquement les neighbor qui sont trouvés sur le chemin de l'AS entre ce dernier ainsi que ses neighbor.**
Vous pouvez voir ce lien pour plus de details (https://asrank.caida.org/about#rank)

:us: DEGREE  
>Degree is the number of neighbors that a node, AS has.  
There are various types of degrees: global, out, and transit:  
***-Specifically, a global degree is a standard degree in which all of an AS's neighbors are counted***  
-Out and transit degrees, however, change based on the observed paths.  
For example, **out degree only counts neighbors that follow the AS in the path** and **transit degree only counts neighbors that are found in at least one path where the AS is in between that neighbor and another neighbor of the AS.**
see this link for more details (https://asrank.caida.org/about#rank)

:fr: DEGREE CUSTOMER
>Un customer achete du transit à un AS
Peer to peer c'est un accord de peering entre les deux isp
Le customer à une relation de lien de montant à descendant 

:us: DEGREE CUSTOMER
>A customer buy some transit to a specific AS 
Peer to peer is an agreement between two ISP's
The customer have a uplink to downlink relationship

:fr: ASN DEGREE TOTAL  
Total des ASN DEGREE

:us: ASN DEGREE TOTAL  
Total of ASN DEGREES

:fr: reste à documenter :
***les cones , AS rank de CAIDA***
  

related project : Epic_stamina (coming soon)
  
(it may contain some bugs)
