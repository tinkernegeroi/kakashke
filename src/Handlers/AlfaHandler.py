class AlfaHandler:
    def create_data_for_db(self, text):
        text_s = text.split("\n")
        return text_s

    def get_type(self, text):
        text_s = self.create_data_for_db(text)
        return text_s[3]

    def get_city_from_text(self, text):
        text_s = self.create_data_for_db(text)
        city = text_s[0][4:].strip()
        return city

    def get_title_from_text(self, text):
        text_s = self.create_data_for_db(text)
        title = text_s[4]
        return title

    def get_year_from_text(self, text):
        text_s = self.create_data_for_db(text)
        year = text_s[5][12:].strip()
        return year

    def get_mileage_from_text(self, text):
        text_s = self.create_data_for_db(text)
        mileage = text_s[6][7:].strip()
        mileage = self.replace_all(mileage)
        return mileage

    def replace_all(self, text):
        return text.replace(" ", "").replace("\xa0", "").replace("км", "")