from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from task3.serializer import ProductSerializer
from task3.models import Product
from task3.renderers import CustomAesRenderer
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .renderers import AES_SECRET_KEY, AES_IV
import json

class ProductListPlainView(APIView):
    def get(self, request):
        agents = Product.objects.all()
        if agents:
            serializer = ProductSerializer(agents, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
            }
        return Response(data, status=status.HTTP_200_OK)


class ProductListEncryptedView(APIView):
    renderer_classes = [CustomAesRenderer]

    def get(self, request):
        agents = Product.objects.all()
        if agents:
            serializer = ProductSerializer(agents, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
            }
        return Response(data, status=status.HTTP_200_OK)


class DecryptProductList(APIView):
    def post(self, request, *args, **kwargs):
        encrypted_data = request.data['ciphertext']
        enc = base64.b64decode(encrypted_data)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        try:
            decrypted_data = unpad(cipher.decrypt(enc), 16)
            decrypted_data = json.loads(decrypted_data)
            data = {
                "data": decrypted_data
            }
            return Response(data)
        except Exception as e:
            return Response({"data": f"An error- {e}"})
