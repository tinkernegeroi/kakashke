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

    @abstractmethod
    async def get_item_text_without_selector(self, item): ...

    @abstractmethod
    async def scroll_up(self): ...

    @abstractmethod
    async def get_items_from_tg(self, target_url): ...
