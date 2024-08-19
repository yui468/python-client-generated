import unittest
import logging
from swagger_client.api.default_api import DefaultApi
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient

class TestPokemonAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # ログの設定
        logging.basicConfig(
            filename='test_pokemon_api.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
        )
        cls.logger = logging.getLogger()

    def setUp(self):
        # APIクライアントの設定
        configuration = Configuration()
        self.api_client = ApiClient(configuration)
        self.api_instance = DefaultApi(self.api_client)

    def test_get_pokemon_by_id_success(self):
        """IDでポケモンを取得する成功ケース"""
        pokemon_id = 1  # フシギダネのID
        self.logger.info(f"Starting test_get_pokemon_by_id_success with ID: {pokemon_id}")
        
        try:
            # APIリクエストを実行
            response = self.api_instance.get_pokemon_by_id(pokemon_id)
            self.assertEqual(response.id, pokemon_id)
            self.assertEqual(response.name, 'bulbasaur')
            self.logger.info("test_get_pokemon_by_id_success passed")
        except ApiException as e:
            self.logger.error(f"API request failed with exception: {e}")
            self.fail(f"API request failed with exception: {e}")

    def test_get_pokemon_by_id_not_found(self):
        """無効なIDでポケモンを取得する失敗ケース"""
        invalid_id = 99999  # 存在しないID
        self.logger.info(f"Starting test_get_pokemon_by_id_not_found with ID: {invalid_id}")
        
        try:
            self.api_instance.get_pokemon_by_id(invalid_id)
            self.logger.error("Expected ApiException but none was raised")
            self.fail("Expected ApiException but none was raised")
        except ApiException as e:
            # 404 Not Foundが返ることを期待
            if e.status == 404:
                self.logger.info("test_get_pokemon_by_id_not_found passed")
            else:
                self.logger.error(f"Unexpected ApiException: {e}")
                self.fail(f"Unexpected ApiException: {e}")

    def test_custom_header(self):
        """カスタムヘッダーを設定してポケモンを取得"""
        pokemon_id = 1  # フシギダネのID
        self.logger.info(f"Starting test_custom_header with ID: {pokemon_id}")
        
        # カスタムヘッダーを設定
        self.api_client.default_headers['Custom-Header'] = 'TestValue'
        
        try:
            # APIリクエストを実行
            response = self.api_instance.get_pokemon_by_id(pokemon_id)
            self.assertEqual(response.id, pokemon_id)
            self.assertEqual(response.name, 'bulbasaur')
            self.logger.info("test_custom_header passed")
        except ApiException as e:
            self.logger.error(f"API request failed with exception: {e}")
            self.fail(f"API request failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
