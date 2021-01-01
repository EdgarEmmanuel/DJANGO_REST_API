from django.shortcuts import render
from tutorials.models import Article
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 
from tutorials.serializers import ArticleSerializer

# Create your views here.

@api_view(['GET','POST','DELETE'])
def articles_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        title = request.GET.get('title',None)

        if title is not None:
            articles = articles.filter(title_icontains=title)
        
        articles_serializer = ArticleSerializer(articles,many=True)

        return JsonResponse(articles_serializer.data,safe=False,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        count = Article.objects.all().delete()
        return JsonResponse({"message":"Tutorials were delete successfully"},status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(data=article_data)

        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse({'message':"error during save"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def articles_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)

        if request.method == 'GET' :
            article_serializer = ArticleSerializer(article)
            return JsonResponse(article_serializer.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            article_data = JSONParser().parse(request)
            article_serializer = ArticleSerializer(article,data=article_data)
            if article_serializer.is_valid() :
                article_serializer.save()
                return JsonResponse(article_serializer.data,status=status.HTTP_201_CREATED)
            return JsonResponse({'message':"error during update"},status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            article.delete()
            return JsonResponse({"message":"delete with Success"},status=status.HTTP_200_OK)

    except Article.DoesNotExist:
        return JsonResponse({"message":"The Article do not exist "},
        status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def articles_list_published(request):
    articles_published = Article.objects.filter(published=True)

    if request.method == 'GET':
        article_serializer = ArticleSerializer(articles_published,many=True)
        return JsonResponse(article_serializer.data,safe=False,status=status.HTTP_200_OK)
    


@api_view(['GET'])
def articles_list_no_published(request):
    articles = Article.objects.filter(published=False)

    if request.method == 'GET':
        article_serializer = ArticleSerializer(articles,many=True)
        return JsonResponse(article_serializer.data,safe=False,status=status.HTTP_200_OK)
