from enum import Enum


class Extension(str, Enum):
    jpeg = "jpeg"
    png = "png"
    webp = "webp"


class Language(str, Enum):
    """Tesseract OCR language codes."""

    spa = "spa"  # Español
    eng = "eng"  # English
    fra = "fra"  # Français
    deu = "deu"  # Deutsch
    ita = "ita"  # Italiano
    por = "por"  # Português
    nld = "nld"  # Nederlands
    pol = "pol"  # Polski
    rus = "rus"  # Русский
    ara = "ara"  # العربية
    chi_sim = "chi_sim"  # 简体中文
    chi_tra = "chi_tra"  # 繁體中文
    jpn = "jpn"  # 日本語
    kor = "kor"  # 한국어
