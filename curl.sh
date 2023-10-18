# attemp to search for a name
curl -i -H "Content-type: application/json" -X POST -d '{"nombre": "deNiSE SMitH"}' http://localhost:5000/api/v1/persons/searchByName

# insert a new name to the database
curl -i H "Content-type: application/json" -X POST -d '{"nombre": "nEw NAme"}' http://localhost:5000/api/v1/persons/insertName
