from flask_failsafe import failsafe

@failsafe
def create_app():
    '''为了在拼写错误的情况下，让app重启，需要用failsafe'''
    from quotation import create_app as create_app1
    return create_app1()

if __name__ == '__main__':
    #print('Hello World!')
    #print('哈哈!')
    create_app().run(host='0.0.0.0', port=5000, debug=True)
