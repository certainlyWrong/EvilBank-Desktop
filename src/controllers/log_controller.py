import json
import sqlite3
from rich import print

from ..models.log_model import LogModel


class LogController:
    __slots__ = [
        "__connection",
        "__cursor",
        "__querys",
    ]

    def __init__(self, pathToCreateDB: str) -> None:
        self.__connection = sqlite3.connect(pathToCreateDB)
        self.__cursor = self.__connection.cursor()
        self.__querys: dict[str, str] = self.__loadQuerys()
        self.__createLogTable()

    def __loadQuerys(self) -> dict[str, str]:
        result: dict[str, str] = {}

        with open("resources/querys/log_querys.json", "r") as file:
            result = json.load(file)

        return result

    def __createLogTable(self) -> None:
        self.__cursor.execute(self.__querys["createLogTable"])
        self.__connection.commit()

    def addLog(self, log: LogModel) -> None:
        self.__cursor.execute(
            self.__querys["addLog"],
            log.toTuple(),
        )
        self.__connection.commit()

    def getLogByUserId(self, userId: str) -> list[LogModel]:
        self.__cursor.execute(self.__querys["getLogByUserId"], (userId,))
        result = self.__cursor.fetchall()
        return [LogModel(*log) for log in result]

    def getLogByDate(self, date: str) -> list[LogModel]:
        self.__cursor.execute(self.__querys["getLogByDate"], (date,))
        result = self.__cursor.fetchall()
        return [LogModel(*log) for log in result]

    def getLogByType(self, type: str) -> list[LogModel]:
        self.__cursor.execute(self.__querys["getLogByType"], (type,))
        result = self.__cursor.fetchall()
        return [LogModel(*log) for log in result]

    def viewLog(self, log: LogModel) -> None:
        print(log.toJson())

    def viewLogs(self, logs: list[LogModel]) -> None:
        for log in logs:
            self.viewLog(log)

    def viewLogByUserId(self, userId: str) -> None:
        self.viewLogs(self.getLogByUserId(userId))

    def viewLogByDate(self, date: str) -> None:
        self.viewLogs(self.getLogByDate(date))

    def viewLogByType(self, type: str) -> None:
        self.viewLogs(self.getLogByType(type))

    def viewAllLogs(self) -> None:
        self.__cursor.execute(self.__querys["viewAllLogs"])
        result = self.__cursor.fetchall()
        self.viewLogs([LogModel.fromTuple(log) for log in result])
