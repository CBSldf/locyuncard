# locyk
loc云卡，基于py，目前没弃坑，版本0.6,用来代替shequ开源，可实现类似图床（但是显示的图片像卡片一样）的效果，本项目基于教学课件进行二次翻版，但是大部分都被我翻了，只有图片排版没翻，如有侵权联系我，立马删（）

# 部署方法
建议python3.8.5，存储以及用户名都采用txt存储，而且未经加密，如真的要部署可以自行进行rsa非对称加密传输数据，sha3加密等，并且设置禁止访问里面的users.txt，否则用户名泄露别怪我，并且最好https

# 使用方法
如果部署成功，可以访问【域名：8000】就是主页，当然如果你想可视化删除图片的话可以访问【域名：8000/admin】,当然密码在index.py的rm路由那里，请自行改密码

# 干货提示
file.zip里的一个ppt里有重要信息，一定要看，不然部署完嗝屁了别找我

# 关于未来可能的更新
由于我第一次用py做后端，所以发现了一些缺点，日后会加以更新，如果有可能的话就是取消flask返回html，直接让服务器返回，并且https
