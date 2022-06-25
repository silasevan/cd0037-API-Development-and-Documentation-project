import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','blessing','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #test for pagination
    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["categories"])

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/questions?page=500")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        # Test for search words in questions
    def test_get_search_questions_with_results(self):
        res = self.client().post("/questions", json={"search": "faith"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 1)

    def test_get_search_questions_without_results(self):
        res = self.client().post("/questions", json={"search": "silas"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        #self.assertEqual(data["total_questions"], 0)
        self.assertEqual(len(data["questions"]), 1)
# test for new question
    def test_new_question(self):
        res = self.client().post('/questions',
                                 json={
                                     'question': 'What best footballer',
                                     'answer': 'Messi',
                                     'difficulty': 1,
                                     'category': 1
                                 }
                                 )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['questions']))

    def test_422_if_new_question_not_allowed(self):
        res = self.client().post('/questions',
                                 json={
                                     'question': 'Who is elon musk',
                                     'difficulty': 1,
                                     'category': 5
                                 }
                                 )
        self.assertEqual(res.status_code, 404)
        self.assertTrue(len(res.get_json()['message']), 'bad request')
    #test for delete question
    def test_delete_question(self):
        res = self.client().delete("/questions/6")
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 6).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 6)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["question"]))
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    #test for quiz
    def test_play_quiz(self):
        new_quiz = {'previous_questions': [],
                          'quiz_category': {'type': 'History', 'id': 6}}

        res = self.client().post('/quizzes', json=new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_play_quiz(self):
        new_quiz = {'previous_questions': []}
        res = self.client().post('/quizzes', json=new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

        #test for category
    def test_get_questions_per_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['current_category'])

    def test_404_get_questions_per_category(self):
        res = self.client().get('/categories/i/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

   
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()