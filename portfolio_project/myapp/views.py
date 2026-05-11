from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    About,
    Experience,
    Education,
    Project,
    LiveProject,
    ContactMessage
)

import json


# ================= HOME PAGE =================
def home(request):

    about = About.objects.first()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()
    live_projects = LiveProject.objects.all()

    for exp in experiences:
        exp._tech_list = [t.strip() for t in exp.technologies.split(',') if t.strip()]
        exp._achievements_list = [a.strip() for a in exp.achievements.split('|') if a.strip()]

    return render(request, 'myapp/portfolio.html', {
        'about': about,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
        'live_projects': live_projects
    })


# ================= CONTACT FORM =================
def contact_submit(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            name = data.get("name")
            email = data.get("email")
            subject = data.get("subject")
            message = data.get("message")

            # ✅ Save message in database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # ================= AUTO REPLY TO USER =================
            send_mail(
                subject="Thanks for contacting Jaspreet Singh",
                message=f"""
Hi {name},

Thank you for contacting me.

I have received your message and will respond soon.

Regards,
Jaspreet Singh
Data Analyst\Python Developer
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            # ================= NOTIFICATION EMAIL TO YOU =================
            send_mail(
                subject=f"New Portfolio Message from {name}",
                message=f"""
You received a new message from your portfolio website.

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return JsonResponse({
                "status": "success",
                "message": "Message sent successfully"
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })

    return JsonResponse({"status": "invalid request"})
