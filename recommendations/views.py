from django.http import JsonResponse
from django.views import View
import json
import requests


class RecommendationAPIView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Проверяем, есть ли данные в теле запроса
            if request.body:
                try:
                    data = json.loads(request.body)
                    answer1 = data.get('answer1', '')
                    answer2 = data.get('answer2', '')
                    answer3 = data.get('answer3', '')
                    answer4 = data.get('answer4', '')
                    answer5 = data.get('answer5', '')

                    # Формируем запрос на основе полученных ответов
                    query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()

                    if query:
                        url = 'http://localhost:9200/products/_search'
                        headers = {'Content-Type': 'application/json'}
                        body = {
                            "query": {
                                "multi_match": {
                                    "query": query,
                                    "fields": ["title", "description"]
                                }
                            }
                        }

                        response = requests.post(url, json=body, headers=headers)

                        if response.status_code == 200:
                            products = [hit['_source'] for hit in response.json()['hits']['hits']]
                            return JsonResponse(
                                {'products': products, 'message': 'Recommendations found successfully.'},
                                status=200)
                        else:
                            return JsonResponse({'message': 'Failed to fetch recommendations.'}, status=500)
                    else:
                        return JsonResponse({'message': 'No search query provided.'}, status=400)
                except json.JSONDecodeError as e:
                    return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
            else:
                return JsonResponse({'message': 'No data provided.'}, status=400)
