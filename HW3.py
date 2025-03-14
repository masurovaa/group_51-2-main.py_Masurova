""" HW3"""

import flet as ft
from datetime import datetime

def get_time_of_day():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text(
        f"{get_time_of_day()}, мир!", 
        size=15,
        weight=ft.FontWeight.BOLD,
        opacity=1, 
        animate_opacity=ft.Animation(600, 'ease_in_out'),
        animate_scale=ft.Animation(500, 'bounce_out'),
        text_align=ft.TextAlign.CENTER
    )

    greeting_history = []

    history_text = ft.Text(
        "История приветствий:", 
        style='bodyMedium',
        opacity=1,
        animate_opacity=ft.Animation(700, 'ease_in_out')
    )
    
    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"{get_time_of_day()}, {name}!"
            greeting_text.scale = 1.2
            greeting_text.opacity = 1
            greet_button.text = 'Поздороваться снова'
            greet_button.bgcolor = ft.colors.BLUE
            name_input.value = ''

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            history_text.opacity = 1
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)

    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить", on_click=clear_history)

    greet_button = ft.ElevatedButton(
        "Поздороваться", 
        on_click=on_button_click,
        bgcolor=ft.colors.RED_600,
        animate_opacity=ft.Animation(30, 'ease_in_out')
    )

    page.add(
        ft.Column(
            [
                ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER),
                greeting_text,
                name_input,
                ft.Row([greet_button, clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER 
        ),
        history_text
    )

ft.app(target=main)
