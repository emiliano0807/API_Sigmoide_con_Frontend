# core/views.py
import numpy as np
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 1. Vista para mostrar el HTML (Frontend)
def index_view(request):
    return render(request, 'index.html')

# 2. API para calcular la sigmoide (Backend)
class SigmoideDesplazadaView(APIView):
    def get(self, request):
        try:
            x_val = float(request.query_params.get('x', 0))
            c_val = float(request.query_params.get('c', 0))

            # Fórmula: 1 / (1 + e^-(x - c))
            z = x_val - c_val
            sigmoid_result = 1 / (1 + np.exp(-z))

            clasificacion = "Clase A" if sigmoid_result >= 0.5 else "Clase B"

            data = {
                "input_x": x_val,
                "desplazamiento_c": c_val,
                "probabilidad": round(sigmoid_result, 4),
                "clasificacion": clasificacion,
            }
            return Response(data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Números inválidos"}, status=status.HTTP_400_BAD_REQUEST)