TRANSLATIONS = {
    "spa": {
        "download": "Descargar",
        "error": "El `renderingToken` de tu currículum debe ser una cadena alfanumérica de 24 caracteres",
        "placeholder": "Introduce el `renderingToken` de tu currículum",
        "title": "Transformador de Resume.io a PDF",
    },
    "eng": {
        "download": "Download",
        "error": "Your resume `renderingToken` must be a 24-character alphanumeric string",
        "placeholder": "Enter your resume `renderingToken`",
        "title": "Resume.io to PDF converter",
    },
    "fra": {
        "download": "Télécharger",
        "error": "Le `renderingToken` de votre CV doit être une chaîne alphanumérique de 24 caractères",
        "placeholder": "Entrez le `renderingToken` de votre CV",
        "title": "Convertisseur Resume.io en PDF",
    },
    "deu": {
        "download": "Herunterladen",
        "error": "Der `renderingToken` Ihres Lebenslaufs muss eine 24-stellige alphanumerische Zeichenkette sein",
        "placeholder": "Geben Sie den `renderingToken` Ihres Lebenslaufs ein",
        "title": "Resume.io zu PDF Konverter",
    },
    "ita": {
        "download": "Scarica",
        "error": "Il `renderingToken` del tuo curriculum deve essere una stringa alfanumerica di 24 caratteri",
        "placeholder": "Inserisci il `renderingToken` del tuo curriculum",
        "title": "Convertitore Resume.io in PDF",
    },
    "por": {
        "download": "Baixar",
        "error": "O `renderingToken` do seu currículo deve ser uma string alfanumérica de 24 caracteres",
        "placeholder": "Digite o `renderingToken` do seu currículo",
        "title": "Conversor Resume.io para PDF",
    },
    "nld": {
        "download": "Downloaden",
        "error": "De `renderingToken` van je CV moet een alfanumerieke tekenreeks van 24 tekens zijn",
        "placeholder": "Voer de `renderingToken` van je CV in",
        "title": "Resume.io naar PDF converter",
    },
    "pol": {
        "download": "Pobierz",
        "error": "`renderingToken` Twojego CV musi być 24-znakowym ciągiem alfanumerycznym",
        "placeholder": "Wprowadź `renderingToken` swojego CV",
        "title": "Konwerter Resume.io do PDF",
    },
    "rus": {
        "download": "Скачать",
        "error": "`renderingToken` вашего резюме должен быть 24-символьной буквенно-цифровой строкой",
        "placeholder": "Введите `renderingToken` вашего резюме",
        "title": "Конвертер Resume.io в PDF",
    },
    "ara": {
        "download": "تحميل",
        "error": "يجب أن يكون `renderingToken` لسيرتك الذاتية سلسلة أبجدية رقمية مكونة من 24 حرفًا",
        "placeholder": "أدخل `renderingToken` لسيرتك الذاتية",
        "title": "محول Resume.io إلى PDF",
    },
    "chi_sim": {
        "download": "下载",
        "error": "您的简历 `renderingToken` 必须是24个字符的字母数字字符串",
        "placeholder": "输入您简历的 `renderingToken`",
        "title": "Resume.io 转 PDF 转换器",
    },
    "chi_tra": {
        "download": "下載",
        "error": "您的履歷 `renderingToken` 必須是24個字元的英數字串",
        "placeholder": "輸入您履歷的 `renderingToken`",
        "title": "Resume.io 轉 PDF 轉換器",
    },
    "jpn": {
        "download": "ダウンロード",
        "error": "履歴書の `renderingToken` は24文字の英数字である必要があります",
        "placeholder": "履歴書の `renderingToken` を入力してください",
        "title": "Resume.io から PDF へのコンバーター",
    },
    "kor": {
        "download": "다운로드",
        "error": "이력서의 `renderingToken`은 24자의 영숫자 문자열이어야 합니다",
        "placeholder": "이력서의 `renderingToken`을 입력하세요",
        "title": "Resume.io를 PDF로 변환",
    },
}


def i18n(lang: str, key: str) -> str:
    """
    Get a translated string for a given language and key.

    Parameters
    ----------
    lang : str
        Language code (e.g., "spa", "eng").
    key : str
        Translation key.

    Returns
    -------
    str
        Translated string, or the key if not found.
    """
    lang = lang or "spa"
    return TRANSLATIONS.get(lang, TRANSLATIONS["spa"]).get(key, key)
