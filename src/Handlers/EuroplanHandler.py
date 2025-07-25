class EuroplanHandler:
    def create_data_for_db(self, text):
        text_s = text.split("\n")
        return text_s

    def get_city_from_text(self, text):
        return text[0][21:]

    def get_title_from_text(self, text):
        return text[1]

    def get_year_from_text(self, text):
        return text[2][12:]

    def get_mileage_from_text(self, text):
        mileage = text[3][6:]
        return self.replace_all(mileage)

    def get_price_from_text(self, text):
        price = text[4][12:]
        return self.replace_all(price)

    def get_url_from_text(self, text):
        return text[6]

    def replace_all(self, text):
        return text.replace("рублей с полным НДС", "").replace(" ", "").replace("\xa0", "").replace("км", "").replace("руб.", "")
