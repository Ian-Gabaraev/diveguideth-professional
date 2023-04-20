from django.contrib import admin

from .models import (
    Certification,
    Language,
    Professional,
    Review,
    School,
    Specialty,
    ContactInfo,
    SchoolMembership,
)


class SchoolMembershipAdmin(admin.ModelAdmin):
    model = SchoolMembership


class ReviewAdmin(admin.ModelAdmin):
    model = Review


class ContactInfoAdmin(admin.ModelAdmin):
    model = ContactInfo


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "joined")
    model = Professional


class LanguageAdmin(admin.ModelAdmin):
    model = Language


class SchoolAdmin(admin.ModelAdmin):
    model = School


class SpecialtyAdmin(admin.ModelAdmin):
    model = Specialty


class CertificationAdmin(admin.ModelAdmin):
    model = Certification


admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(SchoolMembership, SchoolMembershipAdmin)
