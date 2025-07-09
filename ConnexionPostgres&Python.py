import psycopg2

try:
    # Établir la connexion
    connection = psycopg2.connect(
        database="gestion_equipement",
        user="postgres",
        password="1972004d",
        host="localhost",  # ou l'adresse IP de votre serveur PostgreSQL
        port="5432"        # port par défaut de PostgreSQL
    )
    print("Connexion à la base de données PostgreSQL réussie")
except (Exception, psycopg2.Error) as error:
    print("Erreur lors de la connexion à PostgreSQL", error)
cursor = connection.cursor()
# Exécuter une requête SQL
cursor.execute("SELECT * FROM employe;")

# Récupérer les résultats
records = cursor.fetchall()

print("Données récupérées depuis la table employe :")
for row in records:
    print(row)
if connection:
    cursor.close()
    connection.close()
    print("Connexion PostgreSQL est fermée")
