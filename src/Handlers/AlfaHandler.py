class AlfaHandler:
    def create_data_for_db(self, text):
        text_s = text.split("\n")
        return text_s

    def get_price_from_text(self, text):
        price_t = text[8][15:]
        return self.replace_all(price_t)


    def get_type(self, text):
        return text[3]

    def get_city_from_text(self, text):
        city = text[0][4:].strip()
        return city

    def get_title_from_text(self, text):
        title = text[4]
        return title

    def get_year_from_text(self, text):
        year = text[5][12:].strip()
        return year

    def get_mileage_from_text(self, text):
        mileage = text[6][7:].strip()
        mileage = self.replace_all(mileage)
        return mileage

    def replace_all(self, text):
        return text.replace("рублей с НДС", "").replace(" ", "").replace("\xa0", "").replace("км", "")