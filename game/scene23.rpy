define man = Character("男人", what_prefix="「", what_suffix="」", ctc="ctc_blink", ctc_position="nestled") # 男人

image black:
    Solid("#000")

image white:
    Solid("#FFF")

transform eye_blink:
    "eye_half_open.png"
    .1
    "eye_closed.png" 
    .1
    "eye_open.png"
    .2
    "eye_half_open.png"
    .1
    "eye_closed.png"
    .1
    "eye_open.png"
    .2
    "eye_half_open.png"
    .1
    "eye_closed.png"
    .1
    "eye_open.png"
    alpha 0.0


init -10 python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)

init python:
    # 全屏抖动特效
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [ self.anchors.get(i, i) for i in start ]
            self.dist = dist
            # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers. 
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

    Shake = renpy.curry(_Shake)

label scene2:
    $ renpy.movie_cutscene("images/background/logo.webm")
    scene bg grey with dissolve
    #背景6：黑暗的房间#
    scene bg_room_dark with dissolve
    # （主角：立绘1：呆滞）
    show duhong1 sad at truecenter
    with dissolve
    "我抱着自己的双膝，窝在外公家逼仄的房间里。"
    "一片黑暗中，亮着的只有我的电脑。屏幕上，是我查阅的，关于九年前“栗村妇儿医院重大感染事件”的报道。"
    "我呆滞地念出屏幕上的一行行字。"
    hide duhong1 sad
    me 1 sad "“4月22日至6月7日，共计手术292例，至9月1日止，发生感染166例，死亡2例……”"
    "我知道那死亡的两例是谁。那是一对母女。那本该是一对母女。"
    "鼻头一阵发酸，我把自己的脸埋在膝盖之间。"
    me 1 sad "只是一瓶配错了的戊二醛而已……怎么会这样……"
    
    "按报道来看，事发的直接原因是栗村妇儿医院消毒中心的一位药师，误看了消毒用的戊二醛浓度，导致全院产妇与新生儿爆发了以龟型分枝杆菌为主的混合感染。"
    "仅是一处疏忽，后果竟如此严重。"
    "我难以想象有一百多位像尹青姐一样的产妇遭遇了这样的痛苦。"
    "作为一名准医务工作者，我更是痛心疾首。"
    # （主角：立绘1：悲伤）
    "悲痛之中，尹青姐曾告诉我的那番话再度响起："
    scene bg grey
    with dissolve
    show yiqing smile
    with pixellate
    yiqing "好呀，那姐姐就等着小杜医生的好消息咯！"
    yiqing "……要记得，尽到一个医生的职责。"
    scene bg grey
    with pixellate
    "医生的……职责？"
    "儿时的我似乎曾这么问过她。"
  
    me 1 confused "是要把每一个患者救回来，对吗？"
    "……按我的印象，这就是正确答案。"
    # show duhong grief
    with dissolve
    "可我却看着和我曾如此亲近之人这么离开……"
    "黑暗中，回想起我在大学中学过的院感防控与管理知识，我不由得产生了一个无端的想法。"
    me 1 sad "要是……我能回到那个时候……把一切都纠正过来……"
    "是不是就能杜绝她们的痛苦了呢？"
    "是不是……还能看见尹青姐的笑容呢？"
    show duhong1 sad at truecenter with dissolve
    "我凄凉地笑了笑。我深知这只是我的奢望。尹青姐的离开是无法扭转的事实。"
    "就没有任何办法了吗……"
    "我靠在自己的双腿上，意识与双眼一起，逐渐模糊。"
    stop music fadeout 2.0
    scene bg grey
    with Dissolve(2)
    jump scene3

label scene3:
    # 第三幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    scene bg grey with dissolve
    # #背景1：全黑#
    man "……醒醒……杜鸿！……"
    "……似乎有人在……叫我的名字吗？是邻居叔叔吗？"
    # #背景5：双人宿舍内#
    scene bg_dormitory
    show eye_half_open at eye_blink
    with Pause(2)
    "我头疼欲裂，艰难地睁开双眼。"
    # # （主角：立绘1：疑惑）
    # show duhong confused
    # with dissolve
    show fangmin confused:
        zoom 2.0
        truecenter
    "映入眼帘的是一张巨大的陌生男人的脸。"
    # *对话框震动*
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    # （主角：立绘1：惊吓）
    # show duhong scared
    me 2 shocked "{size=+35}啊啊啊啊！{/size}"
    # *全画面：撞击特效* # TODO
    "我被吓得弹射起来，脑袋狠狠地撞上背后的墙。"
    # （主角：立绘1：悲伤）
    # show duhong grief
    me 2 shocked "痛死……"
    # *全画面：眨眼特效*
    scene bg_dormitory
    show eye_half_open at eye_blink
    with Pause(2)
    # （主角：立绘1：疑惑）
    # show duhong confused
    with dissolve
    "我四下打量，我似乎正身处我毫无印象的地方。"

    play music "audio/music/bgm3_back.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    "两张单人床陈列在狭小的房间里，旁边的衣架上挂着再熟悉不过的白大褂。"
    "我这是在学校宿舍？但我住的不是双人间啊。"
    "不……我……我不是在外公家吗？我记得我查着九年前院感事件，查着查着就睡着了……"
    "我边揉着还疼着的后脑勺，边把目光投到面前的陌生男人身上。"
    # （◎立绘：方岷：疑惑）#居中#
    show fangmin confused
    with dissolve
    "高个，背心，短裤。"
    "…不认识。"
    "会不会是哪个我记不得了的亲戚或者邻居？"
    "我试探着开口。"
    
    me 2 shocked "不好意思，我昨晚喝多了，请问您是……?"
    # （◎立绘：方岷：吃惊）#居中#
    show fangmin shocked
    with dissolve
    "男人脸上的表情逐渐由疑惑转变为惊恐。"
    man "老杜，你这是咋了？不就睡个懒觉吗，咋还傻了呢？"
    # （主角：立绘2：惊吓）
    # show duhong frightened at left
    with dissolve
    me 2 shocked "啊？"
    man "我是方岷啊！咱俩是室友啊！今天还得一起去上班啊！"
    # （主角：立绘2：疑惑）
    # show duhong confused at left
    with dissolve
    me 2 shocked "上班？上什么？"
    fangmin "咱、咱俩不是在栗村院感科上班吗？你别吓我哈？"

    "院感科？医院感染管理科？不，不对——"

    # *对话框震动*
    # （主角：立绘1：惊吓）
    scene bg_dormitory with fade
    # show duhong scared at left
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    # （◎立绘：方岷：吃惊）#居中#
    show fangmin shocked at center
    with dissolve
    me 2 shocked "你、你刚刚说我们在哪家医院上班？"
    # （◎立绘：方岷：吃惊）#居中#
    fangmin "啊？在、在栗村啊，栗村妇儿医院啊，我们都叫栗村的……"
    "栗村妇儿医院？这不就是——"
    "我脑中划过一个不切实际的想法。"

    # （主角：立绘1：疑惑）
    # show duhong confused at left
    with dissolve
    me 2 shocked "方岷，今天是几号？"
    # （◎立绘：方岷：疑惑）#居中#
    # show duhong confused at center
    with dissolve
    "方岷一脸狐疑地看向墙上的日历。"
    # （◎立绘：方岷：疑惑）#居中#
    fangmin "那个，4月22号……"

    # *全画面震动*
    "我立马下床，跑到日历面前，看着日历顶端的年份——"
    show bg_calendar with dissolve
    # *画面中央：日历*
    # （主角：立绘1：惊吓）
    me 2 shocked "果然……"
    # with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    # *画面中央：日历*
    "是九年前的4月22号……"
    jump scene4