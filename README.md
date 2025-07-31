# Project_ONE_1
Для работы с проектом необходиомо создать файл .env, и указать там такие переменные как:
POSTGRES_DB,
POSTGRES_USER,
POSTGRES_PASSWORD,
POSTGRES_HOST,
POSTGRES_PORT,
USE_SQLIT.
Самая интересная из них это USE_SQLIT, она нужна для того, чтобы можно было использовать локально на машине SQLite(
для этого нужно просто в .env написать USE_SQLIT=true),
а чтобы в докере поднимать Postgres нужно прописать(USE_SQLIT=false) и собрать dokcer compose

    GET /rooms - получить список комнат
    POST /rooms - указать при этом в теле price и description
    DELETE /rooms/(id) -удаление комнаты, передать id комнаты в url
    GET /booking - список броней указанной комнаты, указать комнату через ?room_id=(номер комнаты)
    POST /booking -создать бронь для комнаты, передать нужно room_id, date_start, date_end
    DELETE /booking/(id)- удалить бронь, в url предать номер брони
