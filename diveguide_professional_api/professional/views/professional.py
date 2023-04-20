from rest_framework import generics, status
from rest_framework.response import Response

from ..models import Professional
from ..serializers import (
    CreateProfessionalSerializer,
    EssentialProfessionalStatusSerializer,
    ProfessionalSerializer,
    ProfessionalToggleActiveStatusSerializer,
    ContactInfoSerializer,
)


class ProfessionalActiveUpdateView(generics.UpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalToggleActiveStatusSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = request.data.get("active", instance.active)
        instance.save()
        serializer = EssentialProfessionalStatusSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessionalCreateView(generics.CreateAPIView):
    serializer_class = CreateProfessionalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessionalDetailView(generics.RetrieveAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    def get(self, request, pk):
        try:
            professional = self.queryset.get(pk=pk, active=True)
        except Professional.DoesNotExist:
            return Response(
                {"message": "Professional does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(professional)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessionalContactInfoView(generics.RetrieveAPIView):
    queryset = Professional.objects.all()
    serializer_class = ContactInfoSerializer

    def get(self, request, pk):
        try:
            professional = self.queryset.get(pk=pk, active=True)
        except Professional.DoesNotExist:
            return Response(
                {"message": "Professional does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not hasattr(professional, "contact_info"):
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        serializer = self.serializer_class(professional.contact_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
