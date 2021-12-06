#%% 07-09arbitraryargs.py	여러 친구에게 인사하는 함수 구현
def hello(*names):
    """가변 인자 name 활용"""
    for each in names:
        print('안녕, {}!'.format(each))

hello('나타샤')
hello('수빈', '현수', '지효')
hello(*['방탄소년단', '여자친구'])
