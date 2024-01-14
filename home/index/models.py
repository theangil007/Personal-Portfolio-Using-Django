from django.db import models


# Create your models here.
class color(models.Model):
    color_code = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Website Color"
        verbose_name_plural = "Website Color"

    def __str__(self):
        return self.color_code


class about_me(models.Model):
    profile_pic_url = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return "About me"


class experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.CharField(max_length=50)
    to_date = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.position


class education(models.Model):
    course = models.CharField(max_length=50)
    collage = models.CharField(max_length=50)
    from_date = models.CharField(max_length=50)
    to_date = models.CharField(max_length=50)
    grade = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return self.course


class skills(models.Model):
    language = models.CharField(max_length=50)
    score = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Skills"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.language


class certifications(models.Model):
    course_name = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Certifications"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.course_name


class project(models.Model):
    image_url = models.CharField(max_length=100)
    project_name = models.CharField(max_length=50)
    project_url = models.CharField(max_length=50)
    language1 = models.CharField(max_length=50)
    language2 = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"

    def __str__(self):
        return self.project_name
