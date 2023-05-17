from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from api.serializers import RecipeSerializer
from recipes.models import Recipe


class ListCreateRetriveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class AddDeleteViewMixin:

    def _add_delete_obj(self, request, model_name, **kwargs):
        recipe = get_object_or_404(Recipe, id=kwargs['pk'])
        if request.method == 'POST':
            serializer = RecipeSerializer(
                data={'user': request.user.id, 'recipe': recipe, },
                context={"request": request})
            serializer.is_valid(raise_exception=True)
            if not model_name.objects.filter(user=request.user,
                                             recipe=recipe).exists():
                model_name.objects.create(user=request.user, recipe=recipe)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        get_object_or_404(model_name, user=request.user,
                          recipe=recipe).delete()
        return Response({'detail': 'Рецепт успешно удален из избранного.'},
                        status=status.HTTP_204_NO_CONTENT)
