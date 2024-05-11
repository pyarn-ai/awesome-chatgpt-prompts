import pyttsx3

# Создаем объект для синтеза речи
engine = pyttsx3.init()

# Устанавливаем свойства голоса
engine.setProperty('rate', 150)  # Скорость речи
engine.setProperty('volume', 0.9)  # Громкость речи

# Устанавливаем желаемый голос (если доступны)
voices = engine.getProperty('voices')
for voice in voices:
    if "anime" in voice.name.lower():  # Проверка наличия голоса по ключевому слову
        engine.setProperty('voice', voice.id)
        break

# Текст, который нужно проговорить
text = "Привет, я милый аниме-тян!"

# Произносим текст
engine.say(text)

# Дожидаемся завершения произношения
engine.runAndWait()
