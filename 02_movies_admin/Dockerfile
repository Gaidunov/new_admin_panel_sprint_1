# Ставим питон
FROM python:3.10

# устанавливаем рабочую дерикторию
WORKDIR /home/pro

# PYTHONDONTWRITEBYTECODE: Запрещает Python записывать файлы pyc на диск (эквивалент опции python -B)
# PYTHONUNBUFFERED: Запрещает Python буферизовать stdout и stderr (эквивалент опции python -u)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установить psycopg2
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc netcat && \
    apt-get clean


# Обнов пип. Скопировать файл в раб дерикторю. установить зависимости из requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# ENV HOME=/home/pro
ENV APP_HOME=/home/pro/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

COPY . .
# Точка входа в приложение. Проверяем стартовала ли база и есть ли подключение 
ENTRYPOINT ["/home/pro/web/entrypoint.sh"]