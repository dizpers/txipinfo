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

• IP;
• PTR;
• Whois;
• Date Time.

Ниже таблицы находится кнопка, при нажатии на которую, происходит очистка истории. История хранится исключительно в
памяти приложения. Никаких файлов и БД использовать нельзя. После завершения процесса приложения история теряется.

Будет плюсом возможность запуска в Vagrant и Docker.