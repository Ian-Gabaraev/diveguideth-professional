from ..models.reviews import Review
from ..serializers import ReviewSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class ProfessionalReviewsView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, pro_pk):
        reviews = self.queryset.filter(pro__pk=pro_pk)

        if reviews.count() == 0:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        serializer = self.serializer_class(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
