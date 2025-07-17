from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    async def get_element_by_selector(self, selector): ...

    @abstractmethod
    async def get_all_by_selector(self, selector): ...

    @abstractmethod
    async def get_element_text_by_selector(self, selector): ...

    @abstractmethod
    async def go_to_page(self, url): ...

    @abstractmethod
    async def wait_for_selector(self, selector): ...

    @abstractmethod
    async def get_item_text(self, item, selector): ...

    @abstractmethod
    async def get_href(self, item, selector): ...
