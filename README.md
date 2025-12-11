# Анализ эффективности работы разработчиков

Скрипт для чтения файлов с данными о закрытых задачах и формирования отчетов.

Примеры запуска:
<details>
<summary>Запуск из контейнера</summary>
<img src=/execution_screenshots/run_container.png>
</details>

<details>
<summary>Запуск локально</summary>
<img  src=/execution_screenshots/run_locally.png>
</details>

Подробнее установка и запуск описаны в разделе <a href="#установка,-использование-и-примеры-запуска">Установка, использование и примеры запуска</a>.

## Возможности

Скрипт позволяет читать информацию из командной строки, обрабатывать CSV-файлы и формировать и выводить в консоль отчёт <span style="color:green;font-weight: bold;">"performance"</span> - таблицу со средней эффективностью (среднее арифметическое) разработчиков по позициям. 

### Чтение информации из командной строки
Скрипт считывает названия файлов, пути к ним и названия отчетов через командную строку с помощью двух обязательных параметров:
- Названия файлов и пути к ним передаются с помощью параметра `--files`<br>
```console
... --files /path/to/file1.csv /path/to/file2.csv ...
```
- Названия отчетов передается через параметр `--report` <br>
```console
... --report performance
```

### Проверка введённой информации
Скрипт проверяет
- присутствие обязательных параметров ([`_arguments_parser`](data_processing/data_processing.py#L15));
- существование файлов по заданному пути, названия и расширения файлов<br> ([`_arguments_files_checker`](data_processing/data_processing.py#L24));
- названия отчетов ([`_arguments_report_checker`](reports/reports.py#L17)).

### Формирование отчетов
Скрипт формирует реализованные отчёты
- В данный момент реализован один отчет - <span style="color:green;font-weight: bold;">"performance"</span>.

### Добавление отчётов
Скрипт предусматривает быстрое добавление новых отчетов.<br>
Для добавления нового отчета достаточно
- добавить новый метод с логикой нового отчёта и именем идентичным аргументу/названию отчета в класс [`Report`](reports/reports.py#L9) модуля `reports/reports.py`(для отчета с аргументом `skills` метод должен называться идентично - `skills`);
- добавить название нового аргумента/отчета в список [`valid_report_types`](report_generator.ini) для добавления нового отчёта в некоторые тесты (для отчёта с аргументом `skills` в список должен быть добавлен элемент `skills`).

## Структура репозитория

```
.
├── .devcontainer                       # Настройки контейнеров для разработки в VSCode
├── csv_examples                        # Примеры валидных CSV-файлов
│   ├── employees1.csv
│   └── employees2.csv
├── src                                 # Модули
│   ├── data_processing                 # Обработка данных
│   │   ├── data_model.py               # Датакласс - модель данных
│   │   └── data_processing.py          # Модуль обработки данных из консоли и файлов
│   ├── reports                         # Формирование отчётов
│   │   └── reports.py                  # Модуль формирования отчётов
├── tests                               # Тесты
│   ├── conftest.py                     # PyTest - конфигурация тестов и вспомогательные фикстуры
│   ├── tests_data_processing           # PyTest - тесты обработки данных
│   │   |── test_ArgumentProcessor.py   # PyTest - тесты модуля обработки данных
│   │   └── test_CSVLoader.py           # PyTest - тесты модуля загрузки данных
│   └── tests_reports                   # PyTest - тесты формирования отчётов
│       └── test_reports.py             # PyTest - тесты модуля формирования отчётов
├── .python-version                     # Версия Python
├── Dockerfile                          # Инструкции сборки Docker образа
├── main.py                             # ❗Основной исполняемый файл
├── pytest.ini                          # PyTest - настройки
├── README.ru.md                        # Документация
├── requirements.txt                    # Список зависимостей
└── uv.lock                             # Подробный список зависимостей uv
```

## Установка, использование и примеры запуска

Проект можно запустить в контейнере или локально.

### Клонируйте репозиторий
- Перейдите в директорию, в которую вы хотите клонировать репозиторий:
```console
cd <путь к директории>
```
- Клонируйте репозиторий:
```console
git clone https://github.com/mrBrain101/report_generator.git
```

### Docker

<details>
<summary><b>Скриншот запуска в контейнере</b>b</summary>
<img src=/execution_screenshots/run_container.png>
</details>

- При необходимости установите <a href="https://www.docker.com/" target="_blank">Docker</a>
#### Создание Docker-образа:
```console
docker build -t report_generator .
```
- `docker build` - создает образ на основе Dockerfile в текущей директории
- `-t report_generator` - установка имени образа `report_generator`
- `.` - текущая директория

#### Запуск Docker-контейнера в режиме консольного ввода
```console
docker run -it --name report report-generator /bin/bash
```
`docker run` - запуск контейнера<br>
`-it` - запуск в интерактивном режиме<br>
`--name report` - установка имени контейнера `report`<br>
`report-generator` - имя образа<br>
`/bin/bash` - запуск командной строки внутри контейнера<br>

#### Запуск тестов
`pytest` или `pytest --cov` для тестов с покрытием.

#### Запуск контейнера в режиме консольного ввода
- Для запуска скрипта с данными из примеров CSV-файлов используйте команду 
```console
uv run main.py --files csv_examples/employees1.csv csv_examples/employees2.csv --report performance
```
`uv run` - запуск скрипта<br>
`main.py` - имя скрипта<br>
`--files csv_examples/employees1.csv csv_examples/employees2.csv` - параметр файлов<br>
`--report performance` - параметр отчета<br>

- Для выхода из консоли внутри и остановки Docker-контейнера используйте команду `exit`.
- Для запуска уже созданного остановленного Docker-контейнера в режиме консольного ввода используйте команду 
```console
docker start -ai report
```
`docker start` - запуск контейнера<br>
`-ai` - запуск в интерактивном консольном режиме<br>
`report` - имя контейнера<br>

- Другие команды доступны <a href=https://docs.docker.com/reference/cli/docker/ target="_blank">здесь</a>.

### Локально
<details>
<summary><b>Скриншот запуска локально</b>b</summary>
<img src=/execution_screenshots/run_locally.png>
</details>

Все команды выполняются в директории проекта.
#### Установка uv
```console
pip install uv
```
Другие опции установки доступны <a href=https://docs.astral.sh/uv/getting-started/installation/#standalone-installer target="_blank">здесь</a> 

#### Установка локальной среды
```console
uv venv
```
#### Активация локальной среды
Linux / MacOS:
```bash 
source venv/bin/activate`
```
Windows:
```console
.venv/Scripts/activate
```
#### Установка зависимостей
```console
uv sync
```
#### Запуск тестов
```console
pytest
```
#### Запуск тестов с покрытием
```console
pytest -cov
```
#### Запуск скрипта с данными из примеров CSV-файлов
```console
uv run main.py --files csv_examples/employees1.csv csv_examples/employees2.csv --report performance
```
#### Деактивация локальной среды
```console
deactivate
```

## Ограничения

- При изменении структуры CSV-файлов, необходимо внести изменения в модель данных `data_processing/data_model.py`;
- При добавлении новых типов файлов, необходимо добавить класс для нового типа данных с наследованием от `ArgumentProcessor` в модуле `data_processing/data_processing.py` и при необходимости внести изменения в модель данных `data_processing/data_model.py`.
