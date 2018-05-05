class Word:
    word = ''
    definitions = []
    type = ''

    def __init__(self, word, description, type):
        self.definitions = description
        self.type = type
        self.word = 'to ' + word if self.type.lower() == 'verb' else word

    def append_definition(self, definitions_to_append: []):
        for definition in definitions_to_append:
            self.definitions.append(definition)

    def prepare_for_quizlet(self):
        definitions = ''
        for definition in self.definitions:
            definitions += definition + '; '
        return self.word + '\t' + definitions