NAME = "Милорадова Дарья"
ROLE = "Начинающий Data Scientist"
DESC = "Пишу pet-projects по классическим моделям машинного обучения"
LINK_TG_CHANNEL = "https://t.me/DaryaMDK"
LINK_GITHUB = "https://github.com/DaryaMDK"
CONTACT_TG = "https://t.me/DaryaMDK"
CONTACT_EMAIL = "darya.miloradova@mail.ru"
CONTACT_PHONE = "+79850588099"


def footer():
    return "\n\n<em>Нажмите Меню для возврата.</em>"


def home_text():
    return "<strong>Выберите раздел</strong> 👇"


def about_text():
    return (
        f"<strong>{NAME}</strong>\n"
        f"<em>{ROLE}</em>\n\n"
        f"{DESC}\n\n"
        "🔗 <strong>Ссылки:</strong>\n"
        f'<a href="{LINK_TG_CHANNEL}">Telegram</a>\n'
        f'<a href="{LINK_GITHUB}">GitHub</a>'
        + footer()
    )


def projects_text():
    return f"""<strong>Мои проекты:</strong>
    
    • <a href="https://github.com/DaryaMDK/otus_ui_tests">UI тесты на Python</a>
    • <a href="https://github.com/DaryaMDK/codeceptjs_otus">Проект по тестированию на CodeceptJS</a>
    • <a href="https://github.com/DaryaMDK/otus_playwright">Проект по тестированию на Playwright</a>
{footer()}"""


def contacts_text():
    return (
        "<strong>Контакты</strong>\n\n"
        f'Telegram: <a href="{CONTACT_TG}">Написать</a>\n'
        f"Email: <code>{CONTACT_EMAIL}</code>\n"
        f"Phone: <code>{CONTACT_PHONE}</code>"
        + footer()
    )