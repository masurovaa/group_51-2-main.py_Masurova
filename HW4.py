""" HW4"""
"""
1 .Изменить цвет текста приветствия в зависимости от времени суток.
2. Добавить кнопку "Случайное имя"
3. Добавить кнопку "Скрыть/Показать историю"
"""

import flet as ft
import random
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Список случайных имен
    random_names = ["Алтынай", "Бегимай", "Умут", "Ширин", "Элина", "Курманбек", "Адилет", 
                    "Ислам", "Диана", "Мария", "Иван", "Дмитрий", "Анастасия", "Сергей"]

    def get_greeting_and_color():
        current_hour = datetime.now().hour
        if 6 <= current_hour < 12:
            return "Доброе утро", ft.colors.YELLOW
        elif 12 <= current_hour < 18:
            return "Добрый день", ft.colors.ORANGE
        elif 18 <= current_hour < 24:
            return "Добрый вечер", ft.colors.RED
        else:
            return "Доброй ночи", ft.colors.BLUE

    greeting, color = get_greeting_and_color()

    greeting_text = ft.Text(
        f"{greeting}, мир!",
        size=25,
        weight=ft.FontWeight.BOLD,
        color=color,
        opacity=1,
        animate_opacity=ft.Animation(600, 'ease_in_out'),
        animate_scale=ft.Animation(500, 'bounce_out'),
        text_align=ft.TextAlign.CENTER
    )

    greeting_history = []
    history_text = ft.Text(
        "История приветствий:",
        size=15,
        style='bodyMedium',
        opacity=1)
    history_visible = True  # История изначально видна

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True)

    def on_button_click(e):
        name = name_input.value.strip()
        if name:
            greeting, color = get_greeting_and_color()
            greeting_text.value = f"{greeting}, {name}!"
            greeting_text.color = color
            greet_button.text = 'Поздороваться снова'
            greet_button.bgcolor = ft.colors.BLUE_400
            name_input.value = ''
            name_input.focus()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {greeting}, {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"
            greeting_text.color = ft.colors.RED_100
        page.update()

    def set_random_name(e):
        name_input.value = random.choice(random_names)
        name_input.focus()
        page.update()

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def toggle_history(e):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        toggle_history_button.text = "Показать историю" if not history_visible else "Скрыть историю"
        page.update()

    # Передаём обработчик on_submit после её объявления
    name_input.on_submit = on_button_click

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)
    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить историю", on_click=clear_history)
    random_name_button = ft.ElevatedButton("Случайное имя", on_click=set_random_name, bgcolor=ft.colors.BLUE_200)
    toggle_history_button = ft.ElevatedButton("Скрыть историю", on_click=toggle_history, bgcolor=ft.colors.BLACK12)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click, bgcolor=ft.colors.RED_300)

    page.add(
        ft.Column(
            [
                ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER),
                greeting_text,
                ft.Row([greet_button, random_name_button, clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
                name_input,
                ft.Row([toggle_history_button], alignment=ft.MainAxisAlignment.START),
                ft.Row([history_text], alignment=ft.MainAxisAlignment.START)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)