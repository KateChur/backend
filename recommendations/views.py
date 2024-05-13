from django.shortcuts import render
from rest_framework import viewsets
from .models import Recommendation
from .serializers import RecommendationSerializer
from elasticsearch_dsl import Q
from .documents import RecommendationIndex
from django.http import JsonResponse


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


def search_documents(request):
    # query = request.GET.get('query', '')
    query = request.POST.get('answer1', 'answer2', 'answer3', 'answer4', 'answer5')

    if query:
        search_results = RecommendationIndex.search().query(
            Q("match", query=query, fields=['title', 'description'])
        )
        documents = search_results.to_queryset()
    else:
        documents = []
        return JsonResponse({'documents': documents, 'message': 'Error in recommendations'}, status=400)

    print(documents)
    print(search_results)
    return JsonResponse({'documents': documents, 'message': 'Recommendations founded successfully.'}, status=200)
