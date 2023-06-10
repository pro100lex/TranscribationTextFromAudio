import whisper
from pathlib import Path


def speech_recognition(file_path, model='base'):
    normalized_path = file_path.replace('\\', '/').replace('"', '')

    if Path(normalized_path).is_file() and Path(normalized_path).suffix == '.mp3':
        print('Ожидайте, процесс запущен...')
        speech_model = whisper.load_model(model)
        result = speech_model.transcribe(normalized_path)

        with open(f'recognized_texts/transcription_{normalized_path[normalized_path.rfind("/") + 1:normalized_path.rfind(".")]}_{model}.txt', 'w') as file:
            file.write(result['text'])
    else:
        print('Ошибка! Проверьте корректность пути до файла')


def main():
    models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

    path_to_file = str(input('Введите путь до файла, который нужно транскрибировать: '))

    for key, value in models.items():
        print(f'{key} => {value}')

    model_for_transcribe = int(input('Выберите модель для транскрибации: '))

    if model_for_transcribe not in models.keys():
        raise KeyError(f'Модели со значиением {model_for_transcribe} нет в списке!')

    speech_recognition(path_to_file, model=models[model_for_transcribe])


if __name__ == '__main__':
    main()
