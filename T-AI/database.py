import mysql.connector

cnx = mysql.connector.connect(
    user="hackathon@tharsus-hackathon-2020",
    password="zzp2AqqcTrkUeKH",
    host="tharsus-hackathon-2020.mysql.database.azure.com",
    port=3306, ssl_verify_cert=False)



cnx.close()