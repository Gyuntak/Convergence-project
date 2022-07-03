import pandas as pd

def process_AI(df):
    facial_result = df[df["facial_result"] != "null"]
    facial_result1 = facial_result["facial_result"].values[0]
    split_df = df['feelings_action'].str.split(',')

    split_df = split_df.apply(lambda x: pd.Series(x))
    split_df.columns = ['Happy', 'Anger', 'Unrest', 'Hurt', 'Sad', 'Neutral']


    a = pd.DataFrame(split_df.groupby('Happy')['Happy'].count())
    b = pd.DataFrame(split_df.groupby('Anger')['Anger'].count())
    c = pd.DataFrame(split_df.groupby('Unrest')['Unrest'].count())
    d = pd.DataFrame(split_df.groupby('Hurt')['Hurt'].count())
    e = pd.DataFrame(split_df.groupby('Sad')['Sad'].count())
    f = pd.DataFrame(split_df.groupby('Neutral')['Neutral'].count())

    count_df = pd.concat([a, b, c, d, e, f], axis=1).fillna(0)

    count_df['index'] = count_df.index

    count_df.columns = ['Happy', 'Anger', 'Unrest', 'Hurt', 'Sad', 'Neutral','ai_result']


    count_df_num = count_df.reset_index()
    del count_df_num['index']

    count_df = pd.concat([count_df_num], axis=1).fillna(0)



    ######################## 감정 시작 ######################


    ### HAPPY ##### ### HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY ######## HAPPY #####
    action_result = ""
    if facial_result1 == 'Happy':
        Happy = count_df.nlargest(4, ['Happy'], keep='all')

        
        Happy = Happy[["Happy", "ai_result"]]

        # Happy 인덱스를 리셋
        Happy = Happy.reset_index()
        del Happy['index']
        

        a = Happy.loc[1, "ai_result"]


        action_result = a


    #### ANGER ######### #### ANGER ######### #### ANGER ######### #### ANGER ######### #### ANGER ######### #### ANGER #########v
    elif facial_result1 == 'Anger':
        Anger = count_df.nlargest(4, ['Anger'], keep='all')

        # 기쁨 Happy 의 1~4순위 활동
        Anger = Anger[["Anger", "ai_result"]]

        # Happy 인덱스를 리셋

        Anger = Anger.reset_index()
        del Anger['index']

        # loc로 Act 값 추출 : Happy의 1~4순위 값

        a = Anger.loc[1, "ai_result"]

        action_result = a

    #######UNREST #############
    elif facial_result1 == 'Unrest':

        Unrest = count_df.nlargest(4, ['Unrest'], keep='all')

        # 기쁨 Happy 의 1~4순위 활동
        Unrest = Unrest[["Unrest", "ai_result"]]

        # Happy 인덱스를 리셋

        Unrest = Unrest.reset_index()
        del Unrest['index']

        # loc로 Act 값 추출 : Happy의 1~4순위 값

        a = Unrest.loc[1, "ai_result"]



        action_result = a

    ######HURT #####################HURT #####################HURT #####################HURT #####################HURT #####################HURT #####################HURT ###############
    elif facial_result1 == 'Hurt':
        Hurt = count_df.nlargest(4, ['Hurt'], keep='all')

        # 기쁨 Happy 의 1~4순위 활동
        Hurt = Hurt[["Hurt", "ai_result"]]

        # Happy 인덱스를 리셋

        Hurt = Hurt.reset_index()
        del Hurt['index']

        # loc로 Act 값 추출 : Happy의 1~4순위 값

        a = Hurt.loc[1, "ai_result"]



        action_result = a



    ##########SAD ############################SAD ###########################SAD #################
    elif facial_result1 == 'Sad':
        Sad = count_df.nlargest(4, ['Sad'], keep='all')

        # 기쁨 Happy 의 1~4순위 활동
        Sad = Sad[["Sad", "ai_result"]]

        # Happy 인덱스를 리셋

        Sad = Sad.reset_index()
        del Sad['index']

        # loc로 Act 값 추출 : Happy의 1~4순위 값

        a = Sad.loc[1, "ai_result"]

        action_result = a

    ########## NEUTRAL ##############
    elif facial_result1 == 'Neutral':
        Neutral = count_df.nlargest(4, ['Neutral'], keep='all')

        # 기쁨 Happy 의 1~4순위 활동
        Neutral = Neutral[["Neutral", "ai_result"]]

        # Happy 인덱스를 리셋

        Neutral = Neutral.reset_index()
        del Neutral['index']

        # loc로 Act 값 추출 : Happy의 1~4순위 값

        a = Neutral.loc[1, "ai_result"]

        action_result = a

    return action_result

###################################################################END #################################################

# loc로 Act 값 추출 : Happy의 1~4순위 값

# b = Happy.loc[1, "Act"]
# c = Happy.loc[2, "Act"]
# d = Happy.loc[3, "Act"]
#
# # 랜덤한 활동 1개 추출
#
# E = Ori_ex_Happy.sample(1)
# e = list(E.index)
# e = e[0]
#
# e = Ori_ex_Happy.loc[e, "Act"]

# act_col = pd.DataFrame([['OTT 시청'],
    #                         ['TV 시청'],
    #                         ['게임(모바일·PC·콘솔)'],
    #                         ['그림 그리기'],
    #                         ['글쓰기'],
    #                         ['낚시'],
    #                         ['노래방 가기'],
    #                         ['독서(도서관·책/잡지보기)'],
    #                         ['만화·애니'],
    #                         ['맛집 탐방'],
    #                         ['미용(미용실·네일아트 등)'],
    #                         ['반려 동물 활동'],
    #                         ['보드 게임(장기·바둑 포함)'],
    #                         ['사진 찍기'],
    #                         ['생활공예(라탄·도자기 클래스 포함)'],
    #                         ['쇼핑몰 가기'],
    #                         ['수집 활동(곤충·돌 등)'],
    #                         ['스포츠 관람(야구장·TV 등)'],
    #                         ['스포츠 활동(등산·테니스·축구 등)'],
    #                         ['악기 연주'],
    #                         ['여행(해외·국내)'],
    #                         ['영화관 가기'],
    #                         ['요리(쿠킹 클래스 등)'],
    #                         ['원예·재배'],
    #                         ['음주'],
    #                         ['인터넷 서치'],
    #                         ['인터넷 쇼핑'],
    #                         ['자기 개발'],
    #                         ['콘서트·공연·전시회 관람']], columns=['Act'])
