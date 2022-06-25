## API Reference



### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 
-curl:Using curl to access the default 'http://127.0.0.1:5000 ,return json error 404
- sample curl http://127.0.0.1:5000
'''
{
error: 404,
message: "resource not found",
success: false
}
'''

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 

### List of Endpoints 
#### GET /questions
- General:
    - Returns a list of question objects,with category list , total questions and success value, 
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions`

```{
categories: [
"Science",
"Art",
"Geography",
"History",
"Entertainment",
"Sports"
],
current_category: [ ],
questions: [
{
answer: "Tom Cruise",
category: 5,
difficulty: 4,
id: 4,
question: "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
},
{
answer: "Maya Angelou",
category: 4,
difficulty: 2,
id: 5,
question: "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
},
{
answer: "Muhammad Ali",
category: 4,
difficulty: 1,
id: 9,
question: "What boxer's original name is Cassius Clay?"
},
{
answer: "Brazil",
category: 6,
difficulty: 3,
id: 10,
question: "Which is the only team to play in every soccer World Cup tournament?"
},
{
answer: "Uruguay",
category: 6,
difficulty: 4,
id: 11,
question: "Which country won the first ever soccer World Cup in 1930?"
},
{
answer: "George Washington Carver",
category: 4,
difficulty: 2,
id: 12,
question: "Who invented Peanut Butter?"
},
{
answer: "Lake Victoria",
category: 3,
difficulty: 2,
id: 13,
question: "What is the largest lake in Africa?"
},
{
answer: "The Palace of Versailles",
category: 3,
difficulty: 3,
id: 14,
question: "In which royal palace would you find the Hall of Mirrors?"
},
{
answer: "Agra",
category: 3,
difficulty: 2,
id: 15,
question: "The Taj Mahal is located in which Indian city?"
},
{
answer: "Escher",
category: 2,
difficulty: 1,
id: 16,
question: "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
}
],
success: true,
total_questions: 197
} 
```
#### get /categories/
- General:
    - returns the json object of categories with id  and success value
- `curl http://127.0.0.1:5000/categories`
```
{
categories: {
1: "Science",
2: "Art",
3: "Geography",
4: "History",
5: "Entertainment",
6: "Sports"
},
success: true
}
```

### DELETE /questions/<int:question_id>
-This delete each question in the category and return json object of deleted question id, current question ,paginated question and the sucess value

### POST/question
- This endpoint is responsible for adding new question and to search question
-The search seach for key words in the question and return error 422 if there is no result
-using curl tool for search will return json object of question,success value,and total question
-using curl tool to add question will return json object of question_id , question and success value
if there is error adding question json error of 422 will be return


### POST/play_quiz
-This endpoint responsible for adding answer to random question
-this return json object of questions and success value

