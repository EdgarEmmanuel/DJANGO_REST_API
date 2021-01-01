from rest_framework import serializers
from tutorials.models import Article



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id',
                    'title',
                    'description',
                    'published'
                    )