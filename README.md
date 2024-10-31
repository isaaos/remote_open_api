

### 拉取项目构建并运行
```shell
git clone https://github.com/isaaos/remote_open_api.git
cd remote_open_api
# 创建虚拟环境
python3 -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
# 测试
python strat.py
```

```shell
# 停止虚拟环境
deactivate
```

### 强制拉取更新的代码
```shell
# 当前使用的提交代码是什么
git reset --hard
# 先获取远程更新
git fetch origin
# 当前分支重置为远程master分支状态-这是一个不可逆的操作
git reset --hard origin/master
```



### 打包依赖
```shell
# 打包依赖
pip freeze > requirements.txt
```


### Supervisor 守护
````shell
/opt/remote_open_api
/opt/remote_open_api/venv/bin/python3 strat.py
````

