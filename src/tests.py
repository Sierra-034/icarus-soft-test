import json
import unittest
from datetime import datetime

from config import config_dict
from main import create_app
from models import db, Bitacora

def helper_time_evaluation(time_1, time_2):
    return (
        time_1.hour == time_2.hour and
        time_1.minute == time_2.minute and
        time_1.second == time_2.second
    )

class PersonTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        environment = config_dict['test']
        cls.app = create_app(environment)

    @classmethod
    def tearDownClass(cls) -> None:
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def setUp(self) -> None:
        self.client = self.app.test_client()
        self.content_type = 'application/json'

    def test_search_by_name(self):
        path = 'http://127.0.0.1:5000/api/v1/persons/searchByName'
        request_data = { 'nombre': 'DEnIse sMIth' }
        response = self.client.post(
            path=path,
            data=json.dumps(request_data),
            content_type=self.content_type, )

        response_data = json.loads(response.data.decode('utf-8'))
        encontrado = response_data['encontrado']

        with self.app.app_context():
            stmt = db.select(Bitacora).order_by(Bitacora.date_time)
            bitacora = db.session.execute(stmt).fetchone()
            bitacora_time = bitacora[0].date_time
            now = datetime.now()
        
        self.assertTrue(helper_time_evaluation(bitacora_time, now))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(encontrado)
    
    def test_insert_name(self):
        path = 'http://127.0.0.1:5000/api/v1/persons/insertName'
        request_data = { 'nombre': 'Jamie Drake'}
        response = self.client.post(
            path=path,
            data=json.dumps(request_data),
            content_type=self.content_type, )

        response_data = json.loads(response.data.decode('utf-8'))
        insert_response = response_data['message']

        self.assertEqual(insert_response, 'Successful operation')
        self.assertEqual(response.status_code, 201)
        pass


if __name__ == '__main__':
    unittest.main()
