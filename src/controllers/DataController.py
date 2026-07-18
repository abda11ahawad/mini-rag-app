from fastapi import UploadFile
from .BaseController import BaseController
from .ProjectController import ProjectController
from models import ResponseSignal
import re
import os


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Convert MB to Bytes

    # Validate the uploaded file based on type and size
    
    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True , ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    # def generate_unique_filename(self, original_filename: str, project_id: str):
    #     extension = original_filename.split(".")[-1]
    #     unique_name = self.generate_random_string()
    #     return f"{unique_name}.{extension}"