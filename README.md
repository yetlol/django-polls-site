this is a project about polls.
just record django oprations

1. 添加了 polls 的template 使用 django.template.loader 加载 index.html
2. HttpResponse(template.render()) 加载数据

2.26
学习 generic view 

3.3
TDD 开发驱动
写关于 method index detail 相关的测试
涉及到 assertEqual assertContains asserQuerysetEqual.需要了解更多的 TestCase 的相关函数。
还可以添加多个测试用例
例如：
检查 question 没有 choice 是否发布
检查 question 有 choice 是否发布
Django 可以用 LiveServerTestCase 来和selenium 工具结合测试。
