# Importing files
from neo4j import GraphDatabase
import pandas as pd


# Creating a class to generate KG 
class RetailGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_knowledge_graph(self, data):
        with self.driver.session() as session:
            session.write_transaction(self._create_constraints)
            for index, row in data.iterrows():
                session.write_transaction(self._create_and_link, row, index)

    # Creating a constraint mechanism 
    @staticmethod
    def _create_constraints(tx):
        tx.run("CREATE CONSTRAINT FOR (s:Stock) REQUIRE s.code IS UNIQUE")
        tx.run("CREATE CONSTRAINT FOR (c:Customer) REQUIRE c.id IS UNIQUE")
        tx.run("CREATE CONSTRAINT FOR (country:Country) REQUIRE country.name IS UNIQUE")

    # Creating links
    @staticmethod
    def _create_and_link(tx, row, index):
        tx.run("""
        MERGE (stock:Stock {code: $stockCode})
        ON CREATE SET stock.description = $description
        MERGE (customer:Customer {id: $customerId})
        MERGE (country:Country {name: $country})
        CREATE (transaction:Transaction {
            index: $index,
            invoiceNumber: $invoice, 
            quantity: $quantity, 
            price: $price,
            invoiceDate: $invoiceDate})
        MERGE (transaction)-[:CONTAINS]->(stock)
        MERGE (transaction)-[:MADE_BY]->(customer)
        MERGE (customer)-[:LOCATED_IN]->(country)
        MERGE (stock)-[:POPULAR_IN]->(country)
        """, 
        index=index,
        invoice=row['Invoice'], 
        invoiceDate=str(row['Invoice Date']),
        stockCode=row['Stock Code'], 
        description=row['Description'],
        quantity=row['Quantity'], 
        price=row['Price'], 
        customerId=row['Customer ID'], 
        country=row['Country'])


# Reading the excel to DataFrame 
df = pd.read_excel(r'C:\Users\bhavi\Downloads\Ira\KG_dataset.xlsx')


# Establishing the Neo4j connection
retail_graph = RetailGraph(
    uri="neo4j+s://f2df9b6b.databases.neo4j.io", 
    user="neo4j", 
    password="J2e-cxFQ89JWoHnsN2LWPZaj0wtU8BfeaSXJxuCEsiY"
)

# Creating graph
retail_graph.create_knowledge_graph(df)

# Closing connection
retail_graph.close()
