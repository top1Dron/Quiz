from .models import Module
from django.shortcuts import get_object_or_404
from subjects.models import Subject


class ModuleServices:
    def getSubjectModules(self, subjectId):
        """return all modules with given subject"""

        subject = self.getSubject(subjectId)
        return Module.objects.filter(subject=subject[0]).all()

    def getSubject(self, subjectId):
        """return subject with given subject id"""
        
        return Subject.objects.filter(pk=subjectId)