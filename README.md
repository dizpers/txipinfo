# IP info (docs WIP)

Dockerized Twisted application to get DNS and whois infor by IP address. Please, see task description below (ENglish
and RUssian version).

# Description

## EN

### Intro

Test assessment for candidate to Python-developer position ("It Security Group" company).

### Description

We need to create the async web application using Twisted framework. It will get Reverse DNS (PTR) record and whois data
by IPv4 address.

For getting whois data you can use Linux utility of the same name - `whois`. I.e., just call that command and get output.

All operations must be performed asynchronously, without creation of additional threads, application must not be blocked
by any way.

UI doesn't matter, you haven't use any styles or JS, all the essential is under the hood.

UI of the application will have 2 pages.

**Main page**. It will contains a form with a input field for IPv4 address and button to send this form. User will get
response immediately (saying that data was received successfully and will be processed soon). Processing is performing
at the background.

**History page**. This page will contains a table with a hisotry of retrieved DNS and whois data. Table must have the
following structure:

* IP;
* PTR;
* Whois;
* Date Time.

A button to clean up the history will be located under that table. History is stored only in memore of application. No
files or DB are allowed. After termination of the application - a history is lost.

Bonus points for ability to run with Vagrant or Docker.

### Installation and run

Please, follow these steps:

```
git clone git@github.com:dizpers/txipinfo.git
cd txipinfo/txipinfo
docker-compose up -d
```

After the last command will execute - you'll be able to access the web interface on http://127.0.0.1/.

To run without docker (e.g., during development) you can use following command (**assuming you're at the project root
directory**):

```
env PYTHONPATH=. twistd -n web --class=txipinfo.server.resource
```

### TODO

There's something to do more:

1. handle more errors;
2. implement whois client (instead of using linux command);
3. make clientside interactive (single page application);
4. use more convenient template engine (Jinja? remember about blocking). 

## RU

### Интро

Тестовое задание для кандидата на позицию Python-разработчика (компания "It Security Group").

### Описание

Необходимо написать асинхронное веб приложение при помощи фреймворка Twisted, которое будет получать Reverse DNS (PTR) 
по IPv4 адресу, а также Whois информацию.

Для получения Whois информации можно использовать стандартную одноименную Linux утилиту whois. То есть просто вызывать 
ее из приложения и получить ответ.

Все операции должны проходить асинхронно, без создания дополнительных потоков, приложение не должно блокироваться ни 
коим образом.

На UI внимание обращать не будем, никаких стилей и JS использовать не нужно, вся суть находится под капотом.

Интерфейс приложения состоит из двух страниц.

**Главная страница**. На ней отображается форма с полем для ввода IPv4 адреса и кнопка отправки формы. Пользователю 
мгновенно выводится ответ, сообщающий что данные приняты в обработку. Обработка происходит в фоне.

**Страница с историей**. На ней находится таблица с историей получения Whois & PTR по IP. Таблица имеет следующие
колонки:

* IP;
* PTR;
* Whois;
* Date Time.

Ниже таблицы находится кнопка, при нажатии на которую, происходит очистка истории. История хранится исключительно в
памяти приложения. Никаких файлов и БД использовать нельзя. После завершения процесса приложения история теряется.

Будет плюсом возможность запуска в Vagrant и Docker.

### Установка и запуск

Для запуска продукта используйте следующий набор команд:

```
git clone git@github.com:dizpers/txipinfo.git
cd txipinfo/txipinfo
docker-compose up -d
```

После окончания работы последней команды, вы можете начать использовать web интерфейс по адресу http://127.0.0.1/.

Для запуска вне контейнера (например, в ходе разработки) используйте следующую команду (**находясь в корневой папке
проекта**):

```
env PYTHONPATH=. twistd -n web --class=txipinfo.server.resource
```

### TODO

Список возможных улучшений:

1. обрабатывать больше ошибок;
2. реализовать whois клиент (вместо использования одноименной linux команды);
3. сделать клиентсайд интерактивным (одностраничное приложение);
4. использовать более удобный шаблонизатор (jinja? помнить про блокировки).
