import re


def clean_text(text):
    """Remove unnecessary spaces and empty lines from text."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def anonymize_email(text):
    """Replace email addresses with a placeholder."""
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.sub(pattern, "[EMAIL]", text)


def anonymize_phone(text):
    """Replace common phone-number formats with a placeholder."""
    pattern = r"(?<!\w)(?:\+?\d[\d\s()/.-]{6,}\d)(?!\w)"
    return re.sub(pattern, "[PHONE]", text)


def process_document(text):
    text = clean_text(text)
    text = anonymize_email(text)
    text = anonymize_phone(text)
    return text


if __name__ == "__main__":
    example = """
    Contact: example@example.com
    Telephone: +49 123 456789

    This is an example administrative document.
    """

    print(process_document(example))
