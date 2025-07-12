from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    is_public = models.BooleanField(default=True)
    availability = models.CharField(max_length=100, blank=True, null=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=True)  # Admin approval

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    OFFERED = 'OFFERED'
    WANTED = 'WANTED'
    TYPE_CHOICES = [
        (OFFERED, 'Offered'),
        (WANTED, 'Wanted'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username}: {self.skill.name} ({self.skill_type})"

class SwapRequest(models.Model):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (CANCELLED, 'Cancelled'),
    ]

    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Swap request from {self.from_user} to {self.to_user}"


class Feedback(models.Model):
    swap_request = models.ForeignKey(SwapRequest, on_delete=models.CASCADE)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Who gave feedback
    rating = models.IntegerField(default=5, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.from_user} (Rating: {self.rating})"

class AdminAction(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # "ban_user", "reject_skill", etc.
    target_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_actions', null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admin action: {self.action} on {self.target_user}"
