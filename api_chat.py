import requests
import json

def remove_first_duplicate_sentence(text):
    sentences = text.split('. ')  # 문장을 ". "로 분리
    if len(sentences) > 1 and sentences[0] == sentences[1]:
        # 첫 번째 문장이 두 번째 문장과 동일하면 첫 번째 문장을 제거
        sentences.pop(0)
    return '. '.join(sentences)  # 문장을 다시 합침

class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id
        self.processed_messages = set()  # 중복 메시지를 추적하기 위한 셋

    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }

        response_text = ""
        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                        headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    if decoded_line.startswith("data:"):
                        # JSON 부분만 추출하여 파싱
                        json_data = json.loads(decoded_line[len("data:"):])
                        if "choices" in json_data:
                            for choice in json_data["choices"]:
                                if "delta" in choice and "content" in choice["delta"]:
                                    content = choice["delta"]["content"]
                                    if content and content not in self.processed_messages:
                                        response_text += content
                                        self.processed_messages.add(content)
                        elif "message" in json_data and "content" in json_data["message"]:
                            content = json_data["message"]["content"]
                            if content and content not in self.processed_messages:
                                response_text += content
                                self.processed_messages.add(content)

        # 중복된 첫 번째 문장을 제거하고 반환
        return remove_first_duplicate_sentence(response_text)