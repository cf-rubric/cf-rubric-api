"""Serializers for models.py translates to and from JSON
"""
from rest_framework import serializers
from .models import (
    Student, 
    ClassList,
    Instructors,
    Whiteboard,
    WhiteboardImage,
    CategoryNotes,
    ScoreTable,
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Student


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ClassList


class InstructorsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Instructors
        
        
class WhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Whiteboard


class CategoryNotesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CategoryNotes
        


class WhiteboardImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = WhiteboardImage



class ScoreTableSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ScoreTable
    

