from src.repositories.address_repository import RepositoryAddress


class RepositoryAPI:
    def __init__(self) -> None:
        self.tbl_address = RepositoryAddress()