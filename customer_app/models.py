from django.db import models


class HelpRequest(models.Model):
    ISSUE_CHOICES = [
        ('billing', 'Billing Issue'),
        ('tech', 'Technical Support'),
        ('general', 'General Inquiry'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    issue_category = models.CharField(max_length=20, choices=ISSUE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.issue_category}"
