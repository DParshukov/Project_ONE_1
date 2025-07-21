# Project_ONE_1
Для работы с проектом необходиомо создать файл .env, такие как:
POSTGRES_DB,
POSTGRES_USER,
POSTGRES_PASSWORD,
POSTGRES_HOST,
POSTGRES_PORT,
USE_SQLIT.
Самая интересная из них это USE_SQLIT, она нужна для того, чтобы можно бфло использовать локально на машине SQLite(
для этого нужно просто в .env написать USE_SQLIT=true)
, чтобы в докере поднимать Postgres нужно прописать false) и собрать dokcer compose

    path('rooms/list/', RoomListView.as_view(), name="rooms_list" ), - просмотр спика комнат
    path('room/create/',RoomCreateView.as_view(),name="room_create"), -создание комната, такжк нужно передать description и price
    path('room/delete/<int:room_id>/',RoomDeleteView.as_view(),name="room_delete"),-удаление комнаты, передать id комнаты в url
    path('booking/list/', BookingListView.as_view(), name="booking_list"),-список броней указанной комнаты, указать комнату через ?room_id=(номер комнаты)
    path('booking/create/', BookingCreateView.as_view(), name="booking_create"),-создать бронь для комнаты, передать нужно room_id, date_start, date_end
    path('booking/delete/<int:booking_id>/', BookingDeleteView.as_view(), name="booking_delete")- удалить бронь, в url предать номер брони
