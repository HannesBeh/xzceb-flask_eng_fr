import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

def englishToFrench(englishText, language_translator):
    """
    Translates english text to french text
    """
    if not englishText:
        return ''
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation.translations

def frenchToEnglish(frenchtText, language_translator):
    """
    Translates french text to english text
    """
    if not frenchtText:
        return ''
    translation = language_translator.translate(
        text=englishText,
        model_id='fr-en').get_result()
    return translation.translations


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')
