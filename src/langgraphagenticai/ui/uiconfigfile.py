from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def _split_options(self, key):
        return [i.strip() for i in self.config['DEFAULT'].get(key).split(',')]

    def get_llm_options(self):
        return self._split_options('LLM_OPTIONS')

    def get_usecase_options(self):
        return self._split_options('USECASE_OPTIONS')

    def get_groq_model_options(self):
        return self._split_options('GROQ_MODEL_OPTIONS')

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')
