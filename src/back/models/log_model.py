
from uuid import uuid4
from datetime import datetime

from ..entities.log_entity import LogEntity


class LogModel:

    __slots__ = [
        '__logId',
        '__acocuntId',
        '__logDate',
        '__logType',
        '__logMessage',
    ]

    def __init__(
        self,
        logId: str,
        acocuntId: str,
        logDate: datetime,
        logType: str,
        logMessage: str,
    ):
        self.__logId = logId
        self.__acocuntId = acocuntId
        self.__logDate = logDate
        self.__logType = logType
        self.__logMessage = logMessage

    @classmethod
    def create(
        cls,
        acocuntId: str,
        logType: str,
        logMessage: str,
    ):
        result = None

        if not logType.isalpha():
            if not logMessage.isalpha():
                result = cls(
                    str(uuid4()),
                    acocuntId,
                    datetime.now(),
                    logType,
                    logMessage,
                )

        return result

    @classmethod
    def fromEntity(cls, logEntity: LogEntity) -> 'LogModel':
        return cls(
            logEntity.logId,
            logEntity.acocuntId,
            logEntity.logDate,
            logEntity.logType,
            logEntity.logMessage,
        )

    def toEntity(self) -> LogEntity:
        return LogEntity(
            self.__logId,
            self.__acocuntId,
            self.__logDate,
            self.__logType,
            self.__logMessage,
        )

    @property
    def logId(self) -> str:
        return self.__logId

    @property
    def acocuntId(self) -> str:
        return self.__acocuntId

    @property
    def logDate(self) -> datetime:
        return self.__logDate

    @property
    def logType(self) -> str:
        return self.__logType

    @property
    def logMessage(self) -> str:
        return self.__logMessage
