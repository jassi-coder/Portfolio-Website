from django.db import models

# Create your models here.


# ABOUT
class About(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    subtitle = models.TextField()
    description=models.TextField()

    image=models.ImageField(upload_to='about/')

    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    education = models.CharField(max_length=100)

    cv_link = models.URLField()

    def __str__(self):
        return self.name



class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)

    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    description = models.TextField()
    extra_description = models.TextField(blank=True)

    technologies = models.CharField(max_length=300)
    achievements = models.TextField(help_text="Separate using |")

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def achievements_list(self):
        return [a.strip() for a in self.achievements.split('|') if a.strip()]


    def __str__(self):
        return self.company_name
    

    
class Education(models.Model):
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    description = models.TextField()

    technologies = models.CharField(
        max_length=500,
        help_text="Comma separated technologies"
    )

    learnings = models.TextField(
        help_text="Write each learning in new line"
    )

    def tech_list(self):
        return self.technologies.split(',')

    def learning_list(self):
        return self.learnings.split('\n')

    def __str__(self):
        return self.title
    


CATEGORY_CHOICES = [
    ('all','All Projects'),
    ('DA', 'Data Analysis'),
    ('WD', 'Web Development'),
    ('SD', 'Software Development'),
]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES
    )
    tech_stack = models.CharField(max_length=300)

    def tech_list(self):
        return self.tech_stack.split(',')
    

    def __str__(self):
        return self.title
    


class LiveProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    demo_link = models.URLField()
    tech_stack = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
