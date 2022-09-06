import sqlite3
import re
import pprint

# find your "History" file
conn= sqlite3.connect('C:/Users/ygok/AppData/Local/Google/Chrome/User Data/Default/History')

c= conn.cursor()

print("history length", c.execute('SELECT count(1) FROM urls').fetchone()[0])

domain_pattern= re.compile(r"http?://([^/]+)/")

domains= {}

result= True
id= 0

while result:
    result= False
    ids= []

    for row in c.execute('SELECT id, url, title FROM urls WHERE id>? LIMIT 1000', (id,)):

        result= True
        match= domain_pattern.search(row[1])
        id= row[0]

        if match:
            domain= match.group(1)
            domains[domain]= domains.get(domain, 0) + 1

            if "imgur" in domain:
                ids.append((id,))

    c.executemany("DELETE FROM urls WHERE id= ?",ids)
    conn.commit()
conn.close()

pprint.pprint(domains)