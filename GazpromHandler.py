class GazpromHandler():

    def delete_space(self, text):
        return text.strip().replace("&nbsp;", "").replace("\xa0", "").replace("\n", " ")

    def create_url(self, href):
        url = f"https://autogpbl.ru{href}" if href and href.startswith("/") else href
        return url