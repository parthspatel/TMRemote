from xml.etree import ElementTree as ET
import configparser
import re
import os


class ProfileManager():
    def getConfig(self, profilePath):
        if os.path.isfile(profilePath):
            assert profilePath.endswith('.xml'), 'Profile is not an xml: {}'.format(profilePath)
            return self.__getConfig(profilePath)
        else:
            raise IOException('File does not exist: {}'.format(profilePath))

    def setConfig(self, profilePath, type, setting, value):
        if os.path.isfile(profilePath):
            assert profilePath.endswith('.xml'), 'Profile is not an xml: {}'.format(profilePath)
            return self.__writeConfig(profilePath,
                                      config=self.__setConfig(profilePath, type, setting, value))
        else:
            raise IOException('File does not exist: {}'.format(profilePath))

    def enableScript(self, profilePath, script_path):
        if os.path.isfile(profilePath) and os.path.isfile(script_path):
            assert profilePath.endswith('.xml'), 'Profile is not an xml file: {}'.format(profilePath)
            assert script_path.endswith('.py'), 'Profile is not an py file: {}'.format(script_path)

            script_path = script_path.replace('\\', '/')
            try:
                enabled_profile = self.__check_profile(profile_path=profilePath,
                                                       script_path=script_path)
                if type(enabled_profile) is bool:
                    if enabled_profile == 'enabled':
                        return 'enabled'
                    return True
                else:
                    return self.__replace_profile(path=profilePath,
                                                  data=enabled_profile)
            except:
                return False
        else:
            if not profilePath:
                raise IOException('File does not exist: {}'.format(profilePath))
            if not script_path:
                raise IOException('File does not exist: {}'.format(script_path))

    def __getConfig(self, path):
        config = configparser.ConfigParser()
        root = ET.parse(path)
        docroot = root.getroot()
        xmlFile = docroot.find('settings')
        SettingDict = {'checkbox': 'state', 'action': 'state', 'pushbutton': 'state',
                       'radiobutton': 'state', 'combobox': 'index', 'spinbox': 'val', 'slider': 'val'}
        DoNotINI = ['loginid', 'loginpw', 'loginspw']
        for section in xmlFile:
            sectionHeader = str(section.tag)
            try:
                config.add_section(sectionHeader)
            except:
                pass
            for element in section:
                if sectionHeader == 'lineedit':
                    if not section.find('name').text.lower() in DoNotINI:
                        value = section.find('text').text
                else:
                    elementHeader = str(element.tag)
                    value = section.find(SettingDict[sectionHeader]).text
                config.set(str(sectionHeader), str(element.text), str(value))
        return config

    def __writeConfig(self, profile_path, config):
        if os.path.isfile(profile_path):
            assert profile_path.endswith('.xml'), 'Profile is not an xml file: {}'.format(profile_path)

            try:
                if type(config) is bool:
                    if not config:
                        return False
                else:
                    return self.__replace_profile(path=profile_path,
                                                  data=config)
            except:
                return False
        else:
            if not profile_path:
                raise IOException('File does not exist: {}'.format(profile_path))
            if not script_path:
                raise IOException('File does not exist: {}'.format(script_path))

    def __setConfig(self, path, type, setting, value):
        try:
            with open(path) as xml:
                xml_file = xml.read()
        except:
            IOError('Cannot read file: {}'.format(path))

        regex_lookup = '.*<{0}>.*\n.*<name>{1}</name>.*\n.*<.*>.*</.*>.*\n.*</{0}>'.format(type, setting)
        p = re.compile(regex_lookup)
        s = p.search(xml_file)
        try:
            if 'action' in type.lower() or 'checkbox' in type.lower() or 'pushbutton' in type.lower() or 'radiobutton' in type.lower():
                sub_val = 'state'
            elif 'combobox' in type.lower():
                sub_val = 'index'
            elif 'lineedit' in type.lower():
                sub_val = 'text'
            elif 'spinbox' in type.lower() or 'slider' in type.lower():
                sub_val = 'val'
            else:
                raise ValueError('> Not valid type in ProfileManager.setConfig()')

            lookup_val = '.*<{0}>.*</{0}>.*\n'.format(sub_val)
            replace_val = '            <{0}>{1}</{0}>\n'.format(sub_val, value)
            q = re.compile(lookup_val)
            s2 = q.sub(replace_val, s.group())
            xml_fixed = p.sub(s2, xml_file)

            return xml_fixed
        except:
            return False

    def __replace_profile(self, path, data):
        try:
            with open(path, 'w') as file:
                file.write(data)
            return True
        except:
            IOError('Cannot write to file: {}'.format(path))
            return False

    def __check_profile(self, profile_path, script_path):
        '''
        This serves two purposes, to check if the script exists and to see if it is regex_disabled
        If the script does not exist it will throw an exception and will add the script
        If the script exists and is disabled then it will enable the script
        If the script exists and is enabled then it will return True
        '''
        script_path_formatted = r'<path>{}</path>'.format(script_path)
        try:
            with open(profile_path, 'r') as xml:
                xml_file = xml.read()
        except:
            IOError('Cannot read file: {}'.format(profile_path))

        regex_disabled = '.*<auto>0</auto>.*\n.*<name>.*</name>.*\n.*(' + script_path_formatted + ')\n'
        regex_enabled = '.*<auto>1</auto>.*\n.*<name>.*</name>.*\n.*(' + script_path_formatted + ')\n'
        try:
            p = re.compile(regex_disabled)
            s = p.search(xml_file)
            if s:
                q = re.compile('.*<auto>0</auto>.*\n')
                s2 = q.sub('            <auto>1</auto>\n', s.group())
                xml_fixed = p.sub(s2, xml_file)
                return 'enabled'
            else:
                p = re.compile(regex_enabled)
                s = p.search(xml_file)
                if s:
                    return True
                else:
                    xml_fixed = re.sub(r'(.*<scripts>.*\n)(.*<item>)',
                                       r'\1        <item>\n            <auto>1</auto>\n            <name></name>\n            <path>{}</path>\n        </item>\n\2'.format(
                                           script_path),
                                       xml_file)
                    return xml_fixed
        except:
            xml_fixed = re.sub(r'(.*<scripts>.*\n)(.*<item>)',
                               r'\1        <item>\n            <auto>1</auto>\n            <name></name>\n            <path>{}</path>\n        </item>\n\2'.format(
                                   script_path),
                               xml_file)
            return True
