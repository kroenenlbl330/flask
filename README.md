** 虚拟环境文件迁移 **

有网络：
在项目目录下新建一个whls文件夹(用来存储我们依赖包)然后在虚拟环境cmd命令下切换到whls目录

执行 pip freeze --all > requirements.txt 命 令 将安装包版本信息导入到requireents.txt文件中(该文件位置在执行cmd命令当前目录下，也就是whls下); 注意--all参数，加上此参数会将setuptools、urllib3包进行打包；如果不加，这两个不会打包。

无网络：
将包下载到whls目录下

whls目录下执行虚拟环境cmd命令pip install --download . -r requirements.txt （注意--download后边的点，代表是下载到当前目录，并且requirements.txt存在于当前目录中，否则会报错）

迁移
新建虚拟环境，并将项目目录放入该虚拟环境中
激活虚拟环境
虚拟环境cmd命令进入复制过来的项目下whls目录
执行命令安装包：
有网络：
pip install -r requirements.txt #安装依赖包

无网络：
pip install --no-index --find-index= . -r requirements.txt
注意命令中的.点 代表是当前目录也就是whls目录；是下载的包和requirements.txt所在目录