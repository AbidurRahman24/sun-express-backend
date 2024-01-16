from rest_framework import serializers
from . import models

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    editor = serializers.StringRelatedField(many=False)
    # doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Article
        fields = '__all__'

    # def get_queryset(self):
    #     queryset = super().get_queryset() # 7 no line ke niye aslam ba patient ke inherit korlam
    #     print(self.request.query_params)
    #     article_id = self.request.query_params.get('article_id')
    #     if article_id:
    #         queryset = queryset.filter(id=article_id)
    #     return queryset
        
class ReviewSerializer(serializers.ModelSerializer):
    viewer_email = serializers.SerializerMethodField()
    class Meta:
        model = models.Review
        fields = '__all__'

    def get_viewer_email(self, obj):
        return obj.viewer.user.email