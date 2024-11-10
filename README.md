<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Описание программы LogAnalyzer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Описание программы LogAnalyzer</h1>
    <p>Программа <strong>LogAnalyzer</strong> предназначена для анализа логов и извлечения данных из файлов, упакованных в архивы формата RAR. Она позволяет пользователям эффективно обрабатывать и анализировать информацию, содержащуюся в логах, а также экспортировать результаты в формате SQL.</p>

    <h2>Как использовать программу</h2>
    <p>Для корректной работы программы необходимо разместить файл <code>task4.rar</code> в указанной директории. Программа автоматически извлечет данные из этого архива и начнет процесс анализа.</p>

    <h2>Расположение файла task4.rar</h2>
    <p>Файл <code>task4.rar</code> должен находиться в корневом каталоге проекта, где находится исполняемый файл программы. Например:</p>
    <pre>
    /путь/к/вашему/проекту/
    ├── LogAnalyzer.py
    ├── requirements.txt
    └── task4.rar
    </pre>

    <h2>Структура файла task4.rar</h2>
    <p>Архив <code>task4.rar</code> должен содержать следующие файлы и папки:</p>
    <pre>
    task4.rar
    ├── logs/
    │   ├── log1.txt
    │   ├── log2.txt
    │   └── log3.txt
    ├── config/
    │   └── settings.json
    └── README.md
    </pre>
    <ul>
        <li><strong>logs/</strong> - папка, содержащая файлы логов, которые будут проанализированы.</li>
        <li><strong>config/</strong> - папка с конфигурационными файлами, например, <code>settings.json</code>, где могут храниться настройки анализа.</li>
        <li><strong>README.md</strong> - файл с описанием проекта и инструкциями по его использованию.</li>
    </ul>

    <h2>Заключение</h2>
    <p>Следуя данным инструкциям, вы сможете успешно использовать программу LogAnalyzer для анализа логов и извлечения необходимой информации. Убедитесь, что структура архива <code>task4.rar</code> соответствует указанной, чтобы избежать ошибок в процессе работы программы.</p>
</body>
</html>
