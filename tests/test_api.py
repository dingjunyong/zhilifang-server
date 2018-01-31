import requests
from unittest.case import TestCase
from unittest import main


class ApiTest(TestCase):
    def test_api_shop_register(self):
        url = 'http://127.0.0.1:5000/api/shops/register'
        data = {
            'shop_name': '喜洋洋汽车美容会所',
            'mobile_number': '13632914171',
            'mobile_code': '0000',
            'password':'123456',
        }
        r = requests.post(url=url,data=data)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    main()
