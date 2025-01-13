# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
# from contact.models import Contact  # Use the correct app name

# from django.contrib import messages

# def contact_view(request):
#     if request.method == 'POST':
#         # Get form data
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save data to the database
#         contact = Contact.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )

#         # Send an email notification
#         send_mail(
#             subject=f"New Contact Form Submission: {subject}",
#             message=f"Message from {name} ({email}):\n\n{message}",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[settings.EMAIL_RECEIVER],
#             fail_silently=False,
#         )

#         return render(request, 'contact.html', {'name': name})

#     # Handle GET requests
#     return render(request, 'contact.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from contact.models import Contact
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic form validation
        if not name or not email or not subject or not message:
            messages.error(request, "All fields are required.")
            return render(request, 'contact.html')

        # Save data to the database
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send an email notification
        try:
            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=f"Message from {name} ({email}):\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_RECEIVER],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")

        return render(request, 'contact.html', {'name': name})

    # Handle GET requests
    return render(request, 'contact.html')
