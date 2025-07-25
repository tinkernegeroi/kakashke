class CarcadeHandler:
    def replace_all(self, text):
        return text.replace(" ", "").replace("\xa0", "").replace("км", "")