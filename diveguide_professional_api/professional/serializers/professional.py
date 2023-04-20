from rest_framework import serializers

from ..models import (
    Certification,
    Language,
    Professional,
    School,
    Specialty,
    ContactInfo,
)


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = (
            "phone_number",
            "email",
            "website",
            "instagram_handle",
            "diveplus_handle",
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"


class CreateProfessionalSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True
    )
    specialties = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(), many=True
    )
    certifications = serializers.PrimaryKeyRelatedField(
        queryset=Certification.objects.all(), many=True
    )

    class Meta:
        model = Professional
        fields = [
            "first_name",
            "last_name",
            "yoe",
            "joined",
            "languages",
            "specialties",
            "certifications",
        ]


class ProfessionalSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    specialties = SpecialtySerializer(many=True)
    certifications = CertificationSerializer(many=True)

    class Meta:
        model = Professional
        fields = [
            "id",
            "first_name",
            "last_name",
            "yoe",
            "joined",
            "languages",
            "specialties",
            "certifications",
        ]


class ProfessionalToggleActiveStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = [
            "active",
        ]


class EssentialProfessionalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = [
            "id",
            "first_name",
            "last_name",
            "active",
        ]
