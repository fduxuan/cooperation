import mediate.i18n as i18n


class I18N(i18n.I18N):
    please_bind = i18n.Item(zh_CN="请先绑定", en_US="Please bind first")
    please_buy = i18n.Item(zh_CN="请先购买相关功能", en_US="Please buy cornerstone first")
    please_buy_course_again = i18n.Item(
        zh_CN="课程不完整，请联系管理员重新购买课程",
        en_US="Broken course! Please contact the admin to buy the complete course"
    )
    buy_paid_course = i18n.Item(zh_CN="请联系我们购买收费课程", en_US="Please contact us to buy paid courses")
    not_owner = i18n.Item(zh_CN="您不是所有者", en_US="You are not the owner")
    cannot_read = i18n.Item(zh_CN="您无权读取", en_US="You do not as the privilege to read")
    cannot_write = i18n.Item(zh_CN="您无权创建/修改/删除", en_US="You do not as the privilege to create/modify/delete")
    not_started_session = i18n.Item(zh_CN="未开始课程", en_US="The session is not started")
    finished_session = i18n.Item(zh_CN="课程已结束", en_US="The session is finished")
    please_enable_websocket = i18n.Item(zh_CN="请使用websocket", en_US="Please enable websocket")
    exceeded_chapter = i18n.Item(zh_CN="请不要提前进入章节", en_US="Do not enter the chapter in advance")
    no_exam = i18n.Item(zh_CN="请参加一个测试", en_US="Please take a exam")
    existent_exam = i18n.Item(zh_CN="Please finish your exam", en_US="Please finish your exam")
    inadequate_score = i18n.Item(zh_CN="分数不够，请重新测试", en_US="Inadequate score! Please retake the exam")
    exam_timeout = i18n.Item(zh_CN="考试超时，请重新测试", en_US="exam timeout!")
    strange_answers = i18n.Item(zh_CN="请按照格式提交答案", en_US="strange answers")
    # roadmap
    roadmap_aready_use = i18n.Item(zh_CN="对应数据已存在", en_US="roadmap already in your company!")
    post_empty_json = i18n.Item(zh_CN="提交表单为空！", en_US="The form is empty!")
    exceeded_node_length = i18n.Item(zh_CN="节点索引超出节点长度！", en_US="The index exceeded the length of node!")
    duplicated_course = i18n.Item(zh_CN="课程不可重复添加！", en_US="This course is already in your repository!")