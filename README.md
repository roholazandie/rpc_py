## How to Run the Program
- In one terminal run ```python main.py``` to run the XMLRPC server
- In a seperate terminal run ```python app.py``` to run the flask app
- Send curl messages in another (a 3rd) terminal in the format of

```curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/wiki```

```curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/news```

For the semantic similarity service 

```curl --header "Content-Type: application/json" --request POST --data '{"concept":"basketball", "text":"I love playing sports"}' http://localhost:8080/similarity```

```curl --header "Content-Type: application/json" --request POST --data '{"concept":"Intel", "text":"I need an Macbook."}' http://localhost:8080/similarity```