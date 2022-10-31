import json
from Enumeration import SaveData


class Save():
    def __init__(self):
        self.file_name = "score.json"
        self.data = {'high score': 0, 'score': 0}
        self.restore_data()
    def update_scores(self,score:tuple):
        self.data['score'] =score[0]
        self.data['high score'] =score[1]
    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file)

    def get_data(self, data: SaveData):
        if data == SaveData.SCORE:
            return self.data['score']
        elif data == SaveData.HIGH_SCORE:
            return self.data['high score']

    def restore_data(self):
        try:

            with open(self.file_name) as file:
                self.data = json.load(file)
        except Exception as e:
            print(e)
