from configparser import ConfigParser # to read .ini file

class Config:
    def __init__(self, config_file=r"C:\Users\LENOVO\OneDrive\Desktop\Mayur_Projects\AgenticAI\AGENTS\src\langgraphagenticai\ui\uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get('LLM_OPTIONS').split(',')
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get('USECASE_OPTIONS').split(',')
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get('GROQ_MODEL_OPTIONS').split(',')

    def get_page_title(self):
        return self.config["DEFAULT"].get('PAGE_TITLE', 'Agentic AI')
    
    def get_setting(self, section, option, fallback=None):
        return self.config.get(section, option, fallback=fallback)

    def get_int_setting(self, section, option, fallback=0):
        return self.config.getint(section, option, fallback=fallback)

    def get_boolean_setting(self, section, option, fallback=False):
        return self.config.getboolean(section, option, fallback=fallback)