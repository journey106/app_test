import pytest
from datetime import datetime

if __name__ == '__main__':
    pytest.main(['-m login'])
    # ts = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    # pytest.main([
    #     "-s",
    #     "--resultlog=report/{}.txt".format(ts),
    #     "--junitxml=report/{}.xml".format(ts),
    #     "--html=report/{}.html".format(ts),
    #     "--alluredir=allurdir/"
    # ])

