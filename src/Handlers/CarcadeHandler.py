class CarcadeHandler:
    def create_data_for_db(self, text):
        text_s = text.split("\n")
        return text_s

    def replace_all(self, text):
        return text.replace(" ", "").replace("\xa0", "").replace("км", "").replace("руб.", "")

    def get_title_from_text(self, text):
        title = text[0][10:]
        return title

    def get_price_from_text(self, text):
        price = text[2][5:]
        return self.replace_all(price)

    def get_hashtags_from_text(self, text):
        return text[-1]

    def get_year_from_text(self, text):
        return text[3][13:]

    def get_city_from_text(self, text):
        return text[4][16:]

    def get_mileage_from_text(self, text):
        mileage = text[5][7:]
        mileage = self.replace_all(mileage)
        return mileage