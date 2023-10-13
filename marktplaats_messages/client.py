
import requests
from http.cookiejar import LWPCookieJar
from dotenv import load_dotenv
import os
import logging


class Client:
    def __init__(self, base_url="https://www.marktplaats.nl/messages/api"):
        self.base_url = base_url
        self.headers = {
            'Referer': 'https://www.marktplaats.nl/messages',
        }

        # Load environment variables from .env file
        load_dotenv()

        if os.environ.get("COOKIE") != None:
            print('Loading cookie from .env')
            self.headers['Cookie'] = os.environ.get("COOKIE")

        cookie_file = '.cookies'
        self.jar = LWPCookieJar(cookie_file)

        # Load existing cookies (file might not yet exist)
        try:
            self.jar.load()
        except:
            pass

        s = requests.Session()
        s.cookies = self.jar
        self.session = s


    def _make_request(self, endpoint, method="GET", params=None, data=None):
        url = f"{self.base_url}/{endpoint}/"
        response = self.session.request(method, url, headers=self.headers, params=params, json=data)

        # Save cookies to disk, even session cookies
        self.jar.save(ignore_discard=True)
        
        # Check if the request was successful
        response.raise_for_status()
        logging.debug('reply: %s', response.json())

        return response.json()


    def get_conversations(self, params={}):
        """
        Retrieves a list of conversations.

        Args:
            params (dict, optional): Additional parameters to filter conversations.

        Returns:
            list: A list of conversations.
        """
        
        default_params = {
            'offset': '0',
            'limit': '2',
            'excluded': 'mp:advertisement,_links'
        }
        endpoint = "conversations"
        return self._make_request(endpoint, params=default_params | params)


    def get_conversation(self, conversation_id):
        """
        Retrieves a specific conversation by its ID.

        Args:
            conversation_id (str): The ID of the conversation to retrieve.

        Returns:
            dict: The conversation details.
        """
        endpoint = f"conversations/{conversation_id}"
        return self._make_request(endpoint)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filename='app.log',
                        filemode='a')
    c = Client()
    convs = c.get_conversations()
    print(convs)
    for conv in convs['_embedded']['mc:conversations']:
        print(conv)
