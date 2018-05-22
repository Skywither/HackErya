# HackErya

都不好意思放出来了，仅仅是为了吐槽上午黑科技解决尔雅的验证码（dalao全程助攻那种）到下午就封了的那种心情

## Tricky，太Tricky了
刷完视频就有 30 分和 60%+ 的进度，这东西存在的意义就是为了刷 90% 进度去考试

首先首先，题目对了多少不影响那 30

其次其次，你不选答案直接提交也是可以的！

最后最后，设置个延时就完成了


## 细节，全都是细节
requests 需要获取太多参数，我选择 selenium

有个懂前端的 dalao 很重要，不然卡在 get_elements_by_xxx 都不知道怎么回事

页面都跳转了，那个提交按钮嵌入在 iframe 你敢信?

三层 iframe 跳转！

还要提交两次！

验证码在本地执行 JS 语句就能 ban 掉？

### 切换至第三层 iframe
    driver.switch_to.frame(driver.find_element_by_id("iframe"))
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.switch_to.frame(driver.find_element_by_id("frame_content"))
### 去掉验证码流程
    切换至第三层 iframe
    初次提交：document.getElementsByClassName('Btn_blue_1 marleft10')[0].click()
    出现验证码
    切换至顶层：iframe (driver.switch_to.frame(driver.find_element_by_id("iframe"))
    WAY.box.hide()
    切换至第三层 iframe
    toadd && toadd('', '')
    确认提交：document.getElementsByClassName('bluebtn')[0].click()

然后早上测试通过，下午就封了（#@￥……%￥&%YDFKGH%……T#￥%

其实最后才加的 lxml，至于为什么 selenium 用不了这条正则我没搞懂：`//em[@class='orange']/../../span[@class='articlename']//@href`

## 到时候补图，晚安