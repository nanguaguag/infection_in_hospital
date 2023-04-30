# 人物立绘指导：（正文按以下编号）
# ① 主角杜鸿：男大学生模样，看着像个聪明人的样子就行
#   1.便装：笑、呆滞、疑惑、悲伤（可以闭眼？）、惊吓（呆滞+眉毛抬高即可）
#   2.白大褂装、严肃（面无表情）、愤怒、笑、疑惑、呆滞、惊吓
# ② 药师潘叶：女医生模样，25岁左右，比较活泼的样子
#   1.白大褂装：笑、疑惑、闭眼（难过）、吃惊、严肃
# ③ 室友方岷：个高，30岁左右
#   1.白大褂装：疑惑、吃惊
# ④ 院长岳为：男医生模样，45岁左右，戴眼镜，看着像个地位高的人就行
#   1.白大褂装：严肃、吃惊、闭眼（有点无奈的意思）、笑
# ⑤ 姐姐尹青：低麻花辫，格子条纹的衣服，看着很温柔的样子就行
#   1.格子衣服装：站立，不抱小孩，透明度略高（不太清楚的样子，表现出是回忆）只有笑一个表情
#   2.格子衣服装：站立，抱小孩：笑、疑惑
#   3. 立绘2（即抱小孩）的黑影
# ⑥ 大叔：黑影即可，便装，无表情变化
# ⑦ 阿姨：黑影即可，便装，无表情变化
# ⑧ 药师（抵触男主那个）：不需要立绘

# TODO: 语句结束的 >>>
#       屏幕颤动特效
#       眨眼特效
#       正在说话的人物高亮
#       模糊视野特效

define me = Character("我", color="#707de2", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 就是主角杜鸿
define panye = Character("潘叶", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 药师潘叶
define fangmin = Character("方岷", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 室友方岷
define yuewei = Character("岳为", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 院长岳为
define yinqing = Character("尹青", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 姐姐尹青
define uncle = Character("大叔", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 大叔
define aunt = Character("阿姨", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 阿姨
define pharmaceutist = Character("药师", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 药师（抵触男主那个）
image bg grey = Solid("#2a2a2a") # 背景1：全黑


label splashscreen:
    scene black
    # 这里需要一个大的logo图片作为开场
    show house with dissolve
    with Pause(2)
    scene black with dissolve
    return

init -2:
    image ctc_blink:
        "gui/arrow2.png"
        yanchor -0.5
        xanchor -0.5
        zoom 0.5
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat 

# 第一幕（bgm1：轻快）
label start:
    jump scene2
    # 背景1：全黑
    scene bg grey
    "两小时前的我根本不会想到接下来会发生什么。"
    "那时，我还在跟老家栗镇的长辈们喝着酒谈天说地。"
    "我从小学毕业后离开栗镇就再没回来过，此次归乡是因为要帮外公外婆处理一些手续。"
    "令我意外的是，我一从大巴上下来，就有一排叔叔阿姨来迎接我，那些面孔上都挂着熟悉的、亲切的微笑。"

    # 背景2：餐厅白天
    # （主角：立绘1：笑）
    show duhong smile at center
    with dissolve
    "他们都是看着我长大的，对我来说和亲人无异。"
    "我本打算任务完成后即刻离开，谁料长辈们硬要拉着我叙旧，我盛情难却，只得把返程时间延后到了明早。"

    # （◎立绘：大叔）#居左#
    show uncle at left
    with dissolve
    uncle "小杜啊，没想到这一别竟是十年啊！你跟你爸妈走的时候还只是个小学生呢！"

    # （◎立绘：大叔）#居左#
    show uncle at left
    # （◎立绘：阿姨）#居右#
    show aunt at right
    with dissolve
    aunt "是啊，一回来都大四了，学的是医学？"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    me "是的，正在准备年底考研。"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    aunt "哎，医生真好啊，工作稳定，但是也有风险，我记得隔壁家的……"
    "阿姨话说到一半，突然好像想起来什么似的，匆忙地咳了两声。"

    me "隔壁家的……？"
    "我正在纳闷，一旁的大叔突然接过话茬。"

    # # （主角：立绘1：疑惑）
    # show duhong confused at center
    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    uncle "欸，那个，小杜啊，你那个，要吃水果吗，我去家里给你拿点……"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    me "哦，隔壁家的是那位——"

    # # （主角：立绘1：笑）
    # show duhong smile at center
    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    me "对了，小时候接过我放学的尹青姐呢？我记得我走时，她正怀着孕呢，现在怎么样了？"

    "回想起尹青姐，我的脸上不由浮现出了笑容。"

    # 背景1：全黑
    scene bg grey
    with dissolve
    # （◎立绘：尹青（立绘1：笑））#居中#
    show yinqing smile at center
    with dissolve
    "我记得，尹青姐住外公家隔壁，家里是开小卖部的。"

    # （◎立绘：尹青（立绘1：笑））#居中#
    "她爱梳一条麻花辫，穿格子花纹的衣服，很瘦弱，爱笑，对人非常温柔。"

    # （◎立绘：尹青（立绘1：笑））#居中#
    "她老公是个皮肤黝黑的汉子，一对伉俪恩爱非常，都对我很好。"
    "可以说，尹青姐是帮助我能走上医学道路的重要人物。"
    "我记得很深，她在听说我的医学梦想后，对我说过的那番话————"

    yinqing "好呀，姐姐就等着小杜医生的好消息咯！"

    # （◎立绘：尹青（立绘3））#居中#
    show yinqing pregnant at center
    with dissolve
    "我走时，她刚被查出来怀孕，到现在，孩子也该有九岁了吧？"

    # 背景1：全黑
    scene bg grey
    "可叔叔阿姨却不回应我的好奇。"

    # （主角：立绘1：疑惑）
    show duhong confused at center
    with dissolve
    "一片死寂。"

    "我心里不由“咯噔”一声。"

    # 背景2：餐厅白天
    scene bg restaurant day
    with dissolve
    # （主角：立绘1：呆滞）
    me "叔叔阿姨？尹青姐怎么了？"

    # （◎立绘：大叔）#居左#
    show uncle at left
    # （◎立绘：阿姨）#居右#
    show aunt at right
    with dissolve
    "叔叔阿姨灿烂的微笑已然消失，蒙着一片阴影，表情复杂。"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    "终于，阿姨叹了一口气。"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    "阿姨1" "「小青她……走了好久了。」"

    "我愣了一下。"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    me "走……是指？"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    "大叔1" "「……镇上那个栗村妇儿医院，出了一些事情。」"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    me "这和栗村妇儿医院……有什么关系？"

    # # （◎立绘：大叔）#居左#
    # show uncle at left
    # # （◎立绘：阿姨）#居右#
    # show aunt at right
    # with dissolve
    "阿姨1" "「小青她当年在栗村妇儿医院生孩子，可是医院出了问题，小青本来身子骨也不硬，就……」"

    # 背景1：全黑
    scene bg grey
    with dissolve
    # *对话框震动*
    "……"
    "我瞠目结舌，一句话也说不出来。"

    me "尹青姐和孩子，都……"
    "我已经有了不好的预感。"
    
    # （◎立绘：大叔）#居左#
    show uncle at left
    with dissolve
    "大叔1" "「都没了……她老公这之后起诉过栗村妇儿医院，很艰难，只得了一点赔偿，后来他就离开栗镇了……」"

    "我还呆在原处。"
    
    scene bg grey
    show yinqing smile at center
    with dissolve
    "脑海里浮现出尹青姐的容貌，但倏忽之间，她的影像就像流沙一般消散了。"
    scene bg grey
    with Dissolve(2)
    with Pause(1)
    jump scene2