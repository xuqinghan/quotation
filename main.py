from quotation import create_app

app = create_app()

if __name__ == '__main__':
    #print('Hello World!')
    #print('哈哈!')
    app.run(host='0.0.0.0', port=5000,debug=True)
    
