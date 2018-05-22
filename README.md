# HackErya

## 食用方式
adblock.crx

chromedriver.exe

填写 `username`、`password`、`fid`、`chromedriver_path`

    pip install -r requirements.txt
    python main.py

## 坑

Q: 为什么不做成 Headless Mode，这样就可以后台播放了

A: [headless mode doesn't support extensions][headless mode doesn't support extensions]

Q: 为什么要 Adblock 插件啊？

A: `*.chaoxing.com/richvideo/initdatawithviewer*` 这条规则能屏蔽视频播放到一半弹出来的答题请求

Q: 为什么他（卡住了）（停止了）（不能跳转）不会自动播放啊

A:

    1. 确保环境配置正常
    2. 确保系统屏幕缩放为 100%
    3. 查看获取到的控件坐标是否与实际横坐标相符，纵坐标因为 `screenshot` 函数只截取网页内容的缘故，与实际坐标有一段差值

Q: 中间那一长段 `move_to_element_with_offset` 是什么鬼啊

A:

    move_by_offset(xoffset, yoffset)
        Moving the mouse to an offset from current mouse position.
        Args :
            xoffset: X offset to move to, as a positive or negative integer.
            yoffset: Y offset to move to, as a positive or negative integer.

    move_to_element_with_offset(to_element, xoffset, yoffset)
        Move the mouse by an offset of the specified element.
        Offsets are relative to the top-left corner of the element.
        Args :
            to_element: The WebElement to move to.
            xoffset: X offset to move to.
            yoffset: Y offset to move to.

为了屏蔽掉所有 **pyautogui** 的强制鼠标移动操作，先获取 top 层的 `toolOpenBtn` 坐标，再根据图片识别 Flash 控件坐标来做相应计算移动差值。**`move_by_offset` 并不能使用**

## Next Version？
更新是不能更新的了，一辈子都不可能更新的了。
JavaScript 又不会，也就只有复制粘贴别人的代码才能维持了生活的样子。
群里个个是 dalao，说话又好听，写代码 debug 起来一个比一个优雅。
我敲喜欢这里的~


[headless mode doesn't support extensions]: https://docs.google.com/document/d/1OeUik1MZb1qSQ_Dnf1kIYcyCgLYRZHg1GlZo06bsKx4/edit#