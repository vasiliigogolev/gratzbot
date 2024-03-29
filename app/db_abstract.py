from abc import ABC, abstractmethod

from app.user import GUser


class AbstractDatabase(ABC):
    @abstractmethod
    def get_user(self, user_id: str, user_name: str) -> GUser:
        pass

    @abstractmethod
    def update_user(self, user: GUser) -> None:
        pass

    @abstractmethod
    def create_user(self, user_id: str, name: str) -> dict[str, any]:
        pass

    @abstractmethod
    def get_all_users(self) -> dict[str, dict[str, any]]:
        pass

    @abstractmethod
    def get_saved_lgbt_person(self) -> dict:
        pass

    @abstractmethod
    def set_lgbt_person(self, user_id: str, name: str, epoch_days: int) -> None:
        pass
