from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# APIクライアントの設定
configuration = swagger_client.Configuration()

# APIクライアントのインスタンスを作成
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pokemon_id = 1  # 例: ポケモンID 1（フシギダネ）

try:
    # IDでポケモン情報を取得
    api_response = api_instance.get_pokemon_by_id(pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pokemon_by_id: %s\n" % e)
