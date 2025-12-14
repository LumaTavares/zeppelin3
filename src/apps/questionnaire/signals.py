from .models import  QuestionnaireExcel, QuestionnaireGoogleForms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .services import QuestionnaireExcelService, QuestionnaireGoogleFormsService
import os

@receiver(post_save, sender=QuestionnaireExcel)
def save_document(sender, instance, created, **kwargs):
    
    if created:
        # Check if document file exists before processing
        document_path = os.path.join(settings.MEDIA_ROOT, str(instance.document))
        if os.path.exists(document_path):
            questionnaire_excel_service = QuestionnaireExcelService()
            questionnaire_excel_service.process_data(instance=instance)

@receiver(post_save, sender=QuestionnaireGoogleForms)
def save_document_google_forms(sender, instance, created, **kwargs):
    if created:
        questionnaire_google_forms_service = QuestionnaireGoogleFormsService()
        questionnaire_google_forms_service.process_data(instance=instance)