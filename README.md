## How to Run the Program
- In one terminal run ```python main.py``` to run the XMLRPC server
- In a seperate terminal run ```python app.py``` to run the flask app
- Send curl messages in another (a 3rd) terminal in the format of

```curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/wiki```

```curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/news```

