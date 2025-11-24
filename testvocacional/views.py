import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
from django.conf import settings

class TestVocacionalView(APIView):
    def post(self, request):
        data = request.data

        area_dominante = data.get("areaDominante")
        descripcion = data.get("descripcionArea")
        counts = data.get("countsByArea")
        selecciones = data.get("selecciones")

        if not area_dominante:
            return Response({"error": "areaDominante es requerido"}, status=400)

        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        prompt = f"""
Genera análisis vocacional.
Devuelve SOLO JSON válido sin texto adicional.

Estructura:

{{
  "descripcion_personalizada": "...",
  "carreras": [
      {{ "nombre": "...", "motivo": "..." }},
      ...
  ]
}}

Datos:
Área dominante: {area_dominante}
Descripción: {descripcion}
Conteos: {counts}
Selecciones: {selecciones}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )

        contenido = response.choices[0].message.content


        # 🔥 LIMPIEZA FINAL → Convertir string a JSON real
        try:
            json_result = json.loads(contenido)
        except json.JSONDecodeError:
            return Response({
                "error": "La IA no devolvió JSON válido",
                "raw": contenido
            }, status=500)

        return Response(json_result, status=200)
