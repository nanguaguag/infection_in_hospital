label scene7:
    # 第七幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    # #背景4：医院消毒中心内#
    
    scene hospital sanitary center with dissolve
    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    me "大家好！我是栗村医院感染管理科的杜鸿医师。这位是方岷医师。"

    "我站在栗村的消毒中心里。消毒中心的十余位医生们围绕着我，向我投来狐疑和忧虑的眼神。"

    "方岷站在我身后，紧张难安。"

    show fangmin confused at center
    with dissolve
    # （◎立绘：方岷：疑惑）#居中#
    fangmin "真的要这样吗……"

    me "消毒中心的各位，关于我上午所查到的戊二醛消毒液的重大疏漏，相信你们也有所耳闻。"

    "消毒中心的医生们表情立刻变得更加焦虑。"

    # （◎立绘：潘叶）#居中#
    hide fangmin confused with dissolve
    show panye serious at center with dissolve
    panye "杜医生，我们会弥补这次疏忽的……"

    me "你们不用担心，我不会追究你们的过错，这本质上是管理层的错误。但你们有义务为这次过错赎罪，因为如果未被发现的话……会造成你们难以想象的严重后果。"

    panye "好的好的，我们一定严格按照杜医生的指示做，对、对吧？"

    "潘叶一暗示，消毒中心的大家立马接二连三地附和。"

    "嗯，有这股士气就够了。"

    me "很好，首先，我需要一部分人去查验医院里所有的消毒液浓度，并更换为正确浓度。"

    "根据零零星星举起的手，我选了几个，并让他们立刻去忙活，一刻也不能搁。"

    me "方岷，你去监督他们。"

    # （◎立绘：方岷：吃惊）#居中#
    hide panye serious with dissolve
    show fangmin shocked at center with dissolve
    fangmin "啊？哦。"
    show fangmin serious at center with dissolve
    me "剩下的人，我需要先知道你们对医院感染的了解程度。"

    "我顿了一下，开始提问。"

    # （注：以下是杜鸿医生的问答时间，需要考查大家对于医院感染相关知识的了解，你准备好了吗？）

    # 【问题4】
    me "问题一，这是送分题——医院工作人员在医院内获得的感染属于院感吗？"

    menu:
        "属于":
            call correct from _call_correct_3
            "没错，医院工作人员的院内感染也属于院感。"
        "不属于":
            "医院工作人员的感染当然也属于院感了……为了尹青姐，打起精神啊。"

    # 【问题5】
    me "问题二，院感分为外源感染和内源感染，其中交叉感染是指？"

    menu:
        "内源感染":
            "交叉交叉，指的当然是外源啊……为了尹青姐，打起精神啊。"
        "外源感染":
            call correct from _call_correct_4
            "没错，外源感染是天然宿主的病原体感染或传递给非天然宿主的现象，是指细菌、病毒、真菌、寄生虫等病原体侵入人体所引起的局部组织和全身性炎症反应。"

    # 【问题6】
    me "问题三，在我们栗村妇儿医院，新生儿经胎盘获得的感染属于院感吗？"

    menu:
        "不属于":
            call correct from _call_correct_5
            "经胎盘获得的感染只与父母有关，和医院无关，其感染自然不属于院感。"
        "属于":
            "经胎盘感染和医院有什么关系呢？哎，为了尹青姐，打起精神啊。"

    hide fangmin serious with dissolve
    show panye smile at center with dissolve
    # （◎立绘：潘叶：笑）#居中#
    panye "杜医生，这几个题还挺简单的嘛。"

    # （主角：立绘2：笑）
    show duhong smile with dissolve
    "我回了笑嘻嘻的潘叶一个笑容。"

    me "别高兴得太早。接下来，我会问你们几道关于医院卫生护理，也就是院感防控的题目。"

    # （◎立绘：潘叶：笑）#居中#
    panye "尽管问！我们都是接受过专业培训的。"

    me "哦，那你知道七步洗手法吗？"

    panye "当然了！这是医务人员的基本要求，是最专业的洗手方法。"

    # （主角：立绘2：严肃）
    show duhong serious with dissolve
    # 【问题7】
    me "那问题四，请问七步洗手法的“弓”这一步，也就是洗指背这一步，是在第几步完成的呢？"

    menu:
        "第四步":
            call correct from _call_correct_6
            "是的，“弓”这一步是洗指背，曲各手指关节，半握拳把指背放在另一手掌心旋转揉搓，双手交换进行。"
            "另外，“七步洗手法”的全步骤为“内、外、夹、弓、大、立、腕”，即分别清洗手掌、指缝、指背、拇指、指间和手腕手臂。"
        "第五步":
            "不对！第五步应该是洗拇指的“大”才对啊！"
            "忘了吗，“七步洗手法”的全步骤为“内、外、夹、弓、大、立、腕”，即分别清洗手掌、指缝、指背、拇指、指间和手腕手臂。"

    # （◎立绘：潘叶：严肃）#居中#
    panye "我……我还是勉强记得的！"

    me "好啊，那你还知道消毒和灭菌的区别吗？"

    panye "知道啊！"

    # 【问题8】

    me "好，那问题五：根据斯伯尔丁分类法，下列哪项全部属于高度危险物品？"

    menu:
        "手术器械、胃肠道内镜、麻醉机管道":
            "粗心了……胃肠道内镜只与完整黏膜相接触，而不进入人体无菌组织、器官和血流，也不接触破损皮肤、破损黏膜的物品，只能算是中度危险物品。"
        "心脏导管、腹腔镜、穿剌针":
            call correct from _call_correct_7
            "正确！它们都属于高度危险物品。"
            "要记得，高度危险物品有手术器械、穿剌针、腹腔镜、活检钳、心脏导管、植入物等等。"

    "它们进入人体无菌组织、器官、脉管系统，或有无菌体液从中流过的物品或接触破损皮肤、破损黏膜的物品，一旦被微生物污染，具有极高感染风险！"

    "我接连抛出多个院感防护相关问题，难度逐步加深，不少消毒中心的医生面露难色。"

    # （主角：立绘2：悲伤）
    show duhong sad with dissolve
    "……这些基础知识巩固得还不够到位啊。"
    show duhong serious with dissolve
    # （主角：立绘2：严肃）
    "我咳了两声。"

    me "问题到此结束。"

    "大家都兴奋地抬起头。"

    me "……但并不代表你们就能疏忽了。最重要的不是考住你们，而是让你们把这些知识应用到日常工作中，切实地履行。"

    "众人都惭愧地面面相觑，恐怕是想起了那瓶戊二醛的事。"

    "我叹了口气。"

    me "总之，我需要你们把曾经学过的知识再捡起来，越快越好，然后认真检查医院的每个角落，场所的消毒、医生的防护、手术的进行……"

    me "从现在开始行动，一刻都不能耽搁。"

    "依稀地，我听到有医生小声嘀咕。"
    
    scene hospital sanitary center with dissolve
    # （◎立绘：药师）#居左#
    show pharmaceutist at left
    pharmaceutist "不就是一瓶戊二醛吗，何必闹这么大……"
    # （主角：立绘2：愤怒）
    show duhong angry at center with dissolve
    me "就一瓶戊二醛？"

    "我再次想到九年后的我所见的、一篇篇关于“栗村妇儿医院重大感染事件”的惨烈报道。"

    "就会因为这些医生这么想，才会导致这些悲剧出现……"

    "我怒火涌上心头，正欲骂他一通——"

    play music "audio/music/bgm3_back.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    # （◎立绘：药师）#居左#
    # （◎立绘：潘叶：严肃）#居右#
    show panye serious at right with dissolve
    panye "你怎么能这么说！"

    # （主角：立绘2：惊吓）
    show duhong shocked with dissolve
    "我被吓了一跳，立马闭上嘴。"
    panye "我们一直都没想过确认购入戊二醛的浓度，长达半年之久，谁不知道消毒对于院感防控的重要性……说不定医院之中，已经埋下了祸根。"

    "那位医生瞟了潘叶一眼，低下头去。"

    # （◎立绘：潘叶：笑）#居右#
    show panye smile at right with dissolve
    "潘叶回头看我，骄傲地笑了笑。"

    # （主角：立绘2：笑）
    show duhong smile with dissolve
    "我也回了她一个笑容，随即恢复冷脸，望向消毒中心的众位医生。"

    scene hospital sanitary center with dissolve
    # （主角：立绘2：严肃）
    show duhong serious at left with dissolve
    me "潘医生说得很对！但现在改正错误为时不晚。要记得，你们是医生，是更应该珍视生命的一群人。"

    # （◎立绘：潘叶：笑）#居中#
    show panye smile at center with dissolve
    "潘叶冲我点点头。"

    me "那你们现在可以开始行动了。潘叶，你去监督他们。"
    # （◎立绘：潘叶：疑惑）#居中#
    show panye confused at center with dissolve
    panye "欸？那杜医生你……"

    "我像在为自己鼓劲似的，握紧了拳头。"

    "经过我这次的疏导，九年前的“栗村妇儿医院重大感染事件”应该可以避免。尹青姐……应该也能顺利出院。"

    "……这么看来，救了尹青姐和她的女儿，我穿越而来的初衷就已经圆满了。"

    # #背景1：全黑#
    scene bg grey

    "……是这样吗？"
    show yiqing smile at center
    with pixellate 
    # （◎立绘：尹青（立绘1））#居中#
    yiqing "……小鸿，你要记得，作为一个医生的职责。"

    scene hospital sanitary center with pixellate
    
    "……没错，不是这样的。"

    "我并不能因为今日问题的解决而放松。"

    "经过方才的问答，以及那位抵触我的医生，我深刻意识到了这座医院的管理之混乱。"

    "我记得，在我所见的报道上，也有相关部门对于栗村妇儿医院在管理方面缺漏的批评。"

    "只要栗村的管理问题一日不改，即使我暂时阻止了这时的感染事件，也难保后来不会发生相同或更严重的事故。"

    "院感的防控，不能满足于一时，更注重的是将后患扼杀。"

    # #背景4：医院消毒中心内#
    show duhong serious with dissolve

    "我看向消毒中心的大家。"

    me "……我有自己的要事要办。"
    stop music fadeout 1.0

    jump scene8

label scene8:
    # 第八幕
    $ renpy.movie_cutscene("images/background/logo.webm")
    # #背景1：全黑#
    scene bg grey with dissolve
    show duhong serious at left with dissolve
    # （主角：立绘2：严肃）
    "我站在那扇门前，深吸了一口气。"

    "终于，我伸出手，缓慢地叩了三下。"

    "紧闭的房间里，一个男人的声音传来。"

    "男人" "「进来吧。」"

    "我推开门，见到了那张熟悉的脸。"

    play music "audio/music/bgm2_tense.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center with dissolve

    "我在报道上见过他——栗村妇儿医院的院长，岳为。"
    "按照曾经的报道所述，他的不作为直接导致了那场感染事件的恶化。"
    "……凭我一己之力，不可能动员整个医院。我一定要、必须要说服他。"

    # （◎立绘：岳为：吃惊）#居中#
    show yuewei surprise at center with dissolve
    "岳为见我进来，立马从办公桌前站了起来，似乎颇为意外。"

    yuewei "杜医生？医院感染管理科有什么事吗？"

    "我深呼吸了一口。"

    me "院长，我必须要向你揭露一些事情。"

    show yuewei serious at center with dissolve
    "岳为的笑容僵在脸上，表情旋即严肃。"

    yuewei "说吧。"

    "我掏出早上检验科的报告单。"

    me "这是我今早拜托检验科测得的，我院使用的戊二醛消毒液的浓度说明。"

    "岳为缓缓地拿走报告单。"

    yuewei "0.1%%……"

    me "您应该知道这不是正常的消毒液浓度吧？"

    yuewei "……"

    "他把报告单还给我。"

    yuewei "……这有多久了？消毒液的事。"

    me "听消毒中心的人说，应该有半年了。"

    yuewei "半年都一直在使用错误浓度的消毒液吗？"

    me "……是的。因为购入的戊二醛溶液上未标示有效浓度，所以大家都……"

    yuewei "原来采购部那边也有过失……"

    "我观察着他的脸色，继续开口。"

    me "院长，这并不是我想向您报告的唯一的事。经过我的调查发现，这重大的过失根本上是源于医院的管理混乱。"

    yuewei "……"

    me "院长，我有几个问题想要问您。"

    "岳为叹了口气。"

    # （◎立绘：岳为：闭眼）#居中#
    show yuewei eyeclosed at center with dissolve
    yuewei "你说吧。"

    # 【问题9】
    me "……好的。您知道医院感染三级护理管理体系分别为哪三级吗？"
    yuewei "一级管理为病区护士长和兼职监控护士，二级管理为专科护士长，三级……三级……"

    "我替他回答："

    menu:
        "护理部副主任":
            call correct from _call_correct_8
            "没错，护理部副主任即医院感染管理科副主任。"
        "医院感染管理科临床医师":
            "不对啊！应该是护理部副主任。"

    me "医院感染三级护理管理体系的职责是评估医院感染发生的危险性，目的是及时发现，及时处理。"

    yuewei "……哎，我记不清楚了。"

    "我顿了顿，再次发话。"

    # 【问题10】
    me "那院长，您了解院感防控所需完善的规章制度吗？"

    yuewei "消毒隔离制度、供应室物品消毒制度和……"

    "他再次愣住了。但这次似乎并不是他忘记了，而是不敢说了。"

    me "包括对院内各项消毒措施的管理、对消毒剂使用，感染高发科室等的及时监测、对感染源和易感人群的控制和保护、以及院内人员的院感防控知识教育，等等。"

    "岳为仍然一语不发，甚至不敢和我对视。"

    stop music fadeout 2.0

    # TODO
    # （这里可以再插几个拷问院长的问题hhh或者就不设分支搞单纯问答，知识展示那种）

    # （注：此处为结局分支。若危险值至此仍在20以上，则开启BE。以下为BE。）
    
    if risk_level >= 20:
        jump bad_ending
    else:
        jump happy_ending

label bad_ending:
    scene bg grey with dissolve
    "我的一番问话之后，岳为早已无话可说。"
    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center with dissolve
    "我咽了口口水。"

    me "院长，您明白事态的严重性了吗？"

    # （◎立绘：岳为：笑）#居中#
    show yuewei smile at center with dissolve
    "岳为笑了一声。"

    yuewei "当然。你想说的是，我是如何疏于医院感染管理的，对吧？"

    me "……没错。我认为目前栗村的状况已经非常危险，错用半年的低浓度戊二醛溶液已经足够引起您的注意了。"

    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center with dissolve
    "岳为缓缓抬头，犀利的眼神与我对视。"

    play music "audio/music/bgm4_surprised.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    yuewei "小杜医生，你还是太年轻了。"

    "我皱起眉。"

    yuewei "我知道院感防控的重要性，但现在……还来得及吗？"

    scene bg grey with dissolve
    # （主角：立绘2：惊吓）
    show duhong shocked at center
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)

    me "你在说什么？难道你还要继续这样——"

    yuewei "我会派人更换所有戊二醛溶液。但仅此而已。"

    # （主角：立绘2：呆滞）
    show duhong mindblank at center
    with dissolve
    me "……"

    hide duhong with dissolve
    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center
    with dissolve
    yuewei "你以为我不知道吗？你从今早就开始指挥消毒中心的医生们在医院各处检查。"

    hide yuewei with dissolve
    # （主角：立绘2：严肃）
    show duhong serious at center
    with dissolve
    me "这是为了杜绝一切隐患……"

    hide duhong with dissolve
    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center
    with dissolve
    yuewei "杜鸿，你别忘了，我才是栗村的院长！"

    stop music fadeout 2.0

    hide yuewei with dissolve
    # （主角：立绘2：愤怒）
    show duhong angry at center
    with dissolve
    "我一时语塞，只能用眼神表达愤怒。"

    hide duhong with dissolve
    # （◎立绘：岳为：闭眼）#居中#
    show yuewei eye_closed at center
    with dissolve
    yuewei "你出去吧，为了避免检查时出意外，戊二醛的事情我会解决的。"

    me "可是，医院从管理上就有问题，怎么是更换一下戊二醛就能解决的——"

    show yuewei serious at center
    with dissolve
    "岳为严肃地朝我瞪来。那种眼神里毫无医者的慈悲，仅仅闪烁着利益的光芒。"

    yuewei "……我知道该怎么做。你安心回去吧，我不会追究你的责任的。"

    "我还倔强地不愿意离去。此时，响起敲门声。"

    scene bg grey
    # （◎立绘：潘叶：严肃）#居中#
    show panye serious at center
    with dissolve
    "进来的是潘叶。"

    hide panye with dissolve
    # （主角：立绘2：呆滞）
    show duhong mindblank at center
    with dissolve
    me "……"

    hide duhong with dissolve
    # （◎立绘：潘叶：严肃）#居中#
    show panye serious at center
    with dissolve
    panye "院长，我是来找杜医生的。"

    yuewei "嗯。"

    "还没等我反应过来，潘叶就把我拉出院长办公室了。"

    scene bg grey with dissolve

    "回去的路上，我始终抑制不住愤恨的怒火。"

    # （主角：立绘2：愤怒）
    show duhong angry at center
    with dissolve
    me "这种人也配当院长……"

    # （◎立绘：潘叶：闭眼）#居中#
    show panye eye_closed at right
    with dissolve
    panye "杜医生，就是院长派人叫我拉你走的……你别再顶撞院长了，什么也不会改变的……"

    # （主角：立绘2：闭眼）
    show duhong eye_closed
    with dissolve
    "我悔恨地摇了摇头。"

    "或许更换了戊二醛会暂时安定一段时间，但难保后面不会发生相同或更严重的事故。"

    "可我在这个本就不属于我的时空里，还能干什么呢……"

    # #背景1：全黑#
    scene bg grey with dissolve
    # （主角：立绘2：呆滞）
    show duhong mindblank at center
    with dissolve
    "后来，我几次三番企图去找院长继续申诉，都被他拒之门外。"

    "到后来，他甚至找了个由头把我停职了。"

    "我在员工宿舍里混了很久，只有每天听着方岷带回来的情报度日。"

    "幸运的是，尹青姐顺利生下了她的女儿，现在已经在幸福地带孩子了。"

    "恍惚中，我安慰自己说："
    
    "「这或许就是最好的结局了吧？」"

    "我安分了一段时间，后来也顺利恢复职位了。"

    "直到半个月后，我在医院大厅看到了一个熟人——尹青姐的老公。"

    "他大声地哭喊着，声称要见岳为院长，最后被保安拖走。"

    "我愣在原地。"

    "尹青姐还是没有逃脱被龟型分枝杆菌感染的命运。"

    "以尹青姐为开端，我亲眼见证了九年前那噩梦般的感染事故。"

    "痛苦的患者、声讨的家属、混乱的管理层……"

    "一切都没有改变。"

    "我也只能在痛苦的悔恨中、在九年前的时空里，度过余生。"

    scene Solid("#000")
    with Dissolve(5)
    return

label happy_ending:
    stop music
    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    me "……院长，您应该明白了状况的重要性了。"

    # （◎立绘：岳为：笑）#居中#
    show yuewei smile at center
    with dissolve
    "岳为却突然抬眼看我，嘴角漾起微笑。"

    yuewei "小杜医生，你是不是发生了什么事啊？"

    # （主角：立绘2：惊吓）
    show duhong surprise at left
    with dissolve
    # （◎立绘：岳为：笑）#居中#
    me "欸？"

    # （主角：立绘2：闭眼）
    show duhong eye_closed at left
    with dissolve
    "我把目光移到一边。"

    "我只是……不愿尹青姐那样的悲剧再次出现罢了。"

    "我想把那些母子幸福的人生还给他们。"

    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    me "……算是吧。"

    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center
    with dissolve
    "岳为的表情突然严肃。"
    yuewei "……幸亏你来通知我，不然我还一直被蒙在鼓里。"

    # （主角：立绘2：吃惊）
    show duhong shocked at left
    with dissolve
    me "欸？"

    play music "audio/music/bgm3_back.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    "他的发言出乎我的意料。"

    yuewei "如今最应该做的事是更换所有戊二醛溶液为正常浓度……其他的消毒液浓度也有必要检查。"

    yuewei "从始至终我都忽略了你们医院感染管理科的工作……责任在我啊。"

    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    "我试探着开口。"

    me "院长……您这是……"

    # （◎立绘：岳为：笑）#居中#
    show yuewei smile at center
    with dissolve
    "岳为微笑着看着我。"

    yuewei "我们是妇儿医院，妇产科是医院里最美好的科室，生命的诞生比什么都令人开心。"

    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center
    with dissolve
    yuewei "但我的医院却发生了如此低级的错误，若不是你告诉我，这些幸福地前来的家庭可能就会哭着离开……"

    yuewei "我过了一段平安的院长日子，就忘了院感是多么危险又轻易的事……"

    yuewei "只是一个小小细菌的蔓延，就可能导致无数伤口的感染，无数痛苦的产生……"

    # （主角：立绘2：闭眼）
    show duhong eye_closed at left
    with dissolve
    "……是啊，院感这么可怕，却被我们忽视良久。"

    "我们都以为医院是最安全的场所，它医治患者，缓解病痛，给予病人们健康。"

    "但正因如此，感染才更容易发生。并且，在一个细菌病毒如此集中的公共场合，感染的传播更为轻松，也更容易发生重大的感染事故。"

    "作为医生，我们有必要担起杜绝院感的重任，将自己所学的专业防控知识，应用到医院的运作之中去。"

    # （主角：立绘2：严肃）
    show duhong serious at left
    with dissolve
    me "您说得没错，院长。所以请您……"

    "岳院长突然把手搭在我的肩上。"

    # （主角：立绘2：惊吓）
    show duhong scared at left
    with dissolve
    # （◎立绘：岳为：笑）#居中#
    show yuewei smile at center
    with dissolve
    yuewei "小杜医生，你放心吧，我一定会尽快把医院扳回正轨的。"

    "我呆呆地望着院长。"

    # （◎立绘：岳为：严肃）#居中#
    show yuewei serious at center
    with dissolve
    yuewei "当医生最顾忌的是自负……我忘记了自己身为医者的使命。"

    "……没错。身为医生的职责，就像尹青姐告诉我的那样。"

    "我脑海中的版图逐渐清晰。"

    # （主角：立绘2：笑）
    show duhong smile at left
    with dissolve
    yuewei "你就尽管说要怎么做，我作为院长，一定严格执行。"

    stop music fadeout 2.0

    "我眼神坚定，点了点头。"
    jump scene9

label scene9:
    play music "audio/music/bgm7_good.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    # 第九幕（HE）（BE无该幕）
    $ renpy.movie_cutscene("images/background/logo.webm")
    # #背景6：医院走廊#
    scene hospital corridor with dissolve
    # （主角：立绘2：笑）
    show duhong smile at left
    with dissolve
    "两个月后。"

    "我踏进栗村妇儿医院的大门，扑面而来的消毒液气味竟让我觉得如此清香。"

    "我走在前往医院感染管理科的路上，迎面而来，是一张我再熟悉不过的面孔。"

    me "早啊，潘医生。"

    # （◎立绘：潘叶：笑）#居中#
    show panye smile at center
    with dissolve
    panye "杜医生早上好！你有没有觉得，最近医院格外得干净整齐啊！病人们也都赞不绝口，有一种飞升为大医院的感觉呢！"

    "我冲她笑笑。再次寒暄了几句后，我们就走上了各自的道路。"

    hide panye
    show duhong at center
    with dissolve

    "上个月，我被院长升职为了医院感染管理科的主任。院长说，这远不足以表彰我对栗村做出的贡献。"

    "栗村妇儿医院按照我的预想走上了正轨，那场可怕的感染事件自然也被扼杀在了襁褓里。"

    "我们的医院愈来愈健康，这还不是令我最高兴的。"

    "最为高兴的是，我们医院大刀阔斧的改革措施被报道在了杂志和报纸上，这吸引了全市乃至全国的注意。"

    "政府开始严加监控医院的院感防控事宜，管理力度的加大直接导致了院感风险的大大降低。"

    "栗村被作为院感防控方面的表率，在全国接受了褒奖。许多医院也沿用了我们的方针政策，在院感预防上大下功夫。"

    "边回想着这奇异的穿越之旅，没过多久，我就来到了自己的办公室门前。"

    stop music fadeout 1.0

    # （主角：立绘2：严肃）
    show duhong serious with dissolve
    "站在门前，我突然停下了动作。过了片刻，才扭开门把。"

    play music "audio/music/bgm8_fareware.mp3" fadein 1.0 fadeout 2.0 volume 0.5 loop 

    # （主角：立绘2：呆滞）
    show duhong mindblank with dissolve
    scene office with dissolve
    # （◎立绘：尹青（立绘2：笑））#居中#
    show yiqing smile at center
    "尹青姐站在我的办公室里，抱着她满月不久的宝宝。"

    "微笑着，麻花辫，格子裙。"

    me "尹青姐……"

    "这是我在她生下孩子后第一次看见她。上次，是我在产房远处，远远地望着她。"

    # （◎立绘：尹青（立绘2：疑惑））#居中#
    show yiqing confused at center
    with dissolve
    "尹青姐似乎十分惊讶。"

    yiqing "您认识我？"

    # （主角：立绘22：闭眼）
    hide yiqing
    show duhong eye_closed at center
    with dissolve
    "我愣了一下，苦笑着摇摇头，把呼之欲出的眼泪一点点收回去。"

    # （主角：立绘22：笑）
    show duhong smile at center
    with dissolve
    me "您……您是我院接待过的产妇吗？"

    hide duhong
    # （◎立绘：尹青（立绘2：疑惑））#居中#
    show yiqing confused at center
    with dissolve
    pause 0.5
    # （◎立绘：尹青（立绘2：笑））#居中#
    show yiqing smile at center
    with dissolve
    "尹青姐笑了。"

    yiqing "您是小杜医生吧？我在报纸上看到了您的报道，您做了很了不起的事。要不是您，也许我的女儿就不能顺出生了呢。"

    "我害羞地低下头。"

    "尹青姐就像我记忆中一样，温柔地笑着。"

    yiqing "谢谢你。"

    "阳光穿过窗玻璃，照在尹青姐的脸庞上。她怀里的小孩“咯吱咯吱”地笑起来。"

    "我也笑了。"

    me "不……是我该谢谢你。"

    # （◎立绘：尹青（立绘2：疑惑））#居中#
    show yiqing confused at center
    with dissolve
    "尹青姐歪着头，露出疑惑的神情。"

    hide yiqing
    # （主角：立绘22：呆滞）
    show duhong mindblank at center
    with dissolve
    "突然，我有一阵强烈的感觉——"

    "我可能，要离开这个时空了。"

    "……可是，我回去之后，一切是改变之后的，还是……"

    # （主角：立绘22：闭眼）
    show duhong eye_closed at center
    with dissolve
    "我摇了摇头，把那些想法赶出脑海。"

    # （主角：立绘22：笑）
    show duhong smile at center
    with dissolve
    "我眼中含着泪水，对尹青姐说出，“小杜医生”的最后一番话："

    # （◎立绘：尹青（立绘2：疑惑））#居中#
    me "尹青姐，如果不是你，我根本不会这么明了地意识到医院感染的危害性……这是我们医务工作者，最容易忽略的隐患。"

    me "尹青姐，就算我回去了，我也不会荒废我学过的、向栗村的大家传播过的院感防控知识。我会在我接下来的医者生涯中，继续传播它、宣扬它，不让那样的事故再次发生。"

    hide duhong
    show yiqing confused at center
    with dissolve
    "尹青姐眨巴着眼睛，抚摸着怀里的孩子。"

    "还有最后一句话……但我实在不好意思说出口。"

    "阳光渐而灿烂，刺眼。"

    "尹青姐的身影在阳光里模糊，我的意识也逐渐混沌。"

    "——我终于完整地想起了那段对话。"

    # #背景1：全黑#
    scene bg grey with pixellate
    show duhong young at left with dissolve
    me "尹青姐姐，我长大之后，也要当医生，把你身上的病都治好！"
    show yiqing smile at center with dissolve
    yiqing "好呀，那姐姐就等着小杜医生的好消息咯。"

    me "没问题！"

    yiqing "小鸿啊，你一定要记得，作为医生的职责是什么。"

    me "职责……就是把所有患者都救回来，对吗？"

    yiqing "……说的没错，但能不能救回来，并不是你所能控制的。"

    me "怎么会呢？我就是会把所有人都治好的。"

    yiqing "……"

    yiqing "小鸿，你要记住。"

    yiqing "作为医生最应该铭记于心的，是平等地珍视每一条生命。"

    yiqing "无论能力大小，无论困难与否……无论究竟能不能成功。"

    yiqing "都要把每位病人的生命当做自己的家人一样，去珍惜，去为他们……着想。"

    scene office with pixellate

    show yiqing smile with dissolve

    "我眼前的尹青姐，像回忆里那样灿烂地笑着。"

    "……如果回去了，我还能见到如此幸福的尹青姐吗？"

    "我不确定。"

    "……但我确定的是，要是尹青姐还在，她见到的一定是她所想见到的——"

    # （◎立绘：主角（本作中唯一的全身立绘2：笑））#居中#
    scene bg grey with dissolve
    show duhong smile standing at center
    "那位“小杜医生”。"

    stop music fadeout 2.0

    scene bg grey
    show text "{size=+35}{color=#90EE90}—The End—{/color}{/size}"
    with dissolve
    scene bg grey
    with Dissolve(2)
    return
