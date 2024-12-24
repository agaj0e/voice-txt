import whisper
import os

def speech_recognition(model = 'base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe('C:\\Users\\USER\\PycharmProjects\\pythonProject3\\audio_eva.wav')

    with open(f'transcription_{model}.txt', 'w') as file:
        file.write(result['text'])


def main():
    models = {1: 'tiny', 2: 'base', 3:'small', 4: 'medium', 5: 'large'}
    for k, v in models.items():
        print(f'{k}:{v}')

    model = int(input('Выберите модель передав цифру от 1 до 5: '))

    if model not in models.keys():
        raise KeyError(f'Модели {model} нет в списке!')

    print('Запущен процесс транскрибации, ожидайте...')
    speech_recognition(model=models[model])


if __name__ == '__main__':
    main()