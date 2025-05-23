# Скрипт подсчёта зарплаты сотрудников

Скрипт, который читает данные сотрудников из файлов в формате csv и формирует простой отчет по заработной плате.

---

## Описание

В скрипт можно передать несколько файлов и тип отчета который нужно сформировать, в данном случае отчёт по зарплатам payout. Файлы на вход всегда в формате csv, валидные и без ошибок. Название отчета передается через  параметр --report.

---

## Пример файла csv с данными сотрудников:

```
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60
```
Название колонки hourly_rate может быть разными в разных файлах, а именно hourly_rate, rate, salary.

## Пример запуска скрипта:

```
python main.py data1.csv data2.csv data3.csv --report payout
```

## Запуск тестов

```bash
pytest
```