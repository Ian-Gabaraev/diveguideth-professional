from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Professional(models.Model):
    GENDERS = (("Male", "male"), ("Female", "female"))
    first_name = models.CharField(max_length=64, verbose_name="First name")
    last_name = models.CharField(max_length=64, verbose_name="Last name")
    gender = models.CharField(max_length=32, choices=GENDERS, verbose_name="Gender")
    yoe = models.IntegerField(verbose_name="Years of experience")
    specialties = models.ManyToManyField(
        to=Specialty, verbose_name="Specialties they teach"
    )
    certifications = models.ManyToManyField(
        to=Certification, verbose_name="Certifications they hold"
    )
    languages = models.ManyToManyField(to=Language, verbose_name="Languages spoken")

    joined = models.DateTimeField(
        null=False, blank=False, auto_now_add=True, verbose_name="Joined the platform"
    )
    active = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class SchoolMembership(models.Model):
    school = models.ForeignKey(to=School, on_delete=models.CASCADE)
    member_number = models.CharField(max_length=32, blank=True, null=True)
    pro = models.ForeignKey(to=Professional, on_delete=models.CASCADE)


class ContactInfo(models.Model):
    professional = models.OneToOneField(
        to=Professional, on_delete=models.CASCADE, related_name="contact_info"
    )
    phone_number = models.CharField(
        max_length=20, verbose_name="Phone number", null=True, blank=True
    )
    email = models.EmailField(
        max_length=254, verbose_name="Email", null=False, blank=False
    )
    website = models.URLField(
        max_length=200, verbose_name="Website", null=True, blank=True
    )
    instagram_handle = models.CharField(
        max_length=30, verbose_name="Instagram handle", null=True, blank=True
    )
    diveplus_handle = models.CharField(
        max_length=30, verbose_name="Dive+ handle", null=True, blank=True
    )

    def __str__(self):
        return "Contact info of %s %s" % (
            self.professional.first_name,
            self.professional.last_name,
        )
