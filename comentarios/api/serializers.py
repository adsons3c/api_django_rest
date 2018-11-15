from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentarios


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('id', 'usuarios', 'comentario', 'data', 'aprovado')
