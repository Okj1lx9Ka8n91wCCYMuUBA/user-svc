import json

import google.generativeai as genai
from PIL import Image
import io
from typing import Dict, re
from fastapi import UploadFile
from ..core.config import settings


async def process_image(file: UploadFile) -> Image.Image:
    """Конвертирует UploadFile в PIL Image."""
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    return image


class GeminiService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-002",
            # system_instruction=prompt_v3
        )

    def _clean_response(self, response_text: str) -> str:
        """Очищает ответ от маркеров форматирования и лишних символов."""
        cleaned = response_text.replace('```json', '').replace('```', '').strip()
        return cleaned

    @staticmethod
    def list_models():
        print("models supporting generateContent:")
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                print(m.name)

        print("\nModels supporting embedContent:")
        for m in genai.list_models():
            if "embedContent" in m.supported_generation_methods:
                print(m.name)

        print("\nOther models:")
        for m in genai.list_models():
            if not any(method in m.supported_generation_methods
                       for method in ["generateContent", "embedContent"]):
                print(m.name, m.supported_generation_methods)

    async def recognize_passport_data(
            self,
            main_page: UploadFile,
            registration_page: UploadFile | None = None
    ) -> Dict:
        try:
            main_image = await process_image(main_page)

            main_prompt = """
                Проанализируй изображение паспорта РФ и извлеки следующие данные в формате JSON:
                - series (серия паспорта, 4 цифры)
                - number (номер паспорта, 6 цифр)
                - last_name (фамилия)
                - first_name (имя)
                - middle_name (отчество)
                - birth_date (дата рождения в формате DD.MM.YYYY)
                - birth_place (место рождения)
                - issue_date (дата выдачи в формате DD.MM.YYYY)
                - issuing_authority (кем выдан)
                - department_code (код подразделения в формате XXX-XXX)
        
                Верни только JSON без дополнительного текста.
                """

            # берем данные с основной страниицы
            main_response = self.model.generate_content([main_prompt, main_image])
            cleaned_response = self._clean_response(main_response.text)
            main_data = json.loads(cleaned_response)  # Преобразуем строку JSON в dict

            if registration_page:
                reg_image = await process_image(registration_page)
                reg_prompt = """
                    Проанализируй страницу с регистрацией паспорта РФ и извлеки следующие данные в формате JSON:
                    - registration_address (адрес регистрации)
                    - registration_date (дата регистрации в формате DD.MM.YYYY)
        
                    Верни только JSON без дополнительного текста.
                    """

                reg_response = self.model.generate_content([reg_prompt, reg_image])
                reg_data = eval(reg_response.text)  # Преобразуем строку JSON в dict
                main_data.update(reg_data)

            return main_data

        except Exception as e:
            raise Exception(f"Error processing passport data: {str(e)}")


gemini_service = GeminiService()

if __name__ == '__main__':
    gemini_service.list_models()
    pass
