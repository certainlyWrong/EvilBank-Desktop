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
    def factoryLogModel(
        cls,
        accountId: str,
        logType: str,
        logMessage: str,
    ):
        result = None

        result = cls(
            str(uuid4()),
            accountId,
            datetime.now(),
            logType,
            logMessage,
        )

        return result

    @classmethod
    def fromEntity(cls, logEntity: LogEntity) -> 'LogModel':
        return cls(
            logEntity.log_id,  # type: ignore
            logEntity.account_id,  # type: ignore
            logEntity.log_date,  # type: ignore
            logEntity.log_type,  # type: ignore
            logEntity.log_message,  # type: ignore
        )

    def toEntity(self) -> LogEntity:
        return LogEntity(
            log_id=self.__logId,
            account_id=self.__acocuntId,
            log_date=self.__logDate,
            log_type=self.__logType,
            log_message=self.__logMessage,
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
