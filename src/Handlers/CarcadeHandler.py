class CarcadeHandler:
    def create_data_for_db(self, text):
        text_s = text.split("\n")
        return text_s

    def replace_all(self, text):
        return text.replace(" ", "").replace("\xa0", "").replace("км", "").replace("руб.", "")

    def get_title_from_text(self, text):
        title = text[0][9:]
        return title

    def get_price_from_text(self, text):
        price = text[2][4:]
        return self.replace_all(price)