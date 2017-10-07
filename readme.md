#启动方式：
##命令行
    docker run --name quotation_api -itd -p 5000:5000 -v /home/xuqinghan/lazyman35/quotation:/code quotation_dev:latest

    attach
    python3 main.py
##docker-compose
    创建并启动
    docker-compose up
    docker-compose run quotation_api
    重启
    docker-compose start