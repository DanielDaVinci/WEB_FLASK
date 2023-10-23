import typing as t

from pymysql import connect
from pymysql.cursors import Cursor
from pymysql.err import OperationalError

class DBContextManager:
    """Контекстный менеджер для работы с БД. """

    def __init__(self, config) -> t.Dict:  # t.Dict
        """
        Инициализация класса конфигов.

        Args:
            config: t.dict[str] - Словарь с параметрами подключения к БД.
        :param config:
        """
        self.config = config
        self.conn = None
        self.cursor = None

    def __enter__(self) -> t.Optional[Cursor]:
        """
        Попытка создать курсор для работы с БД.

        Returns:
        t.Optional[cursor] - Курсор для работы с БД.

        """
        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as err:
            print(err.args)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Завершение работы контекстного менеджера и закрытие соединений

        Args:
            exc_type - Тип ошибки.
            exc_val - Значение ошибки.
            exc_tb - Traceback ошибки.

        Returns:
            bool - Успешное завершение работы.
        """
        if exc_type:
            print(exc_type)
            print(exc_val)
        if self.conn and self.cursor:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()
            self.cursor.close()
        return True