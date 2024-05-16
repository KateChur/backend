from django.http import JsonResponse
from django.views import View
import json
import requests
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# class RecommendationAPIView(View):
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             # Проверяем, есть ли данные в теле запроса
#             if request.body:
#                 try:
#                     data = json.loads(request.body)
#                     answer1 = data.get('answer1', '')
#                     answer2 = data.get('answer2', '')
#                     answer3 = data.get('answer3', '')
#                     answer4 = data.get('answer4', '')
#                     answer5 = data.get('answer5', '')
#
#                     # Формируем запрос на основе полученных ответов
#                     query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()
#
#                     if query:
#                         url = 'http://localhost:9200/products/_search'
#                         headers = {'Content-Type': 'application/json'}
#                         body = {
#                             "query": {
#                                 "multi_match": {
#                                     "query": query,
#                                     "fields": ["title", "description"]
#                                 }
#                             }
#                         }
#
#                         response = requests.post(url, json=body, headers=headers)
#
#                         if response.status_code == 200:
#                             products = [hit['_source'] for hit in response.json()['hits']['hits']]
#                             return JsonResponse(
#                                 {'products': products, 'message': 'Recommendations found successfully.'},
#                                 status=200)
#                         else:
#                             return JsonResponse({'message': 'Failed to fetch recommendations.'}, status=500)
#                     else:
#                         return JsonResponse({'message': 'No search query provided.'}, status=400)
#                 except json.JSONDecodeError as e:
#                     return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
#             else:
#                 return JsonResponse({'message': 'No data provided.'}, status=400)



# class RecommendationAPIView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             data = json.loads(request.body)
#             answer1 = data.get('answer1', '')
#             answer2 = data.get('answer2', '')
#             answer3 = data.get('answer3', '')
#             answer4 = data.get('answer4', '')
#             answer5 = data.get('answer5', '')
#
#             query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()
#
#             if not query:
#                 return JsonResponse({'message': 'No search query provided.'}, status=400)
#
#             url = 'http://localhost:9200/products/_search'
#             headers = {'Content-Type': 'application/json'}
#             body = {
#                 "query": {
#                     "multi_match": {
#                         "query": query,
#                         "fields": ["title", "description"]
#                     }
#                 }
#             }
#
#             response = requests.post(url, json=body, headers=headers)
#             response.raise_for_status()  # Raise an error for non-200 status code
#
#             products = [hit['_source'] for hit in response.json()['hits']['hits']]
#             return JsonResponse({'products': products, 'message': 'Recommendations found successfully.'}, status=200)
#
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
#
#         except requests.RequestException as e:
#             return JsonResponse({'message': f'Failed to fetch recommendations: {str(e)}'}, status=500)




# @csrf_exempt
# def post(request):
#     try:
#         data = json.loads(request.body)
#         answer1 = data.get('answer1', '')
#         answer2 = data.get('answer2', '')
#         answer3 = data.get('answer3', '')
#         answer4 = data.get('answer4', '')
#         answer5 = data.get('answer5', '')
#
#         query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()
#
#         url = 'http://localhost:9200/products/_search'
#         headers = {'Content-Type': 'application/json'}
#         body = {
#             "query": {
#                 "multi_match": {
#                     "query": query,
#                     "fields": ["title", "description"]
#                 }
#             }
#         }
#
#         response = requests.post(url, json=body, headers=headers)
#         response.raise_for_status()  # Raise an error for non-200 status code
#
#         products = [hit['_source'] for hit in response.json()['hits']['hits']]
#         print(products)
#         return JsonResponse({'products': products, 'message': 'Recommendations found successfully.'}, status=200)
#
#     except json.JSONDecodeError:
#         return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
#
#     except requests.RequestException as e:
#         return JsonResponse({'message': f'Failed to fetch recommendations: {str(e)}'}, status=500)

# Add this method to handle OPTIONS requests
# @csrf_exempt
# def options(self, request, *args, **kwargs):
#     response = JsonResponse({'message': 'Your CORS allowed message'})
#     response["Access-Control-Allow-Origin"] = "http://http://localhost:5173/user"
#     response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
#     response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
#     response["Access-Control-Allow-Credentials"] = "true"  # Если куки должны быть отправлены
#     return response


# @csrf_exempt
# def post(request):
#     try:
#         data = json.loads(request.body)
#         answer1 = data.get('answer1', '')
#         answer2 = data.get('answer2', '')
#         answer3 = data.get('answer3', '')
#         answer4 = data.get('answer4', '')
#         answer5 = data.get('answer5', '')
#
#         query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()
#
#         url = 'http://localhost:9200/products/_search'
#         headers = {'Content-Type': 'application/json'}
#         body = {
#             "query": {
#                 "multi_match": {
#                     "query": query,
#                     "fields": ["title", "description"]
#                 }
#             }
#         }
#
#         response = requests.post(url, json=body, headers=headers)
#         response.raise_for_status()  # Raise an error for non-200 status code
#
#         products = [hit['_source'] for hit in response.json()['hits']['hits']]
#         print(products)  # Выводим продукты в консоль
#         return JsonResponse({'products': products, 'message': 'Recommendations found successfully.'}, status=200)
#
#     except json.JSONDecodeError:
#         return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
#
#     except requests.RequestException as e:
#         return JsonResponse({'message': f'Failed to fetch recommendations: {str(e)}'}, status=500)


@csrf_exempt
def post(request):
    try:
        # Используем json.loads для преобразования данных тела запроса в формате JSON в словарь Python
        data = json.loads(request.body.decode('utf-8'))
        answer1 = data.get('answer1', '')
        answer2 = data.get('answer2', '')
        answer3 = data.get('answer3', '')
        answer4 = data.get('answer4', '')
        answer5 = data.get('answer5', '')

        query = f"{answer1} {answer2} {answer3} {answer4} {answer5}".strip()

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
        response.raise_for_status()  # Raise an error for non-200 status code

        products = [hit['_source'] for hit in response.json()['hits']['hits']]
        print(products)  # Выводим продукты в консоль
        return JsonResponse({'products': products, 'message': 'Recommendations found successfully.', 'status': '200'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON data.'}, status=400)

    except requests.RequestException as e:
        return JsonResponse({'message': f'Failed to fetch recommendations: {str(e)}'}, status=500)