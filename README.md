<h1 align="center">Телеграм бот-парсер <a href="https://www.ozon.ru/" target="_blank">Ozon</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Этот бот очень прост, дайте ему ссылку на товар и он выдаст вам цену на него.</h3>


# Для запуска бота вам нужно выполнить следующие шаги:

### 1. Создать бота с помощью https://t.me/BotFather , и взять Ваш Токен у него для дальнейшего взаимодействия с нашим ботом.


### 2. В терминале прописать след. команду
```commandline
git clone https://github.com/Dastan-Oskonbaev/Ozon-parser.git
```
### 3. Перейти в директорию
```commandline
cd Ozon-parser/
```
### 4. Создать виртуальное окружение
```commandline
python3 -m venv venv
```
### 5. Затем активировать
```commandline
source venv/bin/activate
```
### 6. Скачать все зависимости
```commandline
pip install -r requirements.txt
```
### 7. Создать файл .env в текущей дериктории
```commandline
touch .env
```
### 8. Записать в этот файл наш Токен который взяли у @BotFather
```commandline
BOT_TOKEN=<Ваш Токен>
```
### 9. И конечная, запускаем наш бот
```commandline
python3 main.py
```
