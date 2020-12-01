from mycroft import MycroftSkill, intent_file_handler


class PiholeAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.pihole.intent')
    def handle_assistant_pihole(self, message):
        number = ''

        self.speak_dialog('assistant.pihole', data={
            'number': number
        })


def create_skill():
    return PiholeAssistant()

