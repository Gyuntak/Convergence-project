import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

def process_bigdata(data) :
    total_list = [""]


    new_df = pd.DataFrame(data)
    usss = new_df.copy()
    usss = usss[["id","tendencies"]]
    usss = usss.set_index('id')

    lst = []
    for i in usss['tendencies'].values:
        lst.append(list(i))

    # new=df[["유저","상상력","창의적",'호기심','생각깊이','세련됨','체계적','무책임함','현실성','철저함','근면함','말_많음','자기주장','모험적','정열적','대담함','친절함','협조적','이타적','관대함','타인신뢰','이완됨','편안함','안정됨','만족','침착']]
    new_lines = pd.DataFrame(lst,
                             columns=["상상력", "창의적", '호기심', '생각깊이', '세련됨', '체계적', '무책임함', '현실성', '철저함', '근면함', '말_많음',
                                      '자기주장', '모험적', '정열적', '대담함', '친절함', '협조적', '이타적', '관대함', '타인신뢰', '이완됨', '편안함',
                                      '안정됨', '만족', '침착'])
    new_lines = new_lines.astype(int)


    user_sim1 = cosine_similarity(new_lines, new_lines)
    user_sim_df1 = pd.DataFrame(user_sim1)

    ## 맨 마지막에 들어온 유저에게 비슷한 취미 5개를 인덱스 형태로 반환하는 코드 ##
    user_sim_df1[len(user_sim_df1)-1].sort_values(ascending=False)[2:7]

    result = new_df.iloc[user_sim_df1[len(user_sim_df1)-1].sort_values(ascending=False)[2:20].index]
    lst = []

    for i in result[['final_result']].values:
        for j in i:
            lst.append(j)

    final_list = []

    for i in lst:
        if (i not in final_list):
            final_list.append(i)



    return final_list[:5]





