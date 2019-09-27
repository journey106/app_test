from configparser import ConfigParser
import config


class HandleConf:
    '''处理配置文件'''
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.config = ConfigParser()
        self.config.read(self.file_name, encoding='utf-8')

    def get_value(self, section, option):
        '''

        :param section: 区域名
        :param option: 选项名
        :return: 返回选项值
        '''
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_bool(self, section, option):
        return self.config.getboolean(section, option)

    def get_eval_value(self, section, option):
        return eval(self.get_value(section, option))

    @staticmethod
    def write_conf(datas, file_name):
        config = ConfigParser()
        for key in datas:
            config[key] = datas[key]
        with open(file_name, 'w') as f:
            config.write(f)


do_config = HandleConf(config.CONF_FILE_PATH)

if __name__ == '__main__':
    do_config = HandleConf(config.CONF_FILE_PATH)
    print(do_config.get_value('log', 'file_level'))
    datas = {
        'file_path': {'file_name': 'cases.xlsx', 'log_path': 'result.txt'},
        'msg': {'success_msg': 'Pass', 'fail_msg': 'Fail'}
    }
    HandleConf.write_conf(datas, config.CONF_USER_FILE_PATH)
