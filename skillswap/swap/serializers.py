from rest_framework import serializers
from .models import CustomUser, Skill, UserSkill, SwapRequest, Feedback, AdminAction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'location', 'profile_photo', 'is_public', 'availability']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'is_approved']

class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    class Meta:
        model = UserSkill
        fields = ['id', 'user', 'skill', 'skill_type']

class SwapRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()
    class Meta:
        model = SwapRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at', 'updated_at']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'swap_request', 'from_user', 'rating', 'comment', 'created_at']
