init -10 python:
    risk_level = 100

transform center_to_corner:
    xalign 0.5
    yalign 0.5
    pause 1.0
    ease 2.0:
        xalign 0.0
        yalign 0.0
        zoom 0.5

label scene4:
    # 第四幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    scene office with dissolve
    # #背景3：医生办公室内#
    show duhong serious
    # （主角：立绘2：严肃）
    "我身穿栗村妇儿医院的白大褂，坐在自己的办公室里。"
    "没错，我现在有自己的办公室了。"
    "——我确定，自己确实是穿越了。"
    "现在是九年前的4月22日。"
    
    "换句话说，是“栗村妇儿医院重大感染事件”涉及的第一例手术的前一天。"
    "而我，是栗村妇儿医院感染管理科的一名医生。"
    "我一直不信穿越这种小说里的套路，但现在，我只能而且必须相信。"
    "是我昨晚的嘟囔灵验了，老天让我回来，改变那场院感危机，挽回尹青姐和她女儿的性命。"
    "身负如此重大的使命，我很快就接受了现实。"

    # #此时屏幕中央显示一个框框，显示“危险值 100”#
    show text "{color=#f76d47}{size=+35}危险值：{b}[risk_level]{/b}{/size}{/color}" at center_to_corner
    with dissolve

    "我还记得，院感危机的导火索是——"
    # 【问题1】
    menu:
        "消毒用戊二醛浓度配错":
            call correct from _call_correct
            me "没错，现在要做的第一件事是去找到那位配错消毒液的药师，纠正他致命的错误。"
        "消毒用碘伏浓度配错":
            me "我酒还没醒吗……应该是戊二醛啊！"

    "尹青姐现在应该就在医院里……虽然很想见见尹青姐……但应该先做重要的事。"
    "事不宜迟，确定下一步行动后，我立马起身，前往医院的消毒中心。"
    jump scene5

label scene5:
    # 第五幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    # #背景4：医院消毒中心内#
    scene hospital sanitary center with dissolve
    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    "根据印象中的名字，我很快就找到了那名粗心的药师。"

    # （◎立绘：潘叶：疑惑）#居中#
    show panye confused at center
    with dissolve
    "是个娇小的女孩，她对于我的到来似乎很害怕。一听我找她有事，她立马点头，换好防护服便出来见我了。"
    "一刻也不能耽搁，我开门见山。"
    me "潘叶医生，请问您对配制消毒用戊二醛溶液熟悉吗？"
    "毕竟我是医院感染管理科的一员，这种询问算是分内之事。"
    panye "啊？熟悉……熟啊，我通过了培训的……"
    me "那请问消毒用戊二醛浓度应该是多少才合理呢？"

    "我自然很清楚，戊二醛类消毒剂的戊二醛含量应为："
    # 【问题2】
    menu:
        "0.5%%-1%%":
            "怎么脑袋短路了！应该是2%%-2.5%%啊！"
        "2%%-2.5%%":
            call correct from _call_correct_1
            "没错，看来我消毒这门课学得不错啊！"

    # （◎立绘：潘叶：疑惑）#居中#
    "潘叶微微一愣，脱口回答出："
    panye "2%%？"
    me "……竟然是对的。"
    "看来得切换对策了。"
    panye "啊？"
    me "嗯……我能察看一下你配制的戊二醛溶液吗？可能需要重测一下浓度。"
    panye "啊？是，是我做的有什么不好的吗？"
    me "不不不，就是一个常规检查，没有针对你的意思——"
    "她这副态度把我都整不安了。说实话，我本来想劈头骂她一顿的。"
    "我把她配出的、将应用于明天手术的戊二醛溶液带去了化验科。不一会儿，令我大跌眼镜的结果就出来了。"

    # （主角：立绘2：惊吓）
    show duhong scared
    me "0…………0.1%%？"
    "随我一起等待的潘叶也大吃一惊。"

    # （◎立绘：潘叶：吃惊）#居中#
    show panye shocked at center
    panye "怎么会这样？我确实稀释了10倍啊，医院购买的戊二醛不是20%%的吗？"
    # （主角：立绘2：疑惑）
    show duhong confused
    me "20%%？你确定吗？"
    # （◎立绘：潘叶：疑惑）#居中#
    show panye confused
    panye "那个瓶上确实没标有效浓度……"
    me "什么？"
    # （主角：立绘2：严肃）
    show duhong serious
    "潘叶一脸忧虑地看着我。我猛烈地预感到，这或许并不是她粗心的过失。"

    # （◎立绘：潘叶：疑惑）#居中#
    # show panye confused at center
    "接下来，可能会是一场硬仗……"
    jump scene6

label scene6:
    # 第六幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    scene duhong office with dissolve
    # #背景3：医生办公室内#
    # （主角：立绘2：悲伤）
    show duhong grief at center
    with dissolve
    "一小时后。"
    "我把自己关在办公室里，瘫坐在地。"
    "我刚刚才知道，栗村妇儿医院的消毒中心从半年前开始就把购入的1%%戊二醛溶液当做20%%在用"
    "也就是说，这半年来，医院所用的戊二醛溶液浓度都是0.1%%……"
    "同时，我还了解到他们手术室所用的浸泡手术刀片、剪刀的戊二醛消毒液已经近15天未更换。"

    "连我都记得每隔多久就该更换戊二醛消毒液——"

    # 【问题3】至少每隔多久就该更换一次戊二醛消毒液？
    menu:
        "至少每周更换一次":
            call correct from _call_correct_2
            "是啊，怎么可能两周都不更换呢……"
        "至少每10天更换一次":
            "不对，像栗村这种常用消毒液的医院，至少每周就应该换一次啊！"

    "我无力地揉搓着太阳穴，脑中嗡嗡作响。"
    "没想到这个医院的管理已经差到了这种地步，那我一时半会儿的努力真的还有用吗……"
    "先不说其他，首先就需要重新配制所有戊二醛溶液，更换所有正在使用的戊二醛消毒液……"
    "我用手用力地捂住双眼，眼前一片斑斓的眩晕。"
    "逐渐地，我仿佛在那片眩晕中看见了一张脸。"
    scene bg grey with dissolve
    # （◎立绘：尹青（立绘1：笑））#居中#
    show yiqing smile at center
    with pixellate
    me "尹青姐……"
    "尹青姐现在怎么样了呢？她是明天的手术吗？还是后天？"
    "我很想见她，见她最后一面。"
    scene bg grey with pixellate
    # （主角：立绘2：严肃）
    show duhong serious with dissolve
    "……不，不能是最后一面。"
    "我要把尹青姐救回来。我要把尹青姐和其他一百多位产妇都救回来。"
    "因为……我是医生。"
    "……这就是尹青姐所说的，医生的职责吧？"
    "这座医院的崩坏需要我来拯救。"
    "我下定决心，从地上站起来，推开办公室的门。"
    jump scene7

label correct:
    show text "{color=#f76d47}{size=25}危险值 {b}-5{/b}{/size}{/color}" at truecenter
    with dissolve
    hide text "{color=#f76d47}{size=25}危险值 {b}-5{/b}{/size}{/color}"
    with dissolve
    $ risk_level -= 5
    show text "{color=#f76d47}{size=+35}危险值：{b}[risk_level]{/b}{/size}{/color}":
        xalign 0.0
        yalign 0.0
    return