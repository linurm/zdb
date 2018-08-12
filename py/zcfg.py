import ConfigParser

class zcfgFile():
    def __init__(self, file):
        self.file = file
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.file)

    def getSectionOptionValue(self, section, option, def_value):
        try:
            return self.config.get(section, option)
        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            self.config.set(section, option, def_value)
        except ConfigParser.NoOptionError:
            self.config.set(section, option, def_value)
        with open(self.file, 'wb') as configfile:
            self.config.write(configfile)
        return def_value

    def setSectionOptionValue(self, section, option, value):
        try:
            self.config.set(section, option, value)
        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            self.config.set(section, option, value)
        except ConfigParser.NoOptionError:
            self.config.set(section, option, value)
        with open(self.file, 'wb') as configfile:
            self.config.write(configfile)
