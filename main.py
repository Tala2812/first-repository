def main():

    text = "Привет из ветки main!"

    # ANSI escape-коды для изменения цвета текста
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    reset_color = "\033[0m"


    colored_text = ""
    for i, char in enumerate(text):
        color_code = colors[i % len(colors)]  # Выбор цвета по индексу
        colored_text += f"{color_code}{char}"

    # Добавляем сброс цвета в конце
    colored_text += reset_color

    
    print(colored_text)

if __name__ == "__main__":
    main()


