# Ira-Assignment Submission

## PART 1: Provide a detailed report outlining your approach, solution design, and the rationale behind your choices

Answer: 

Approch-
   Here, we plan on implementing a Knowledge Graph to create relationships between the various entities in our dataset, that is, customers, products they purchased, invoice Numbers, countries the customers belong to, date of purchase etc.  Once the KG is modelled generate nodes for these entities and capture the relationships between them, we plan on implementing a RAG Pipeline using LLaMa Index to retrieve the desired output by inputting a user query.
   
We have used Knowledge Graphs rather than Vector Databases for the following reason:

i. While both KG and Vector DB cab return responses for simple queries, KG outspaces Vector DB when it comes to complex queries as it looks for precise information based on traversing a graph connected by relationships

ii. Vector DB often return incomplete responses as it depends upon similarity index  and chunk limit whereas KG are directly connected by relationships.

iii. KG have a human readable representation of data whereas vector DB acts as a black box and increases hallucinations.




Code-
  The code provided includes 2 parts:
1. Code for creating KG on neo4j which is a graph DBMS
2. Code for Data Retrieval Engine.
   

