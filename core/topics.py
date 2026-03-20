"""
Модуль тем и сообщений.

Модуль предназначен для создания тем форума
и добавления сообщений в обсуждения.
"""

def create_topic(title, author):
    """
    Создаёт новую тему форума.

    Args:
        title (str): Название темы.
        author (str): Автор темы.

    Returns:
        None
    """
    print(f"Тема '{title}' создана пользователем {author}")

def add_message(topic, author, text):
    """
    Добавляет сообщение в тему.

    Args:
        topic (str): Название темы.
        author (str): Автор сообщения.
        text (str): Текст сообщения.

    Returns:
        None
    """
    print(f"В тему '{topic}' добавлено сообщение от {author}: {text}")