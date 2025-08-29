# 二开 CocosCreator 开拓版源码编译与搭建教程（附视频演示）

今天给大家带来 **藏宝库荣耀二开的 CocosCreator 开拓版源码** 的编译与搭建演示视频。  
本套源码之前已经发布过，但当时未包含完整的内核代码，这次补全并附带详细的环境配置与搭建流程，方便开发者快速上手。

---

## 一、环境准备

在开始编译和部署之前，请先准备好以下运行环境：

1. **安装 IIS**

   * 勾选 CGI，确保支持 PHP 运行。
2. **安装 SQL Server 2014 或更高版本**

   * 还原数据库时需要，建议使用标准版或企业版。
3. **安装 Visual Studio**

   * VS2015：用于编译服务端
   * VS2017 及以上：编译管理后台必须使用更高版本，否则因代码新特性会报错
4. **安装 Cocos Dashboard & Creator 2.4.3**

   * 用于客户端构建与打包
5. **安装 .NET 5**

   * 如果系统没有预装，请自行下载并安装。

---

## 二、数据库还原

源码附带 **9个数据库文件**，请依次在 SQL Server 中进行还原。  
示例数据库连接配置：

`server=.;database=RYAccountsDB;uid=sa;pwd=123456`

如果数据库不在本机，可以指定 IP 与端口：

`server=120.111.111.11,1433;database=RYAccountsDB;uid=sa;pwd=123456`

后台数据库配置示例：

`$uid = "sa"; // 数据库用户名  
$pwd = "123456"; // 数据库密码`

⚠️ 如果启用微信登录，还需在后台配置开发者秘钥。

---

## 三、IIS 网站搭建与 PHP 配置

1. 在 `php.ini` 中添加以下扩展：

   `extension=php_pdo_sqlite.dll  
   extension=php_pdo_sqlsrv_56_nts.dll  
   extension=php_sqlsrv_56_nts.dll`

   这三项用于支持 SQL 连接。
2. 为支持热更新，需额外配置 MIME 类型：

   `.jsc application/octet-stream  
   .plist application/octet-stream`
3. 确认网站端口（后续客户端配置会用到）。

---

## 四、后台与服务器配置

1. 修改 SQL 账号与密码：

   `sa / 123456`
2. 编译服务端（VS2015 / VS2017），如有报错，多数为编译顺序问题。
3. 数据库机器标识加密配置：

   `FE49E49699363EB65BD013C5D398708F`

后台默认账号：`admin`  
后台默认密码：`123456`

---

## 五、客户端配置

修改客户端主要配置项：

`` window.LOGIN_SERVER_IP = '192.168.3.12'; // 服务器IP  
window.PHP_PORT = 8089; // PHP网站端口  
window.WEB_PORT = 8081; // 后台端口  
window.APP_VERSION = `1.0.0.0`; // 版本号 ``

同时修改热更新路径：

`127.0.0.1:8090/hot-update`

---

## 六、Android 构建注意事项

如果需要打包 APK，需要安装：

* **Android SDK**
* **NDK**

构建过程中注意 **target API level** 配置。

---

## 七、热更新配置

1. 将构建好的客户端版本复制到 PHP 网站目录下。
2. 确认客户端热更新目录与服务器配置保持一致。

例如：

`http://127.0.0.1:8090/hot-update`

---

## 八、完成效果

至此，源码已成功编译并搭建完成：

* 后台正常运行
* 客户端可登录游戏
* 热更新功能可用

🎥 **完整视频教程下载：** [点击下载]（此处可插入实际链接）

---

## 关键词优化（SEO）

* 藏宝库荣耀二开源码
* CocosCreator开拓版源码
* 棋牌房卡源码搭建
* 创胜二开源码编译教程
* 热更新棋牌游戏源码
* CocosCreator源码下载

![图片[1]-源码狗](https://yuanmago.com/wp-content/uploads/2025/08/photo_2025-08-18_14-25-20.jpg)

配套的源码  https://yuanmago.com/137581.html

原文：https://yuanmago.com/137583.html?utm_source=github&utm_medium=syndication
