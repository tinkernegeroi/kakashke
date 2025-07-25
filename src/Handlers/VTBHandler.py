class VTBHandler():

    def delete_space(self, text):
        return text.strip().replace("\xa0", "")

    def create_car_url(self, href):
        url = f"https://www.vtb-leasing.ru{href}" if href and href.startswith("/") else href
        return url
