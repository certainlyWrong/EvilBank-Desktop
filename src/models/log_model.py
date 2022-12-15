from uuid import uuid4

from datetime import datetime


class LogModel:

    __slots__ = [
        "__userId",
        "__logType",
        "__value",
        "__date",
        "__logId",
    ]

    def __init__(
        self,
        userId: str,
        logType: str,
        value: str,
        date: str,
        logId: str,
    ):
        self.__userId = userId
        self.__logType = logType
        self.__value = value
        self.__date = date
        self.__logId = logId

    @classmethod
    def create(
        cls,
        userId: str,
        logType: str,
        value: str,
    ) -> "LogModel":
        return LogModel(
            userId,
            logType,
            value,
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            str(uuid4()),
        )

    @classmethod
    def fromJson(cls, log: dict) -> "LogModel":
        return LogModel(
            log["userId"],
            log["logType"],
            log["value"],
            log["date"],
            log["logId"],
        )

    @classmethod
    def fromTuple(cls, log: tuple) -> "LogModel":
        return LogModel(
            logId=log[0],
            userId=log[1],
            date=log[2],
            logType=log[3],
            value=log[4]
        )

    def toTuple(self):
        return (
            self.__logId,
            self.__userId,
            self.__date,
            self.__logType,
            self.__value,
        )

    def toJson(self):
        return {
            "logId": self.__logId,
            "userId": self.__userId,
            "date": self.__date,
            "logType": self.__logType,
            "value": self.__value,
        }
